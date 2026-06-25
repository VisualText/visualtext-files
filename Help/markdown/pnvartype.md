[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# pnvartype

## Purpose

Fetch the data type of a parse tree node's variable value.

## Syntax

```
returnedValue = pnvartype(pnode, var_str);
```

```
returnedValue - type: int

pnode - type: pnode

var_str - type: str
```

## Returns

An integer code for the type of the variable's first value:

```
0 - string
1 - int
2 - concept
3 - float
```

## Remarks

Pnvartype looks up the variable named var_str on the given pnode and returns a number describing the type of its first value. Returns nothing if the variable does not exist or has no value.

## Example

```
@POST

if (pnvartype(N(1), "pos") == 0)     # 0 means the value is a string.
   single();

@RULES

_xNIL <- _noun @@
```

## See Also

[pnvar](pnvar.md), [pnvarnames](pnvarnames.md), [pnmakevar](pnmakevar.md), [Parse Tree Functions](Table_of_Parse_Tree_Functions.md)
