[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# uppercase

## Purpose

Pre action that succeeds if leaf token is all uppercase.

## Syntax

```
<fromRuleEltNumber,toRuleEltNumber>uppercase();
```

```
fromRuleEltNumber - type: int

toRuleEltNumber - type: int
```

## Returns

## Remarks

## Example

The action **uppercase** specifies that the first rule element (_xALPHA) must be a word in all capital letters in order to be reduced to the suggested node _noun.

```
@PRE

<1,1>uppercase();
```

```
@RULES

_noun <- _xALPHA@@
```

## See Also

[lowercase](lowercase.md), [cap](cap.md), [PRE Actions](NLP_PP_Stuff/AT-PRE_Actions.md#table_of_@PRE_Actions)
