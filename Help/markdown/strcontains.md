[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# strcontains

## Purpose

Check if string 1 is contained in string 2.

## Syntax

```
returnedBoolean = strcontains(string1, string2)
```

```
returnedBoolean - type: bool

string1 - type: str

string2 - type: str
```

## Returns

True if string1 occurs as a substring of string2, otherwise false.

## Remarks

## Example

```
@POST
if (strcontains("cat", N("$text",1)))
    excise(1,1);
@@RULES
_word <- _xWILD @@
```

## See Also

[strcontainsnocase](strcontainsnocase.md), [strpiece](strpiece.md), [strsubst](strsubst.md), [strendswith](strendswith.md), [strstartswith](strstartswith.md), [String Functions](Table_of_String_Functions.md)
