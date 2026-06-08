[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# passes

## Purpose

Invoke a recursive rules pass on nodes that matched the current rule element.

## Remarks

**nest**, **recurse** and **pass** are alternate forms for passes.

See the [RECURSE Region](RECURSE.md) discussion for more information on recursion.

## Example

```
_tag <- \< _xWILD [passes=(tagrules)]
 \> @@
```

## See Also

[Phrase Element Modifiers](NLP_PP_Stuff/Phrase_element_modifiers.md).
