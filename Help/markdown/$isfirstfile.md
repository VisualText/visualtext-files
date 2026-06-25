[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# $isfirstfile

## Purpose

Checks to see if the current file is the first file being analzyed in a directory.

## Syntax

```
returnedBoolean = variableType("$isfirstfile")
```

```
returnedBoolean - type: bool

variableType - type: G
```

## Returns

Returns 1 if the current file is the first file, 0 if not.

## Remarks

## Example

```
@CODE
    if (G("$isfirstfile")) {
        "summary.txt" << "Header\n";
    }
@@CODE
```

## See Also

[$isdirrun]($isdirrun.md), [$islastfile]($islastfile.md), [$inputpath]($inputpath.md), [Special Variables](NLP_PP_Stuff/Special_Variables.md#table)
