# pninsert

## Purpose

Programmatically insert a nonliteral node into the parse tree.

## Syntax

```
returnedPnode = pninsert(name,pnode,after_n)
```

```
returnedPnode - type: pnode

name - type: str          Name for nonliteral node

pnode- type: node         Node to insert after or before

after_n - type: int       If == 1, insert after. If == 0, insert before
```

## Returns

Returns the created and inserted node.

## Remarks

Can only be used within the @CODE region, not meant to be used in rule action regions.

## Example

# Get the root node of the parse tree, go to its first child, add a _BLANKLINE node after the child. # This function helps place separators and other markers or sentinels into a parse tree. L("n") = pndown(pnroot()); pninsert("_BLANKLINE",L("n"),1);

## See Also

[pnmove](pnmove.md)
