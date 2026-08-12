[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# $silent

## Purpose

Check whether the engine was run in silent mode (`nlp.exe -SILENT`). Returns 1 under `-SILENT`, else 0.

## Syntax

```
returnedBoolean = variableType("$silent")
```

```
returnedBoolean - type: int

variableType - type: G
```

## Returns

Returns 1 if the engine was run with `-SILENT`, 0 otherwise.

## Remarks

`-SILENT` selects the engine's quietest configuration. It suppresses logs and dump files — and also the analyzer's **own** output files, so a `-SILENT` run writes no `out.txt` even if the analyzer asks for one. Anything an analyzer does under `-SILENT` other than build the parse tree is therefore invisible.

Because of that, `$silent` is mostly useful for skipping work whose only product is a file that will not be written anyway. If what you want is "run fast but still produce my results", do not use `-SILENT`: run in the default mode (neither `-DEV` nor `-SILENT`) and gate diagnostics on [$dev]($dev.md) instead.

`-SILENT` is not a speed switch. Measured against the default mode on a 9 KB input it made no difference (8.39 sec vs 8.41 sec) — the default already writes no dump files. The switch that costs real time is `-DEV`.

**NEW 3.8.4**

## Example

```
@CODE
    # Nothing this pass produces can be written under -SILENT, so skip it.
    if (G("$silent"))
        exitpass();

    "report.txt" << "clauses: " << str(G("clause count")) << "\n";
@@CODE
```

## See Also

[$dev]($dev.md), [$isdirrun]($isdirrun.md), [Special Variables](NLP_PP_Stuff/Special_Variables.md#table)
