[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# strspellcandidate

## Purpose

Select the best spell-correct candidate for a word, given a list of space-separated candidates (as returned by spellcandidates, for example.)

## Syntax

```
returnedString = strspellcandidate(wordString, listString)
```

```
returnedString - type: str

wordString - type: str

listString - type: str
```

## Returns

The single best-matching candidate from the given space-separated list, adjusted to match the letter case of the word (all-uppercase or capitalized).  Returns an empty string if either argument is empty or no candidate is selected.

## Remarks

The candidate list is typically the string returned by [spellcandidates](spellcandidates.md).

## Example

```
@CODE

L("cands") = spellcandidates("recieve");
"output.txt" << strspellcandidate("recieve", L("cands")) << "\n";

@@CODE
```

```
Outputs:
```

```
receive
```

## See Also

[spellcandidates](spellcandidates.md), [spellcorrect](spellcorrect.md), [spellword](spellword.md), [strspellcompare](strspellcompare.md), [Spelling Functions](Table_of_Spelling_Functions.md)
