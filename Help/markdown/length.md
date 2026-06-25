[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# length

## Purpose

Pre action that succeeds if leaf token has length exactly equal to* lengthNumber*.

## Syntax

```
<fromRuleEltNumber,toRuleEltNumber>length(lengthNumber);
```

```
fromRuleEltNumber - type: int

toRuleEltNumber - type: int

lengthNumber - type: int
```

## Returns

Succeeds (keeps the match) if the leaf token has length exactly equal to lengthNumber; otherwise fails and the element does not match.

## Remarks

The length is measured in Unicode characters. This is a single-leaf-token action: if the matched node covers more than one leaf token, the action automatically fails.

## Example

```
@PRE

<1,1>length(3);

@RULES

_threeLetterWord <- _xALPHA@@
```

## See Also

[lengthr](lengthr.md), [numrange](numrange.md), [PRE Actions](NLP_PP_Stuff/AT-PRE_Actions.md#table_of_@PRE_Actions)
