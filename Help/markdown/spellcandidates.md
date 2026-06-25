[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# spellcandidates

## Purpose

Make a list of space separated candidates for spell-correcting a given wordString.

## Syntax

```
returnedString = spellcandidates(wordString)
```

```
returnedString - type: str

wordString - type: str
```

## Returns

A string of space-separated spelling candidates for the given word.  The candidates are returned in lowercase.  Returns an empty string if the input is empty or if no candidates are found.

## Remarks

The given word is lowercased before candidates are generated, so the returned candidates are always lowercase.

## Example

```
@CODE

"output.txt" << spellcandidates("recieve") << "\n";

@@CODE
```

```
Outputs something like:
```

```
receive
```

## See Also

[strspellcandidate](strspellcandidate.md), [spellcorrect](spellcorrect.md), [spellword](spellword.md), [strspellcompare](strspellcompare.md), [Spelling Functions](Table_of_Spelling_Functions.md)
