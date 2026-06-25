[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# pnpush

## Purpose

Group a single parse tree node under a new nonliteral parent node.

## Syntax

```
returnedValue = pnpush(pnode, name_str);
```

```
returnedValue - type: pnode

pnode - type: pnode

name_str - type: str
```

## Returns

The new parent pnode.

## Remarks

Pnpush groups the given node under a newly created nonliteral parent node named name_str. The name must start with an underscore (`_`); literal node names are not allowed.

It reuses the same parse-tree splice and rule-scanner bookkeeping as the group() builtin, so it is safe to use in @POST regions. All of the original node's variables are copied up onto the new parent node.

New in 06/14/26.

## Example

## See Also

[pnmakevar](pnmakevar.md), [pnpushval](pnpushval.md), [Parse Tree Functions](Table_of_Parse_Tree_Functions.md)
