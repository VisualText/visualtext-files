[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# varlt

## Purpose

**Feature-based matching**. Match if the given nodes have a variable called varName whose numeric value is less than the number in the second argument.

## Syntax

```
<fromRuleEltNumber,toRuleEltNumber>varlt(varName,num);
```

```
fromRuleEltNumber - type: int

toRuleEltNumber - type: int

varName - type: string

num - type: int
```

## Returns

Succeeds (keeps the match) if the matched node has a variable called varName whose numeric value is less than num; otherwise fails and the element does not match.

## Remarks

The comparison is defined only numerically. If the variable holds a string value (or is absent), the match fails.

## Example

# The example counts nouns with a variable called "count" whose value is less than 5. @PRE <1,1> varlt("count",5); @POST ++G("count low-count nouns"); @RULES _xNIL <- _noun @@

## See Also

[vargt](vargt.md), [vareq](vareq.md), [varne](varne.md), [var](var.md), [varz](varz.md), [PRE Actions](NLP_PP_Stuff/AT-PRE_Actions.md)
