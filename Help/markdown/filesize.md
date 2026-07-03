[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# filesize

## Purpose

Return the size of a regular file, in bytes.

## Syntax

```
returnedInt = filesize(pathStr)
```

```
returnedInt - type: int

pathStr - type: str
```

## Returns

The size of the file in bytes. Returns -1 if the path does not exist, is not a regular file, or cannot be read. Because a missing file returns -1 (which is non-zero), test the result against a specific value rather than relying on truthiness.

## Remarks

Paths may use forward slashes or backslashes on Windows. Use [fileexists](fileexists.md) first if you need to distinguish "empty file" (size 0) from "no such file" (size -1).

## Example

```
@CODE

if (filesize("c:\tmp\input.txt") > 0) {
    # ... the file exists and is non-empty ...
}

@@CODE
```

## See Also

[fileexists](fileexists.md), [deletefile](deletefile.md), [File Functions](Table_of_File_Functions.md)
