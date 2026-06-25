[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# xinc

## Purpose

Increment the variable ***var*** stored on the context (dominant) node. If the variable has no numeric value, it is set so that incrementing yields 1.

## Syntax

```
xinc(var)
```

## Returns

## Remarks

***xinc*** increments a variable belonging to the context ("X") node — the dominant node selected for the current rule match. A context node must be present for the action to take effect.

To increment a global variable, use **inc** or **ginc**. To increment a variable on a phrase-element node, use **ninc**.

## Example

```
@POST

xinc("count");

single();  # Need to put the default reduce in manually, since POST is not empty.

@RULES

_item <- _noun @@
```

## See Also

[inc](inc.md), [ginc](ginc.md), [ninc](ninc.md), [xaddlen](xaddlen.md), [xaddnvar](xaddnvar.md), [fprintxvar](fprintxvar.md), [POST Actions](NLP_PP_Stuff/AT-POST_Actions.md#table_of_@POST_Actions)
