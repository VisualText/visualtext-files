[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# readlines

## Purpose

Read a text file as an array of its lines.

## Syntax

```
returnedArray = readlines(pathStr)
```

```
returnedArray - type: str array

pathStr - type: str
```

## Returns

An array holding one element per line of the file, with line terminators stripped. Returns an empty array if the file is empty or is not a readable regular file; a warning is written to the log in the latter case.

## Remarks

`readlines` streams the file, so unlike [readfile](readfile.md) it has no size limit and is the right choice for large data files.

CRLF and LF are treated alike, so a file written on Windows reads the same on Linux. A leading UTF-8 byte order mark is stripped from the first line.

A trailing newline at the end of the file does **not** produce a final empty element: a file holding `a\nb\n` yields two elements, not three. Blank lines in the middle of the file do come back as empty elements, so the element numbering always lines up with the line numbering of the file.

Use [arraylength](arraylength.md) to get the count and index the result with square brackets, exactly as with [split](split.md).

An empty or unreadable file gives an empty array. Guard a loop over it by testing the **first element** rather than the count: assigning an empty array to a variable collapses it back to no value, and `arraylength` reports 1 for a variable holding no value, so a count test would run the loop once over a phantom line.

## Example

```
@CODE

L("lines") = readlines(G("$apppath") + "/data/terms.txt");

# Guard on the first element, not the count -- see Remarks.
if (strlength(L("lines")[0])) {
    L("len") = arraylength(L("lines"));
    L("i") = 0;
    while (L("i") < L("len")) {
        L("line") = L("lines")[L("i")];
        # Skip blank lines and "#" comments.
        if (strlength(L("line")) && !strstartswith(L("line"),"#")) {
            addword(L("line"));
        }
        L("i")++;
    }
}

@@CODE
```

## See Also

[readfile](readfile.md), [dirlist](dirlist.md), [split](split.md), [arraylength](arraylength.md), [File Functions](Table_of_File_Functions.md)
