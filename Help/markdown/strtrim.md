[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# strtrim

## Purpose

Remove leading and trailing whitespace from a string.

## Syntax

```
returnedString = strtrim(string)
```

```
returnedString - type: str

string - type: str
```

## Returns

Returns the input string with leading and trailing whitespace removed.

## Remarks

## Example

```
@CODE
G("out") = strtrim("   hello   ");
"output.txt" << G("out") << "\n";   # hello
@@CODE
```

## See Also

[strclean](strclean.md), [String Functions](Table_of_String_Functions.md)
