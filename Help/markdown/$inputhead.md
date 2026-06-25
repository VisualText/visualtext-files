[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# $inputhead

## Purpose

Get the head (name) of the input file.

## Syntax

```
returnedString = variableType("$inputhead")
```

```
returnedString - type: str

variableType - type: G
```

## Returns

Returns the head (base name without extension) of the input file as a string (e.g., "rez").

## Remarks

## Example

$inputhead returns "rez" if the input file is "rez.txt".

```
@CODE
    L("file") = "output.txt";
    L("file") << "Input head: " << G("$inputhead") << "\n";
@@CODE
```

## See Also

[$apppath]($apppath.md), [$input]($input.md), [$inputname]($inputname.md), [$inputpath]($inputpath.md), [$inputtail]($inputtail.md), [Special Variables](NLP_PP_Stuff/Special_Variables.md#table)
