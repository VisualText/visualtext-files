[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# lastnode

## Purpose

Fetch the last node in a phrase *aPhrase*.

## Syntax

```
returnedConcept = lastnode(aPhrase)
```

```
returnedConcept - type: con

aPhrase - type: phrase
```

## Returns

The last node (CON) in *aPhrase*, or none if the phrase is empty.

## Remarks

## Example

```
G("vp") = makeconcept(findroot(),"verb phrase");

G("phr") = makephrase(G("vp"),"verb");

addnode(G("phr"),"adverb",2);

G("node") = lastnode(G("phr"));
```

## See Also

[firstnode](firstnode.md), [listnode](listnode.md), [findnode](findnode.md), [Knowledge Base Functions](Table_of_Knowledge_Base_Functions.md)
