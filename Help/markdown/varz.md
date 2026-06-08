[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# varz

## Purpose

**Feature-based matching**. Match if the given nodes have a variable called varName with zero value.

## Syntax

```
<fromRuleEltNumber,toRuleEltNumber>varz(varName);
```

```
fromRuleEltNumber - type: int

toRuleEltNumber - type: int

varName - type: string
```

## Returns

## Remarks

## Example

# The example counts nouns that have a zero feature (i.e., node variable) called "mass". @PRE <1,1> varz("mass"); @POST ++G("count nonmass nouns"); @RULES _xNIL <- _noun @@

## See Also

[var](var.md), [vareq](vareq.md), [varne](varne.md), [PRE Actions](NLP_PP_Stuff/AT-PRE_Actions.md)
