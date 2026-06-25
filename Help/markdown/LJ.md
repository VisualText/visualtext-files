[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# LJ

## Purpose

Left-justify a string in a given field size.

## Syntax

```
returnedStr = LJ(str,fieldsize_num)
```

```
returnedStr - type: str

str - type: str

fieldsize_num - type: num
```

## Returns

A string of the given field size, with the text left-justified (padded on the right with spaces). If the text is longer than the field size, a wider string is returned.

## Remarks

The first argument is a string. Field size is the total width of the returned string.

## Example

```
@CODE
```

```
"output.txt" << LJ("abc",6) << "|" << "\n";   # Prints: abc   |
```

```
@@CODE
```

## See Also

[rightjustifynum](rightjustifynum.md), [percentstr](percentstr.md), [Formatting and I/O Functions](Table_of_Formatting_and_I_O_Functions.md)
