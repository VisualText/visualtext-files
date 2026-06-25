[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# pnmakevar

## Purpose

Make a variable for a given pnode *aPnode*.

## Syntax

```
None = pnmakevar(aPnode, varName, valString);

 
```

```
aPnode - type: pnode

varName - type: str
```

```
valString - type: str
```

```
None = pnmakevar(aPnode, varName, valInteger);

 
```

```
aPnode - type: pnode

varName - type: str
```

```
valInteger - type: int
```

```
None = pnmakevar(aPnode, varName, valPnode);

 
```

```
aPnode - type: pnode

varName - type: str
```

```
valPnode - type: pnode
```

```
None = pnmakevar(aPnode, varName, valCon);

 
```

```
aPnode - type: pnode

varName - type: str
```

```
valCon - type: con
```

```
None = pnmakevar(aPnode, varName, valPhrase);

 
```

```
aPnode - type: pnode

varName - type: str
```

```
valPhrase - type: phrase
```

```
None = pnmakevar(aPnode, varName, valAttribute);

 
```

```
aPnode - type: pnode

varName - type: str
```

```
valAttribute - type: attr
```

```
None = pnmakevar(aPnode, varName, valValue);

 
```

```
aPnode - type: pnode

varName - type: str
```

```
valValue - type: val
```

## Returns

Nothing. Creates the named variable on the given node and sets it to the supplied value. It is an error if the variable already exists with a value, or if the name begins with `$`.

## Remarks

Functionally equivalent to statements such as

N("name", 3) = "xyz";

But, whereas with the G, N, X, and S references the variable name must be a literal string, pnmakevar allows string-valued NLP++ expressions to specify the variable name.  For example:

pnmakevar(N(3), "na" + "me", "xyz");

In this way, the name of a variable can be created dynamically.

## Example

```
@POST

pnmakevar(N(1), "pos", "noun");     # Make a "pos" string variable on the matched node.

@RULES

_xNIL <- _noun @@
```

## See Also

[pnvar](pnvar.md), [Parse Tree Functions](Table_of_Parse_Tree_Functions.md)
