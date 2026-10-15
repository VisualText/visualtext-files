[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# ispn

## Purpose

Test whether a value is a parse tree node.

## Syntax

```
returnedBool = ispn(value)
```

```
returnedBool - type: bool

value - any value: a string, number, concept, parse tree node or array
```

## Returns

1 if the value is a parse tree node; otherwise 0.

## Remarks

NLP++ is loosely typed, and a function given the wrong kind of value often fails without saying so. **ispn** and the other type tests let code check first. They accept any value and never print a warning, even for an empty one. Pass exactly one argument.

**NEW 4.2.34**

## Example

```
@CODE

L("n") = N("head", 1);
if (ispn(L("n")))
    "output.txt" << pnname(L("n")) << "\n";

@@CODE
```

## See Also

[iscon](iscon.md), [isstr](isstr.md), [isnum](isnum.md), [isfloat](isfloat.md), [isarray](isarray.md), [pnvartype](pnvartype.md)

[Special Functions](Table_of_Special_Functions.md)
