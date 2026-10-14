[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# _xWILD

## Purpose

Match anything.  _xWILD is an unrestricted wildcard. Key-value pairs may add restrictions on number of nodes matched and on what is matched.

## Remarks

With a match or fail list, _xWILD becomes an "OR" matching function.

An unrestricted _xWILD covers nodes up to the first node that the elements after it can match. Matching never backs up to try a longer stretch, so a wildcard stops at the first possible place.

When an optional element follows the wildcard, the wildcard also stops at the first node that a later element matches, up to and including the next required element. In that case the optional element is absent. In

```
_xNIL <- the _xWILD _xWILD [opt match=(three)] _xWILD [one match=(bears)] @@
```

on "the big bears met three bears", the wildcard covers only "big" and "three" is absent, so the rule matches "the big bears". When the optional element and a later one both match the same node, the optional element is used. Before engine 4.2.27 the wildcard ran past the first "bears" to reach "three". Here the rule then failed, because "three" is followed by a space, not "bears". To stop the wildcard, a rule had to repeat the later elements in a fail list, as in `_xWILD [fail=(three bears)]`.

**NEW 4.2.27**

## Example

```
@RULES

_parens <- \( _xWILD [fail=(\) )] \) @@
```

## See Also

[min](NLP_PP_Stuff/Phrase_element_modifiers.md#min), [max](NLP_PP_Stuff/Phrase_element_modifiers.md#max), [matches](NLP_PP_Stuff/Phrase_element_modifiers.md#match), [Phrase Element Modifiers](NLP_PP_Stuff/Phrase_element_modifiers.md), [Special Rule Elements](NLP_PP_Stuff/Special_rule_elements.md)
