[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

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

Returns the value(s) of the named variable on the given node, as an array. Names beginning with `$` fetch special (built-in) node variables such as `$text`. Returns nothing if the variable has no value.

## Remarks

NLP++ currently doesn't let you parameterize things like **N**("tmp",1).  That is, "tmp" must be a literal string.  Pnvar provides a way around this, by saying pnvar(N(1), "NAME"), where "NAME" can be a literal string, a variable, or string-valued NLP++ expression.  So, something like pnvar(G("node"), G("varname")) lets you dynamically determine the node and variable to fetch.

## Example

```
@POST

G("pos") = pnvar(N(1), "pos");     # Fetch the "pos" variable from the matched node.

@RULES

_xNIL <- _noun @@
```

## See Also

[varinlist](varinlist.md), [pnmakevar](pnmakevar.md), [Parse Tree Functions](Table_of_Parse_Tree_Functions.md)
