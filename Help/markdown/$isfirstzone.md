[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# $isfirstzone

## Purpose

In zone mode, check whether the zone being run is the first one. Use it for per-document setup in a pass that runs once per zone.

## Syntax

```
returnedBoolean = variableType("$isfirstzone")
```

```
returnedBoolean - type: bool

variableType - type: G
```

## Returns

1 while the first zone runs, else 0. Outside zone mode, and in the passes before the `zone` line or after the `endzone` line, it is 0.

## Remarks

A pass after a `zone` line in `analyzer.seq` runs once per zone, so its `@CODE` runs once per zone too. Code that should run once per document goes before the `zone` line, or is guarded by `$isfirstzone`.

With `nlp -ZONES 40-45` (engine 4.2.50), only those zones run, and `$isfirstzone` is 1 in zone 40, the first zone that runs.

**NEW 4.2.47**

## Example

```
@CODE
    if (G("$isfirstzone"))
        "summary.txt" << "zone\twords\n";
@@CODE
```

## See Also

[$islastzone]($islastzone.md), [$isfirstfile]($isfirstfile.md), [Large Files](vscode/largefiles.md), [Special Variables](NLP_PP_Stuff/Special_Variables.md#table)
