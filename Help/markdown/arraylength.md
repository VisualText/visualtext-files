[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# arraylength

## Purpose

Count the number of values in a given variable.

## Syntax

```
returnedNumber = arraylength(variableName)
```

```
returnedNumber - type: int

variableName - type: var
```

## Returns

Returns the number of values held by the given variable. A single-valued or empty variable returns 1; an array returns its element count.

## Remarks

Note that the variableName must evaluate to a variable reference (G, S, X, N).

**WARNING:** arraylength() never returns 0, since every variable is considered to have at least one value.  This may yield unexpected behaviors at times.

## Example

```
@POST

G("len") = arraylength(N("vals",1));   # Count the values in the matched node's "vals" variable.

@RULES

_xNIL <- _item @@
```

## See Also

[Parse Tree Functions](Table_of_Parse_Tree_Functions.md)
