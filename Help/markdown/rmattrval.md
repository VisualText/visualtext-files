[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# rmattrval

## Purpose

Remove the string *valNameString* as a string value of the concept *aConcept*'s attribute that has name *attrNameStr*.

## Syntax

```
NULL = rmattrval(aConcept, attrNameStr, valNameStr)
```

```
aConcept - type: con

attrNameString - type: str

valNameString - type: str
```

## Returns

Nothing

## Remarks

`rmattrval` also removes the attribute.

## Example

```
G("Malibu") = makeconcept(findroot(), "Malibu");

addstrval(G("Malibu"),"Latitude Direction","North");

rmattrval(G("Malibu"),"Latitude Direction","North");
```

## See Also

[rmval](rmval.md), [rmvals](rmvals.md), [rmattr](rmattr.md), [rmattrs](rmattrs.md), [Knowledge Base Functions](Table_of_Knowledge_Base_Functions.md)
