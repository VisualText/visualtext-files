[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# strequal

## Purpose

Check if string 1 is identical to string 2.

## Syntax

```
returnedBoolean = strequal(string1, string2)
```

```
returnedBoolean - type: bool

string1 - type: str

string2 - type: str
```

## Returns

True if string1 is identical to string2, otherwise false.

## Remarks

## Example

```
@POST
if (strequal(N("$text",1), "dog"))
    excise(1,1);
@@RULES
_word <- _xWILD @@
```

## See Also

[strequalnocase](strequalnocase.md), [strnotequal](strnotequal.md), [strnotequalnocase](strnotequalnocase.md), [String Functions](Table_of_String_Functions.md)
