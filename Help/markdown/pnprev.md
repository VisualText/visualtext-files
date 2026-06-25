[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# pnprev

## Purpose

Fetch a parse tree node *aPnode'*s left sibling if one exists.

## Syntax

```
returnedPnode = pnprev(aPnode)
```

```
returnedPnode - type: pnode

aPnode - type: pnode
```

## Returns

Returns the node's left sibling. Returns nothing if the node is the first in its list of siblings.

## Remarks

## Example

```
@POST

L("sib") = pnprev(N(2));     # Node to the left of the second matched node.

@RULES

_xNIL <- _det _noun @@
```

## See Also

[pnnext](pnnext.md), [pnsingletdown](pnsingletdown.md), [pndown](pndown.md), [pnup](pnup.md), [Parse Tree Functions](Table_of_Parse_Tree_Functions.md)
