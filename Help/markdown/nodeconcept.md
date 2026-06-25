[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# nodeconcept

## Purpose

Fetch the concept that the given node is a proxy for.

## Syntax

```
returnedConcept = nodeconcept(node)
```

```
returnedConcept - type: con

node - type: con
```

## Returns

The old functionality of this has been usurped by the new function *nodeowner*.

The concept (CON) that the given node is a proxy for, or none if the node has no associated concept.

## Remarks

## Example

```
G("vp") = makeconcept(findroot(),"verb phrase");

G("node") = addcnode(G("vp"),G("verb"));

G("con") = nodeconcept(G("node"));
```

## See Also

[Knowledge Base Functions](Table_of_Knowledge_Base_Functions.md)
