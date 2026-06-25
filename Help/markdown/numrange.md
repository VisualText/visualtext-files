[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# numrange

## Purpose

Pre action that succeeds if leaf token is numeric in the given range.

## Syntax

```
<fromRuleEltNumber,toRuleEltNumber>numrange(number1,number2);
```

```
fromRuleEltNumber - type: int

toRuleEltNumber - type: int

number1 - type: int

number2 - type: int
```

## Returns

Succeeds (keeps the match) if the leaf token is numeric and its value lies within the inclusive range (number1, number2); otherwise fails and the element does not match.

## Remarks

The leaf token must convert to a number; a non-numeric token reports an error and fails. The range must be valid: both numbers non-negative and number1 not greater than number2, otherwise the action reports a bad-range error and fails. This is a single-leaf-token action: if the matched node covers more than one leaf token, the action automatically fails.

## Example

```
@PRE

<1,1>numrange(1,31);

@RULES

_dayNumber <- _xNUM@@
```

## See Also

[length](length.md), [lengthr](lengthr.md), [PRE Actions](NLP_PP_Stuff/AT-PRE_Actions.md#table_of_@PRE_Actions)
