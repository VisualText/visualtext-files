# setunsealed

## Purpose

Set the UNSEALED attribute of the ***num***th node to "true" or "false".

## Syntax

```
setunsealed(num, bool_str)
```

## Returns

## Remarks

A path of unsealed nodes in the parse tree can be searched via the @NODES selector.  If a node is sealed, then @NODES won't look inside it.  Another way is with the element modifier **unsealed**.  The code below places the unsealed attribute on a _sentence node.

```
@RULES

_sentence [unsealed] <- _np _vp @@
```

## Example

```
@POST

setunsealed(1,"true");  # Allows _sentence nodes to be examined by a subsequent pass that uses @NODES.

@RULES

_xNIL <- _sentence @@
```

## See Also

[setbase](setbase.md), [POST Actions](NLP_PP_Stuff/AT-POST_Actions.md#table_of_@POST_Actions)
