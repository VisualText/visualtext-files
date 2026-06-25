[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# inc

## Purpose

Increment the value of the global variable ***var***. If the variable has no numeric value, it is set so that incrementing yields 1.

## Syntax

```
inc(var)
```

## Returns

Nothing is returned to NLP++. As a side effect, the global variable ***var*** is incremented by 1.

## Remarks

***inc*** operates on the parse's **global** variable list (the same variable space used by **ginc**, **fprintgvar**, and **gdump**). ***inc*** and **ginc** are equivalent; **ginc** is the explicitly "global" spelling.

To increment a variable belonging to a phrase-element node, use **ninc**. To increment a variable belonging to a context (dominant) node, use **xinc**.

## Example

```
@POST

inc("count");

single();  # Need to put the default reduce in manually, since POST is not empty.

@RULES

_item <- _noun @@
```

## See Also

[ginc](ginc.md), [ninc](ninc.md), [xinc](xinc.md), [fprintgvar](fprintgvar.md), [POST Actions](NLP_PP_Stuff/AT-POST_Actions.md#table_of_@POST_Actions)
