# tree

## Purpose

Search node's entire subtree for a match.

## Remarks

Overuse of this may degrade analyzer performance.

Note that "t" is short for "trigger", not "tree".

## Example

# If a node labeled _det is followed by a node with a thousand child nodes, that subtree # will be searched for a node with a _noun label.  So tree can be costly and wildly inaccurate, # and must be used with caution. @RULES _np <- _det _noun [tree] @@

## See Also

[singlet](singlet.md), [Phrase Element Modifiers](NLP_PP_Stuff/Phrase_element_modifiers.md).
