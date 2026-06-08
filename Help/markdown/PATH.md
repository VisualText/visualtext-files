[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# PATH Selector

The PATH Selector lets you specify a **path** of node names that must start with _ROOT, the root of the parse tree. The path specifies the root, its child, grandchild, and so on. The selection algorithm traverses the parse tree starting at the root and searches for a context node that matches the entire path. The phrase immediately under such a context node will be traversed to look for rule matches. (PATH does not check the **unsealed** flag.)

## See Also

[Context Zone](NLP_PP_Stuff/Context_Zone.md)

[SELECT Region](SELECT.md)

[MULTI Selector](MULTI.md)

[NODES Selector](NODES.md)
