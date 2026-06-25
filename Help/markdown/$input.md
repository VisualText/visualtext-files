[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# $input

## Purpose

Get the full input path for the file.

## Syntax

```
returnedString = variableType("$input")
```

```
returnedString - type: str

variableType - type: G
```

## Returns

Returns the full path of the input file being analyzed as a string (e.g., "D:\apps\Resume\input\Dev1\rez.txt").

## Remarks

## Example

$input returns "D:\apps\Resume\input\Dev1\rez.txt" if the input file is "rez.txt".

```
@CODE
    L("file") = "output.txt";
    L("file") << "Input file: " << G("$input") << "\n";
@@CODE
```

## See Also

[$inputhead]($inputhead.md), [$inputname]($inputname.md), [$inputpath]($inputpath.md), [$inputtail]($inputtail.md), [Special Variables](NLP_PP_Stuff/Special_Variables.md#table)
