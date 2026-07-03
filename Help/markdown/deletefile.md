[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# deletefile

## Purpose

Delete a regular file.

## Syntax

```
returnedBool = deletefile(pathStr)
```

```
returnedBool - type: bool

pathStr - type: str
```

## Returns

True (1) if a regular file was removed, otherwise false (0) — including when the path does not exist or names a directory.

## Remarks

As a safeguard, `deletefile` only removes regular files; it never deletes directories. Paths may use forward slashes or backslashes on Windows. The removal is permanent — the file does not go to a recycle bin or trash.

## Example

```
@CODE

if (fileexists("c:\tmp\scratch.txt")) {
    deletefile("c:\tmp\scratch.txt");
}

@@CODE
```

## See Also

[fileexists](fileexists.md), [filesize](filesize.md), [direxists](direxists.md), [File Functions](Table_of_File_Functions.md)
