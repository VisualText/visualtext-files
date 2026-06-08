# openfile

## Purpose

Open output file stream.

## Syntax

```
returnedOstream = openfile(path_str [, mode_str [, mode_str [, mode_str]]] )
```

```
returnedOstream - type: ostream

path_str - type: str
```

```
mode_str - type: str
```

## Returns

## Remarks

Zero to three mode strings selected from: 1) "app" = append; 2) "ate" = special C++ append; 3) "binary" = open in binary mode (text is default).

`openfile` is analogous to C++ open file function.

| **WARNING: **Default mode is OVERWRITE, not APPEND. Unlike `fileout()`, does not create a global variable for the file stream. |
| --- |

In specifying file names, double slashes should be used.  To specify output.txt use `c:\\output.txt`, not `c:\output.txt`.

Files should not be placed in the application's input folder since VisualText wipes out the files after each text analysis.  For example, a file called blob.txt in the folder c:\\apps\input\\eg1.txt_log will get deleted each time the text gets analyzed.

## Example

```
@CODE

G("file") = openfile("c:\\tmp.txt");

closefile(G("file"));

@@CODE
```

## See Also

[closefile](closefile.md), [Formatting and I/O Functions](Table_of_Formatting_and_I_O_Functions.md)
