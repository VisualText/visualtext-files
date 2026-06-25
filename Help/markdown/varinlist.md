[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# varinlist

## Purpose

Find var_str variable's value(s) in any pnode that matched elt_numth element.

## Syntax

```
returnedValue = varinlist(var_str, elt_num)
```

```
returnedValue - type: var value

var_str - type: str

elt_num - type: int
```

## Returns

Returns the value(s) of the var_str variable from the first node (among those that matched the elt_numth rule element) that has that variable. Returns nothing if no matching node carries the variable. Special ($-prefixed) variables are not handled.

## Remarks

Useful when a single rule element matches multiple nodes (for example, a `[plus]` or `[star]` element): varinlist scans those nodes left to right and returns the variable from the first one that has it.

## Example

```
@POST

G("pos") = varinlist("pos", 2);     # First "pos" value among the nodes matching the 2nd element.

@RULES

_xNIL <- _det _noun [plus] @@
```

## See Also

[pnvar](pnvar.md), [Parse Tree Functions](Table_of_Parse_Tree_Functions.md)
