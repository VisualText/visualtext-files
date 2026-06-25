[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# striscaps

## Purpose

Check if the entire string is uppercase.

## Syntax

```
returnedBoolean = striscaps(string1)
```

```
returnedBoolean - type: bool

string1 - type: str
```

## Returns

Returns true if the entire string is uppercase, otherwise false.

## Remarks

Unlike strisupper, which tests only the first character, striscaps checks every character in the string.

## Example

```
@CHECK

if (striscaps(N("$text",1)))

 fail();

@RULES

_name <- will @@
```

## See Also

[strislower](strislower.md), [strisupper](strisupper.md), [String Functions](Table_of_String_Functions.md)
