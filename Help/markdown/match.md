[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# match

## Purpose

Match if the element is in a match list.  **match** is used only with _xWILD, and succeeds only if one of the list names matches a node.  match and fail basically convert _xWILD from a wildcard to a restricted match or fail on a list of names.

## Remarks

**match** can only be used with _xWILD rule elements. **matches** is an alternate form for match.

## Example

`_james <- _xWILD [`**match**`=(jim jimmy james) singlet min=1 max=1] @@`

## See Also

[fails](fails.md), [excepts](excepts.md), [Phrase Element Modifiers](NLP_PP_Stuff/Phrase_element_modifiers.md)
