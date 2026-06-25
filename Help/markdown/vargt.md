[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# vargt

## Purpose

**Feature-based matching**. Match if the given nodes have a variable called varName whose numeric value is greater than the number in the second argument.

## Syntax

```
<fromRuleEltNumber,toRuleEltNumber>vargt(varName,num);
```

```
fromRuleEltNumber - type: int

toRuleEltNumber - type: int

varName - type: string

num - type: int
```

## Returns

## Remarks

The comparison is defined only numerically. If the variable holds a string value (or is absent), the match fails.

## Example

# The example counts nouns with a variable called "count" whose value is greater than 5. @PRE <1,1> vargt("count",5); @POST ++G("count high-count nouns"); @RULES _xNIL <- _noun @@

## See Also

[varlt](varlt.md), [vareq](vareq.md), [varne](varne.md), [var](var.md), [varz](varz.md), [PRE Actions](NLP_PP_Stuff/AT-PRE_Actions.md)
