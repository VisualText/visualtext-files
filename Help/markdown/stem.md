# stem

## Purpose

Compute a stem for nouns and verbs.

## Syntax

```
returnedString = stem(word)
```

```
returnedString - type: str

word- type: str
```

## Returns

Returns a lowercase string.  If no stem is computed, returns the given string.

## Remarks

Uses dictionary, morphological, and heuristic methods to compute the stem for a word.  Stems only nouns and verbs.  Assumes that the given string is a valid English word or name, limited to about 35 characters.

## Example

```
@CODE

G("stem") = stem("lounging");

@@CODE
```

## See Also

[suffix](suffix.md), [strendswith](strendswith.md), [strstartswith](strstartswith.md), [String Functions](Table_of_String_Functions.md)
