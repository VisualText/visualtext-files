[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# sqlstr

## Purpose

Convert string to SQL format.

## Syntax

```
returnedString = sqlstr(string)
```

```
returnedString - type: str

string - type: str
```

## Returns

String with special SQL chars converted appropriately.  Merely converts a single quote to two single quotes.

## Remarks

## Example

"output.txt" << sqllstr("hello'bye") << "\n";

Outputs:

hello''bye

## See Also

[String Functions](Table_of_String_Functions.md)
