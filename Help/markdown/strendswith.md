# strendswith

## Purpose

Check if a string is terminated by the given substring.

## Syntax

```
returnedBoolean = strendswith(wordString, suffixString)
```

```
returnedBoolean - type: bool

wordString - type: str

suffixString - type: str
```

## Returns

## Remarks

Unlike the function called **suffix**, **strendswith** does a simple check for terminal string.

## Example

```
@POST

if (!strendswith(N("$text",1),"ing"))

 fail();

@RULES

_ving <- _verb @@
```

## See Also

[strendswith](strendswith.md), [strcontains](strcontains.md), [strcontainsnocase](strcontainsnocase.md), [strpiece](strpiece.md), [strsubst](strsubst.md), [suffix](suffix.md), [String Functions](Table_of_String_Functions.md)
