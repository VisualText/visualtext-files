# strstartswith

## Purpose

Check if a string starts with the given substring.

## Syntax

```
returnedBoolean = strstartswith(wordString, suffixString)
```

```
returnedBoolean - type: bool

wordString - type: str

suffixString - type: str
```

## Returns

## Remarks

Unlike the function called **suffix**, **strstartswith** does a simple check for terminal string.

## Example

```
@POST

if (!strstartswith(N("$text",1),"ing"))

 fail();

@RULES

_ving <- _verb @@
```

## See Also

[strcontains](strcontains.md), [strcontainsnocase](strcontainsnocase.md), [strpiece](strpiece.md), [strsubst](strsubst.md), [suffix](suffix.md), [String Functions](Table_of_String_Functions.md)
