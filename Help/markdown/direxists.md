[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# direxists

## Purpose

Test whether a path names an existing directory (folder).

## Syntax

```
returnedBool = direxists(pathStr)
```

```
returnedBool - type: bool

pathStr - type: str
```

## Returns

True (1) if the path exists and is a directory, otherwise false (0). A regular file returns false — use [fileexists](fileexists.md) to test for a file.

## Remarks

Paths may use forward slashes or backslashes on Windows. A relative path is resolved against the analyzer's current working directory. Pair with [mkdir](mkdir.md) to create a directory only when it does not already exist.

## Example

```
@CODE

if (!direxists("c:\tmp\output")) {
    mkdir("c:\tmp\output");
}

@@CODE
```

## See Also

[fileexists](fileexists.md), [mkdir](mkdir.md), [File Functions](Table_of_File_Functions.md)
