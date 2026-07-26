[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# ceiling

## Purpose

Round a number up to the nearest whole number.

## Syntax

```
returnedInt = ceiling(numFlt)
```

```
returnedInt - type: int

numFlt - type: float
```

## Returns

The smallest whole number that is greater than or equal to the given number.

## Remarks

Analogous to the ceil function in C/C++. Rounds toward positive infinity, so the ceiling of a negative number moves toward zero: the ceiling of -3.7 is -3.

## Example

```
@CODE

"output.txt" << ceiling(3.2) << "\n";

@@CODE
```

```
Outputs:
```

```
4
```

## See Also

[floor](floor.md), [ceiling](ceiling.md), [round](round.md), [truncate](truncate.md)

[Math Functions](Table_of_Math_Functions.md)
