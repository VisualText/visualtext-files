# POST Action

NLP++ code in the POST Region executes **after** the rule matcher has successfully matched a rule and the match is accepted.

## Types of POST Actions

POST Actions are divided into four groups:

- Node Actions

- Reduce Actions

- Print Actions

- Variable Actions

One suite of POST Actions for the RFA (Rule-File Analyzer) is not described, as they are not relevant to the VisualText™ user. Their names typically begin with the prefixes** rfa-** or **rfb-**.

## Tables of POST Actions

Actions available in the POST Region are provided in the table below.  For examples on using these actions, refer to the individual action topics in the included in the @POST Actions sections.

## Node Actions

| POST Action | Description |
| --- | --- |
| **pncopyvars(aPnode)** pncopyvars(num) pncopyvars(0) | Copy a node's variables to the suggested node of a rule match. Must be called from the POST Region and can be considered a new-style NLP++ **action**. See pncopyvars. |
| setbase(num, bool) | Set the BASE attribute of the ***num***th node to "true" or "false". |
| setunsealed(num, bool) | Set the UNSEALED attribute of the ***num***th node to "true" or "false". |
| xrename(name [, num]) | Rename the ***num***th context node to ***name***. If *num* is absent or 0, rename last context node. |

## Reduce Actions

| POST Action | Description |
| --- | --- |
| setlookahead(num1) | Set the node that rule matcher will continue with, after the current rule match is done. New in 1.7.5.2 |
| **single()** | Single-tier reduce. Reduce the entire set of nodes that matched a rule phrase. |
| **singler(num1,num2)** | Single-tier reduce of a range of rule elements. eg, if finding a period to be end-of-sentence in context, we only want to reduce the period to end-of-sentence, not the whole context. |
| **singlex(num1,num2)** | Single-tier reduce of a range of rule elements. All nodes not in the range are EXCISED. eg, if matching a keyword html tag, we only want to reduce the keywords and to zap the rest of the tag. |
| **singlezap()** | Single-tier reduce. Excise all the nodes in the matched phrase. |
| **merge()** | Single-tier reduce that DISSOLVES each top-level node in the matched phrase. |
| **merger(num1,num2)** | Single-tier reduce that DISSOLVES each top-level node in the matched range. |
| **listadd(olist,oitem [, keep])** | Add a new node to a list node's children. If the item occurs after the list (***olist*** < ***oitem***), it is added as the last child. If the item occurs before the list, it is added as the first child. The optional keep arg can be "true" or "false". If "true", it keeps the nodes between the list and the item as children of list. If "false", it excises all the intervening nodes. |
| **excise(num1,num2)** | Excise the nodes matching the range of elements from the parse tree. For multiple excise actions, operations must be ordered such that the highest number is listed first in the operation. |
| **splice(num1,num2)** | DISSOLVE the top level nodes of given range. |
| **group(num1,num2,label_str)** | Reduce the range of rule elements **(num1,num2)** and name the group node** label**. Unlike other reduce actions, this one can be repeated. ***WARNING:*** The rule element numbers change after each group action, so subsequent POST Actions must account for the new numbering of the rule elements. Reimplemented as an NLP++ function so that args can be NLP++ expressions. |
| **noop(0)** | Perform no POST Action. This is a convenience to disable the default **single()** reduce action. |

## Print Actions

| POST Action | Description |
| --- | --- |
| **print(str)** | Print the literal string **str** to standard output. |
| **printr(num1,num2)** | Print the text for the rule element range from **num1** to **num2** to standard output. |
| **prchild(file, num, name)** | Look for **name** immediately under the node matching rule element **num**. Print its text to **file**, if found. |
| **prtree(file, num, name)** | Look for **name** anywhere under the node matching rule element **num**. Print its text to **file**, if found. |
| **prxtree(filename, prestr,**** ord, name, poststr)** | To the **filename**, print the first node called **name** found in the **ord**th element's tree, preceded by **prestr** and followed by **poststr**. If named node is not found, nothing is printed out. E.g., prxtree("out.txt", "date: ", 3, "_date", "\n") prints out a line like "date: 3/9/99 <cr>" if a _date node is found within the subtree of elt 3. |
| **prlit(file, str)** | Print the literal string **str** to **file**. |
| **fprintnvar(file, var, ord)** | To the **file**, print the value of the variable **var** in the **ord**th element's node. |
| **fprintxvar(file, var, ord)** | To the **file**, print the value of the variable **var** in the **ord**th context node. |
| **fprintgvar(file, var)** | To the **file**, print the value of the global variable **var.** |
| **gdump(file)** | Dump all the global variables and their values to **file**. |
| **xdump(file, ord)** | Dump all the variables in the **ord**th context node and their values to **file**. |
| **ndump(file, ord)** | Dump all the variables in the **ord**th phrase element's node and their values to **file**. |
| **sdump(file)** | Dump all the variables in the suggested node and their values to **file**. |
| **prrange(file, num1,num2)** | Print the text under a range of rule elements (**num1,num2**) to** file**. |
| **pranchor(file,num1,num2)** | Print a web URL to **file**. Treat the range (**num1,num2**) as a URL. Use the global variable named **Base** to resolve and print complete relative URLs. (a prior pass must find the <base> HTML tag and set **Base** appropriately. NOT yet using the file's URL, so not handling cases where <base> itself is a relative URL.) |

## Variable Actions

| POST Action | Description |
| --- | --- |
| **addstrs(var,num)** | Add a string to the multi-string **global** variable **var**. Fetch the string from the nodes matching rule element **num**. **var** should have been declared using the CODE Action **varstrs()**. (***REMOVED***. Use NLP++ array syntax instead.) |

## See Also

[CODE Action](AT-CODE_Actions.md)

[PRE Action](AT-PRE_Actions.md)

[CHECK Action](AT-CHECK_Actions.md)
