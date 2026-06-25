[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# percentstr

## Purpose

Format a percentage (right-justified in field of 3 characters).

## Syntax

```
str ("0" to "100") = percentstr(numerator_num, denominator_num)
```

## Returns

A string holding the integer percentage (numerator * 100 / denominator), right-justified in a field of 3 characters (e.g. " 50", "100").

## Remarks

A denominator of 0 yields "  0". Negative numerator or denominator values are not supported and raise an error.

## Example

```
@CODE
```

```
"output.txt" << percentstr(1,4) << "|" << "\n";   # Prints:  25|
```

```
@@CODE
```

## See Also

[LJ](LJ.md), [rightjustifynum](rightjustifynum.md), [Formatting and I/O Functions](Table_of_Formatting_and_I_O_Functions.md)
