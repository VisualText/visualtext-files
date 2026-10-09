[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# group

## Purpose

**SEE NOTE BELOW.**  Perform a reduction on the range of rule elements from *num1* to *num2* and name the group node *labelString*.  num1 and num2 are rule element numbers and should be a well-formed range in the current rule match, for example elements 1 to 3.

## Syntax

```
group(num1, num2, labelString)
```

```
num1 - type: int (the first rule element in the range)

num2 - type: int (the last rule element in the range)

labelString - type: str
```

The range is given by rule element **numbers**, not nodes: write `group(1,2,"_np")`, not `group(N(1),N(2),"_np")`. Passing nodes stops the rule's @POST code with the error `group: Arg must be integer`.

## Returns

Returns the parse tree node created by the reduction. Must be called from the @POST region.

## Remarks

NOTE: the old group action has long been replaced by this more flexible group function. As of VisualText 2.3.1.9, the group function returns the reduce node that it creates, rather than a boolean "ok".  As with the action, the group function alters the element numbers of subsequent POST actions.

Unlike other reduce actions, **group** can be repeated.  The phrase element modifier **[group](gp.md)** is analogous to this function.

## Example

```
@POST

L("n") = group(1,2,"_np");

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
