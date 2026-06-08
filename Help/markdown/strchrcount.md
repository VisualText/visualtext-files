[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# strchrcount

## Purpose

Count the occurrences of a character in a string.

## Syntax

```
returnedNum = strchrcount(string, characterString)
```

```
returnedNum - type: num

string - type: str

characterString - type: str
```

## Returns

The number of times char occurs in string.

## Remarks

characterString must consist of a single character.

## Example

G("count") = strchrcount("abcabc","b");

# This should evaluate to 2, for the two occurrences of "b" in "abcabc".

## See Also

[strchr](strchr.md), [String Functions](Table_of_String_Functions.md)
