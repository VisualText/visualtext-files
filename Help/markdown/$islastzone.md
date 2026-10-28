[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# $islastzone

## Purpose

In zone mode, check whether the zone being run is the last one. Use it for wrap-up work in a pass that runs once per zone.

## Syntax

```
returnedBoolean = variableType("$islastzone")
```

```
returnedBoolean - type: bool

variableType - type: G
```

## Returns

1 while the last zone runs, else 0. Outside zone mode, and in the passes before the `zone` line or after the `endzone` line, it is 0.

## Remarks

For whole-document work, the passes after an `endzone` line are usually the better place: they run once, after the last zone, on the zone nodes and the whole knowledge base. Use `$islastzone` when the wrap-up belongs in the same pass as the per-zone work.

With `nlp -ZONES 40-45` (engine 4.2.50), only those zones run, and `$islastzone` is 1 in zone 45, the last zone that runs.

**NEW 4.2.47**

## Example

```
@CODE
    G("zones")++;
    if (G("$islastzone"))
        "summary.txt" << G("zones") << " zones\n";
@@CODE
```

## See Also

[$isfirstzone]($isfirstzone.md), [$islastfile]($islastfile.md), [Large Files](vscode/largefiles.md), [Special Variables](NLP_PP_Stuff/Special_Variables.md#table)
