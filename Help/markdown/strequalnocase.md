[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# strequalnocase

## Purpose

Check if string 1 is identical to string 2, ignoring letter case.

## Syntax

```
returnedBoolean = strnotequalnocase(wordString1, wordString2)
```

```
returnedBoolean - type: bool

wordString1 - type: str

wordString2 - type: str
```

## Returns

True if wordString1 equals wordString2 ignoring letter case, otherwise false.

## Remarks

## Example

```
@POST
if (strequalnocase(N("$text",1), "The"))
    excise(1,1);
@@RULES
_word <- _xWILD @@
```

## See Also

[strequal](strequal.md), [strnotequal](strnotequal.md), [strnotequalnocase](strnotequalnocase.md), [String Functions](Table_of_String_Functions.md)
