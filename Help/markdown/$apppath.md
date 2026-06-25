[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# $apppath

## Purpose

Get the base directory path for the current application.

## Syntax

```
returnedString = variableType("$apppath")
```

```
returnedString - type: str

variableType - type: G
```

## Returns

Returns the base directory path of the current application as a string (e.g., "D:\dev\apps\Resume").

## Remarks

## Example

"D:\dev\apps\Resume".

```
@CODE
    L("file") = "output.txt";
    L("file") << "App path: " << G("$apppath") << "\n";
@@CODE
```

## See Also

[$inputpath]($inputpath.md), [Special Variables](NLP_PP_Stuff/Special_Variables.md#table)
