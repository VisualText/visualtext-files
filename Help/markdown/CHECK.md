# CHECK Region

NLP++ code in the CHECK Region applies after the rule matcher has succeeded in matching a rule. These represent the final opportunity to reject the rule match based on inconsistencies spanning one or more rule elements. For example, before accepting a noun-phrase rule, we could check for agreement between the determiner and noun (e.g., accept "this company" but reject "these company").

Code in the CHECK Region precedes the execution of element actions (e.g., the **recurse** action by which an element invokes a minipass). Thus, the rule match can still be rejected before any side effects have been executed.

The special predefined function **fail()** immediately terminates execution of code in the CHECK Region and flags that the rule match has failed. The analogous function **succeed()** also terminates CHECK code immediately, but flags success and goes on to execute the element actions and code in the POST Region.

## See Also

[Grammar Region](NLP_PP_Stuff/Grammar_Region.md)

[CHECK Action](NLP_PP_Stuff/AT-CHECK_Actions.md)

[PRE Region](PRE.md)

[POST Region](POST.md)

[RULES Region](RULES.md)
