[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# $mixcap

## Purpose

Check if the token underlying the node is a mixed-capitalized word.

## Syntax

```
returnedBoolean = variableType("$mixcap")
```

```
returnedBoolean - type: int

variableType - type: N
```

## Returns

Returns **1** if the token is a mixed-capitalized word and **0** if not.

## Remarks

## Example

MIchigan, or abcD

```
@POST
    if (N("$mixcap",1))
        N("mixedcase",1) = 1;
@@POST

@RULES
_word <- _xWILD [one] @@
```

## See Also

[$allcaps]($allcaps.md), [$cap]($cap.md), [$lowercase]($lowercase.md), [$uppercase]($uppercase.md), [Special Variables](NLP_PP_Stuff/Special_Variables.md#table)
