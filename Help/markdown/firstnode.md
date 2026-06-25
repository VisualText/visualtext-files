[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# firstnode

## Purpose

Fetch the first node in a phrase *aPhrase*.

## Syntax

```
returnedConcept = firstnode(aPhrase)
```

```
returnedConcept - type: con

aPhrase - type: phrase
```

## Returns

The first node (CON) in *aPhrase*, or none if the phrase is empty.

## Remarks

## Example

```
G("vp") = makeconcept(findroot(),"verb phrase");

G("phr") = makephrase(G("vp"),"verb");

G("node") = firstnode(G("phr"));
```

## See Also

[lastnode](lastnode.md), [findnode](findnode.md), [listnode](listnode.md), [Knowledge Base Functions](Table_of_Knowledge_Base_Functions.md)
