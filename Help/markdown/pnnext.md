[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# pnnext

## Purpose

Fetch a parse tree node *aPnode'*s right sibling if one exists.

## Syntax

```
returnedPnode = pnnext(aPnode)
```

```
returnedPnode - type: pnode

aPnode - type: pnode
```

## Returns

Returns the node's right sibling. Returns nothing if the node is the last in its list of siblings.

## Remarks

## Example

```
@POST

L("sib") = pnnext(N(1));     # Node to the right of the first matched node.

@RULES

_xNIL <- _noun @@
```

## See Also

[pnprev](pnprev.md), [pnsingletdown](pnsingletdown.md), [pndown](pndown.md), [pnup](pnup.md), [Parse Tree Functions](Table_of_Parse_Tree_Functions.md)
