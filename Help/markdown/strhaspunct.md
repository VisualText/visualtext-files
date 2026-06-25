[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# strhaspunct

## Purpose

Check if a string contains a punctuation character.

## Syntax

```
returnedBoolean = strhaspunct(string)
```

```
returnedBoolean - type: bool

string - type: str
```

## Returns

True if the string contains at least one punctuation character, otherwise false.

## Remarks

## Example

```
@POST
if (strhaspunct(N("$text",1)))
    excise(1,1);
@@RULES
_token <- _xWILD @@
```

## See Also

[strisalpha](strisalpha.md), [strisdigit](strisdigit.md), [striscaps](striscaps.md), [String Functions](Table_of_String_Functions.md)
