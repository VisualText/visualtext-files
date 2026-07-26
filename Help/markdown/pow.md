[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# pow

## Purpose

Raise a number to the given power.

## Syntax

```
returnedFlt = pow(baseFlt,exponentFlt)
```

```
returnedFlt - type: float

baseFlt - type: float

exponentFlt - type: float
```

## Returns

The base raised to the power of the exponent.

## Remarks

Analogous to the pow function in C/C++. A negative base with a fractional exponent is undefined, and a result outside the range of a float is an error.

## Example

```
@CODE

"output.txt" << pow(2,10) << "\n";

@@CODE
```

```
Outputs:
```

```
1024
```

## See Also

[sqrt](sqrt.md), [pow](pow.md), [log](log.md), [logten](logten.md)

[Math Functions](Table_of_Math_Functions.md)
