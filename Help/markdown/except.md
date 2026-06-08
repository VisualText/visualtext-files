# except

## Purpose

Enables an _xWILD element to have exceptions to a *match* or *fail* list.

## Remarks

**except** can be used with _xWILD rule elements on the right-hand side of a rule.  It must be accompanied by a single **match** or **fail** list.

Match and fail cannot occur in the same rule element, or the logic would become murky.  With the except modifier, match and fail are dominant, and except provides a list of exceptions.

## Example

# The rule below enables looking "inside" or "underneath" a node (with the **s** singlet modifier) for _noun, but prevents an _np from being reduced to # an _np. @RULES _np <-   _xWILD [s one match=(_noun) except=(_np)] @@

## See Also

[Phrase Element Modifiers](NLP_PP_Stuff/Phrase_element_modifiers.md)
