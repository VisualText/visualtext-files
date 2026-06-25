[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# strpiece

## Purpose

Fetch substring of a string from startNumber to endNumber indexes. Zero-based.

## Syntax

```
returnedString = strpiece(string, startNumber, endNumber)
```

```
returnedString - type: str

string - type: str

startNumber - type: int

endNumber - type: int
```

## Returns

The substring of `string` from the zero-based index startNumber to endNumber, inclusive.

## Remarks

## Example

```
@CODE
G("piece") = strpiece("hello", 1, 3);
"output.txt" << G("piece") << "\n";
# Writes "ell"
@@CODE
```

## See Also

[strsubst](strsubst.md), [strcontains](strcontains.md), [strcontainsnocase](strcontainsnocase.md), [strendswith](strendswith.md), [strendswith](strendswith.md), [String Functions](Table_of_String_Functions.md)
