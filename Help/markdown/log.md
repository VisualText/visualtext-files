[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# log

## Purpose

Compute the natural (base e) logarithm of a number.

## Syntax

```
returnedFlt = log(numFlt)
```

```
returnedFlt - type: float

numFlt - type: float
```

## Returns

The natural logarithm of the given number.

## Remarks

Analogous to the log function in C/C++. The argument must be positive. See [logten](logten.md) for the base 10 logarithm.

## Example

```
@CODE

"output.txt" << log(2.718282) << "\n";

@@CODE
```

```
Outputs:
```

```
1
```

## See Also

[sqrt](sqrt.md), [pow](pow.md), [log](log.md), [logten](logten.md)

[Math Functions](Table_of_Math_Functions.md)
