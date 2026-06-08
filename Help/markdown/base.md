# base

## Purpose

The base suggested-element modifier specifies that the reduce node will be the bottom-most node in a *singlet chain*.  That is, subsequent rules using the singlet element modifier will not look "down" past a node labeled with the base attribute.

## Remarks

Base and singlet provide a mechanism for layering multiple attributes and syntactic and semantic ambiguities directly into the parse tree.

The example will help clarify the use of the base modifier.

## Example

# The rule below reduces a node labeled _noun to an _np.  It places an internal flag called "base" on the _np node. # Subsequent rules (e.g., in subsequent passes) that are searching for _noun will not find it under an _np created with the current rule. @RULES _np [base] <- _noun @@

# Say a subsequent pass has this rule.  Even though the s (or singlet) modifier says to look "within" a node for _noun, it won't find it within an _np # labeled with a base flag, as created by the rule above. @RULES _np <- _adj _noun [s] @@

[Suggested Element Modifiers](NLP_PP_Stuff/Suggested_element_modifiers.md).
