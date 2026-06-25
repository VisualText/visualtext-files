[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# pnroot

## Purpose

Fetch the root of the parse tree.

## Syntax

```
returnedPnode = pnroot()
```

```
returnedPnode - type: pnode
```

## Returns

Returns the root node of the current parse tree.

## Remarks

## Example

```
@POST

L("top") = pndown(pnroot());     # First child under the root of the parse tree.

@RULES

_xNIL <- _noun @@
```

## See Also

[pnname](pnname.md), [pnrename](pnrename.md), [Parse Tree Functions](Table_of_Parse_Tree_Functions.md)
