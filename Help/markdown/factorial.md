[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# factorial

## Purpose

Compute the factorial of a non-negative integer.

## Syntax

```
returnedInt = factorial(numInt)
```

```
returnedInt - type: int

numInt - type: int
```

## Returns

The factorial of the given number (numInt!). The factorial of 0 and 1 is 1.

## Remarks

The argument must be non-negative; a negative value produces an error. An error is also raised if the result would overflow the integer range.

## Example

```
@CODE

"output.txt" << factorial(5) << "\n";

@@CODE
```

```
Outputs:
```

```
120
```

## See Also

[abs](abs.md), [mod](mod.md), [logten](logten.md)

[Math Functions](Table_of_Math_Functions.md)
