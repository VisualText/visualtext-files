[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# pnrename

## Purpose

Rename a given parse tree node *aPnode*. This function returns the interned name.

## Syntax

```
returnedString = pnrename(aPnode, newNameString)
```

```
returnedString - type: str

aPnode - type: pnode

newNameString - type: str
```

## Returns

Returns the interned new name string. It is an error if no rename string is supplied.

## Remarks

## Example

```
@POST

pnrename(N(1), "_propernoun");     # Rename the matched node.

@RULES

_xNIL <- _noun @@
```

## See Also

[pnname](pnname.md), [pnroot](pnroot.md), [Parse Tree Functions](Table_of_Parse_Tree_Functions.md)
