[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# addstrval

## Purpose

Add the string *valueString* as a string value to the concept *concept'*s attribute that has name *nameString*.

## Syntax

```
addstrval(concept, nameString, valueString)
```

```
concept - type: con

nameString - type: str

valueString - type: str
```

## Returns

Nothing

## Remarks

If the attribute doesn't exist yet, `addstrval` will create it. If the concept is bad, an error appears in the log output window at runtime.

## Example

```
G("Malibu") = makeconcept(findroot(), "Malibu");

addstrval(G("Malibu"),"Latitude Direction","North");

addstrval(G("Malibu"),"Longitude Direction","West");

addnumval(G("Malibu"),"Latitude value",33);

addnumval(G("Malibu"),"Longitude value",118);

addsval(G("Malibu"),"Route",1+2);
```

## See Also

[addconval](addconval.md), [addsval](addsval.md), [addnumval](addnumval.md), [Knowledge Base Functions](Table_of_Knowledge_Base_Functions.md)
