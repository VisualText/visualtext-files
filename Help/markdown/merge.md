# merge

## Purpose

Perform a single tier reduction that dissolves each top level node in the matched phrase.

## Syntax

```
merge()
```

## Returns

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
