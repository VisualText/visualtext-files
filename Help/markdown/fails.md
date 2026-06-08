# fails

## Purpose

Fail to match if node matches anything on the list.

## Remarks

**fails** can be used with an _xWILD rule element on the right-hand side of a rule.  **fail** is an alternate form for fails.

## Example

```
# This rule collects everything up to
 an _endofpar or a subsequent _par, and reduces that

# set of one or more nodes to _par (which could be short for paragraph).



_par <- _xWILD [plus fails=(_endofpar _par)] @@
```

## See Also

[match](match.md), [excepts](excepts.md), [Phrase Element Modifiers](NLP_PP_Stuff/Phrase_element_modifiers.md).
