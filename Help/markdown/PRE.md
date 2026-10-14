[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# PRE Region

The PRE Region is used to extend the pattern matcher's mechanism for matching each rule element.   Currently, the PRE Region does not support general NLP++ expressions and statements.

## PRE Action Syntax

The actions used in the PRE Region have a mandatory range. Their form is

**<num,num> pre_action_name(args....)**

The PRE Action applies to each rule element in the <num, num> range individually.

PRE Actions operate only on tokens, or leaf nodes of the parse tree, at present. So, if the current node covers more than a *single* leaf node, the PRE Action automatically *fails*. Another thing to be careful of is that PRE Actions disregard the **base** attribute of a node. That is, even if the current node or a subnode has the **base** attribute set, the PRE Action will look under it for the leaf node.

## PRE Actions on a Wildcard

A PRE Action on a plain **_xWILD** element (one with no match or fail list) must hold on every node the wildcard covers, including whitespace. The wildcard is matched greedily, and it stops at whichever comes first:

- the first node where a PRE Action fails;
- the first node that matches the next rule element.

The first stopping point is how a line can be gathered up to its newline:

```
@PRE
<2,2> varz("NL");
@RULES
_LINE <- _xSTART _xWILD [plus] @@
```

The second lets a condition hold on everything between two elements:

```
@PRE
<2,2> varz("num");
@RULES
_span <- one _xWILD [plus] three @@
```

This matches `one two three` when neither `two` nor the spaces around it has a `num` attribute.

**NEW 4.2.20**: before this version, a wildcard with a PRE Action did not stop at the next rule element. It ran past it, so a rule like the second example never matched.

## Conditions on the Element Itself

A PRE Action can also be written as a key on the rule element it applies to, so there is no range to keep in step with the element's position. The key is the action's name, and its value is the action's arguments: a single value, or a list in parentheses for several. An action with no arguments is written by name alone.

```
@RULES
_np <- _det _xWILD [plus match=(_noun _adj) vareq=("pos" "noun") varz="num"] @@
```

means the same as

```
@PRE
<2,2> vareq("pos", "noun");
<2,2> varz("num");
@RULES
_np <- _det _xWILD [plus match=(_noun _adj)] @@
```

Every PRE Action can be written this way: **var**, **varz**, **vareq**, **varne**, **vargt**, **varlt**, **regexp**, **regexpi**, **uppercase**, **lowercase**, **cap**, **length**, **lengthr**, **numrange**, **unknown** and **debug**. For example, `_xALPHA [cap]`, `_xNUM [numrange=(5 10)]`, `_xALPHA [regexp="t*"]`. Conditions on an element and a PRE region on the same rule both apply. A wildcard with a condition behaves as described under PRE Actions on a Wildcard.

**NEW 4.2.26**

## See Also

[Grammar Region](NLP_PP_Stuff/Grammar_Region.md)

[PRE Action](NLP_PP_Stuff/AT-PRE_Actions.md)

[CHECK Region](CHECK.md)

[POST Region](POST.md)

[RULES Region](RULES.md)
