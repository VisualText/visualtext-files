[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# $inputtail

## Purpose

Get the tail (extension type) of the input file.

## Syntax

```
returnedString = variableType("$inputtail")
```

```
returnedString - type: str

variableType - type: G
```

## Returns

Returns the tail (file extension, without the dot) of the input file as a string (e.g., "txt").

## Remarks

## Example

$inputtail returns "txt" if the input file is "rez.txt".

```
@CODE
    L("file") = "output.txt";
    L("file") << "Input tail: " << G("$inputtail") << "\n";
@@CODE
```

## See Also

[$apppath]($apppath.md), [$input]($input.md), [$inputhead]($inputhead.md), [$inputname]($inputname.md), [$inputpath]($inputpath.md), [Special Variables](NLP_PP_Stuff/Special_Variables.md#table)
