[← Help Contents](../index.md) | [📘 NLP++ Textbook](../NLP++_Textbook.md)

# Actions

Actions are NLP++ functions that are specialized to know about particular contexts. For example, the POST Action **single** assumes that a rule has successfully matched.

Historically, actions preceded NLP++, and many do not allow full NLP++ expressions as arguments. The CODE, PRE, CHECK, and POST regions all have associated actions.

Many actions, such as the PRINT actions, are superseded by the C++ -like << operator and are retained for backward compatibility.

| **Note**: Some actions are slated for review. |
| --- |

## See Also

[CODE Action](AT-CODE_Actions.md)

[PRE Action](AT-PRE_Actions.md)

[CHECK Action](AT-CHECK_Actions.md)

[POST Action](AT-POST_Actions.md)

[Functions](Functions.md)
