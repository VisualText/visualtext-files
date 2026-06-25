[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# pnremoveval

## Purpose

Remove a variable from a parse tree node.

## Syntax

```
None = pnremoveval(pnode, var_str);
```

```
pnode - type: pnode

var_str - type: str
```

## Returns

None

## Remarks

Pnremoveval removes the variable named var_str, along with all of its values, from the given pnode. The variable name cannot start with `$`.

## Example

```
@POST

pnremoveval(N(1), "tags");     # Remove the "tags" variable from the matched node.

@RULES

_xNIL <- _noun @@
```

## See Also

[pnpushval](pnpushval.md), [pnrpushval](pnrpushval.md), [pnvar](pnvar.md), [Parse Tree Functions](Table_of_Parse_Tree_Functions.md)
