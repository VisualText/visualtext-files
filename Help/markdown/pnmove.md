# pnmove

## Purpose

Programmatically move a node in the parse tree..

## Syntax

```
returnedPnode = pnmove(node,tonode,before_after_n)
```

```
returnedPnode - type: pnode

pnode- type: node         The node to be moved

pnode- type: tonode       The node to move to

after_n - type: int       If == 1, insert after. If == 0, insert before
```

## Returns

Returns the moved node.

## Remarks

Can only be used within the @CODE region, not meant to be used in rule action regions.

## Example

# Switch places of first two children of parse tree root (assumes they exist). L("n1") = pndown(pnroot()); L("n2") = pnnext(L("n1")); pnmove(L("n1"),L("n2"),1);

## See Also

[pninsert](pninsert.md)
