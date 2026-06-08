# splice

## Purpose

Dissolve the top level nodes of given range.

## Syntax

```
splice(number1, number2)
```

```
number1 - type: int

number2 - type: int
```

## Returns

## Remarks

## Example

```
# This rule removes the _adjs nodes

# from the parse tree, replacing them

# with their children.

@POST

 splice(1,2);

@RULES

_xNIL <- _adjs _adjs @@
```

## See Also

[excise](excise.md), [group](group.md), [merge](merge.md), [merger](merger.md), [POST Actions](NLP_PP_Stuff/AT-POST_Actions.md#table_of_@POST_Actions)
