[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# group

## Purpose

**SEE NOTE BELOW.**  Perform a reduction on the range of rule elements from *node1 *to* node2 *and name the group node *labelString*.  node1 and node2 should be a well-formed range in the current rule match.  For example from N(1) to N(3).

## Syntax

```
group(node1, node2, labelString)
```

```
node1- type: parse tree node

node2 - type: parse tree node

labelString - type: str
```

## Returns

## Remarks

NOTE: the old group action has long been replaced by this more flexible group function. As of VisualText 2.3.1.9, the group function returns the reduce node that it creates, rather than a boolean "ok".  As with the action, the group function alters the element numbers of subsequent POST actions.

Unlike other reduce actions, **group** can be repeated.  The phrase element modifier **[group](gp.md)** is analogous to this function.

## Example

```
@POST

L("n") = group(N(1),N(2),"_np");

"output.txt" << pnname(L("n")) << "\n";

@RULES

_xNIL <- _det _noun _xWILD [s lookahead fail=(_noun)] @@
```

```
output.txt then gets an output like:
```

```
_np
```

## See Also

[splice](splice.md), [Phrase Element Modifiers](NLP_PP_Stuff/Phrase_element_modifiers.md), [POST Actions](NLP_PP_Stuff/AT-POST_Actions.md#table_of_@POST_Actions), [group action](group_action.md)
