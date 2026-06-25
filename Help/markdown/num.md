[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# num

## Purpose

Convert a string to a number, if possible.

## Syntax

```
returnedNumber = num(string)
```

```
returnedNumber - type: int

string - type: str
```

## Returns

Returns the integer value of the string if it can be converted; a float argument is truncated to an int, and an int argument is returned unchanged.

## Remarks

This function also accepts a num arg.

## Example

```
@CODE
G("count") = num("123");
"output.txt" << G("count") << "\n";   # 123
@@CODE
```

## See Also

[str](str.md), [String Functions](Table_of_String_Functions.md)
