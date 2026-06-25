[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# strtotitle

## Purpose

Convert string to title capitalization.

## Syntax

```
returnedString = strtotitle(string)
```

```
returnedString - type: str

string - type: str
```

## Returns

Returns the input string with title capitalization (the first letter capitalized).

## Remarks

## Example

```
@CODE
G("out") = strtotitle("hello world");
"output.txt" << G("out") << "\n";   # Hello world
@@CODE
```

## See Also

[strtolower](strtolower.md), [strtoupper](strtoupper.md), [String Functions](Table_of_String_Functions.md)
