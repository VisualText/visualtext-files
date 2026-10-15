[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# isstr

## Purpose

Test whether a value is a string.

## Syntax

```
returnedBool = isstr(value)
```

```
returnedBool - type: bool

value - any value: a string, number, concept, parse tree node or array
```

## Returns

1 if the value is a string; otherwise 0.

## Remarks

NLP++ is loosely typed, and a function given the wrong kind of value often fails without saying so. **isstr** and the other type tests let code check first. They accept any value and never print a warning, even for an empty one. Pass exactly one argument. A string of digits such as "42" is a string, and so is the empty string "".

**NEW 4.2.34**

## Example

```
@CODE

if (isstr(N("lemma", 1)))
    "lemmas.txt" << N("lemma", 1) << "\n";

@@CODE
```

## See Also

[iscon](iscon.md), [isnum](isnum.md), [isfloat](isfloat.md), [ispn](ispn.md), [isarray](isarray.md), [pnvartype](pnvartype.md)

[Special Functions](Table_of_Special_Functions.md)
