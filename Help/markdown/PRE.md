[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# PRE Region

The PRE Region is used to extend the pattern matcher's mechanism for matching each rule element.   Currently, the PRE Region does not support general NLP++ expressions and statements.

## PRE Action Syntax

The actions used in the PRE Region have a mandatory range. Their form is

**<num,num> pre_action_name(args....)**

The PRE Action applies to each rule element in the <num, num> range individually.

PRE Actions operate only on tokens, or leaf nodes of the parse tree, at present. So, if the current node covers more than a *single* leaf node, the PRE Action automatically *fails*. Another thing to be careful of is that PRE Actions disregard the **base** attribute of a node. That is, even if the current node or a subnode has the **base** attribute set, the PRE Action will look under it for the leaf node.

## See Also

[Grammar Region](NLP_PP_Stuff/Grammar_Region.md)

[PRE Action](NLP_PP_Stuff/AT-PRE_Actions.md)

[CHECK Region](CHECK.md)

[POST Region](POST.md)

[RULES Region](RULES.md)
