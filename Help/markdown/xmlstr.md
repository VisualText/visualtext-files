[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# xmlstr

## Purpose

Convert string to XML or HTML string.

## Syntax

```
returnedString = xmlstr(string)
```

```
returnedString - type: str

string - type: str
```

## Returns

String with special XML/HTML chars converted appropriately.

## Remarks

## Example

"output.txt" << xmlstr("hello&bye") << "\n";

Outputs:

hello&amp;bye

## See Also

[String Functions](Table_of_String_Functions.md)
