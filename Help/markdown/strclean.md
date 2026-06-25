[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# strclean

## Purpose

Remove leading, trailing, and repeating whitespace separators.

## Syntax

```
returnedString = strclean(string)
```

```
returnedString - type: str

string - type: str
```

## Returns

Returns the input string with leading and trailing whitespace removed and repeated internal whitespace separators collapsed to a single space.

## Remarks

## Example

```
@CODE
G("out") = strclean("  hello    big   world  ");
"output.txt" << G("out") << "\n";   # hello big world
@@CODE
```

## See Also

[strtrim](strtrim.md), [String Functions](Table_of_String_Functions.md)
