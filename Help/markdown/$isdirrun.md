[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# $isdirrun

## Purpose

Check if the engine is processing a directory of files instead of an individual file. Returns 1 if it is analyzing a directory, else 0.

## Syntax

```
returnedBoolean = variableType("$isdirrun")
```

```
returnedBoolean - type: int

variableType - type: G
```

## Returns

Returns 1 if processing a directory, 0 if not.

## Remarks

## Example

```
@CODE
    if (G("$isdirrun")) {
        "summary.txt" << "Processing a directory of files.\n";
    }
@@CODE
```

## See Also

[$isfirstfile]($isfirstfile.md), [$islastfile]($islastfile.md), [$inputpath]($inputpath.md), [Special Variables](NLP_PP_Stuff/Special_Variables.md#table)
