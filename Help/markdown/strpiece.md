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

A position outside the string, or an end before the start, gives an empty string: `strpiece("abc", -5, -1)`, `strpiece("abc", 2, 0)` and `strpiece("ab", 0, -3)` are all empty. A negative position out of range, an end before the start, or an empty string also writes `strpiece: Error.` to err.log; a start past the end does not.

**Older code that computes a position can change meaning.** Before 4.2.15 a negative position ran off the start of the string. Now it counts from the end, so a position worked out as `strlength(s) - k` goes wrong when `s` is shorter than `k`: the result is negative and wraps round to the end instead. `strpiece(",", 0, strlength(",") - 2)` was meant to be empty and is now `,` -- and a loop that trims a trailing character this way never ends on a one-character string. Write the from-the-end position directly instead:

```
L("trimmed") = strpiece(L("s"), 0, -2);    # not strpiece(L("s"), 0, strlength(L("s")) - 2)
```

It gives the same result for any string long enough, and an empty one for a string too short. `strlength(s) - 1` is still safe, because it is -1 only for an empty string, where every position gives an empty result. Any larger subtraction can wrap, including one that subtracts another length, such as `strlength(s) - strlength(suffix) - 1`. If short strings are expected, test the length first; that also keeps err.log clean.

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
