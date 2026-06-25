[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# xaddnvar

## Purpose

Add the value of the node variable ***nvar*** (taken from the node matching the ***num***th rule element) to the variable ***xvar*** stored on the context (dominant) node.

## Syntax

```
xaddnvar(num, nvar, xvar)
```

## Returns

## Remarks

***xaddnvar*** reads the numeric value of ***nvar*** from the phrase-element ("N") node that matched rule element ***num***, then adds that value to the context ("X") node's variable ***xvar***. If ***xvar*** has no numeric value yet, the added value becomes its value.

If the ***num***th rule element matched more than one node, the action is ignored. A context node must be present for the action to take effect.

## Example

```
@POST

xaddnvar(1, "len", "total");

single();  # Need to put the default reduce in manually, since POST is not empty.

@RULES

_item <- _noun @@
```

## See Also

[xinc](xinc.md), [xaddlen](xaddlen.md), [ninc](ninc.md), [fprintxvar](fprintxvar.md), [POST Actions](NLP_PP_Stuff/AT-POST_Actions.md#table_of_@POST_Actions)
