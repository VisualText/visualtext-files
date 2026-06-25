[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# $cap

## Purpose

Check if the token underlying the node is a capitalized word.

## Syntax

```
returnedBoolean = variableType("$cap")
```

```
returnedBoolean - type: int

variableType - type: N
```

## Returns

Returns **1** if the token is a capitalized word and **0** if not.

## Remarks

| **WARNING**: $cap is not identical to the @PRE action **cap**( ). $cap will traverse down to the leafiest node it can find, in order to perform its check. The @PRE action only chains down if the [s] flag is present in the associated phrase element(s). Also, $cap is not stopped by a [base] attribute in a node. |
| --- |

## Example

```
@POST
    if (N("$cap",1))
        N("proper",1) = 1;
@@POST

@RULES
_word <- _xWILD [one] @@
```

## See Also

[$allcaps]($allcaps.md), [$lowercase]($lowercase.md), [$mixcap]($mixcap.md), [$uppercase]($uppercase.md), [Special Variables](NLP_PP_Stuff/Special_Variables.md#table)
