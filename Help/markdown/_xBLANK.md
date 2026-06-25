[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# _xBLANK

## Purpose

Match a whitespace token, excluding newline.

## Remarks

_xBLANK is equivalent to _xWILD [match=(\ \t)].

## Example

```
@RULES

_word <- _xALPHA _xBLANK _xALPHA @@
```

## See Also

[_xWHITE](_xWHITE.md), [Special Rule Elements](NLP_PP_Stuff/Special_rule_elements.md)
