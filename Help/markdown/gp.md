[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# gp

## Purpose

Gather nodes that matched the current element under a single node with NAME as its name.

## Remarks

**group** is an alternative form for gp.  gp is analogous to the [group](group.md) Post Action.

## Example

# Do a mini-reduction of all the nodes that matched _noun, naming the reduce node _nouns, # before reducing the entire pattern to an _np. @RULES _np <-  _det _quan _adj _noun [plus group=_nouns] @@

## See Also

[rename](rename.md), [Phrase Element Modifiers](NLP_PP_Stuff/Phrase_element_modifiers.md).
