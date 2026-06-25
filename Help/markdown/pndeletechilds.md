[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# pndeletechilds

## Purpose

Remove the children of a given parse tree node *aPnode*.

## Syntax

```
None = pndeletechilds(aPnode)
```

```
aPnode - type: pnode
```

## Returns

Nothing. Deletes the entire subtree beneath the given node, leaving the node itself as a leaf. Has no effect if the node has no children.

## Remarks

## Example

```
@POST

pndeletechilds(N(1));     # Remove the children of the first matched node.

@RULES

_np <- _det _noun @@
```

## See Also

[Parse Tree Functions](Table_of_Parse_Tree_Functions.md)
