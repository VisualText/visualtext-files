[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# renameattr

## Purpose

Rename an attribute named *oldAttrNameStr* to *newAttrNameStr* belonging to the concept *aConcept*.

## Syntax

```
renameattr(aConcept, oldAttrNameStr, newAttrNameStr)
```

```
aConcept - type: con

oldAttrNameString - type: str

newAttrNameString - type: str
```

## Returns

Nothing

## Remarks

Does not change values of existing attribute, just the name.

## Example

```
if(findconcept(findroot(),"apples"))

rmconcept(findconcept(findroot(),"apples"));

G("apples") = makeconcept(findroot(),"apples");

addstrval(G("apples"),"have","seeds");

renameconcept(G("apples"),"fruit");

"output.txt" << conceptname(G("apples")) << "\n";

renameattr(G("apples"),"have","are");

"output.txt" << attrname(findattr(G("apples"),"are")) << "\n";

"output.txt" << strval(G("apples"),"are") << "\n";

# rmconcept(G("apples"));
```

This code prints out:

```
fruit

are

seeds
```

## See Also

[attrchange](attrchange.md), [Knowledge Base Functions](Table_of_Knowledge_Base_Functions.md)
