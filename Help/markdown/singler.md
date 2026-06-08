# singler

## Purpose

Perform a single tier reduction of a range of rule elements. eg. If finding a period to be end-of-sentence in context, we only want to reduce the period to end-of-sentence, not the whole context.

## Syntax

```
singler(number1, number2)
```

```
number1 - type: int

number2 - type: int
```

## Returns

## Remarks

## Example

# Reduce the _det and _noun to an _np, but # not the node that matched element 3. @POST  singler(1,2); @RULES _np <- _det _noun _xWILD [one fail=(_noun)] @@

## See Also

[single](single.md), [singlex](singlex.md), [singlezap](singlezap.md), [noop](noop.md), [POST Actions](NLP_PP_Stuff/AT-POST_Actions.md#table_of_@POST_Actions)
