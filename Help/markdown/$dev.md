[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# $dev

## Purpose

Check whether the engine was run in development mode (`nlp.exe -DEV`). Returns 1 under `-DEV`, else 0.

Use it to gate an analyzer's own diagnostic passes on what the caller actually asked for, instead of hardcoding a flag in the analyzer.

## Syntax

```
returnedBoolean = variableType("$dev")
```

```
returnedBoolean - type: int

variableType - type: G
```

## Returns

Returns 1 if the engine was run with `-DEV`, 0 otherwise.

## Remarks

Before `$dev`, NLP++ had no way to ask which mode the engine was running in, so analyzers had to hardcode their debug flags and no engine switch could reach them. Gating a diagnostic flag on `$dev` lets the same analyzer run fast in production and verbose during development, with no edit between the two.

`-DEV` also makes the engine itself far more expensive: it writes a full parse-tree dump per pass. On a 9 KB input against a 136-pass analyzer that was measured at 137 files / 44 MB and roughly 3.6x total run time. Do not use `-DEV` when measuring processing speed.

`-SILENT` is not the opposite of `-DEV`. It selects the engine's quietest configuration, which suppresses the analyzer's **own** output files as well, so a `-SILENT` run produces no `out.txt` at all. For "run fast but still write my results", use the default mode (neither switch) together with `$dev`-gated diagnostics.

**NEW 3.8.4**

## Example

```
@CODE
    # Diagnostic passes run only when the caller asked for them.
    G("verbose") = G("$dev");

    if (G("verbose"))
        "trace.txt" << "pass " << str(G("$passnum")) << " reached\n";
@@CODE
```

A pass whose only job is diagnostics can bail out immediately:

```
@CODE
    if (!G("$dev"))
        exitpass();
@@CODE
```

## See Also

[$silent]($silent.md), [$passnum]($passnum.md), [$isdirrun]($isdirrun.md), [Special Variables](NLP_PP_Stuff/Special_Variables.md#table)
