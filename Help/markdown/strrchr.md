[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# strrchr

## Purpose

Find the last occurrence of a character in a string. This function returns the string headed by the character.

## Syntax

```
returnedString = strchr(string, characterString)
```

```
returnedString - type: str

string - type: str

characterString - type: str
```

## Returns

The portion of `string` starting at the last occurrence of the character characterString, or an empty string if the character is not found.

## Remarks

The second argument must be a single character (one Unicode code point); otherwise a warning is issued.

## Example

```
@CODE
G("ext") = strrchr("foo.bar.txt", ".");
"output.txt" << G("ext") << "\n";
# Writes ".txt"
@@CODE
```

## See Also

[strchr](strchr.md), [strchar](strchar.md), [strlength](strlength.md), [strwrap](strwrap.md), [String Functions](Table_of_String_Functions.md)
