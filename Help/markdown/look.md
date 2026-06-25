[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# look

## Purpose

Designate the first lookahead element of a rule. The first node matching the lookahead element or to the right of it will be the locus where the rule matcher continues matching.

## Remarks

**lookahead** is an alternate form for look.

| **WARNING**: A reduce action such as **singler** or **noop** should be used to ensure that the lookahead node and nodes to its right are not included in the current rule reduction. |
| --- |

## Example

```
@POST
singler();
@RULES
_det <- _xWILD [match=(the a an)] _noun [look] @@
```

## See Also

[trigger](trigger.md), [Phrase Element Modifiers](NLP_PP_Stuff/Phrase_element_modifiers.md).
