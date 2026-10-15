[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# isnum

## Purpose

Test whether a value is an integer.

## Syntax

```
returnedBool = isnum(value)
```

```
returnedBool - type: bool

value - any value: a string, number, concept, parse tree node or array
```

## Returns

1 if the value is an integer; otherwise 0.

## Remarks

NLP++ is loosely typed, and a function given the wrong kind of value often fails without saying so. **isnum** and the other type tests let code check first. They accept any value and never print a warning, even for an empty one. Pass exactly one argument. A variable that was never set reads as 0 in NLP++, so it counts as an integer.

**NEW 4.2.34**

## Example

```
@CODE

if (isnum(N("count", 1)) && N("count", 1) > 2)
    "output.txt" << "frequent\n";

@@CODE
```

## See Also

[iscon](iscon.md), [isstr](isstr.md), [isfloat](isfloat.md), [ispn](ispn.md), [isarray](isarray.md), [pnvartype](pnvartype.md)

[Special Functions](Table_of_Special_Functions.md)
