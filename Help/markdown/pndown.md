[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# pndown

## Purpose

Fetch the first child of the given parse tree node.

## Syntax

```
returnedPnode = pndown(aPnode)
```

```
returnedPnode - type: pnode

aPnode - type: pnode
```

## Returns

Returns the node's first child. Returns nothing if the node is a leaf (has no children).

## Remarks

## Example

```
@POST

L("child") = pndown(N(1));     # First child of the first matched node.

@RULES

_xNIL <- _np @@
```

## See Also

[pnsingletdown](pnsingletdown.md), [pnup](pnup.md), [pnprev](pnprev.md), [pnnext](pnnext.md), [Parse Tree Functions](Table_of_Parse_Tree_Functions.md)
