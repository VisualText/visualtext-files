[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# strcontainsnocase

## Purpose

Check if string 1 is contained in string 2, ignoring letter case.

## Syntax

```
returnedBoolean = strcontainsnocase(wordString1, wordString2)
```

```
returnedBoolean - type: bool

wordString1 - type: str

wordString2 - type: str
```

## Returns

True if wordString1 occurs as a substring of wordString2 ignoring letter case, otherwise false.

## Remarks

## Example

```
@POST
if (strcontainsnocase("CAT", N("$text",1)))
    excise(1,1);
@@RULES
_word <- _xWILD @@
```

## See Also

[strcontains](strcontains.md), [strpiece](strpiece.md), [strendswith](strendswith.md), [strstartswith](strstartswith.md), [strsubst](strsubst.md), [String Functions](Table_of_String_Functions.md)
