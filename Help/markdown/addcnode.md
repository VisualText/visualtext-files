[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# addcnode

## Purpose

Add the named node *nodeName* to the end of the concept *aConcept*'s phrase.

## Syntax

```
returnedConcept = addcnode(aConcept, nodeName)
```

```
returnedConcept - type: con

aConcept - type:  con

nodeName - type: str
```

The second argument may instead be a concept, in which case the new node is a proxy for that concept:

```
returnedConcept = addcnode(aConcept, nodeConcept)
```

```
returnedConcept - type: con

aConcept - type: con

nodeConcept - type: con
```

## Returns

The newly created node (CON) that was added to the end of *aConcept*'s phrase.

## Remarks

## Example

```
G("vp") = makeconcept(findroot(),"verb phrase");

makephrase(G("vp"),"verb");

G("node") = addcnode(G("vp"),"adverb");
```

## See Also

[addnode](addnode.md), [makephrase](makephrase.md), [Knowledge Base Functions](Table_of_Knowledge_Base_Functions.md)
