# Functions

NLP++ provides a variety of predefined functions for managing the parse tree and knowledge base. Convenient functions also support output formatting, string handling, and spelling. The spell functions can be used to help with unknown word lookup by a text analyzer.

As NLP++ evolved from an "action language" for rules, the Actions section provides functions that expect to apply before, during, and after the matching of a rule.  They are "rule-aware," in that they can address the matched nodes, the suggested concept, and the "dominating" or context nodes within which the rule match occurred.  The actions are deprecated in the sense that some of them cannot accept full NLP++ expressions as function arguments, but require literal arguments.  Some actions, such as group, have been upgraded to full-fledged NLP++ functions and are listed in both the Actions and Functions sections.

| **Note**: Boolean type is currently implemented by integer **1** (or non-zero) for **true** and **0** for **false**. Floating point type is newly (but incompletely) available. Char type is not implemented. |
| --- |

## See Also

[Database Functions](../Table_of_Database_Functions.md)

[Special Functions](../Table_of_Special_Functions.md)

[Knowledge Base Functions](../Table_of_Knowledge_Base_Functions.md)

[Formatting and I/O Functions](../Table_of_Formatting_and_I_O_Functions.md)

Math Functions

[Parse Tree Functions](../Table_of_Parse_Tree_Functions.md)

[String Functions](../Table_of_String_Functions.md)

[Spelling Functions](../Table_of_Spelling_Functions.md)

[Web Functions](../Table_of_Web_Functions.md)

[Actions](Actions.md)
