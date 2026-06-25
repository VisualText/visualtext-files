[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# randomint

## Purpose

Generate a random integer between two given integers, inclusive.

## Syntax

```
returnedInt = randomint(numInt1, numInt2)
```

```
returnedInt - type: int

numInt1 - type: int

numInt2 - type: int
```

## Returns

A random integer in the range from numInt1 to numInt2, inclusive.

## Remarks

Uses the C/C++ rand function to pick a value in the inclusive range [numInt1, numInt2].

## Example

```
@CODE

"output.txt" << randomint(1, 6) << "\n";

@@CODE
```

```
Outputs something like:
```

```
4
```

## See Also

[abs](abs.md), [mod](mod.md), [factorial](factorial.md)

[Math Functions](Table_of_Math_Functions.md)
