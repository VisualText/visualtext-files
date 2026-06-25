[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# spellword

## Purpose

Check if a wordString is a known English word.  Uses an accurate list of English words and their conjugations.

## Syntax

```
returnedBoolean = spellword(wordString)
```

```
returnedBoolean - type: bool

wordString - type: str
```

## Returns

Returns 1 (true) if the word is found in the English word list, otherwise 0 (false).

## Remarks

The word list used by **spellword** is currently not subject to user modification.  But, as always, you can add passes to do any specialized vocabulary handling for your analyzer.

## Example

```
@CODE

if (spellword("receive"))
    "output.txt" << "known\n";
else
    "output.txt" << "unknown\n";

@@CODE
```

```
Outputs:
```

```
known
```

## See Also

[spellcandidates](spellcandidates.md), [strspellcandidate](strspellcandidate.md), [spellcorrect](spellcorrect.md), [strspellcompare](strspellcompare.md), [Spelling Functions](Table_of_Spelling_Functions.md)
