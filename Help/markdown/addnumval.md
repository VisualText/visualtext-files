[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# addnumval

## Purpose

Add the number *valueNumber* as a numeric value to the concept *concept*'s attribute that has name *attrNameString*.

## Syntax

```
addnumval(concept, attrNameString, valueNumber)
```

```
concept - type: con

attrNameString - type: str

valueNumber - type: int
```

## Returns

Nothing

## Remarks

If the attribute doesn't exist yet, `addnumval` will create it. If the concept is bad, an error appears in the log output window at runtime.

## Example

```
@CODE

G("Malibu") = makeconcept(findroot(), "Malibu");

addstrval(G("Malibu"),"Latitude Direction","North");

addstrval(G("Malibu"),"Longitude Direction","West");

addnumval(G("Malibu"),"Latitude value",33);

addnumval(G("Malibu"),"Longitude value",118);

addsval(G("Malibu"),"Route",1+2);
```

## See Also

[addattr](addattr.md), [addsval](addsval.md), [addstrval](addstrval.md), [Knowledge Base Functions](Table_of_Knowledge_Base_Functions.md)
