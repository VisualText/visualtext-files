[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# lowercase

## Purpose

Pre action that succeeds if leaf token is all lowercase.

## Syntax

```
<fromRuleEltNumber,toRuleEltNumber>lowercase();
```

```
fromRuleEltNumber - type: int

toRuleEltNumber - type: int
```

## Returns

Succeeds (keeps the match) if every alphabetic character in the leaf token is lowercase; otherwise fails and the element does not match.

## Remarks

This is a single-leaf-token action: if the matched node covers more than one leaf token, the action automatically fails. Any arguments passed are ignored.

## Example

The action **lowercase** specifies that the first rule element (_xALPHA) must be a word in all lowercase letters in order to be reduced to the suggested node _noun.

```
@PRE

<1,1>lowercase();
```

```
@RULES

_noun <- _xALPHA@@
```

## See Also

[uppercase](uppercase.md), [cap](cap.md), [PRE Actions](NLP_PP_Stuff/AT-PRE_Actions.md#table_of_@PRE_Actions)
