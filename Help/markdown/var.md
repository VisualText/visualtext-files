# var

## Purpose

**Feature-based matching**. Match if the given nodes have a variable called varName with non-zero value.

## Syntax

```
<fromRuleEltNumber,toRuleEltNumber>var(varName);
```

```
fromRuleEltNumber - type: int

toRuleEltNumber - type: int

varName - type: string
```

## Returns

## Remarks

## Example

# The example counts nouns that have a non-zero feature (i.e., node variable) called "mass". @PRE <1,1> var("mass"); @POST ++G("count mass nouns"); @RULES _xNIL <- _noun @@

## See Also

[varz](varz.md), [vareq](vareq.md), [varne](varne.md), [PRE Actions](NLP_PP_Stuff/AT-PRE_Actions.md)
