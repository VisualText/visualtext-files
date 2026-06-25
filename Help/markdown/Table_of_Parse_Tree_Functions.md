[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# Table of Parse Tree Functions

The functions used to operate on parse trees have been listed here in table form for easy reference.  For examples of these functions, refer to the individual function pages included in the Parse Tree Functions section.

The return types include:  **INT** (integer), **PNODE** (parse tree node), **STR** (string), and **VAR VALUES** (variable values). **NONE** indicates nothing is returned.

| **FUNCTION NAME** | **RETURNS** | **DESCRIPTION** |
| --- | --- | --- |
| [**arraylength(VAR)**](arraylength.md) | **INT** | Count number of values in given variable or expr. (Like a call-by-reference) |
| [**eltnode(elt_num)**](eltnode.md) | PNODE | Fetch the first node that matched the nth element of a rule. |
| [**group(start_n,end_n,name_str)**](group.md) | PNODE | Perform a reduction in the @POST region. Replaces the old group action. (2.3.1.9 return the created node.) |
| [**inputrange(start_n,end_n)**](inputrange.md) | STR | Return a substring of the input text as specified by start and end offsets. |
| [**inputrange(start_n,end_n,out_ostr)**](inputrange.md) | BOOL | Print a range of chars from the input text to an output stream. |
| [**lasteltnode(elt_num)**](lasteltnode.md) | **PNODE** | Fetch the last node that matched the nth element of a rule. |
| [**phrasetext()**](phrasetext.md) | **STR** | Fetch the text that matched the right hand side phrase of a rule. Analogous to $text. |
| [**phraseraw()**](phraseraw.md) | **STR** | Fetch the raw text that matched the right hand side phrase of a rule. Analogous to $raw |
| [**pncopyvars(Pnode1,Pnode2)**](pncopyvars.md) [**pncopyvars(Pnode1,aConcept)**](pncopyvars.md) [**pncopyvars()**](pncopyvars.md) [**pncopyvars(aPnode)**](pncopyvars.md) [**pncopyvars(0)**](pncopyvars.md) | NONE | Copy a node's variables to the suggested node of a rule match, or to a concept in the KB hierarchy. Must be called from the POST Region and can be considered a new-style NLP++ action. |
| [**pndeletechilds(pnode)**](pndeletechilds.md) | **NONE** | Delete children of given pnode. |
| [**pninsert(name, pnode, after_n)**](pninsert.md) | **PNODE** | Insert nonliteral node with name into parse tree. If after_n == 1, insert after pnode, else if 0 then before pnode. |
| [**pnmakevar(pnode, var_str, val)**](pnmakevar.md) | NONE | Make a variable for a given pnode. |
| [**pnname(pnode)**](pnname.md) | **STR** | Fetch the name of a pnode. |
| [**pnnext(pnode)**](pnnext.md) | **PNODE** | Fetch a pnode's right sibling, if any. |
| [**pnpushval(pnode, var_str, val)**](pnpushval.md) |   | Push a value onto pnode's variable. **New in 2.7.3.2** |
| [**pnprev(pnode)**](pnprev.md) | **PNODE** | Fetch a pnode's left sibling, if any. |
| [**pnpush(pnode, name_str)**](pnpush.md) | **PNODE** | Group a single node under a new nonliteral parent node named name_str (must start with '_'). |
| [**pnremoveval(pnode, var_str)**](pnremoveval.md) | NONE | Remove a variable and its values from pnode. |
| [**pnrename(pnode, str)**](pnrename.md) | **STR** | Rename given pnode. Returns the interned name. |
| [**pnreplaceval**](pnreplaceval.md) | NONE | Replace the value of pnode's variable. |
| [**pnroot()**](pnroot.md) | **PNODE** | Fetch the root of a parse tree. |
| [**pnrpushval(pnode, var_str, val)**](pnrpushval.md) |   | Push a value onto end of pnode's variable. **New in 2.7.3.2** |
| [**pndown(pnode)**](pndown.md) | PNODE | Fetch the child of a parse tree node. |
| [**pnsingletdown(pnode)**](pnsingletdown.md) | **PNODE** | Fetch the child of a parse tree node, obeying rules about going down a "singlet chain." I.e., get child only if no branching and if not going past node with BASE flag set. |
| [**pnup(pnode)**](pnup.md) | **PNODE** | Fetch a pnode's parent, if any. Only leftmost pnode in a list has a parent. |
| [**pnsetfired(pnode, num)**](pnsetfired.md) | NONE | Set the fired flag of a pnode (num must be 0 or 1). |
| [**pnvar(pnode, var_str)**](pnvar.md) | **ARRAY** | Fetch a pnode's variable value(s). |
| [**pnvarnames(pnode)**](pnvarnames.md) | ARRAY | Fetch a node's variable names as an array. |
| [**pnvartype(pnode, var_str)**](pnvartype.md) | **INT** | Fetch the type of a pnode variable's value (0=string, 1=int, 2=concept, 3=float). |
| [**varinlist(var_str, elt_num)**](varinlist.md) | ARRAY | Find var_str variable's value(s) in any pnode that matched elt_numth element |

## See Also

[Special Functions](Table_of_Special_Functions.md)

[Knowledge Base Functions](Table_of_Knowledge_Base_Functions.md)

[Formatting and I/O Functions](Table_of_Formatting_and_I_O_Functions.md)

[String Functions](Table_of_String_Functions.md)

[Spelling Functions](Table_of_Spelling_Functions.md)
