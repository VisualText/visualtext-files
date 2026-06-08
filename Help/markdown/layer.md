[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# layer

## Purpose

Layer additional attributes for the element in the parse tree, as "mini-reductions".

## Remarks

Use the names in the list to name nodes. Each node that matched current rule element will be layered.  **layers**, **attrs**, and **attr** are alternate forms for layer.

**layer** can also be used as a suggested element modifier.

## Example

# This rule reduces "fly" to a verb and then a vg (or "verb group"). @POST   noop(); @RULES _xNIL <-  to fly [layer=(_verb _vg)] @@

## See Also

[Suggested Element Modifiers](NLP_PP_Stuff/Suggested_element_modifiers.md), [Phrase Element Modifiers](NLP_PP_Stuff/Phrase_element_modifiers.md)
