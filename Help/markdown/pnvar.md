# pnvar

## Purpose

Fetch the value(s) of a parse tree node's *aPnode* variable.

## Syntax

```
returnedValue = pnvar(aPnode, var_str)
```

```
returnedValue - type: var value

aPnode - type: pnode

var_str - type: str
```

## Returns

## Remarks

NLP++ currently doesn't let you parameterize things like **N**("tmp",1).  That is, "tmp" must be a literal string.  Pnvar provides a way around this, by saying pnvar(N(1), "NAME"), where "NAME" can be a literal string, a variable, or string-valued NLP++ expression.  So, something like pnvar(G("node"), G("varname")) lets you dynamically determine the node and variable to fetch.

## Example

## See Also

[varinlist](varinlist.md), [pnmakevar](pnmakevar.md), [Parse Tree Functions](Table_of_Parse_Tree_Functions.md)
