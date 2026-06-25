[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# findnode

## Purpose

Find a node in a phrase.  There are two variants: to find a node in a phrase *aPhrase* by the node's name *nameString* and to find a node in a phrase *aPhrase* by node number *positionNum*.

## Syntax

```
returnedConcept = findnode(aPhrase, nameString);
```

```
returnedConcept - type: con

aPhrase - type: phr

nameString - type: str
```

```
returnedConcept = findnode(aPhrase, positionNum);
```

```
returnedConcept - type: con

aPhrase - type: phr

positionNum - type: int
```

## Returns

The matching node (CON), or none if no node matches. For the name form, the first node with that name is returned. For the number form, the *positionNum*th node is returned; a *positionNum* of 0 returns the last node.

## Remarks

## Example

```
G("vp") = makeconcept(findroot(),"verb phrase");

G("phr") = makephrase(G("vp"),"verb");

addnode(G("phr"),"adverb",2);

G("node") = findnode(G("phr"),"adverb");
```

## See Also

[firstnode](firstnode.md), [lastnode](lastnode.md), [listnode](listnode.md), [Knowledge Base Functions](Table_of_Knowledge_Base_Functions.md)
