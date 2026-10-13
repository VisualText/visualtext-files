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

Positions count characters, not bytes, so accented letters and emoji count as one each.

A negative position counts from the end: `-1` is the last character, `-2` the one before it. `strpiece("hello", 1, -1)` is `ello`, and `strpiece("hello", 0, -2)` is `hell`. **NEW 4.2.15**

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
