[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# nest

## Purpose

Invoke a recursive rules pass on nodes that matched the current rule element.

## Remarks

**recurse**, **passes** and **pass** are alternate forms for nest.

See the [RECURSE Region](RECURSE.md) discussion for more information on nested minipasses.

## Example

```
# This is the tagrules minipass.

@RECURSE tagrules



# This rule in the minipass operates on the phrase of nodes that

# matched _xWILD in the _tag rule.

@RULES

_keywords <-

  keywords

  \=

  \(

  _xALPHA
 [star]

  \)

  @@



@@RECURSE tagrules



# This is the main rules area, called the Grammar Zone.

# When this rule matches, it invokes a minipass to process

# the nodes that matched the _xWILD wildcard.

@RULES

_tag <- \< _xWILD [nest=(tagrules)] \> @@
```

## See Also

[Phrase Element Modifiers](NLP_PP_Stuff/Phrase_element_modifiers.md)
