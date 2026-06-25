[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# strwrap

## Purpose

Break a string at a specified length.

## Syntax

```
returnedString = strwrap(string, number)
```

```
returnedString - type: str

string - type: str

number - type: int
```

## Returns

A copy of `string` broken into lines no longer than `number` characters (word wrap).

## Remarks

## Example

```
@CODE
G("wrapped") = strwrap("the quick brown fox", 10);
"output.txt" << G("wrapped") << "\n";
# Each output line is no longer than 10 characters
@@CODE
```

## See Also

[strlength](strlength.md), [String Functions](Table_of_String_Functions.md)
