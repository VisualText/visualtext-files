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

## Remarks

## Example

```
@PRE

<1,1>cap();

@RULES

_noun <- _xALPHA@@
```

## See Also

[uppercase](uppercase.md), [lowercase](lowercase.md), [PRE Actions](NLP_PP_Stuff/AT-PRE_Actions.md#table_of_@PRE_Actions)
