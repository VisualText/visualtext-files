[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# ninc

## Purpose

Increment the variable ***var*** stored on the node matching the ***num***th rule element. If the variable has no numeric value, it is set so that incrementing yields 1.

## Syntax

```
ninc(num, var)
```

## Returns

## Remarks

***ninc*** increments a variable belonging to a phrase-element ("N") node — the node that matched rule element ***num***. If that rule element matched more than one node, the action is ignored.

To increment a global variable, use **inc** or **ginc**. To increment a variable on the context (dominant) node, use **xinc**.

## Example

```
@POST

ninc(1, "count");

single();  # Need to put the default reduce in manually, since POST is not empty.

@RULES

_item <- _noun @@
```

## See Also

[inc](inc.md), [ginc](ginc.md), [xinc](xinc.md), [fprintnvar](fprintnvar.md), [POST Actions](NLP_PP_Stuff/AT-POST_Actions.md#table_of_@POST_Actions)
