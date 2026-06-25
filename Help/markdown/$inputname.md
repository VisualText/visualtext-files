[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# $inputname

## Purpose

Get the name of the input file.

## Syntax

```
returnedString = variableType("$inputname")
```

```
returnedString - type: str

variableType - type: G
```

## Returns

Returns the name (file name with extension) of the input file as a string (e.g., "rez.txt").

## Remarks

## Example

$inputname returns "rez.txt" if the input file is "rez.txt".

```
@CODE
    L("file") = "output.txt";
    L("file") << "Input name: " << G("$inputname") << "\n";
@@CODE
```

## See Also

[$apppath]($apppath.md), [$input]($input.md), [$inputhead]($inputhead.md), [$inputpath]($inputpath.md), [$inputtail]($inputtail.md), [Special Variables](NLP_PP_Stuff/Special_Variables.md#table)
