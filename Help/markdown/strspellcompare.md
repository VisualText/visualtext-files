[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# strspellcompare

## Purpose

Measure the spelling "distance" between wordString1 and wordString2.

## Syntax

```
returnedNumber = strspellcompare(wordString1, wordString2)
```

```
returnedNumber - type: int

wordString1 - type: str

wordString2 - type: str
```

## Returns

An integer "distance" between the two words.  The smaller the number, the more similar the words; 0 means the words match.

## Remarks

The smaller the number returned, indicates the fewer amount of corrections necessary to get from one word string to the other.

## Example

```
@CODE

"output.txt" << strspellcompare("recieve", "receive") << "\n";

@@CODE
```

```
Outputs something like:
```

```
2
```

## See Also

[spellcandidates](spellcandidates.md), [strspellcandidate](strspellcandidate.md), [spellcorrect](spellcorrect.md), [spellword](spellword.md), [Spelling Functions](Table_of_Spelling_Functions.md)
