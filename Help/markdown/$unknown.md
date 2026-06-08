[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# $unknown

## Purpose

Check if the token underlying a node is an unknown word.

## Syntax

```
returnedBoolean = variableType("$unknown"[, number])
```

```
returnedBoolean - type: bool

variableType - type: N

number - type: int
```

## Returns

Returns **1** if the token is an unknown word and **0** if the token is a known word.

## Remarks

Requires a **lookup**( ) CODE Action prior to any use of this special variable.

| **WARNING**: This special variable is not identical to the @PRE action, **unknown**(). $unknown will traverse down to the leafiest node it can find, in order to perform its check. The @PRE action only chains down if the [s] flag is present in the associated phrase element(s). Also, $unknown is not stopped by a [base] attribute in a node. |
| --- |

## Example

```
@RULES
```

```
@@RULES
```

## See Also

[$exists]($exists.md), [Special Variables](NLP_PP_Stuff/Special_Variables.md#table)
