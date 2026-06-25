[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# phraselength

## Purpose

Get the number of nodes in a concept *aConcept*'s phrase.

## Syntax

```
returnedNumber = phraselength(aConcept);
```

```
returnedNumber - type: int

aConcept - type: con
```

## Returns

The number of nodes (int) in *aConcept*'s phrase.

## Remarks

## Example

```
G("vp") = makeconcept(findroot(),"verb phrase");

makephrase(G("vp"),"verb");

addcnode(G("vp"),"adverb");

N("len") = phraselength(G("vp"));
```

## See Also

[sortphrase](sortphrase.md), [Knowledge Base Functions](Table_of_Knowledge_Base_Functions.md)
