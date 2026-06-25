[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# excise

## Purpose

Excise the nodes matching the range of elements from *ruleEltNumber1 *to *ruleEltNumber2* from the parse tree.

## Syntax

```
excise(ruleEltNumber1, ruleEltNumber2)
```

## Returns

Nothing is returned to NLP++. As a side effect, the nodes matching the range of rule elements (and their subtrees) are excised (removed and deleted) from the parse tree.

## Remarks

For multiple excise actions, operations must be ordered such that the highest number is listed first in the operation.

## Example

```
# This rule excises all whitespace found in the current context.

@POST

  excise(1,1);

@RULES

_xNIL <- _xWHITE [plus] @@
```

## See Also

[POST Actions](NLP_PP_Stuff/AT-POST_Actions.md#table_of_@POST_Actions)
