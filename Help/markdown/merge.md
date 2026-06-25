[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# merge

## Purpose

Perform a single tier reduction that dissolves each top level node in the matched phrase.

## Syntax

```
merge()
```

## Returns

Nothing is returned to NLP++. As a side effect, the matched phrase is reduced to a single new node, and each top-level matched node is dissolved so that its children become direct children of the new node.

## Remarks

## Example

```
# Remove the two _adjs nodes

# from the parse tree, merging

# their children under a new

# _adjs node.

@POST

merge();

@RULES

_adjs <- _adjs _adjs @@
```

## See Also

[merger](merger.md), [group](group.md), [excise](excise.md), [splice](splice.md), [POST Actions](NLP_PP_Stuff/AT-POST_Actions.md#table_of_@POST_Actions)
