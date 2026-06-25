[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# renamechild

## Purpose

Rename the child concept of a concept *parentConcept* with new name *newNameStr*.  Find child by number *childNumber*

## Syntax

```
returnedNumber = renamechild(parentConcept, childNumber, newNameStr)
```

```
returnedNumber - type: int

parentConcept - type: con

childNumber - type: int

newNameStr - type: str
```

## Returns

Nothing

## Remarks

Does not change attributes or values of existing child concept, just the name. If indexed out of bounds of the parent concept, throws an error message in the output log.

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

G("aChild") = makeconcept(G("apples"),"child");

renamechild(G("apples"),1,"descendent");

# rmconcept(G("apples"));
```

This code prints out:

```
fruit

are

seeds
```

After processing, the KB looks like this:

![](../helps/Image%20Files/fruitareseeds.gif)

## See Also

[renameconcept](renameconcept.md), [Knowledge Base Functions](Table_of_Knowledge_Base_Functions.md)
