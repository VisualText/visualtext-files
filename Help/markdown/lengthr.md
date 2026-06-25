[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# lengthr

## Purpose

Pre action that succeeds if leaf token length is in the range of lengths (*lengthNumber1*,*lengthNumber2*), inclusive.

## Syntax

```
<fromRuleEltNumber,toRuleEltNumber>lengthr(lengthNumber1,lengthNumber2);
```

```
fromRuleEltNumber - type: int

toRuleEltNumber - type: int

lengthNumber1 - type: int

lengthNumber2 - type: int
```

## Returns

Succeeds (keeps the match) if the leaf token length is within the inclusive range (lengthNumber1, lengthNumber2); otherwise fails and the element does not match.

## Remarks

The length is measured in Unicode characters. The range must be valid: both numbers non-negative and lengthNumber1 not greater than lengthNumber2, otherwise the action reports a bad-range error and fails. This is a single-leaf-token action: if the matched node covers more than one leaf token, the action automatically fails.

## Example

```
@PRE

<1,1>lengthr(3,6);

@RULES

_shortWord <- _xALPHA@@
```

## See Also

[length](length.md), [numrange](numrange.md), [PRE Actions](NLP_PP_Stuff/AT-PRE_Actions.md#table_of_@PRE_Actions)
