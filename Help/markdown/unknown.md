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

## Remarks

This action is meaningful only if a prior pass has performed the CODE Action **lookup()**.

This mechanism is somewhat obsolete.  Use the function [spellword](spellword.md) instead.

## Example

## See Also

[lookup](lookup.md), [PRE Actions](NLP_PP_Stuff/AT-PRE_Actions.md#table_of_@PRE_Actions), [spellword](spellword.md)
