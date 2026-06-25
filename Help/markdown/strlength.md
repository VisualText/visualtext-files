[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# strlength

## Purpose

Return the length of the string.

## Syntax

```
returnedNumber = strlength(string)
```

```
returnedNumber - type: INT

string - type: str
```

## Returns

The number of characters (Unicode code points) in `string`.

## Remarks

## Example

```
@CODE
G("len") = strlength("hello");
"output.txt" << G("len") << "\n";
# Writes 5
@@CODE
```

## See Also

[strwrap](strwrap.md), [String Functions](Table_of_String_Functions.md)
