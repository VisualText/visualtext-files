[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# isfloat

## Purpose

Test whether a value is a floating-point number.

## Syntax

```
returnedBool = isfloat(value)
```

```
returnedBool - type: bool

value - any value: a string, number, concept, parse tree node or array
```

## Returns

1 if the value is a floating-point number; otherwise 0.

## Remarks

NLP++ is loosely typed, and a function given the wrong kind of value often fails without saying so. **isfloat** and the other type tests let code check first. They accept any value and never print a warning, even for an empty one. Pass exactly one argument.

**NEW 4.2.34**

## Example

```
@CODE

L("x") = 4.5;
"output.txt" << isfloat(L("x")) << "\n";   # 1

@@CODE
```

## See Also

[iscon](iscon.md), [isstr](isstr.md), [isnum](isnum.md), [ispn](ispn.md), [isarray](isarray.md), [pnvartype](pnvartype.md)

[Special Functions](Table_of_Special_Functions.md)
