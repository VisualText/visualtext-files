[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# SELECT Region

The SELECT Region specifies methods for selecting **context nodes** in the parse tree. Each **selected node** serves as a locus for rule matching.

## Selectors

The SELECT Region may include at most one **selector**, chosen from the following:

| **SELECTOR** | **DESCRIPTION** |
| --- | --- |
| **@NODES** | A **list** of node names to be searched for independently in the parse tree. The phrase immediately under such a context node will be traversed to look for rule matches. **NOTE:** The selection algorithm will only find such a node when all of its ancestors have the **unsealed** attribute set. |
| **@PATH** | A **path** of node names that must start with _ROOT, the root of the parse tree. The path specifies the root, its child, grandchild, and so on. The selection algorithm traverses the parse tree starting at the root and searches for a context node that matches the entire path. The phrase immediately under such a context node will be traversed to look for rule matches. (The PATH Selector does not check the **unsealed** flag.) |
| **@MULTI** | A **list** of node names to be searched for independently in the parse tree. The entire subtree under such a context node will be traversed to look for rule matches. (The MULTI Selector currently does not check the **unsealed** flag.) |

In addition to the selector markers @NODES, @PATH, and @MULTI there are optional markers that indicate the termination of a selector specification.  The corresponding markers are  @@PATH, @@NODES, and @@PATH.

The SELECT Region itself is optional. If the region is not included in the pass file, the default is to match the rules of the file against the top-level phrase of the parse tree, that is, the phrase directly under the **_ROOT** node. The default could be made explicit, as in the following:

| @SELECT | # Start of SELECT Region |
| --- | --- |
| @NODES _ROOT | # Specifies nodes whose underlying phrase will be matched against. |
| @@SELECT | # Optional end-marker for SELECT Region |

(The region markers @SELECT and @@SELECT are also optional. The sample SELECT Region above could be simply @NODES _ROOT.)

## See Also

[Context Zone](NLP_PP_Stuff/Context_Zone.md)

[NODES Selector](NODES.md)

[PATH Selector](PATH.md)

[MULTI Selector](MULTI.md)
