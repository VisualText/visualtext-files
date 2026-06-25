[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# mod

## Purpose

Compute the modulus (remainder) of dividing one integer by another.

## Syntax

```
returnedInt = mod(numInt1, numInt2)
```

```
returnedInt - type: int

numInt1 - type: int

numInt2 - type: int
```

## Returns

The remainder of numInt1 divided by numInt2.

## Remarks

Analogous to the % operator in C/C++. An error is raised if numInt2 is zero (division by zero).

## Example

```
@CODE

"output.txt" << mod(17, 5) << "\n";

@@CODE
```

```
Outputs:
```

```
2
```

## See Also

[abs](abs.md), [factorial](factorial.md), [logten](logten.md)

[Math Functions](Table_of_Math_Functions.md)
