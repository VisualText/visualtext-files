[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# Table of Knowledge Base Functions

The functions used to operate on objects in the Knowledge Base have been listed here in table form for easy reference.  For examples of these functions, please refer to the individual function pages within the subsections of the current Help section, Knowledge Base Functions.

The names of KB objects are abbreviated as follows: concept (**CON**), attribute (**ATTR**), value (**VAL**), and phrase (**PHR**).

The return types include: **CON**, **ATTR**, **VAL**, **PHR**, **INT** (integer),  **FLT** (float), **STR** (string), **BOOL** (Boolean).  Boolean type is currently implemented by integer **1** (or non-zero) for **true** and **0** for **false**.)  **NONE** indicates nothing is returned.

In the table below, a **name** must be a STR, **parent** is a CON, **attr_str** is a STR, **hier** is a CON.

| **FUNCTION(ARG1,ARG2...)** | **RETURN TYPE** | **DESCRIPTION** |
| --- | --- | --- |
| **Command File Functions** |   |   |
| [**kbdumptree(root_con, file_str)**](kbdumptree.md) | BOOL | Create a dump file of knowledge base concept. |
| [**loaddict(file_str)**](loaddict.md) | BOOL | Load a `.dict` dictionary file from the `kb/user` directory into the conceptual grammar. |
| [**loadkbb(file_str)**](loadkbb.md) | BOOL | Load a `.kbb` knowledge base file from the `kb/user` directory into the conceptual grammar. |
| [**take(file_str)**](take.md) | BOOL | Execute commands in a knowledge base command file (.KB file) |
| [**writekb()**](writekb.md) | BOOL | Dumps the entire KB currently in memory to the kb/user directory which includes a word.kb, attrs.kb, and main.kb file. |
| **Functions that Find and Fetch** |   |   |
| [**findroot()**](findroot.md) | **CON** | Find the root concept of the knowledge base (named **concept**). |
| [**findconcept(con, str)**](findconcept.md) | **CON** | Find and return the concept with name **str** under the parent concept **con**. |
| [**findconcept(con, num)**](findconcept.md) | **CON** | Find concept number **num** under the parent concept **con**. |
| [**findattr(con, str)**](findattr.md) | **ATTR** | Fetch attribute named **str** belonging to concept **con**. |
| [**findattrs(con)**](findattrs.md) | **ATTR** | Fetch concept's list of attributes. |
| [**attrname(attr)**](attrname.md) | **STR** | Fetch attribute's name. |
| [**attrtype(concept,attrName)**](attrtype.md) | **NUM** | Fetch an attribute's type. 0 = string, 1 = number, 2 = concept, 3 = float. |
| [**attrvals(attr)**](attrvals.md) | **VAL** | Fetch attribute's list of values. |
| [**findvals(con, name)**](findvals.md) | **VAL** | Fetch list of values for a concept's attribute. |
| [**numval(con, name)**](numval.md) | **NUM** | Fetch numeric-value of attribute (must be first). |
| [**fltval(con, name)**](fltval.md) | FLT | Fetch float value of attribute (must be first). |
| [**strval(con, name)**](strval.md) | **STR** | Fetch string-value of attribute (must be first). |
| [**conval(con, name)**](conval.md) | **CON** | Fetch concept-value of attribute (must be first). |
| [**attrwithval(con, attr_str, val_str)**](attrwithval.md) | **BOOL** | Check if concept's attribute has given value (multiple-value aware). Note that second two arguments must be STR. |
| [**inheritval(con, name, topCon)**](inheritval.md) | **STR** | Find string attribute's value up the hierarchy. **con** is the current concept, **topCon** is the root to be searched up to, and **name** is the name of the attribute. If hier==0, goes to root of KB. |
| [**conceptname(con)**](conceptname.md) | **STR** | Fetch name of given concept. |
| [**conceptpath(con)**](conceptpath.md) | **STR** | Fetch entire path of given concept as a string. |
| [**pathconcept(str)**](pathconcept.md) | **CON** | Fetch concept, given the path **str**. |
| [**wordpath(str)**](wordpath.md) | **STR** | Get entire path of dictionary concept for the given string. |
| [**findwordpath(str)**](findwordpath.md) | **STR** | Find entire path of dictionary concept for the given string. (If not present, don't add the word.) |
| [**wordindex(str)**](wordindex.md) | **CON** | Fetch index entry for dictionary concept. Gets index concept that str would be added under. |
| [**findhierconcept(name, hier)**](findhierconcept.md) | **CON** | Find a concept in the subhierarchy of a given concept. e.g.: G("returnedConcept") = findhierconcept("child",G("ancestor")); finds the concept named "child" anywhere under the concept pointed to by G("ancestor"). |
| [**dictfindword(str)**](dictfindword.md) | **CON** | Find dictionary concept in dictionary hierarchy of KB. |
| [**dictfirst()**](dictfirst.md) | CON | Fetch the first word-concept in the KB dictionary hierarchy.** (New in 1.6)** |
| [**dictnext(con)**](dictnext.md) | CON | Fetch the word following the given word in the KB dictionary hierarchy.** (New in 1.6)** |
| [**DICTphraselookup(node, key_str, match_str, list_str, skippunct_num)**](DICTphraselookup.md) | NONE | Look up a phrase in the KB dictionary by walking the parse tree from node alongside a phrase hierarchy reached via the key_str attribute. Annotates matching parse tree nodes with match info. |
| [**attrexists(hier, attr_s, val_s)**](attrexists.md) | **BOOL** | Find attribute and value pair in the subhierarchy of a concept. |
| [**attrchange(hier, attr_s, val_s, new_s)**](attrchange.md) | **BOOL** | Replace all matching attribute-value pairs in the given hierarchy to have the new string value, new_s. |
| [**down(con)**](down.md) | **CON** | Fetch the first child of given concept. |
| [**up(con)**](up.md) | **CON** | Fetch the parent of the given concept. |
| [**prev(con)**](prev.md) | **CON** | Fetch the left or previous sibling of concept. |
| [**next(con)**](next.md) | **CON** | Fetch the right or next sibling of concept. |
| [**nextattr(attr)**](nextattr.md) | **ATTR** | Fetch the next attribute in a list of attributes |
| [**nextval(val)**](nextval.md) | **VAL** | Fetch the next value in a list of values. |
| [**getsval(val)**](getsval.md) | **STR** | Fetch value as a string from a numeric or string-valued KB value object. |
| [**getstrval(val)**](getstrval.md) | **STR** | Fetch the string value from a KB value object. |
| [**getfltval(val)**](getfltval.md) | **FLOAT** | Fetch number from float VAL. |
| [**getnumval(val)**](getnumval.md) | **INT** | Fetch number from numeric VAL. |
| [**getconval(val)**](getconval.md) | **CON** | Fetch concept from value. |
| **Functions that Create** |   |   |
| [**makeconcept(parent, name [, num] )**](makeconcept.md) | **CON** | Make concept under given parent concept. Optionally as the numth child of the parent. num==0 or absent places concept at end of list of children. name is the name of new concept. |
| [**addattr(con, attr_s)**](addattr.md) | **ATTR** | Add an attribute with no value to given concept. |
| [**addsval(con, name, num)**](addsval.md) | **NONE** | Add numeric value num as a string to concept con's attribute called name. |
| [**addstrval(con, name, str)**](addstrval.md) | **NONE** | Add str as string value to concept con's attribute called name. |
| [**addnumval(con, name, num)**](addnumval.md) | **NONE** | Add num as numeric value to concept con's attribute called name. |
| [**addconval(con, name, con_val)**](addconval.md) | **NONE** | Add concept value con_val to concept's name attribute. |
| [**getconcept(parent, name)**](getconcept.md) | **CON** | Get or make named concept under parent. |
| [**addword(str)**](addword.md) | **CON** | Add dictionary concept to the dictionary within the KB, if not present. In either case, fetch the dictionary concept for the word. |
| [**dictgetword(str)**](dictgetword.md) | CON | Same as *addword*; more principled function name. |
| [**sortconsbyattr(arr_c, attr_s, numeric_b, descending_b)**](sortconsbyattr.md) | ARR | Given an array (multi-valued variable) of KB concepts, sort the concepts by the given attribute. numeric_b = 1 if num, 0 if string type attribute. descending_b = 1 if descending order, 0 if ascending. E.g., *G("sorted") = sortconsbyattr(G("cons"),"count",1,0);* will sort an array of KB concepts by their "count" attribute in ascending order, assigning a new sorted array to G("sorted"). The given array in G("cons") is left unaltered. **New in 1.6** |
| **Functions that Move and Remove** |   |   |
| [**rmconcept(con)**](rmconcept.md) | **BOOL** | Remove concept **con** from Knowledge Base. Removes entire subhierarchy. |
| [**rmchild(con, str)**](rmchild.md) | **BOOL** | Remove child named **str** from parent concept **con**. |
| [**rmchild(con, num)**](rmchild.md) | **BOOL** | Remove number **num** child of parent concept **con**. |
| [**rmvals(con, str)**](rmvals.md) | **BOOL** | Remove attributes and values of concept **con**'s attribute named **str**. |
| [**rmval(attr, val)**](rmval.md) | **BOOL** | Remove value **val** from attribute **attr**. |
| [**rmattrval(con, str1, str2)**](rmattrval.md) | **BOOL** | Remove value named **str2** from attribute named **str1** under concept **con**. Also removes the attribute. |
| [**rmattrs(con)**](rmattrs.md) | **BOOL** | Remove concept's attributes (except for system internal ones). |
| [**rmattr(con,name)**](rmattr.md) | **BOOL** | Remove concept's named attr and values. |
| [**rmchildren(con)**](rmchildren.md) | **BOOL** | Remove concept's children and phrase. |
| [**rmword(str)**](rmword.md) | **BOOL** | Remove dictionary concept from KB. |
| [**prunephrases(hier)**](prunephrases.md) | **BOOL** | Remove all phrases from given subhierarchy. |
| [**replaceval(con, name, str)**](replaceval.md) | **NONE** | Replace named attribute's value(s) with str. |
| [**replaceval(con, name, num)**](replaceval.md) | NONE | Replace named attribute's value(s) with num. |
| [**replaceval(con, name, con_val)**](replaceval.md) | NONE | Replace named attribute's value(s) with concept con_val |
| [**renameconcept(con, name)**](renameconcept.md) | NONE | Rename given concept to name. |
| [**renamechild(con, num, name)**](renamechild.md) | NONE | Rename con's numth child concept to name. |
| [**renameattr(con, name, new)**](renameattr.md) | NONE | Rename con's named attribute to new. |
| [**movecleft(con)**](movecleft.md) | NONE | Move concept before previous sibling. (Moves concept to the left in its list.) |
| [**movecright(con)**](movecright.md) | NONE | Move concept after next sibling. (Moves concept to the right in its list.) |
| [**sortchilds(con)**](sortchilds.md) | NONE | Sort concept's immediate children alphabetically. |
| [**sorthier(con)**](sorthier.md) | NONE | Sort concept's subhierarchy alphabetically. |
| **Phrase and Node Functions** |   |   |
| [**findphrase(con)**](findphrase.md) | **PHR** | Fetch concept's phrase. |
| [**sortphrase(con)**](sortphrase.md) | NONE | Sort concept's phrase nodes alphabetically. |
| [**phraselength(con)**](phraselength.md) | **INT** | Get number of nodes in concept's phrase. |
| [**nodeconcept(node)**](nodeconcept.md) | **CON** | Fetch the concept that node is a proxy for. **(Changed in 1.6)** |
| [**nodeowner(node)**](nodeowner.md) | CON | Fetch the concept that owns the node's phrase.** (NEW in 1.6)** |
| [**findnode(phrase, name)**](findnode.md) | **CON** | Find first named node in phrase. |
| [**findnode(phrase, num)**](findnode.md) | **CON** | Find the numth node in phrase. |
| [**listnode(node)**](listnode.md) | **CON** | Fetch the first node in given node's list. |
| [**firstnode(phrase)**](firstnode.md) | **CON** | Fetch the first node in phrase. |
| [**lastnode(phrase)**](lastnode.md) | **CON** | Fetch the last node in phrase. |
| [**makephrase(con, name)**](makephrase.md) | **PHR** | Make a phrase in con by creating named node. |
| [**addcnode(con, name)**](addcnode.md) | **CON** | Add named node at end of con's phrase. |
| [**addnode(phrase, name, num)**](addnode.md) | **CON** | Add named node as numth in phrase. |
| [**rmnode(con)**](rmnode.md) | NONE | Remove node from concept's phrase. |
| [**rmphrase(phrase)**](rmphrase.md) | NONE | Remove phrase from its concept. |
| [**rmcphrase(con)**](rmcphrase.md) | NONE | Remove a concept's phrase. |
| [**renamenode(phrase, name, new)**](renamenode.md) | NONE | Rename phrase's named node to new. |
| [**renamenode(phrase, num, new)**](renamenode.md) | NONE | Rename phrase's numth node to new. |

## See Also

[Special Functions](Table_of_Special_Functions.md)

[Formatting and I/O Functions](Table_of_Formatting_and_I_O_Functions.md)

[Parse Tree Functions](Table_of_Parse_Tree_Functions.md)

[String Functions](Table_of_String_Functions.md)

[Spelling Functions](Table_of_Spelling_Functions.md)
