[← Help Contents](../index.md) | [📘 NLP++ Textbook](../NLP++_Textbook.md)

# Context Zone

The Context Zone of a pass file specifies methods for *selecting* nodes of the parse tree. Each **selected node**, or **context node**, serves as a locus for rule matching. The @SELECT and @@SELECT markers optionally delimit the Context Zone.

## Order in Pass Files

The Context Zone can come either before or after the Code Zone.  The Context Zone is also optional.  If it is absent, it is equivalent to

@NODES _ROOT

That is, rule matching will occur in the phrase of nodes immediately under the root node of the parse tree.

## Rule Matching and Selectors

The mode of rule matching depends on the selector (e.g., @NODES above) and the pass algorithm type (e.g., Pattern or Recursive) for the current pass. For example, with the selectors NODE or PATH, the phrase immediately under the selected node is subjected to rule matching. With the MULTI selector, every phrase in the subtree of the selected node is subjected to rule matching.

## Specifying Selectors

Within the Context Zone, a single SELECT Region may be specified. Currently, a pass file may include at most one **selector** (i.e., @NODES, @PATH, and @MULTI).

## See Also

[SELECT Region](../SELECT.md)

[NODES Selector](../NODES.md)

[PATH Selector](../PATH.md)

[MULTI Selector](../MULTI.md)
