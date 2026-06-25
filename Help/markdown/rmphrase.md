[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# rmphrase

## Purpose

Remove the phrase *aPhrase* from its concept.

## Syntax

```
returnedNumber = rmphrase(aPhrase)
```

```
returnedNumber - type: int

aPhrase - type: phrase
```

## Returns

Returns 1 (int) if the phrase was removed successfully, otherwise 0.

## Remarks

## Example

```
G("vp") = makeconcept(findroot(),"verb phrase");

G("phr") = makephrase(G("vp"),"verb");

rmphrase(G("phr"));
```

## See Also

[rmcphrase](rmcphrase.md), [rmnode](rmnode.md), [Knowledge Base Functions](Table_of_Knowledge_Base_Functions.md)
