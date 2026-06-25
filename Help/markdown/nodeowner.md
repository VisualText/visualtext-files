[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# nodeowner

## Purpose

Fetch the concept that owns the given node's phrase.

## Syntax

```
returnedConcept = nodeowner(node)
```

```
returnedConcept - type: con

node - type: con
```

## Returns

The concept (CON) that owns the phrase containing the given node, or none if the node has no owning concept.

## Remarks

This usurps the functionality formerly given to the *nodeconcept* function.

## Example

```
G("vp") = makeconcept(findroot(),"verb phrase");

G("node") = addcnode(G("vp"),"verb");

G("owner") = nodeowner(G("node"));
```

## See Also

[Knowledge Base Functions](Table_of_Knowledge_Base_Functions.md)
