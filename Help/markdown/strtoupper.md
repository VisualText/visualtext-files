[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# strtoupper

## Purpose

Convert string to uppercase.

## Syntax

```
returnedString = strtoupper(string)
```

```
returnedString - type: str

string - type: str
```

## Returns

Returns the input string converted entirely to uppercase.

## Remarks

## Example

```
@CODE
G("out") = strtoupper("Hello World");
"output.txt" << G("out") << "\n";   # HELLO WORLD
@@CODE
```

## See Also

[strtolower](strtolower.md), [strtotitle](strtotitle.md), [String Functions](Table_of_String_Functions.md)
