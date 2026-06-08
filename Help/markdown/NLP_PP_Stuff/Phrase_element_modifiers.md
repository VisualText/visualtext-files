# Phrase Element Modifiers

Element modifiers that can be used in a rule's phrase are listed in the table below. The element modifier must be enclosed in square brackets** [ ] **and placed **after** the element. Some element modifiers have synonyms.  The modifier trigger, for example can be written as **[trigger]**, **[trig]**, or **[t]**.

| **KEY** | **VALUE TYPE** | **DESCRIPTION** |
| --- | --- | --- |
| deaccent, deacc, da | NONE | Match alphabetic, ignoring presence or absence of accent marks on characters. **NEW IN VERSION 2**. |
| **trigger,trig,**** t** | NONE | Match the current element first. E.g., _*np <- _det _quan _adj _noun ****[t]**** @@* |
| **min** | NUM | Specify the minimum number of nodes to match. 0 means the current element is optional. E.g., *_boys <- the [****min=0**** max=1] boys @@* |
| **max** | NUM | Specify the maximum number of nodes to match. 0 means the current element can match an indefinite number of nodes. E.g., *_htmltag <- \< _xWILD [min=1 ****max=100****] \> @@* |
| **opt,option,optional,**** o** | NONE | Match a minimum of 0 and a maximum of 1 node. (Short for min=0 max=1). E.g., *_vgroup <- _modal [****opt****] _have [****opt****] _be [****opt****] _verb @@* |
| **one** | NONE | Match exactly one node. (Short for min=1 max=1). |
| **star** | NONE | Indefinite repetition. Match a minimum of 0 up to any number of nodes. (Short for min=0 max=0). |
| **plus** | NONE | Indefinite repetition. Match a minimum of 1 up to any number of nodes. (Short for min=1 max=0). |
| **group, gp** | NAME | Gather nodes that matched the current element under a single node with NAME as its name. Analogous to POST Action **group**. |
| **rename,ren** | NAME | Rename every node that matched the current element to NAME. E.g., *_locfield <- location \: _xWILD [****ren=_location****] \n @@* |
| **singlet,**** s** | NONE | Search a node's descendants for a match. Stop looking down when a node has more than one child or has the BASE attribute set. E.g., *_abbr <- _unk \. ****[s]**** @@ *See BASE. |
| **tree** | NONE | Search node's entire subtree for a match. (Overuse of this may degrade analyzer performance.) |
| **matches,**** match** | LIST | For _xWILD element only. Match if element is in a match list. Used as a restricted wildcard and succeeds only if one of the list names matches a node. E.g., *_james <- _xWILD [****match=(jim jimmy james)**** singlet min=1 max=1] @@* |
| **fails,**** fail** | LIST | For *ANY* element. Fail to match if node matches anything on the list. E.g., *_par <- _xWILD [****fail=(_endofpar _par)**** min=1 max=0] @@* |
| **excepts, except** | LIST | For _xWILD only. Matching an item on the except list negates the effect of a match on the *match* or fail *list*. Must be accompanied by a single *match* or *fail* list. |
| **lookahead, look** | NONE | Designate the first lookahead element of a rule. The first node matching the lookahead element or to the right of it will be the locus where the rule matcher *continues* matching. WARNING: A reduce action such as *singler* or *noop* should be used to ensure that the lookahead node and nodes to its right are not included in the current rule reduction. |
| **layers, layer,**** attrs, attr** | LIST | Layer additional attributes for the element in the parse tree, as "mini-reductions". Use the names in the list to name nodes. Note: each node that matched current rule element will be layered. (These modifiers can also be used as suggested element modifiers.) |
| **recurse, nest,**** passes, pass** | LIST | Invoke a recursive rules pass on nodes that matched the current rule element. E.g., *_tag <- \< _xWILD [****nest=(tagrules)****] \> @@. *(See RECURSE Region.) |

| **WARNING**: Don't write rules with _xANY [max=0]. They won't work, because _xANY is not implemented as a wildcard. The nearly equivalent _xANY _xWILD works. More generally, matching with MIN and MAX is *greedy*, and no *backup* is implemented. So the rule _a <- _b [min=1 max=3] _c [s] @@ fails on the phrase **_b _b(subnode _c**), because the repeating _b element greedily gobbles up the second _b node. The rule matcher will not back up to find that the rule can be made to work. Unrestricted _xWILD is the **only** rule element that is "backup-aware". |
| --- |

## See Also

[Special Rule Elements](Special_rule_elements.md)

[Suggested Element Modifiers](Suggested_element_modifiers.md)

[Rule Syntax](Rule_syntax.md)
