[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# makephrase

## Purpose

Make a phrase for the concept *aConcept* by creating the named node *nameString*.

## Syntax

```
returnedPhrase = makephrase(aConcept, nameString);
```

```
returnedphrase - type: phr

aConcept - type: con

nameString - type: str
```

## Returns

The newly created phrase (PHR) for *aConcept*.

## Remarks

To add additional nodes to a concept's phrase, use `addcnode`.

## Example

```
G("vp") = makeconcept(findroot(),"verb phrase");

G("phr") = makephrase(G("vp"),"verb");
```

## See Also

[addnode](addnode.md), [addcnode](addcnode.md), [Knowledge Base Functions](Table_of_Knowledge_Base_Functions.md)
