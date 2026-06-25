[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# rmnode

## Purpose

Remove node from the concept *aConcept*'s phrase.

## Syntax

```
returnedNumber = rmnode(aConcept)
```

```
returnedNumber - type: int

aConcept - type: con
```

## Returns

Returns 1 (int) if the node was removed successfully, otherwise 0.

## Remarks

## Example

```
G("vp") = makeconcept(findroot(),"verb phrase");

G("node") = addcnode(G("vp"),"verb");

rmnode(G("node"));
```

## See Also

[rmphrase](rmphrase.md), [rmcphrase](rmcphrase.md), [Knowledge Base Functions](Table_of_Knowledge_Base_Functions.md)
