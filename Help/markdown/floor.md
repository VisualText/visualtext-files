[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# floor

## Purpose

Round a number down to the nearest whole number.

## Syntax

```
returnedInt = floor(numFlt)
```

```
returnedInt - type: int

numFlt - type: float
```

## Returns

The largest whole number that is less than or equal to the given number.

## Remarks

Analogous to the floor function in C/C++. Rounds toward negative infinity, so the floor of a negative number moves away from zero: the floor of -3.7 is -4. Use [truncate](truncate.md) to discard the fraction and round toward zero instead.

## Example

```
@CODE

"output.txt" << floor(3.7) << "\n";

@@CODE
```

```
Outputs:
```

```
3
```

## See Also

[floor](floor.md), [ceiling](ceiling.md), [round](round.md), [truncate](truncate.md)

[Math Functions](Table_of_Math_Functions.md)
