[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# $inputparent

## Purpose

Get the name of the parent directory of the input file.

## Syntax

```
returnedString = variableType("$inputparent")
```

```
returnedString - type: str

variableType - type: G
```

## Returns

Returns the name of the parent directory of the input file as a string (e.g., "Dev1").

## Remarks

## Example

$inputparent returns "Dev1" assuming input file is "D\apps\Resume\input\Dev1\text.txt".

```
@CODE
    L("file") = "output.txt";
    L("file") << "Input parent: " << G("$inputparent") << "\n";
@@CODE
```

## See Also

[$apppath]($apppath.md), [$input]($input.md), [$inputhead]($inputhead.md), [$inputname]($inputname.md), [$inputtail]($inputtail.md), [Special Variables](NLP_PP_Stuff/Special_Variables.md#table)
