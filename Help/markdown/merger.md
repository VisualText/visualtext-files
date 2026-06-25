[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# merger

## Purpose

Perform a single tier reduction that dissolves each top level node in the matched range.

## Syntax

```
merger(number1, number2)
```

```
number1 - type: int

number2 - type: int
```

## Returns

Nothing is returned to NLP++. As a side effect, the nodes in the range from ***number1*** to ***number2*** are reduced to a single new node, and each top-level node in that range is dissolved so that its children become direct children of the new node.

## Remarks

## Example

```
# Remove the two _adjs nodes

# from the parse tree, merging

# their children under a new

# _adjs node.

@POST

merger(1,2);

@RULES

_adjs <- _adjs _adjs _xyz @@
```

## See Also

[merge](merge.md), [group](group.md), [excise](excise.md), [splice](splice.md), [POST Actions](NLP_PP_Stuff/AT-POST_Actions.md#table_of_@POST_Actions)
