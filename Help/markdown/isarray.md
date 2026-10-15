[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# isarray

## Purpose

Test whether a value is an array: a value with more than one element.

## Syntax

```
returnedBool = isarray(value)
```

```
returnedBool - type: bool

value - any value: a string, number, concept, parse tree node or array
```

## Returns

1 if the value is an array: a value with more than one element; otherwise 0.

## Remarks

NLP++ is loosely typed, and a function given the wrong kind of value often fails without saying so. **isarray** and the other type tests let code check first. They accept any value and never print a warning, even for an empty one. Pass exactly one argument.

**NEW 4.2.34**

## Example

```
@CODE

L("a")[0] = "x";
L("a")[1] = "y";
"output.txt" << isarray(L("a")) << "\n";   # 1

@@CODE
```

## See Also

[iscon](iscon.md), [isstr](isstr.md), [isnum](isnum.md), [isfloat](isfloat.md), [ispn](ispn.md), [pnvartype](pnvartype.md)

[Special Functions](Table_of_Special_Functions.md)
