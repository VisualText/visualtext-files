<#
.SYNOPSIS
  Audit the NLP++ Help markdown for drift against the engine registry and the index TOC.

.DESCRIPTION
  index.md is treated as the ALLOWLIST of what is current. The engine registry
  (nlp-engine/lite) still contains legacy/internal builtins, so "missing a page"
  is reported only as INFORMATION, never as an error to auto-fix.

  Reports:
    1. Broken links     - any ](*.md) reference in the corpus that does not resolve.
    2. Orphaned pages   - *.md files not referenced from index.md (legacy candidates).
    3. Table/index drift- pages linked from a Table_of_* but absent from index.md.
    4. Engine coverage  - (info) engine function/action names with no help page.

.PARAMETER HelpDir
  Path to the Help/markdown directory. Defaults to ./markdown relative to this script.

.PARAMETER EnginePath
  Path to nlp-engine/lite. If absent, the engine-coverage section is skipped.

.EXAMPLE
  pwsh Help/check-help-docs.ps1
  pwsh Help/check-help-docs.ps1 -EnginePath C:\git\nlp-engine\lite
#>
param(
  [string]$HelpDir    = (Join-Path $PSScriptRoot 'markdown'),
  [string]$EnginePath = 'c:\git\nlp-engine\lite'
)

if (-not (Test-Path $HelpDir)) { Write-Error "HelpDir not found: $HelpDir"; exit 2 }
$HelpDir = (Resolve-Path $HelpDir).Path
$indexPath = Join-Path $HelpDir 'index.md'
$indexTxt  = if (Test-Path $indexPath) { Get-Content $indexPath -Raw } else { '' }

$allMd = Get-ChildItem -Path $HelpDir -Recurse -Filter *.md
$issues = 0

# --- 1. Broken intra-repo .md links -------------------------------------------
$broken = @()
foreach ($f in $allMd) {
  $txt = Get-Content $f.FullName -Raw
  foreach ($m in [regex]::Matches($txt, '\]\(([^)]+\.md)(#[^)]*)?\)')) {
    $tgt = $m.Groups[1].Value
    if ($tgt -match '^https?://') { continue }
    $tgt = [uri]::UnescapeDataString($tgt)   # %24 -> $
    if (-not (Test-Path (Join-Path $f.DirectoryName $tgt))) {
      $broken += '{0}  ->  {1}' -f $f.FullName.Substring($HelpDir.Length+1), $tgt
    }
  }
}
Write-Host "== 1. Broken .md links ($($broken.Count)) ==" -ForegroundColor Cyan
$broken | Sort-Object | ForEach-Object { Write-Host "   $_" }
$issues += $broken.Count

# --- 2. Orphaned flat pages (not referenced from index.md) --------------------
$flat = $allMd | Where-Object { $_.DirectoryName -eq $HelpDir -and $_.Name -ne 'index.md' }
$orphans = $flat | Where-Object { $indexTxt -notmatch [regex]::Escape('(' + $_.Name + ')') } |
                   ForEach-Object { $_.BaseName }
Write-Host "`n== 2. Orphaned pages: on disk but not in index.md ($($orphans.Count)) ==" -ForegroundColor Cyan
Write-Host "   (review: legacy to delete, or current to add to the TOC)"
$orphans | Sort-Object | ForEach-Object { Write-Host "   $_" }

# --- 3. In a Table_of_* but not in index.md -----------------------------------
$tableDrift = @()
foreach ($t in ($flat | Where-Object { $_.Name -like 'Table_of_*' })) {
  $ttxt = Get-Content $t.FullName -Raw
  foreach ($m in [regex]::Matches($ttxt, '\]\(([A-Za-z0-9$_]+\.md)\)')) {
    $page = $m.Groups[1].Value
    if ($page -eq 'index.md') { continue }
    if ($indexTxt -notmatch [regex]::Escape('(' + $page + ')')) {
      $tableDrift += '{0}: {1}' -f $t.BaseName, $page
    }
  }
}
$tableDrift = $tableDrift | Sort-Object -Unique
Write-Host "`n== 3. Linked from a table but missing from index.md ($($tableDrift.Count)) ==" -ForegroundColor Cyan
$tableDrift | ForEach-Object { Write-Host "   $_" }

# --- 4. Engine coverage (informational) ---------------------------------------
if (Test-Path $EnginePath) {
  $names = @{}
  $funcsH = Join-Path $EnginePath 'funcs.h'
  if (Test-Path $funcsH) {
    foreach ($m in [regex]::Matches((Get-Content $funcsH -Raw), '_T\("([^"]+)"\)')) { $names[$m.Groups[1].Value] = 'func' }
  }
  foreach ($disp in @('pre.cpp','post.cpp')) {
    $p = Join-Path $EnginePath $disp
    if (Test-Path $p) {
      foreach ($m in [regex]::Matches((Get-Content $p -Raw), 'strcmp_i\(\s*func\s*,\s*_T\("([^"]+)"\)')) { $names[$m.Groups[1].Value] = 'action' }
    }
  }
  $haveLower = @{}; foreach ($f in $flat) { $haveLower[$f.BaseName.ToLower()] = $true }
  $noPage = $names.Keys | Where-Object { -not $haveLower.ContainsKey($_.ToLower()) } | Sort-Object
  Write-Host "`n== 4. Engine names with no help page ($($noPage.Count)) -- INFO ONLY ==" -ForegroundColor Cyan
  Write-Host "   (many are legacy/internal: rfa*/rfb*, codegen, WordNet, disabled stubs)"
  Write-Host ("   " + ($noPage -join ', '))
} else {
  Write-Host "`n== 4. Engine coverage skipped (EnginePath not found: $EnginePath) ==" -ForegroundColor DarkYellow
}

Write-Host "`n--- summary ---" -ForegroundColor Green
Write-Host ("broken links: {0}   orphaned pages: {1}   table/index drift: {2}" -f $broken.Count, $orphans.Count, $tableDrift.Count)
# Exit non-zero only on hard errors (broken links / table-index drift), so it can gate CI.
if (($broken.Count + $tableDrift.Count) -gt 0) { exit 1 } else { exit 0 }
