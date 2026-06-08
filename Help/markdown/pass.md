[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# pass

## Purpose

Invoke a recursive rules pass on nodes that matched the current rule element.

## Remarks

**recurse**, **passes** and **nest** are alternate forms for pass.

See the [RECURSE Region](RECURSE.md) discussion for more information on recursion.

## Example

```
_tag <- \< _xWILD [pass=(tagrules)]
 \> @@
```

## See Also

[Phrase Element Modifiers](NLP_PP_Stuff/Phrase_element_modifiers.md).
