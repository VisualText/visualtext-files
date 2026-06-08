[← Help Contents](../index.md) | [📘 NLP++ Textbook](../NLP++_Textbook.md)

# Pass Files

A pass file (also called a rule file), consists of NLP++™ code and rules. A pass file represents a single pass of a text analyzer over a parse tree. There are two different algorithms used to traverse the parse tree: PAT (for pattern) and REC (for recursive).

The PAT algorithm uses rules in a pattern-based way, traversing each selected phrase in the parse tree only once, while the REC algorithm treats the rules as a recursive grammar, traversing each selected phrase repeatedly till no rules match within that phrase.

## Layout

The pass file, which is used by a single analyzer PAT pass, consists of sets of nonrepeating and repeating regions, which must be ordered in a pass file as follows:

| **REGION** | **REPEATABLE** | **DESCRIPTION** |
| --- | --- | --- |
| **Code** | **NO** | Interpreted actions that precede the rule matching process. |
| **Context** | **NO** | Specifies nodes of the parse tree. Rules will match only against the phrases immediately under those nodes. |
| **Minipass** | **YES** | Recursive minipasses. Each recurse region is named and can contain repeating rules regions. Rule elements in the main RULES region (below) can invoke these named rule sets. |
| **Grammar** | **YES** | The main actions-rules regions for the current file (i.e., the current pass). |

A pass file must contain at least a @CODE region or a main @RULES region.

## Code Region

The CODE region consists of interpreted actions that operate before the rule matching for the current file, but only once for the current file. Each action looks like

**name(arg1,...argN)**

which is identical to the syntax for PRE, CHECK, and POST actions. (PRE actions have an additional bracketed range at the start of each such action.) See the CODE ACTIONS section below for details about available actions. For a particular application, the developer can create new code actions within the application's USER project.

## Select Region

The Select Region allows the user to specify which nodes of the parse tree to execute. The region is optional, and the default is to match the rules of the file against the top-level phrase of the parse tree, that is, the phrase directly under the **_ROOT** node. The default could be made explicit, as in the following sample Select Region:

| @SELECT | # Start of Select Region |
| --- | --- |
| @NODES _ROOT | # Specifies nodes whose underlying phrase will be matched against. |
| @@SELECT | # Optional end-marker for Select Region |

(Note that the region markers @SELECT and @@SELECT are also optional. The sample Select Region above could be simply @NODES _ROOT.)

If there is more than one*** ***@NODES marker, or if more than one name appears after a @NODES marker, those names are all collected into a single list. The pattern matcher makes a single pass through the parse tree, looking for a node from this list. If such a node is found, the phrase under it is matched against the rules of the file. More than one @NODES is unimplemented.

Instead of @NODES, one can specify the @MULTI marker, which also takes a list of node names. This applies the rules in the file to every phrase in the subtree of the selected nodes, allowing multiple matches in the subtree. Needless to say, the rule writer must be careful in using rules with the singlet and tree keys in conjunction with the MULTI specifier.

| **SELECT TYPE** | **DESCRIPTION** |
| --- | --- |
| **@NODES** | Directs the pattern matching algorithm (e.g., PAT or REC) to nodes in the parse tree. The phrase immediately under such a node will be traversed to look for rule matches. **WARNING:** The pattern matcher will only find such nodes inside a path with the unsealed attribute set to true in all nodes of the path. |
| **@MULTI** | Directs the pattern matching algorithm (e.g., PAT or REC) to nodes in the parse tree. The entire subtree under such a node will be traversed to look for rule matches. |
| **@PATH** | Directs the pattern matching algorithm (e.g., PAT or REC) to a specific path of nodes in the parse tree. The phrase immediately under the last node in the path list will be traversed to look for rule matches. The list must always start with the node _ROOT. The second name in the path must be a direct child of _ROOT, the third, a child of that, and so on. |

If one SELECT node is inside the subtree of another SELECT node, then the one inside will not be *seen* by the pattern matcher. @MULTI in combination with [s] or singlet mode can lead to unexpected behavior, such as matching the same pattern multiple times. Normally, you will want to avoid using [s] in rule elements when specifying a @MULTI traversal of a parse subtree.

## Recurse Region

The Recurse Region allows the user to create several passes within a single pass file. Each recurse region acts like an independent pass. But a recurse pass can only be invoked from an element of a rule that has matched. The phrase that the recurse pass operates on is the set of nodes that matched the invoking rule element. Here's an example taken from the RFA (Rules-File Analyzer), which parses the pass files themselves.

```
# Start of recurse region. A name is required.
```

```
@RECURSE actionpass
```

```
# Start of one rules region within the recurse region.
```

```
@RULES
```

```
# The pass converts literals (e.g., "single") to actions in context.
```

```
_ACTION <- _LIT @@
```

```
# End of recurse region. (@@RULES marker is optional).
```

```
@@RECURSE
```

```
# ....
```

```
# A main rules region.
```

```
@RULES
```

```
_POSTS [base] <- _soPOST
```

```
_xWILD [matches=(_LIT _ACTION) recurse=(actionpass)]
```

```
_eoPOST [opt] @@ # Simplified rule for @POST actions region.
```

In the above example, when the RFA sees a plain word like "single" in a file, it doesn't know whether to reduce it to an _ACTION or not. But within the markers @POST and @@POST, the literal should be treated as an action. This allows the parentheses in pass file actions to be optional, when the action takes no arguments. E.g., "single()" and "single" are equivalent.

In general, RECURSE mini-passes enable a mechanism for "roughing out" a text and then applying the correct assignments when the context has been determined unambiguously. They have many other uses, such as traversing nodes that matched a rule element in order to perform cleanups, data gathering, deletions, and so on.

**NOTE:** A Recurse Region cannot contain a Code Region or a Select Region. A Select Region would be meaningless, since the recurse region operates on a phrase specified by the rule element that invokes it. A code region could be implemented if it proves useful.

## **Rules Region**

The main Rules Regions (that follow the Code, Select, and Recurse Regions in a pass file), as well as the Rules Regions nested inside a Recurse Region, must be laid out as follows:

| **SUBREGION** | **DESCRIPTION** |
| --- | --- |
| **PRE** | Additional conditions on the matching of individual rule elements. |
| **CHECK** | When a rule has matched, these actions check self-consistency and/or build semantic data. These actions can be used to reject a rule match. |
| **POST** | Actions that operate once a rule match has been accepted. |
| **RULES** | Subregion containing the actual rules that are subject to immediately preceding Pre,Check, and Post subregions. If a Rules subregion has no preceding action subregions, then it resets its actions to the default (single reduce). |

Each region has a set of markers for it: @PRE and @@PRE, @CHECK and @@CHECK, @POST and @@POST, @RULES and @@RULES. The end-markers are optional. Sections below detail the particular actions available in each category.

## **Rule Syntax**

Within each Rules Subregion, any number of rules can occur. The syntax for a rule is

**_SUGG <- _PHRASE @@**

The _SUGG, or suggested rule element is followed by the rule arrow, then by a phrase of elements, and finally the @@ end-mark. Each element, including the suggested element, consists of a literal or nonliteral. Literals match tokens, or "real text", while nonliterals match nodes with synthetic names. A nonliteral must begin with an underscore, a literal must not begin so.

Optionally, each element can be followed by a list of key=values *pairs* enclosed in square brackets. Though called pairs, some keys, such as **trigger**, take no values. Some special rule elements, as well as the key=value pairs that appear in phrase and suggested elements, are listed in tables below.

## Pass File Tokens

| **ITEM** | **DESCRIPTION** |
| --- | --- |
| **#** | Comment. Text till the end of the line is ignored. |
| **AAA or NNN** | Literal tokens. Completely alphabetic or completely numeric. |
| **_AAA** | Nonliteral tokens must begin with underscore. All the remaining letters MUST be alphabetic. (May expand to underscore,num,dash someday.) |
| **"XXX"** | Strings get double quoted. Everything within string taken literally (except backslashed characters). |
| **\X** | Backslash any nonalphanumeric char you want taken literally. |
| **\\** | Literal backslash character. |
| **\** | At end of line, escapes end of line to NOTHING. [Unimplemented] |
| **\X** | where X=abnrftv special escapes in C/C++. |
| **@AAA** | Reserved start-of-region markers in the pass file (e.g., @RULES). |
| **@@AAA** | Reserved end-of-region markers in the pass file (e.g., @@RULES). |
| **<-** | Rule arrow. |
| **@@** | Rule terminator. |

## Punctuation

Each punctuation character is treated as a separate entity or "token" in the rule file, even if there is no separating space. Constructs like **_xWILD [matches=(_noun)]** and **_xWILD [ matches = ( _noun ) ]** are parsed identically.

## Larger Structures

| **[AAA=XXX AAA=(XXX XXX) AAA]** | PAIRS. Square brackets enclose the key=value pairs for a rule element (phrase element or suggested element). A sample rule with pairs:** _np <- _adj _xWILD [match=( a b) ren="noun" s] _noun [trigger] @@** |
| --- | --- |
| **AAA(XXX,XXX....)** | ACTION. check and post action language. |
| **<NUM,NUM> XXX(XXX,XXX...)** | PRE ACTION. <NUM,NUM> is a range of rule elements that must execute the action during rule matching. |

ALL MATCHING IS CASE-INSENSITIVE. The rule-writer can add restrictive actions, like uppercase(), as needed. Currently, wildcard cannot appear as the start, end, or trigger of a rule. Optional elements cannot be triggers.

## ****Rule Elements

Special rule elements are given in the following table.

| **RULE ELEMENT** | **DESCRIPTION** |
| --- | --- |
| **_xWILD** | Unrestricted wildcard. Key-value pairs may add restrictions on number of nodes matched and on what is matched. (Note: with a *match* or *fail* list, _xWILD becomes an "OR" matching function.) |
| **_xANY** | Matches any single node. (See warning [1] below.) |
| **_xNIL** | Designates a suggested element when the rule performs a special action, such as removing the matched nodes from the parse tree. (_xNIL has no special action, but serves as documentation for the rule writer.) |
| **_xALPHA** | Matches an alphabetic token, including accented and other extended ANSI chars. |
| **_xCTRL** | Matches control and nonalphabetic extended ANSI characters. (see _xALPHA) |
| **_xNUM** | Matches a numeric token. |
| **_xPUNCT** | Matches a punctuation token. |
| **_xWHITE** | Matches a whitespace token, *including* newline. |
| **_xBLANK** | Matches a whitespace token, *excluding* newline. Equivalent to ***_xWILD [match=(\ \t)]*** |
| **_xCAP** | Matches an alphabetic with uppercase first letter. |
| **_xEOF** | Matches the end of file. |
| **_xSTART** | Matches if at the start of a phrase (or "segment"). |
| **_xEND** | Matches if at the end of a phrase (or "segment"). |

## ****Pairs for a Phrase Element** **

| **KEY** | **VALUE** | **DESCRIPTION** |
| --- | --- | --- |
| **trigger,trig,**** t** | NONE | Match the current element first. E.g., _*np <- _det _quan _adj _noun ****[t]**** @@* |
| **min** | NUM | Match a minimum of NUM nodes. 0 means the current element is optional. E.g., *_boys <- the [****min=0**** max=1] boys @@* |
| **max** | NUM | Match a maximum of NUM nodes. 0 means the current element can match an indefinite number of nodes. E.g., *_htmltag <- \< _xWILD [min=1 ****max=100****] \> @@* |
| **optional,option,opt,**** o** | NONE | Optional element. Match a minimum of 0 and a maximum of 1 node. (Short for min=0 max=1). E.g., *_vgroup <- _modal [****opt****] _have [****opt****] _be [****opt****] _verb @@* |
| **one** | NONE | Match exactly one node. (Short for min=1 max=1). |
| **star** | NONE | Indefinite repetition. Match a minimum of 0 up to any number of nodes. (Short for min=0 max=0). |
| **plus** | NONE | Indefinite repetition. Match a minimum of 1 up to any number of nodes. (Short for min=1 max=0). |
| **group, gp** | NAME | Gather nodes that matched elt under a single node with NAME as its name. Analogous to group post-action. |
| **rename,ren** | NAME | Rename every node that matched the current element to NAME. E.g., *_locfield <- location \: _xWILD [****ren=_location****] \n @@* |
| **singlet,**** s** | NONE | Search a node's descendants for a match. Stop looking down when a node has more than one child or has the BASE attribute set (see base below). E.g., *_abbr <- _unk \. ****[s]**** @@* |
| **tree** | NONE | Search node's entire subtree for a match. (Overuse of this may degrade analyzer performance.) |
| **matches,**** match** | LIST | For _xWILD element only. Restricted wildcard succeeds only if one of the list names matches a node. E.g., *_james <- _xWILD [****match=(jim jimmy james)**** singlet min=1 max=1] @@* |
| **fails,**** fail** | LIST | For *ANY* element. Match fails if node matches anything on the list. E.g., *_par <- _xWILD [****fail=(_endofpar _par)**** min=1 max=0] @@* |
| **excepts, except** | LIST | For ANY element. Must be accompanied by a single *match* or *fail* list. Matching an item on the except list negates the effect of a match on the *match* or fail *list*. |
| **lookahead, look** | NONE | Designates the first lookahead element of a rule. The first node matching the lookahead element or to the right of it will be the locus where the pattern matcher *continues* matching. WARNING: A reduce action such as *singler* or *noop* should be used to ensure that the lookahead node and nodes to its right are not included in the current rule reduction. |
| **layers, layer,**** attrs, attr** | LIST | Layer additional attributes for the element in the parse tree, as "mini-reductions". Use the names in the list to name nodes. Note: each node that matched current rule element will be layered. |
| **recurse, nest,**** passes, pass** | LIST | Invoke a recursive rules pass on nodes that matched the current rule element. E.g., *_tag <- \< _xWILD [****nest=(tagrules)****] \> @@. *(See the Recurse Region discussion.) |

**WARNING:** [1] Don't write rules with _xANY [max=0]. They won't work, because _xANY is not implemented as a wildcard. The nearly equivalent _xANY _xWILD works. [2] More generally, matching with MIN and MAX is *greedy*, and no *backup* is implemented. So the rule   _a <- _b [min=1 max=3] _c [s] @@

fails on the phrase **_b _b(subnode _c**), because the repeating _b element greedily gobbles up the second _b node. The pattern matcher will not back up to find that the rule can be made to work. Unrestricted _xWILD is the **only** rule element that is "backup-aware".

## ****Pairs for a Suggested Element

| **base** | NONE | The suggested node is the bottom-most node to search when looking down the parse tree for a match (see singlet above). (Takes no value). |
| --- | --- | --- |
| **unsealed** | NONE | The suggested node will be searched for select nodes (i.e., nodes specified by @NODES). |
| **layers**** layer**** attrs**** attr** | LIST | After normal reduce, perform additional reduces, naming the nodes as in the list. This enables layering of attributes in the parse tree. |

## NLP++ Functions

The code, pre, check, and post actions listed in subsequent sections are still valid. However, a suite of general functions that can occur in any region is being implemented, and some of the old actions may go away or be generalized to work in any region that allows NLP++ code. Reduction and parse tree manipulation functions should still go in the post region, because that code executes when a rule match is deemed to be successful. The check region may be folded into the post region, since NLP++ functions can be implemented to pronounce that a rule match has succeeded or failed. The pre region still does not allow general NLP++ expressions. NLP++ functions are described in the NLP++ and Knowledge Base help pages.

WARNING: Many of the old-style actions are not recognized by the compiled analyzer engine. Use NLP++ expressions wherever possible, rather than the old hard-wired actions. Compiling with MS Visual C++ points out which functions are invalid. The documentation below also marks old-style actions slated to be removed from NLP++.

## ****Output Actions

Code actions and rule actions (pre, check and post) are meant to work together in many cases. The code region in a file operates before any rule-matching is invoked, so that is where the user should initialize variables and perform other functions, such as printouts that are independent of any rule.

There are three output modes: (1) output to standard output, (2) output to a file named in the actions themselves, and (3) output to the "main output file" (default name **output.txt**) that is set by the environment that calls the analyzer. Then we throw into the mix actions that print in the code region as well as actions that print when a rule matches.

Rather than have three types of output (or "print") actions, we maintain two: actions that take a file argument and equivalents that do not. By default, output actions that take no file argument print to standard output. However, when delimited by the code actions **startout()** and **stopout()**, these actions print to the main output file, rather than standard output. If print actions in the rules are also to write to the main output file, then the **stopout()** action must be placed in the code region of a subsequent pass.

For output actions with a filename argument, the file must have been previously declared with a **fileout()** action.

Output is complex, but to allow the analyzer developer as much flexibility as possible, we must support many modes.

## Code Actions

Code actions are not tied to any rule, but execute operations for the entire pass. They are placed within the @CODE and @@CODE markers at the head of the file, called the *code region*. There is only one such region per file, and its actions operate before the pattern matching of the rules in the file. This region represents an embryonic programming language that enables the analyzer developer to perform useful tasks without having to write and compile regular programming language code.

Code actions operate *before* the rules in the file operate on the parse tree. At present, there is no "post code" region to execute actions *after* the rules for a pass have matched. The user must place such code actions in a subsequent analyzer pass.

NLP++ is now valid in the code region.

Variable names must be strings, at present.

A. VARIABLE ACTIONS

| **ACTION(ARG1,ARG2...)** | **DESCRIPTION** |
| --- | --- |
| **var(varname,str)** | Create **global** variable with name **varname** and initial value **str**. If str2 is all numeric, then the code action** inc()** can increment the value of the variable (this implements a counting variable). **(Old-style. Use NLP++)** |
| **varstrs(varname)** | Create an empty multi-string-valued **global** variable with name **varname**. The post action **addstrs()** adds values to this type of variable. |
| **sortvals(varname)** | Sort the strings in multi-string-valued **global** variable **varname**. |
| **gtolower(varname)** | Convert the strings in multi-string valued **global** variable to lower case. |
| **guniq(varname)** | Remove redundancies in a sorted, multi-string valued **global** variable. |
| **lookup(var,file,flag)** | Specialized word lookup. **Global **variable **var** has multiple words as values. **file** is a file of strings, one per line. **flag** tells which bit-flag of the word's symbol table entry to modify. E.g., **lookup("Words", "dict.words", "word")** looks up all the values in the **Words** variable in the **dict.words** file and modifies the **word** bit-flag (which says whether the word is a proper English word). |

B. PRINT ACTIONS

| **print(str)** | Print str to the standard output (usually the console or DOS window). (See ***startout*** below). |
| --- | --- |
| **printvar(var)** | Print the values of the **global** variable named **var** to standard output. (See ***startout*** below). |
| **fprintvar(file, var)** | Print the values of the **global** variable named **var** to **file**. |
| **prlit(file, str)** | Print the literal string **str** to **file**. |
| **gdump(filename)** | Dump the all the global variables and their values to the given filename. |
| **fileout(file)** | Open **file** for appending. **File** becomes a variable useable in print actions with a file argument, e.g. **prlit()**. |
| **startout(0)** | Divert standard output to the main output file, set by the caller of the analyzer (default is **output.txt**). |
| **stopout(0)** | Stop diverting standard output to the main output file. Subsequent file-less output is to standard output. |

## ****Pre Actions

Pre actions extend the pattern matcher's mechanism for matching each rule element. Unlike other actions, pre actions have a mandatory range. Their form is

**<num,num> pre_action_name(args....)**

The pre action applies to each rule element in the <num, num> range individually.

Pre actions operate only on tokens, or leaf nodes of the parse tree, at present. So, if the current node covers more than a *single* leaf node, the pre action automatically *fails*. Another thing to be careful of is that pre actions disregard the **base** attribute of a node. That is, even if the current node or a subnode has the **base** attribute set, the pre action will look under it for the leaf node.

| **uppercase()** | Succeed if leaf token is all-uppercase. |
| --- | --- |
| **lowercase()** | Succeed if leaf token is all-lowercase. |
| **cap()** | Succeed if leaf token has capitalized first letter. |
| **length(num)** | Succeed if leaf token has length exactly equal to **num**. |
| **lengthr(num1,num2)** | Succeed if leaf token length is in the range of lengths (num1,num2), inclusive. |
| **numrange(num1,num2)** | Succeed if leaf token is numeric in the given range. |
| **unknown()** | Succeed if leaf token is an unknown word. Meaningful only if a prior pass has performed **lookup()** code action. |
| **debug()** | Succeed unconditionally. Used to place a C++ breakpoint at a particular rule. |

## Check Actions

Check actions apply after the pattern matcher has succeeded in matching a rule. These represent the final opportunity to reject the rule match based on inconsistencies spanning more than one rule element. For example, before accepting a noun-phrase rule, we could check for agreement between the determiner and noun (e.g., accept "this company" but reject "these company").

See the section on NLP++ for a more generalized way to express conditions in the Check region.

| **or(num1,num2)** | Succeed if any of the rule elements from **num1** to **num2** has matched an actual node. Meaningful only if this is a range of *optional* rule elements. (This action is just a sample. As Text Analysis International™ develops its generic analyzer, more check actions will be implemented.) |
| --- | --- |

## Post Actions

Post actions execute after the pattern matcher has successfully matched a rule and the match is accepted.

#### **A. PARSE TREE ACTIONS**

| **single()** | Single-tier reduce. Reduce the entire set of nodes that matched a rule phrase. |
| --- | --- |
| **singler(num1,num2)** | Single-tier reduce of a range of rule elements. eg, if finding a period to be end-of-sentence in context, we only want to reduce the period to end-of-sentence, not the whole context. |
| **singlex(num1,num2)** | Single-tier reduce of a range of rule elements. All nodes not in the range are EXCISED. eg, if matching a keyword html tag, we only want to reduce the keywords and to zap the rest of the tag. |
| **singlezap()** | Single-tier reduce. Excise all the nodes in the matched phrase. |
| **merge()** | Single-tier reduce that DISSOLVES each top-level node in the matched phrase. |
| **merger(num1,num2)** | Single-tier reduce that DISSOLVES each top-level node in the matched range. |
| **listadd(olist,oitem [, keep])** | Add a new node to a list node's children. If the item occurs after the list (***olist*** < ***oitem***), it is added as the last child. If the item occurs before the list, it is added as the first child. The optional keep arg can be "true" or "false". If "true", it keeps the nodes between the list and the item as children of list. If "false", it excises all the intervening nodes. |
| **excise(num1,num2)** | Excise the nodes matching the range of elements from the parse tree. For multiple excise actions, operations must be ordered such that the highest number is listed first in the operation. |
| **splice(num1,num2)** | DISSOLVE the top level nodes of given range. [NOT TESTED whether a reduce such as single can follow this action.] |
| **xrename(name [, num])** | Rename the ***num***th context node to ***name***. If *num* is absent or 0, rename last context node. |
| **setbase(num, bool)** | Set the BASE attribute of the ***num***th node to "true" or "false". |
| **setunsealed(num, bool)** | Set the UNSEALED attribute of the ***num***th node to "true" or "false". |
| **group(num1,num2,label_str)** | Reduce the range of rule elements **(num1,num2)** and name the group node** label**. Unlike other reduce actions, this one can be repeated. ***WARNING:*** The rule element numbers change after each group action, so subsequent post actions must account for the new numbering of the rule elements. Reimplemented as an NLP++ function so that args can be NLP++ expressions. |
| **noop(0)** | Perform no post action. This is a convenience to disable the default **single()** reduce action. |

#### **B. PRINT ACTIONS**

Code actions and Post actions have distinct sets of printing actions, though we've made them as similar as possible.

| **print(str)** | Print the literal string **str** to standard output. |
| --- | --- |
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

#### C. VARIABLE ACTIONS

| **addstrs(var,num)** | Add a string to the multi-string **global** variable **var**. Fetch the string from the nodes matching rule element **num**. **var** should have been declared using the code action **varstrs()**. (No NLP++ equivalent yet.) |
| --- | --- |

A batch of post actions for the RFA (Rules-File Analyzer) are not described, as they are not relevant to the VisualText™ user. Their names all begin with the prefix **RFA**.
