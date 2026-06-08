[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# matches

## Purpose

Match if the element is in a match list.  **matches** is a restricted wildcard and succeeds only if one of the list names matches a node.

## Remarks

**matches** can only be used with _xWILD rule elements only. **match** is an alternate form for matches.

## Example

```
_james <- _xWILD [matches=(jim
 jimmy james) singlet min=1 max=1] @@
```

## See Also

[match](match.md), [fails](fails.md), [excepts](excepts.md), [Phrase Element Modifiers](NLP_PP_Stuff/Phrase_element_modifiers.md)
