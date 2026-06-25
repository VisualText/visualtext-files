[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# strnotequal

## Purpose

Check if string 1 differs from string 2.

## Syntax

```
returnedBoolean = strnotequal(string1, string2)
```

```
returnedBoolean - type: bool

string1 - type: str

string2 - type: str
```

## Returns

True if string1 differs from string2, otherwise false.

## Remarks

## Example

```
@POST
if (strnotequal(N("$text",1), "the"))
    excise(1,1);
@@RULES
_word <- _xWILD @@
```

## See Also

[strequal](strequal.md), [strequalnocase](strequalnocase.md), [strnotequalnocase](strnotequalnocase.md), [String Functions](Table_of_String_Functions.md)
