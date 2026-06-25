[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# attrs

## Purpose

Layer additional attributes for the element in the parse tree, as "mini-reductions".

## Remarks

Use the names in the list to name nodes. Each node that matched current rule element will be layered.  **layer, layers**, and **attr **are alternate forms for attrs.

**attrs** can also be used as a suggested element modifier.

## Example

```
_np <- _det _noun [attrs=(_head)] @@
```

## See Also

[Suggested Element Modifiers](NLP_PP_Stuff/Suggested_element_modifiers.md), [Phrase Element Modifiers](NLP_PP_Stuff/Phrase_element_modifiers.md)
