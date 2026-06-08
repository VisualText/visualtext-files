[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# singlet

## Purpose

Search a node's descendants for a match. Stop looking down when a node is a leaf, has more than one child, or has the [BASE](NLP_PP_Stuff/Suggested_element_modifiers.md#base) attribute set.

## Remarks

**s** is an alternate form for singlet.

The singlet and base methodology enables attributes and ambiguities to be layered directly into the parse tree nodes, as a "singlet chain."  By using the singlet modifer, a rule can pick up the attribute or possibility that is relevant.

## Example

```
# Even if a prior pass has reduced "per"
 to a preposition, e.g., _prep,

# this rule will still match the word "per".

_adj <- per [s] capita @@
```

## See Also

[tree](tree.md), [Phrase Element Modifiers](NLP_PP_Stuff/Phrase_element_modifiers.md).
