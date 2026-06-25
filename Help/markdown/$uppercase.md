[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# $uppercase

## Purpose

Check if the token underlying the node is all uppercase.

## Syntax

```
returnedBoolean = variableType("$uppercase")
```

```
returnedBoolean - type: int

variableType - type: N
```

## Returns

Returns **1** if the token is all uppercase and **0** if not. If multiple words (even if all words are capitalized) returns **0**.

## Remarks

| **WARNING**: **$uppercase** is not identical to the @PRE action **uppercase**( ). $uppercase will traverse down to the leafiest node it can find, in order to perform its check. The @PRE action only chains down if the [s] flag is present in the associated phrase element(s). Also, $uppercase is not stopped by a [base] attribute in a node. |
| --- |

## Example

```
@POST
    if (N("$uppercase",1))
        N("acronym",1) = 1;
@@POST

@RULES
_word <- _xWILD [one] @@
```

## See Also

[$allcaps]($allcaps.md), [$cap]($cap.md), [$lowercase]($lowercase.md), [$mixcap]($mixcap.md), [Special Variables](NLP_PP_Stuff/Special_Variables.md#table)
