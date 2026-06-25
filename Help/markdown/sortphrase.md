[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# sortphrase

## Purpose

Sort the nodes in a concept *aConcept'*s phrase in alphabetic order.

## Syntax

```
returnedNumber = sortphrase(aConcept);
```

```
returnedNumber - type: int

aConcept - type: con
```

## Returns

Returns 1 (int) if the phrase was sorted successfully, otherwise 0.

## Remarks

## Example

```
G("vp") = makeconcept(findroot(),"verb phrase");

makephrase(G("vp"),"verb");

addcnode(G("vp"),"adverb");

sortphrase(G("vp"));
```

## See Also

[phraselength](phraselength.md), [Knowledge Base Functions](Table_of_Knowledge_Base_Functions.md)
