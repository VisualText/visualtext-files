# group

## Purpose

**SEE NOTE BELOW.**  Perform a reduction on the range of rule elements from *ruleE*ltNumber*1* to* ruleEltNumber2* and name the group node *labelString*.

## Syntax

```
group(ruleEltNumber1, ruleEltNumber2, labelString)
```

```
ruleEltNumber1 - type: int

ruleEltNumber2 - type: int

labelString - type: str
```

## Returns

## Remarks

NOTE: the old group action documented here has long been replaced by a more flexible group function.  Rather than rule element numbers, the first two arguments are the first node and the last node of a range (which may be the same node).  As of VisualText 2.3.1.9, the group function also returns the reduce node that it creates, rather than a boolean "ok".  As mentioned here, group alters the element numbers of subsequent POST actions.

Unlike other reduce actions, **group** can be repeated.  The phrase element modifier **[group](gp.md)** is analogous to this action.

| **WARNING: **The rule element numbers change after each group action, so subsequent POST Actions must account for the new numbering of the rule elements. Reimplemented as an NLP++ function so that args can be NLP++ expressions. |
| --- |

## Example

```
@POST

group(1,2,"_np");

@RULES

_xNIL <- _det _noun _xWILD [s lookahead fail=(_noun)] @@
```

## See Also

[splice](splice.md), [Phrase Element Modifiers](NLP_PP_Stuff/Phrase_element_modifiers.md), [POST Actions](NLP_PP_Stuff/AT-POST_Actions.md#table_of_@POST_Actions), [group function](group.md)
