[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# pnreplaceval

## Purpose

Replace the value of pnode's variable.

## Syntax

```
None = pnreplaceval(aPnode, varName, valString);
```

```
aPnode - type: pnode

varName - type: str
```

```
valString - type: str
```

```
None = pnreplaceval(aPnode, varName, valInteger);
```

```
aPnode - type: pnode

varName - type: str
```

```
valInteger - type: int
```

```
None = pnreplaceval(aPnode, varName, valPnode);
```

```
aPnode - type: pnode

varName - type: str
```

```
valPnode - type: pnode
```

```
None = pnreplaceval(aPnode, varName, valCon);
```

```
aPnode - type: pnode

varName - type: str
```

```
valCon - type: con
```

```
None = pnreplaceval(aPnode, varName, valPhrase);
```

```
aPnode - type: pnode

varName - type: str
```

```
valPhrase - type: phrase
```

```
None = pnreplaceval(aPnode, varName, valAttribute);
```

```
aPnode - type: pnode

varName - type: str
```

```
valAttribute - type: attr
```

```
None = pnreplaceval(aPnode, varName, valValue);
```

```
aPnode - type: pnode

varName - type: str
```

```
valValue - type: val
```

## Returns

Nothing. Replaces all current values of the named variable on the given node with the supplied value. The variable name cannot start with `$`.

## Remarks

Unlike pnmakevar, pnreplaceval overwrites a variable that already has a value.

## Example

```
@POST

pnreplaceval(N(1), "pos", "verb");     # Set the node's "pos" variable to "verb".

@RULES

_xNIL <- _verb @@
```

## See Also

[pnmakevar](pnmakevar.md), [pnpushval](pnpushval.md), [pnrpushval](pnrpushval.md), [Parse Tree Functions](Table_of_Parse_Tree_Functions.md)
