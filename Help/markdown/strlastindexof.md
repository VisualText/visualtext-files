[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# strlastindexof

## Purpose

Find the position of the last occurrence of a substring.

## Syntax

```
returnedInt = strlastindexof(str, substr)
```

```
returnedInt - type: int

str - type: str

substr - type: str
```

## Returns

The zero-based index at which substr last appears in str, or -1 if it does not appear.

## Remarks

The mirror of [strindexof](strindexof.md). Useful for splitting on the final separator, such as taking the extension off a filename or the last segment off a path.

Matching is case sensitive. As with [strindexof](strindexof.md), test against -1 rather than relying on truthiness, since 0 is a valid position.

## Example

```
@CODE

# Take the basename off a path returned by dirlist.
L("cut") = strlastindexof(L("path"),"/");
if (L("cut") >= 0) {
    L("name") = strpiece(L("path"),L("cut") + 1,strlength(L("path")) - 1);
}

@@CODE
```

## See Also

[strindexof](strindexof.md), [strrchr](strrchr.md), [dirlist](dirlist.md), [String Functions](Table_of_String_Functions.md)
