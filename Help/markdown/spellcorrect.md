[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# spellcorrect

## Purpose

Correct spelling of wordString. If wordString is an unknown word, returns the best spelling guess.

## Syntax

```
returnedString = spellcorrect(wordString)
```

```
returnedString - type: str

wordString - type: str
```

## Returns

The corrected spelling of the word.  If the word is already a known word, it is returned unchanged.  If it is unknown, the best spelling candidate is returned.  The result is adjusted to match the letter case of the input (all-uppercase or capitalized).

## Remarks

If the word is unknown and no spelling candidates can be found, the original word is returned.

## Example

```
@CODE

"output.txt" << spellcorrect("recieve") << "\n";

@@CODE
```

```
Outputs:
```

```
receive
```

## See Also

[spellcandidates](spellcandidates.md), [strspellcandidate](strspellcandidate.md), [spellword](spellword.md), [strspellcompare](strspellcompare.md), [Spelling Functions](Table_of_Spelling_Functions.md)
