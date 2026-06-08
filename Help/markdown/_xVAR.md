[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# _xVAR

## Purpose

Match a node that has the named attribute with a value.

## Syntax

```
_xVAR("attr")
```

The attribute name is given in parentheses. The surrounding double quotes are optional, so both ***_xVAR("attr")*** and ***_xVAR(attr)*** are accepted.

## Remarks

_xVAR is a restricted wildcard used as an entry in a match (or fail) list. It matches a single node only when that node carries the attribute named *attr* and that attribute has a value. The attribute is tested on the node at match time.

Because it is a match-list entry, _xVAR is typically combined with _xWILD, which acts as an "OR" matching function over its list.

## Example

Match any node that carries a *pos* attribute (for example, a node that has been assigned a part of speech):

```
@RULES
_token <- _xWILD [match=(_xVAR("pos"))] @@
```

## See Also

[_xWILD](_xWILD.md), [match](NLP_PP_Stuff/Phrase_element_modifiers.md#match), [Phrase Element Modifiers](NLP_PP_Stuff/Phrase_element_modifiers.md), [Special Rule Elements](NLP_PP_Stuff/Special_rule_elements.md)
