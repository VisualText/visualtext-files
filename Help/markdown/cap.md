[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# cap

## Purpose

Pre action that succeeds if leaf token has capitalized first letter.

## Syntax

```
<fromRuleEltNumber,toRuleEltNumber>cap();
```

```
fromRuleEltNumber - type: int

toRuleEltNumber - type: int
```

## Returns

Succeeds (keeps the match) if the leaf token begins with an uppercase alphabetic letter; otherwise fails and the element does not match. A token whose first character is not alphabetic always fails.

## Remarks

This is a single-leaf-token action. If the matched node covers more than one leaf token, the action automatically fails. PRE actions disregard the **base** attribute, looking under it to the leaf node. Any arguments passed are ignored.

## Example

```
@PRE

<1,1>cap();

@RULES

_noun <- _xALPHA@@
```

## See Also

[uppercase](uppercase.md), [lowercase](lowercase.md), [PRE Actions](NLP_PP_Stuff/AT-PRE_Actions.md#table_of_@PRE_Actions)
