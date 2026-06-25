[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# strchr

## Purpose

Find the first occurrence of a character in a string. This function returns the string headed by the character.

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

The portion of `string` starting at the first occurrence of the character characterString, or an empty string if the character is not found.

## Remarks

The second argument must be a single character (one Unicode code point); otherwise a warning is issued.

## Example

```
@CODE
G("tail") = strchr("foo.bar.txt", ".");
"output.txt" << G("tail") << "\n";
# Writes ".bar.txt"
@@CODE
```

## See Also

[strrchr](strrchr.md), [strchar](strchar.md), [strlength](strlength.md), [strwrap](strwrap.md), [String Functions](Table_of_String_Functions.md)
