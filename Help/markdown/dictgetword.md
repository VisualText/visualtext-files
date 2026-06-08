# dictgetword

## Purpose

Find else add dictionary concept *wordString* to the KB dictionary hierarchy.  Return the concept.

## Syntax

```
returnedWordConcept = dictgetword(wordString)
```

```
returnedWordConcept - type: con

wordString - type: str
```

## Returns

The newly created word concept. If the word cannot be added, returns 0.

## Remarks

The dictionary is a specialized part of the KB hierarchy used to store and lookup words.

## Example

```
See addword.
```

## See Also

[addword](addword.md), [wordindex](wordindex.md), [wordpath](wordpath.md), [rmword](rmword.md), [Knowledge Base Functions](Table_of_Knowledge_Base_Functions.md)
