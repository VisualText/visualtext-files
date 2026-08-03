[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# readfile

## Purpose

Read an entire text file into a string.

## Syntax

```
returnedStr = readfile(pathStr)
```

```
returnedStr - type: str

pathStr - type: str
```

## Returns

The full contents of the file as a single string. Returns no value if the path is not a readable regular file, if the file is empty, or if the file is larger than the 16MB limit; a warning is written to the log in the failure cases.

## Remarks

This is the counterpart to the output functions [openfile](openfile.md) and [fileout](fileout.md). It lets a pass load data that did not arrive as the analyzer's input text — a configuration file, a lookup table, or the output of an earlier run.

A leading UTF-8 byte order mark is stripped, so a file saved by a Windows editor does not poison its own first token. A file containing NUL bytes is rejected as binary rather than being silently truncated at the first NUL.

The contents are interned, so they stay allocated for the remainder of the parse. For large files prefer [readlines](readlines.md), which has no size limit because it interns one line at a time.

Line terminators are returned as they appear in the file, so a file written on Windows yields `\r\n` and one written on Linux yields `\n`. If that distinction does not matter, normalize with [resubst](resubst.md) or read the file with [readlines](readlines.md), which strips terminators for you.

Paths may use forward slashes or backslashes on Windows. Use [fileexists](fileexists.md) to test for the file first if a missing file is an expected condition rather than an error.

## Example

```
@CODE

L("path") = G("$apppath") + "/data/config.txt";

if (fileexists(L("path"))) {
    L("text") = readfile(L("path"));
    "out.txt" << "config is " << str(strlength(L("text"))) << " bytes\n";
}

@@CODE
```

## See Also

[readlines](readlines.md), [dirlist](dirlist.md), [fileexists](fileexists.md), [filesize](filesize.md), [File Functions](Table_of_File_Functions.md)
