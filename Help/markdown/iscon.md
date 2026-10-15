[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# iscon

## Purpose

Test whether a value is a knowledge base concept.

## Syntax

```
returnedBool = iscon(value)
```

```
returnedBool - type: bool

value - any value: a string, number, concept, parse tree node or array
```

## Returns

1 if the value is a knowledge base concept; otherwise 0.

## Remarks

NLP++ is loosely typed, and a function given the wrong kind of value often fails without saying so. **iscon** and the other type tests let code check first. They accept any value and never print a warning, even for an empty one. Pass exactly one argument.

**NEW 4.2.34**

## Example

```
@CODE

L("c") = findconcept(findroot(), "colors");
if (!iscon(L("c")))
    L("c") = makeconcept(findroot(), "colors");

@@CODE
```

## See Also

[isstr](isstr.md), [isnum](isnum.md), [isfloat](isfloat.md), [ispn](ispn.md), [isarray](isarray.md), [pnvartype](pnvartype.md)

[Special Functions](Table_of_Special_Functions.md)
