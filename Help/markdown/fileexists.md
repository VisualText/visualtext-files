[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# fileexists

## Purpose

Test whether a path names an existing regular file.

## Syntax

```
returnedBool = fileexists(pathStr)
```

```
returnedBool - type: bool

pathStr - type: str
```

## Returns

True (1) if the path exists and is a regular file, otherwise false (0). A directory returns false — use [direxists](direxists.md) to test for a folder.

## Remarks

Paths may use forward slashes or backslashes on Windows. A relative path is resolved against the analyzer's current working directory.

## Example

```
@CODE

if (fileexists("c:\tmp\input.txt")) {
    # ... process the file ...
}

@@CODE
```

## See Also

[direxists](direxists.md), [filesize](filesize.md), [deletefile](deletefile.md), [File Functions](Table_of_File_Functions.md)
