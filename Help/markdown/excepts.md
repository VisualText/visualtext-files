[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# excepts

## Purpose

Match an item in an except list to negate the effect of a match on the match or fail list.

## Remarks

**except** can be used with any rule element on the right-hand side of the rule.  It must be accompanied by a single **match** or **fail** list.

## Example

```
_par <- _xWILD [fail=(_endofpar _par) excepts=(_quote) min=1 max=0] @@
```

## See Also

[match](match.md), [fails](fails.md), [Phrase Element Modifiers](NLP_PP_Stuff/Phrase_element_modifiers.md)
