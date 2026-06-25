[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# pnname

## Purpose

Fetch the name of a parse tree node *aPnode*.

## Syntax

```
returnedString = pnname(aPnode)
```

```
returnedString - type: str

aPnode - type: pnode
```

## Returns

Returns the node's name as a string. For nonliteral nodes this is the rule name (for example, `_np`); for literal nodes it is the matched word.

## Remarks

## Example

```
@POST

if (pnname(N(1)) == "_noun")
   single();

@RULES

_xNIL <- _noun @@
```

## See Also

[pnrename](pnrename.md), [pnroot](pnroot.md), [Parse Tree Functions](Table_of_Parse_Tree_Functions.md)
