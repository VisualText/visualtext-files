[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# _xWILD

## Purpose

Match anything.  _xWILD is an unrestricted wildcard. Key-value pairs may add restrictions on number of nodes matched and on what is matched.

## Remarks

With a match or fail list, _xWILD becomes an "OR" matching function.

## Example

```
@RULES

_parens <- \( _xWILD [fail=(\) )] \) @@
```

## See Also

[min](NLP_PP_Stuff/Phrase_element_modifiers.md#min), [max](NLP_PP_Stuff/Phrase_element_modifiers.md#max), [matches](NLP_PP_Stuff/Phrase_element_modifiers.md#match), [Phrase Element Modifiers](NLP_PP_Stuff/Phrase_element_modifiers.md), [Special Rule Elements](NLP_PP_Stuff/Special_rule_elements.md)
