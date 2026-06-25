[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# unknown

## Purpose

Pre action that succeeds if leaf token is an unknown word.

## Syntax

```
<fromRuleEltNumber,toRuleEltNumber>unknown();
```

```
fromRuleEltNumber - type: int

toRuleEltNumber - type: int
```

## Returns

Succeeds (keeps the match) if the leaf token has been looked up and is not a known word; otherwise fails and the element does not match. If the word has not been looked up, the action fails.

## Remarks

This action is meaningful only if a prior pass has performed the CODE Action **lookup()**.

This mechanism is somewhat obsolete.  Use the function [spellword](spellword.md) instead.

## Example

```
@PRE

<1,1>unknown();

@RULES

_unknownWord <- _xALPHA@@
```

## See Also

[lookup](lookup.md), [PRE Actions](NLP_PP_Stuff/AT-PRE_Actions.md#table_of_@PRE_Actions), [spellword](spellword.md)
