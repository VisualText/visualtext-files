[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# strtolower

## Purpose

Convert string to lowercase.

## Syntax

```
returnedString = strtolower(string)
```

```
returnedString - type: str

string - type: str
```

## Returns

Returns the input string converted entirely to lowercase.

## Remarks

## Example

```
@CODE
G("out") = strtolower("Hello World");
"output.txt" << G("out") << "\n";   # hello world
@@CODE
```

## See Also

[strtoupper](strtoupper.md), [strtotitle](strtotitle.md), [String Functions](Table_of_String_Functions.md)
