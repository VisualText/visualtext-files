[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# setbase

## Purpose

Set the BASE attribute of the ***num***th node to "true" or "false".

## Syntax

```
setbase(num, bool_str)
```

## Returns

Nothing is returned to NLP++. As a side effect, the BASE attribute is set on the node matching the ***num***th rule element.

## Remarks

The **base** attribute is equivalent to using setbase.  But setbase lets you access any element in the rhs phrase of a rule.

```
@RULES

_np [base] <- _noun @@
```

This example and the one below "hide" the _noun node and any node under it, so that subsequent rules such as

_np <- _det [opt s] _noun [s] @@

won't find a singleton _noun that has already been reduced to an _np.

## Example

```
@POST

setbase(1,"true");

single();  # Need to put the default reduce in manually, since POST is not empty.

@RULES

_np <- _noun @@
```

## See Also

[setunsealed](setunsealed.md), [POST Actions](NLP_PP_Stuff/AT-POST_Actions.md#table_of_@POST_Actions)
