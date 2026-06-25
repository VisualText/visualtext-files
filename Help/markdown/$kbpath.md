[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# $kbpath

## Purpose

Get the path for the kb / user.

## Syntax

```
returnedString = variableType("$kbpath")
```

```
returnedString - type: str

variableType - type: G
```

## Returns

Returns the base directory path of the kb / user directory as a string (e.g., "D:\dev\apps\Resume\kb\user").

## Remarks

## Example

$kbpath returns "D\apps\Resume\input\Dev1\kb\user" assuming the app directory is "D\apps\Resume\input\Dev1" resides in Dev1 directory.

```
@CODE
    L("file") = "output.txt";
    L("file") << "KB path: " << G("$kbpath") << "\n";
@@CODE
```

## See Also

[$apppath]($apppath.md), [$input]($input.md), [$inputhead]($inputhead.md), [$inputname]($inputname.md), [$inputtail]($inputtail.md), [Special Variables](NLP_PP_Stuff/Special_Variables.md#table)
