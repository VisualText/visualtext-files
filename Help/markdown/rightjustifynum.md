[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# rightjustifynum

## Purpose

Right-justify a number in a given field size.

## Syntax

```
str = rightjustifynum(number, fieldsize_num)
```

## Returns

A string of the given field size, with the number right-justified (padded on the left with spaces). If the number is wider than the field size, a wider string is returned.

## Remarks

## Example

```
@CODE
```

```
"output.txt" << rightjustifynum(42,5) << "|" << "\n";   # Prints:    42|
```

```
@@CODE
```

## See Also

[LJ](LJ.md), [percentstr](percentstr.md), [Formatting and I/O Functions](Table_of_Formatting_and_I_O_Functions.md)
