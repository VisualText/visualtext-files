[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# listnode

## Purpose

Fetch the first node in a given node's list.

## Syntax

```
returnedConcept = listnode(node)
```

```
returnedConcept - type: con

node - type: con
```

## Returns

The first node (CON) in the given node's list, or none if there is none.

## Remarks

## Example

```
G("vp") = makeconcept(findroot(),"verb phrase");

G("phr") = makephrase(G("vp"),"verb");

G("node") = firstnode(G("phr"));

G("first") = listnode(G("node"));
```

## See Also

[firstnode](firstnode.md), [lastnode](lastnode.md), [findnode](findnode.md), [Knowledge Base Functions](Table_of_Knowledge_Base_Functions.md)
