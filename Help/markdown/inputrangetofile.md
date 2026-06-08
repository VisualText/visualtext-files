[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# inputrangetofile

## Purpose

Fetch a substring of the input text, as specified by start and end offsets, and print it to an output stream.

## Syntax

```
bool = inputrangetofile(start_num,end_num, out_ostream)
```

## Returns

Boolean (0 or 1) if successful print out.

## Remarks

This is an efficient function in that it directly traverses the input text buffer to output the specified range of chars.

Offsets are zero based.

## Example

G("out") = openfile("c:\\tmp.txt");

inputrangetofile(0,9,G("out"));   # Print the first 10 characters of the input text.

closefile(G("out"));

## See Also

[Parse Tree Functions](Table_of_Parse_Tree_Functions.md)
