[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# or

## Purpose

Check action that succeeds if any of the rule elements from **number1** to **number2** has matched an actual node. Meaningful only if this is a range of *optional* rule elements.

## Syntax

```
or(number1, number1)
```

## Returns

Succeeds (the rule's @CHECK region passes) if at least one rule element in the range **number1** through **number2** matched an actual node; otherwise the check fails and the rule reduction is rejected.

## Remarks

This action is just a sample. As Text Analysis International™ develops its generic analyzer, more CHECK Actions will be implemented.

## Example

```
@CHECK

# Succeed only if at least one of rule elements 1-3 matched a node.
if (!or(1,3))
	fail();

@RULES

_vgroup <- _have [opt] _be [opt] _verb [opt] @@
```

## See Also

[succeed](succeed.md), [fail](Functions/Miscellaneous_Functions/fail.md), [CHECK Actions](NLP_PP_Stuff/AT-CHECK_Actions.md)
