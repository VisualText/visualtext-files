[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# closefile

## Purpose

Close the output file stream.

## Syntax

```
returnedBool = closefile(fileOstream)
```

```
returnedBool - type: bool

fileOstream - type: ostream
```

## Returns

True if the file stream was closed successfully.

## Remarks

The argument must be an output stream returned by [openfile](openfile.md). Closing flushes any pending output and removes the stream.

## Example

```
@CODE

G("file") = openfile("c:\\tmp.txt");

closefile(G("file"));

@@CODE
```

## See Also

[openfile](openfile.md), [Formatting and I/O Functions](Table_of_Formatting_and_I_O_Functions.md)
