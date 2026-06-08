# lookahead

## Purpose

Designate the first lookahead element of a rule. The first node matching the lookahead element or to the right of it will be the locus where the rule matcher continues matching, after finishing with the current rule.

Unlike YACC, BISON, or other grammar frameworks that use a lookahead or "LR" grammar, NLP++ rules require that lookahead constraints, if any, be specified explicitly.

## Remarks

**look** is an alternate form for lookahead.

| **WARNING**: A reduce action such as **singler** or **noop** should be used to ensure that the lookahead node and nodes to its right are not included in the current rule reduction. **FEATURE:** The first element of a rule cannot not be designated as a lookahead element. For now, use the REC recursive pass algorithm to re-match nodes that have been created or operated on by the rule matcher. |
| --- |

## Example

# The rule below reduces a determiner, quantifier, adjective pattern to a noun phrase as long as the subsequent node is not a noun. # The singler action reduces the first three elements and leaves the lookahead element out of the reduction. # When the rule matcher is done with the current rule match, it will move to the node that matched the lookahead element of the current rule. # (Without the lookahead element modifier, the rule matcher normally would continue at the node *after* the one matching the 4th element of the rule.) @POST    singler(1,3); @RULES _np <-    _det    _quan    _adj    _xWILD [one lookahead fail=(_noun)]  # Lookahead element.    @@

## See Also

[trigger](trigger.md), [Phrase Element Modifiers](NLP_PP_Stuff/Phrase_element_modifiers.md)
