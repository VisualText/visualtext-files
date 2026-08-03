[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# strindexof

## Purpose

Find the position of the first occurrence of a substring.

## Syntax

```
returnedInt = strindexof(str, substr)
```

```
returnedInt - type: int

str - type: str

substr - type: str
```

## Returns

The zero-based index at which substr first appears in str, or -1 if it does not appear.

## Remarks

[strchr](strchr.md) takes only a single character and returns the tail of the string rather than a position, so getting an index used to mean subtracting two [strlength](strlength.md) calls. [strcontains](strcontains.md) answers only yes or no. `strindexof` takes a whole substring and gives the position directly.

Matching is case sensitive.

Because "not found" is -1 and 0 is a legitimate result meaning "at the very start", test the result against -1 rather than relying on truthiness.

## Example

```
@CODE

L("at") = strindexof("hello world","world");     # 6
if (L("at") >= 0) {
    L("tail") = strpiece(L("s"),L("at"),strlength(L("s")) - 1);
}

@@CODE
```

## See Also

[strlastindexof](strlastindexof.md), [strchr](strchr.md), [strcontains](strcontains.md), [strpiece](strpiece.md), [String Functions](Table_of_String_Functions.md)
