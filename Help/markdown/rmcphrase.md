[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# rmcphrase

## Purpose

Remove a concept *aConcept*'s phrase.

## Syntax

```
returnedNumber = rmcphrase(aConcept)
```

```
returnedNumber - type: int

aConcept - type: con
```

## Returns

Returns 1 (int) if the concept's phrase was removed successfully, otherwise 0.

## Remarks

## Example

```
G("vp") = makeconcept(findroot(),"verb phrase");

makephrase(G("vp"),"verb");

rmcphrase(G("vp"));
```

## See Also

[rmphrase](rmphrase.md), [rmnode](rmnode.md), [Knowledge Base Functions](Table_of_Knowledge_Base_Functions.md)
