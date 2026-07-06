# Regression Testing

The extension can run **golden-file regression tests** over an analyzer: it analyzes
every input file, captures the analyzer's JSON output, and compares it against a saved
"golden" copy. This catches unintended changes in what your analyzer extracts.

[← Back to Help home](home.md)

## The one requirement: your analyzer must emit `output.json`

Regression testing compares **JSON output**, so each input must produce an
`output.json` next to it (in the engine's `<input-file>_log/` folder). An analyzer
produces this by building a knowledge base (KB) of results and then writing that KB out
as JSON.

### How the JSON gets written: `KBFuncs`

JSON output comes from the shared **`KBFuncs`** library pass. It provides the JSON output
functions (e.g. `JsonSave`) that walk the concepts your analyzer added to the KB and
serialize them to `output.json`.

- **`KBFuncs` is NOT added automatically.** You add it yourself: in the **Analyzer**
  (sequence) view, **right-click → Library Pass → KB Functions**. That inserts the
  `KBFuncs` pass into your sequence (it appears as `nlp KBFuncs`) and drops `KBFuncs` into
  the analyzer's `spec/` folder.
- **What your analyzer does:** during analysis your passes attach the things you want to
  extract as **concepts/attributes under a KB root** (for example a `Snippets` concept
  with one child per extracted item). A final output pass calls the `KBFuncs` JSON
  function to convert that KB into `output.json`.

So the data flow is:

```
your passes  ──►  build KB concepts (.kbb)  ──►  KBFuncs JSON function  ──►  output.json
```

If an analyzer doesn't write `output.json`, regression runs report `MISSING`/empty for
its inputs — add the `KBFuncs` pass and an output pass that calls the JSON function.

## Running the tests

Goldens live under `<analyzer>/test/expected/`, mirroring the `input/` tree
(`test/expected/<relative-input-path>.json`).

**First time — capture the baseline:**

1. Right-click the analyzer (Analyzers view) → **Bless Regression Goldens (All Files)**,
   or right-click a file/folder in the **Text** view → **Bless Regression Goldens**.
   Bless runs every input and writes the goldens. (It only warns about overwriting when
   goldens already exist.)
2. Inspect the goldens and commit them with your analyzer.

**After changes — test against the baseline:**

- Right-click the analyzer → **Run Regression Test (All Files)**, or use the 🧪 **test**
  icon / right-click item on any file or folder in the Text view to scope the run to just
  that file or folder.
- Results stream into the **Logging** view: `PASS`, `FAIL` (with the `+`/`-` record
  differences), or `MISSING` (no golden yet — run Bless), ending with a summary.

## What counts as a difference

The comparison is **semantic**, not textual:

- volatile fields (like `id`) are ignored,
- extraction-record lists are order-insensitive (a renumber/reorder is not a failure),

so cosmetic engine drift won't fail a test, but a real added/removed/changed extraction
will.

## Which files are tested

Every regular file under `input/` (recursively), **except** `*_log/` output folders,
`README`/`SOURCES` docs, and `.json` files. Add an optional
`<analyzer>/test/regress.json` to narrow or widen this:

```json
{
  "include": ["demo/**"],
  "exclude": ["scratch/*"],
  "ignore_fields": ["id"]
}
```