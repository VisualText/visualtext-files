[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# suffix

## Purpose

See if given string is a suffix of given word.

## Syntax

```
returnedBoolean = suffix(word, suff)
```

```
returnedBoolean - type: bool

word- type: str

suff- type: str
```

## Returns

## Remarks

Uses morphological information and heuristics to see if the word's ending is a reasonable suffix.  For example, given "bolts" and "s" as candidate suffix, suffix("bolts","s") tries to determine if "s" is a suffix of "bolts", that is, if "bolts" is either a plural noun or a third person singular verb form.  Suffix is not foolproof, but provides a good indication based on morphological and lexical knowledge and heuristics.

The related function **strendswith** merely does a literal check for the end part of a string.

## Example

```
@CHECK

if (!suffix(N("$text",1),"s"))

fail();

@RULES

_snoun [layer=(_sverb)] <- _xALPHA @@
```

## See Also

[strisupper](strisupper.md), [strendswith](strendswith.md), [strendswith](strendswith.md), [String Functions](Table_of_String_Functions.md)
