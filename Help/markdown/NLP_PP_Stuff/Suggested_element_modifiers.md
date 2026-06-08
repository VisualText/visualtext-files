[← Help Contents](../index.md) | [📘 NLP++ Textbook](../NLP++_Textbook.md)

# Suggested Element Modifiers

Element modifiers for the suggested element are listed in the table below. The element modifier must be enclosed in square brackets** [ ] **and placed **after** the element. The element modifier **layers** has several synonyms, **layer**, **attrs** and **attr**.

| **KEY** | **VALUE TYPE** | **DESCRIPTION** |
| --- | --- | --- |
| base | NONE | The suggested node is the bottom-most node to search when looking down a *singlet chain* for a match. See also the singlet modifier. |
| unsealed | NONE | The suggested node will be searched for select nodes (i.e., nodes specified after @NODES marker). |
| layers layer attrs attr | LIST | After normal reduce, perform additional reduces, naming the nodes as in the list. This enables layering of attributes in the parse tree. |

## See Also

[Phrase Element Modifiers](Phrase_element_modifiers.md)

[Rule Syntax](Rule_syntax.md)
