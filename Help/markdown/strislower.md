[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# strislower

## Purpose

Check if first char of string1 is lowercase.

## Syntax

```
returnedBoolean = strislower(string1)
```

```
returnedBoolean - type: bool

string1 - type: str
```

## Returns

Returns true if the first character of the string is lowercase, otherwise false.

## Remarks

Only the first character is tested, not the whole string.

## Example

```
@CHECK

if (strislower(N("$text",1)))

 fail();

@RULES

_name <- will @@
```

## See Also

[strisupper](strisupper.md), [String Functions](Table_of_String_Functions.md)
