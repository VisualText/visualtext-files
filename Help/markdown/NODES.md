[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# NODES Selector

The NODES Selector allows you to specify a **list** of node names to be searched for independently in the parse tree. The phrase immediately under such a context node will be traversed to look for rule matches.

## Using the NODES Selector

Below are some cautionary notes on using the NODES Selector.

#### Common Error 1: Selecting Nodes inside Sealed Nodes

The selection algorithm will only find such a node when all of its ancestors have the **unsealed** attribute set.

**Example:** Say in one pass you have a rule

_paragraph <- _sentence [s plus] @@

and in the next pass you try to match within the _sentence nodes as follows:

@NODES _sentence

_np <- _det [s star] _quan [s star] _adj [s star] _noun [s plus] @@

When you run this analyzer on a text, the rule creating an _np (i.e., noun phrase) will never apply, assuming all sentences are within paragraphs. The reason is because _paragraph nodes are **sealed**, that is, they don't have the **unsealed** attribute set. In order for the second pass to succeed, the rule in the first pass must be written as

_paragraph [unsealed] <- _sentence [s plus] @@

Having NODES look only within unsealed contexts enables you to build more efficient analyzers. The idea is that you will flag "roughed out" segments as unsealed, so that you may characterize them further later on. But this mechanism may sometimes have you scratching your head as to why a rule didn't match.

#### Common Error 2: Nested Context Nodes

If one context node is inside the subtree of another context node, then the buried one will not be *seen* by the selection algorithm.

#### Common Error 3: Using the X() Context Variable with a Position Number

With NODES as the selector in a pass file, it is usually a mistake to write expressions such as X(2) or X("varname", 3). That is because these variables refer to the second and third node, respectively, when traversing down a parse tree **path**, starting at the root node. That is, they are appropriate for use with the PATH Selector.

Because the names in a NODES Selector are independent of each other, you will, in general, not know the distance of the current context node from the root of the parse tree. So, in this case, the correct variables are X() and X("varname"), which refer to the current context node selected by NODES.

## See Also

[Context Zone](NLP_PP_Stuff/Context_Zone.md)

[SELECT Region](SELECT.md)

[PATH Selector](PATH.md)

[MULTI Selector](MULTI.md)
