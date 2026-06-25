[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# singlex

## Purpose

Perform a single tier reduction of a range of rule elements. All nodes NOT in the range are EXCISED.

## Syntax

```
singlex(number1, number2)
```

```
number1 - type: int

number2 - type: int
```

## Returns

Nothing is returned to NLP++. As a side effect, the nodes in the range from ***number1*** to ***number2*** are reduced to a single new node, and all matched nodes outside the range are excised (removed) from the parse tree.

## Remarks

## Example

# Reduce the _det and _noun to an _np. # REMOVE the node that matched element 3 # from the parse tree. @POST singlex(1,2); @RULES _np <- _det _noun _xWILD [one fail=(_noun)] @@

## See Also

[singlezap](singlezap.md), [single](single.md), [singler](singler.md), [noop](noop.md), [POST Actions](NLP_PP_Stuff/AT-POST_Actions.md#table_of_@POST_Actions)
