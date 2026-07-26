[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# truncate

## Purpose

Discard the fractional part of a number.

## Syntax

```
returnedInt = truncate(numFlt)
```

```
returnedInt - type: int

numFlt - type: float
```

## Returns

The given number with its fractional part removed.

## Remarks

Analogous to the trunc function in C/C++. Rounds toward zero, so truncate of -3.7 is -3, whereas [floor](floor.md) of -3.7 is -4.

## Example

```
@CODE

"output.txt" << truncate(3.7) << "\n";

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
