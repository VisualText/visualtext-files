# MULTI Selector

The MULTI Selector lets you specify a **list** of node names to be searched for independently in the parse tree. The entire subtree under such a context node will be traversed to look for rule matches. (The MULTI Selector currently does not check the **unsealed** flag.)

It may be useful to know that the MULTI algorithm proceeds from the most deeply buried phrases (i.e., those at the leaves of the parse tree) to the phrase immediately below the context node.

## Using the MULTI Selector

Below is a cautionary note on using the MULTI Selector.

#### Common Error: MULTI with [Singlet] or [Tree] Modifier

MULTI in combination with either of the element modifiers [s] (i.e., singlet) or [tree] can lead to unexpected behavior, such as matching the same pattern multiple times. Normally, you will want to avoid using these rule element modifiers when specifying a MULTI traversal of a parse subtree. The problem surfaces in rules of the form

_X <- _Y [s] @@

that is, where the right-hand-side consists of a phrase of one element. If _Y matches a buried node, then it will match the same node every time an ancestor of that node is traversed. E.g., given the subtree

_CONTEXT_NODE   | ...._A ....   |   _B   |   _C   |   _Y

then _Y, _C, _B, and _A will all match the above rule when MULTI is the selector, yielding a (presumably) undesirable subtree such as

_CONTEXT_NODE   | ...._X ....   |   _A   |   _X   |   _B   |   _X   |   _C   |   _X   |   _Y

## See Also

[Context Zone](NLP_PP_Stuff/Context_Zone.md)

[SELECT Region](SELECT.md)

[PATH Selector](PATH.md)

[NODES Selector](NODES.md)
