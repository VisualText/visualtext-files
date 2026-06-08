# xrename

## Purpose

Rename the ***num***th context node to ***name***. If *num* is absent or 0, rename last context node.

## Syntax

```
xrename(name [,num])
```

## Returns

## Remarks

## Example

```
@PATH _ROOT _sentence _segment



# This rule says that if a _noun is the last

# node of a _segment, rename _segment to _np.

@POST

xrename("_np",3);

@RULES

_xNIL <- _noun [s] _xEND @@
```

## See Also

[POST Actions](NLP_PP_Stuff/AT-POST_Actions.md#table_of_@POST_Actions)
