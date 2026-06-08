# $lowercase

## Purpose

Check if the token underlying the node is all lowercase.

## Syntax

```
returnedBoolean = variableType("$lowercase")
```

```
returnedBoolean - type: int

variableType - type: N
```

## Returns

Returns **1** if the token is all lowercase and **0** if not. If multiple words (even if all words are lowercase) returns **0**.

## Remarks

| **WARNING**: $lowercase is not identical to the @PRE action **lowercase**( ). $lowercase will traverse down to the leafiest node it can find, in order to perform its check. The @PRE action only chains down if the [s] flag is present in the associated phrase element(s). Also, $lowercase is not stopped by a [base] attribute in a node. |
| --- |

## Example

## See Also

[$allcaps]($allcaps.md), [$cap]($cap.md), [$mixcap]($mixcap.md), [$uppercase]($uppercase.md), [Special Variables](NLP_PP_Stuff/Special_Variables.md#table)
