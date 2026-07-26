[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# round

## Purpose

Round a number to the nearest whole number.

## Syntax

```
returnedInt = round(numFlt)
```

```
returnedInt - type: int

numFlt - type: float
```

## Returns

The whole number nearest the given number.

## Remarks

Analogous to the round function in C/C++. Halfway cases round away from zero, so round of 3.5 is 4 and round of -3.5 is -4.

## Example

```
@CODE

"output.txt" << round(3.5) << "\n";

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
