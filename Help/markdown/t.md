# t

## Purpose

Match the current element first.

## Remarks

**trig** and **trigger **are alternate forms for t.

An _xWILD element or optional element cannot take the trigger element modifier.

Triggering actually causes the rule matcher to match the trigger element first, then move left (i.e., backwards), then move right from the trigger element.  This is useful to know in designing rules that combine wildcards with a trigger element, for example.

Note that triggering can be tricky.  See the example below, in which, *regardless* of rule ordering in a pass, an unexpected behavior may occur.

## Example

```
# Attempt to match this rule only when
 a _noun node is seen.

_np <- _det _quan _adj _noun [t]
 @@
```

```
# If the following rule is in the same
 pass, it will always match first, so that the rule above will never

# be matched!  Why?
  Because
 the rule matcher will match the rule below whenever an _adj node is found

# (preceded by _det and _quan).

# By the time the _noun node is seen, the rule below has already operated.
  The presence
 or absence of [t]

# below makes no difference to this behavior.

_np <- _det _quan _adj [t] @@
```

## See Also

[optional](optional.md), [lookahead](lookahead.md), [Phrase Element Modifiers](NLP_PP_Stuff/Phrase_element_modifiers.md).
