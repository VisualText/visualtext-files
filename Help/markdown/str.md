[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# str

## Purpose

Convert numeric value to a string.

## Syntax

```
returnedString = str(number)
```

```
returnedString - type: str

number - type: int
```

## Returns

Returns the string representation of a numeric (int or float) value; a string argument is returned unchanged.

## Remarks

This function also accepts a string arg.

## Example

```
@CODE
G("out") = str(42);
"output.txt" << G("out") << "\n";   # 42
@@CODE
```

## See Also

[num](num.md), [String Functions](Table_of_String_Functions.md)
