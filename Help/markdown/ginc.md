[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# ginc

## Purpose

Increment the value of the global variable ***var***. If the variable has no numeric value, it is set so that incrementing yields 1.

## Syntax

```
ginc(var)
```

## Returns

Nothing is returned to NLP++. As a side effect, the global variable ***var*** is incremented by 1.

## Remarks

***ginc*** operates on the parse's **global** variable list (the same variable space used by **fprintgvar** and **gdump**). ***ginc*** and **inc** are equivalent; ***ginc*** is the explicitly "global" spelling.

To increment a variable belonging to a phrase-element node, use **ninc**. To increment a variable belonging to a context (dominant) node, use **xinc**.

## Example

```
@POST

ginc("count");

single();  # Need to put the default reduce in manually, since POST is not empty.

@RULES

_item <- _noun @@
```

## See Also

[inc](inc.md), [ninc](ninc.md), [xinc](xinc.md), [fprintgvar](fprintgvar.md), [POST Actions](NLP_PP_Stuff/AT-POST_Actions.md#table_of_@POST_Actions)
