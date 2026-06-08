[← Help Contents](../index.md) | [📘 NLP++ Textbook](../NLP++_Textbook.md)

# About Pass Files

A pass file holds the NLP++ code and rules associated with a Pattern or Recursive pass type. Five zones divide a pass file and are ordered as follows:

| **ZONE** | **DESCRIPTION** |
| --- | --- |
| Declare | Contains user-defined NLP++ function definitions. |
| **Code** | Contains NLP++ code that is independent of rule matching. |
| **Context** | Selects nodes of the parse tree. Rules will match only against the phrases immediately under the selected nodes. |
| **Minipass** | Contains nested minipasses called Recurse Regions. Each Recurse Region is named and contains a Grammar Region. Rule elements in the Grammar Zone can invoke these named rule sets. |
| **Grammar** | Contains the main Grammar Region of the current pass file. |

## Optional Zones

A minimal pass file may consist solely of a Code Zone or a Grammar Zone.

If absent, the Context Zone defaults to the selector

@NODES _ROOT

which traverses the phrase immediately below the root of the parse tree, invoking the rule matcher on each node of the phrase.

## Pass File Markers

The '@' sign is a reserved character that indicates the start of a region (e.g., @CODE) or a selector (e.g., @NODES).

To indicate the end of a region, the name of the region preceded by two '@' signs is used. The end of a Code Region is indicated by @@CODE. End markers are optional in most cases.

A lone @@ marker indicates the end of a rule, e.g.,

_NP <- _NOUN @@

## Case Sensitivity of Pass File Markers

Pass file markers are case-insensitive.  A marker such as @PRE can be written as @pre.

| **Note**: Unlike pass file markers, NLP++ functions and actions are case-sensitive. |
| --- |

## See Also

[Code Zone](Code_Zone.md) [Context Zone](Context_Zone.md) [Minipass Zone](Minipass_Zone.md) [Grammar Zone](Grammar_Zone.md)
