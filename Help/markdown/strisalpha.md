[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# strisalpha

## Purpose

Check if a string is all alphabetic characters.

## Syntax

```
returnedBoolean = strisalpha(string)
```

```
returnedBoolean - type: bool

string - type: str
```

## Returns

True if every character in the string is alphabetic, otherwise false.

## Remarks

## Example

```
@POST
if (strisalpha(N("$text",1)))
    excise(1,1);
@@RULES
_word <- _xWILD @@
```

## See Also

[strisdigit](strisdigit.md), [String Functions](Table_of_String_Functions.md)
