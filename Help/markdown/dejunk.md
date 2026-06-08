[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# dejunk

## Purpose

Convert string to remove accented and extended ASCII/ANSI characters.

## Syntax

```
returnedString = dejunk(string)
```

```
returnedString - type: str

string - type: str
```

## Returns

String with characters converted to non-accented variants or to question marks if no ASCII/ANSI equivalent is readily apparent.  This function helps clean up "junk" for things like XML readers that break on control characters.  Some chars replaced with question mark ('?'), quote chars, and so on.

## Remarks

## Example

## See Also

[String Functions](Table_of_String_Functions.md)
