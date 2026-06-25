[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# strchar

## Purpose

Index to the numth character of a string.

## Syntax

```
returnedString = strchar(string, number)
```

```
returnedString - type: str

string - type: str

number - type: int
```

## Returns

The single character at the zero-based index `number`, or an empty string if the index is past the end of the string or negative.

## Remarks

Indexing is by Unicode code point, not by byte, so a multi-byte UTF-8 character is returned whole.

## Example

```
@CODE
G("ch") = strchar("hello", 1);
"output.txt" << G("ch") << "\n";
# Writes "e"
@@CODE
```

## See Also

[strchr](strchr.md), [strrchr](strrchr.md), [strlength](strlength.md), [strwrap](strwrap.md), [String Functions](Table_of_String_Functions.md)
