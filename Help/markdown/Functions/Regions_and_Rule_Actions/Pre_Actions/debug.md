[← Help Contents](../../../index.md) | [📘 NLP++ Textbook](../../../NLP++_Textbook.md)

# debug

## Purpose

Pre action that succeeds unconditionally. Used to place a C++ breakpoint at a particular rule.

## Syntax

```
<fromRuleEltNumber,toRuleEltNumber>debug;
```

```
fromRuleEltNumber - type: int

toRuleEltNumber - type: int
```

## Returns

## Remarks

debug can appear in the PRE, CHECK and POST regions.

## Example

```
@PRE

<1,1> debug();
```

```
@RULES
```

```
_xNIL <- _xALPHA @@
```

## See Also

[Special Functions](../../../Table_of_Special_Functions.md), [PRE Actions](../../../NLP_PP_Stuff/AT-PRE_Actions.md#table_of_@PRE_Actions)
