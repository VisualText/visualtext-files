[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# $anaspath

## Purpose

Get the parent folder for the analyzer folders.

## Syntax

```
returnedString = variableType("$anaspath")
```

```
returnedString - type: str

variableType - type: G
```

## Returns

Returns the parent directory path of the analyzer folders as a string.

## Remarks

## Example

$anaspath returns "D\apps\Resume" assuming the app directory is "D\apps\".

```
@CODE
    L("file") = "output.txt";
    L("file") << "Analyzers parent: " << G("$anaspath") << "\n";
@@CODE
```

## See Also

[$apppath]($apppath.md), [$kbpath]($kbpath.md), [$input]($input.md), [$inputhead]($inputhead.md), [$inputname]($inputname.md), [$inputtail]($inputtail.md), [Special Variables](NLP_PP_Stuff/Special_Variables.md#table)
