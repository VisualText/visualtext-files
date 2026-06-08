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

## Remarks

## Example

```
@CODE

G("file") = openfile("c:\\tmp.txt");

closefile(G("file"));

@@CODE
```

## See Also

[openfile](openfile.md), [Formatting and I/O Functions](Table_of_Formatting_and_I_O_Functions.md)
