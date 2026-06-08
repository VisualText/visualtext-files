[← Help Contents](../index.md) | [📘 NLP++ Textbook](../NLP++_Textbook.md)

# PRE Action

PRE Actions operate **after** a rule element has successfully matched. They provide further constraints on the element match, and may result in the match being rejected if the additional constraints are not met.  PRE Actions provide the only means for specifying additional constraints on element matching.

## PRE Action Syntax

Unlike other actions, PRE Actions have a mandatory range. Their form is

**<num,num> pre_action_name(args....)**

The PRE Action applies to each rule element in the <num, num> range individually.

PRE Actions operate only on tokens, or leaf nodes of the parse tree, at present. So, if the current node covers more than a *single* leaf node, the PRE Action automatically *fails*. Another thing to be careful of is that PRE Actions disregard the **base** attribute of a node. That is, even if the current node or a subnode has the **base** attribute set, the PRE Action will look under it for the leaf node.

| **Note**: The PRE Region does not currently accept general NLP++ functions, expressions, and statements. |
| --- |

## Table of PRE Actions

Actions available in the PRE Region are provided in the table below.  For examples on using these actions, refer to the individual action topics in the @PRE Actions section.

| PRE Action | Description |
| --- | --- |
| **uppercase()** | Succeed if leaf token is all uppercase. |
| **lowercase()** | Succeed if leaf token is all lowercase. |
| **cap()** | Succeed if leaf token has capitalized first letter. |
| **length(num)** | Succeed if leaf token has length exactly equal to **num**. |
| **lengthr(num1,num2)** | Succeed if leaf token length is in the range of lengths (**num1**,**num2**), inclusive. |
| **numrange(num1,num2)** | Succeed if leaf token is numeric in the given range. |
| **unknown()** | Succeed if leaf token is an unknown word. Meaningful only if a prior pass has performed the CODE Action **lookup()**. |
| regexp(str) | Succeed if regular expression str matched. str may include characters, with ? meaning a single char, * meaning 0 or more chars. |
| regexpi(str) | Like **regexp**, but case insensitive. |
| var(str) | Succeed if matched node has a variable called **str** with nonzero value. |
| vareq(str,str_or_num) | Succeed if matched node has a variable called **str** whose value equals a string or numeric value in **str_or_num**. |
| varne(str,str_or_num) | Succeed if matched node has a variable called **str** whose value does not equal a string or numeric value in **str_or_num**. |
| varz(str) | Succeed if matched node has a variable called **str** with zero value (or lacks the variable altogether). |
| **debug()** | Succeed unconditionally. Used to place a C++ breakpoint at a particular rule. |

## See Also

[CODE Action](AT-CODE_Actions.md)

[CHECK Action](AT-CHECK_Actions.md)

[POST Action](AT-POST_Actions.md)
