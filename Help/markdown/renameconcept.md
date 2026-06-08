[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# renameconcept

## Purpose

Rename concept *aConcept* with new name *newConceptNameStr*.

## Syntax

```
None = renameconcept(aConcept, newConceptNameStr)
```

```
aConcept - type: con

newConceptNameStr - type: str
```

## Returns

Nothing

## Remarks

Does not change attributes and values of existing concept, just the name.

## Example

```
if(findconcept(findroot(),"apples"))

rmconcept(findconcept(findroot(),"apples"));

G("apples") = makeconcept(findroot(),"apples");

addstrval(G("apples"),"have","seeds");

renameconcept(G("apples"),"fruit");

"output.txt" << conceptname(G("apples")) << "\n";
```

This prints the following to output.txt:

```
fruit
```

## See Also

[renamechild](renamechild.md), [Knowledge Base Functions](Table_of_Knowledge_Base_Functions.md)
