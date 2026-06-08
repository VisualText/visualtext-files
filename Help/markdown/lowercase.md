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

## Remarks

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
