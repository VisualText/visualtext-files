[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# $inputpath

## Purpose

Get the path of the input file.

## Syntax

```
returnedString = variableType("$inputpath")
```

```
returnedString - type: str

variableType - type: G
```

## Returns

Returns the directory path containing the input file as a string (e.g., "D:\apps\Resume\input\Dev1").

## Remarks

## Example

$inputpath returns "D\apps\Resume\input\Dev1" assuming input file "rez.txt" resides in Dev1 directory.

```
@CODE
    L("file") = "output.txt";
    L("file") << "Input path: " << G("$inputpath") << "\n";
@@CODE
```

## See Also

[$apppath]($apppath.md), [$input]($input.md), [$inputhead]($inputhead.md), [$inputname]($inputname.md), [$inputtail]($inputtail.md), [Special Variables](NLP_PP_Stuff/Special_Variables.md#table)
