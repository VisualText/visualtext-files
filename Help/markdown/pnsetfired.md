[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# pnsetfired

## Purpose

Set the fired flag of a parse tree node.

## Syntax

```
None = pnsetfired(pnode, num);
```

```
pnode - type: pnode

num - type: int
```

## Returns

None

## Remarks

Pnsetfired sets the fired flag of the given pnode. The num argument must be 0 or 1; any other value is out of range. When the flag is set to 1, the parse's display tree is enabled.

## Example

```
@POST

pnsetfired(N(1), 1);     # Mark the first matched node as fired.

@RULES

_xNIL <- _noun @@
```

## See Also

[pnvar](pnvar.md), [pnvarnames](pnvarnames.md), [Parse Tree Functions](Table_of_Parse_Tree_Functions.md)
