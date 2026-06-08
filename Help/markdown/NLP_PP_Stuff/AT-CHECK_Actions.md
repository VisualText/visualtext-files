[← Help Contents](../index.md) | [📘 NLP++ Textbook](../NLP++_Textbook.md)

# CHECK Action

CHECK Actions operate **after** the rule's right-hand-side phrase has matched.

The **or** action is the only specialized function built for this region. General NLP++ code serves to implement most CHECK Actions that you would want to perform.

Two special NLP++ functions operate in the CHECK Region. When a rule match is to be aborted, the function **fail** is called to accomplish this. To succeed without performing further checks, call the **succeed** function. Both of these can occur in other regions, but may operate differently. If **succeed** is executed, then element actions and POST Actions are performed next.

## See Also

[succeed](../succeed.md)

[CODE Action](AT-CODE_Actions.md)

[PRE Action](AT-PRE_Actions.md)

[POST Action](AT-POST_Actions.md)
