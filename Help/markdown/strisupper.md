[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# strisupper

## Purpose

Check if first char of string1 is uppercase.

## Syntax

```
returnedBoolean = strisupper(string1)
```

```
returnedBoolean - type: bool

string1 - type: str
```

## Returns

Returns true if the first character of the string is uppercase, otherwise false.

## Remarks

Only the first character is tested, not the whole string.

## Example

```
@CHECK

if (strisupper(N("$text",1)))

  fail();

@RULES

_modal <- will @@
```

## See Also

[strislower](strislower.md), [String Functions](Table_of_String_Functions.md)
