[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# varne

## Purpose

**Feature-based matching**. Match if the given nodes have a variable called varName whose value doe not equal the string or number in the second argument.

## Syntax

```
<fromRuleEltNumber,toRuleEltNumber>varne(varName,numOrString);
```

```
fromRuleEltNumber - type: int

toRuleEltNumber - type: int

varName - type: string

numOrString - type: int or string
```

## Returns

Succeeds (keeps the match) if the matched node has a variable called varName whose value does not equal the string or number given in the second argument; otherwise fails and the element does not match.

## Remarks

If the second argument is a non-empty string, the value is compared as a string; otherwise it is compared numerically.

## Example

# The example counts nouns with variable called "number" whose value is not "plural". @PRE <1,1> varne("number","plural"); @POST ++G("count nonplural nouns"); @RULES _xNIL <-  _noun @@

## See Also

[var](var.md), [varz](varz.md), [vareq](vareq.md), [vargt](vargt.md), [varlt](varlt.md), [PRE Actions](NLP_PP_Stuff/AT-PRE_Actions.md)
