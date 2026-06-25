[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# renamenode

## Purpose

Rename a node's name *oldName* or the numth node *number* in a phrase *aPhrase* with a new name *newName*.

## Syntax

```
returnedNumber = renamenode(aPhrase, oldName, newName)
```

```
returnedNumber - type: int

aPhrase - type: phrase

oldName - type: str

newName - type: str
```

```
returnedNumber = renamenode(aPhrase, number, newName)
```

```
returnedNumber - type: int

aPhrase - type: phrase

number - type: int

newName - type: str
```

## Returns

Returns 1 (int) if the node was renamed successfully, otherwise 0.

## Remarks

## Example

```
G("vp") = makeconcept(findroot(),"verb phrase");

G("phr") = makephrase(G("vp"),"verb");

renamenode(G("phr"),"verb","verbnode");
```

## See Also

[Knowledge Base Functions](Table_of_Knowledge_Base_Functions.md)
