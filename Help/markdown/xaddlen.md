[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# xaddlen

## Purpose

Add the text length of the node(s) matching the ***num***th rule element to the variable ***var*** stored on the context (dominant) node.

## Syntax

```
xaddlen(var, num)
```

## Returns

## Remarks

***xaddlen*** computes the length covered by the node's text-buffer offsets (end − start + 1) and adds it to the context ("X") node's variable ***var***. If ***var*** has no numeric value yet, the length becomes its value.

If the ***num***th rule element matched a contiguous range of nodes, the length spans from the start of the first node to the end of the last node. A context node must be present for the action to take effect.

## Example

```
@POST

xaddlen("len", 1);

single();  # Need to put the default reduce in manually, since POST is not empty.

@RULES

_item <- _noun @@
```

## See Also

[xinc](xinc.md), [xaddnvar](xaddnvar.md), [fprintxvar](fprintxvar.md), [POST Actions](NLP_PP_Stuff/AT-POST_Actions.md#table_of_@POST_Actions)
