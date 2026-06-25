[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# strisdigit

## Purpose

Check if a string is all numeric characters.

## Syntax

```
returnedBoolean = strisdigit(string)
```

```
returnedBoolean - type: bool

string - type: str
```

## Returns

True if every character in the string is a digit, otherwise false.

## Remarks

## Example

```
@POST
if (strisdigit(N("$text",1)))
    excise(1,1);
@@RULES
_num <- _xWILD @@
```

## See Also

[strisalpha](strisalpha.md), [String Functions](Table_of_String_Functions.md)
