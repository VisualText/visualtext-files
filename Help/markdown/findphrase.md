[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# findphrase

## Purpose

Fetch the phrase for a given concept *aConcept*.

## Syntax

```
returnedPhrase = findphrase(aConcept);
```

```
returnedPhrase - type: phr

aConcept - type: con
```

## Returns

The phrase (PHR) attached to *aConcept*. If the concept has no phrase, an empty/null phrase handle is returned.

## Remarks

## Example

```
G("vp") = makeconcept(findroot(),"verb phrase");

makephrase(G("vp"),"verb");

G("phr") = findphrase(G("vp"));
```

## See Also

[rmphrase](rmphrase.md), [Knowledge Base Functions](Table_of_Knowledge_Base_Functions.md)
