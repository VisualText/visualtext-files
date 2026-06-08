[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# vareq

## Purpose

**Feature-based matching**. Match if the given nodes have a variable called varName whose value equals the string or number in the second argument.

## Syntax

```
<fromRuleEltNumber,toRuleEltNumber>vareq(varName,numOrString);
```

```
fromRuleEltNumber - type: int

toRuleEltNumber - type: int

varName - type: string

numOrString - type: int or string
```

## Returns

## Remarks

## Example

# The example counts nouns with variable called "number" whose value is "plural". @PRE <1,1> vareq("number","plural"); @POST ++G("count plural nouns"); @RULES _xNIL <- _noun @@

## See Also

[var](var.md), [varz](varz.md), [varne](varne.md), [PRE Actions](NLP_PP_Stuff/AT-PRE_Actions.md)
