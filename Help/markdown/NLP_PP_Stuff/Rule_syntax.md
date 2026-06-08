# Rule Syntax

All rules are written in the RULES Region of a pass file. Within each RULES Region, any number of rules can occur.

The syntax for a rule is

**_SUGG <- _PHRASE @@**

## Rule Elements

**_SUGG**, is referred to as the **suggested**** rule element**. It is the node that is created if a rule matches. _SUGG is often referred to as the left-hand side of the rule.

**_PHRASE** is the **phrase of elements** that the rule matcher is trying to match. If the rule matcher finds a match for the listed phrase, the node will **suggest** or **reduce** to what is specified in _SUGG. _PHRASE is referred to as the right-hand side of the rule.

| **Note**: Rule elements that make up the phrase of elements do not have to be written on the same line. That is, the rule can extend over several lines with each rule element in _PHRASE occupying its own line. The two rules below are equivalent: _XYZ <- _ABC _DEF @@ _XYZ <- _ABC _DEF @@ When each rule element in the phrase is written on its own line, the rule is said to be written in **standard rule format**. For more information on rule formats, see Standard Rule Format. |
| --- |

**<- **is the rule arrow. It divides the rule between the suggested element and the phrase of rule elements.

**@@** indicates the end of a rule. Rules must always end in the @@ marker.

## Rule Element Types

Each rule element, including the suggested element, consists of a **literal** or a **nonliteral**. What gets matched for each is different:

- **Literals** match tokens, or "real text".

- **Nonliterals** match nodes which begin with an underscore.

A literal is a **terminal node** (or leaf node) in the parse tree. It represents words, numbers and punctuation.

A nonliteral is a **nonterminal node** (also called an internal node). It represents a node which dominates other nodes.

The initial underscore character "_" is an NLP++ convention marking nonterminal or internal nodes. A terminal node cannot begin with an underscore character.

## Special Rule Elements

NLP++ has a set of predefined rule elements called **special rule elements**. These rule elements match various types of tokens such as alpha characters, punctuation, wildcards, etc.. They have properties that make writing rules easier. For a list of these predefined rule elements, see [Special Rule Elements](Special_rule_elements.md).

## Rule Element Modifiers

Each rule element can be followed by **optional** **element modifiers**.  This includes the **suggested element** and **phrase of elements** on a rules right-hand side.

Element modifiers place constraints on how elements in a rule are matched. For example, if you want to specify that the rule matcher should match a specific element in the phrase of elements on a rule's right-hand side first, you would use the **trigger** element modifier with the rule element. Element modifiers can be used for **both** the suggested element and the phrase of elements on the right-hand side of a rule.

The modifier must be enclosed in square brackets **[ ]** **after** the element. The element modifier is made up of a **key** (the modifier name itself) and sometimes a **value**. A value can be a parenthesized list, a name or number. Some element modifiers do not have values. Some examples follow:

_xWILD [s one match=(_adj _noun \n)]

hello [rename=_hello]

For a list of element modifiers used with the suggest rule element, see [Suggested Element Modifiers](Suggested_element_modifiers.md). For a list of element modifiers for the phrase of elements, see [Phrase Element Modifiers](Phrase_element_modifiers.md).

| **WARNING**: When writing lists for an element modifier, we recommend not enclosing them in double quotes, since they are not treated as strings. E.g., write **[match=(_adj _adv)] **rather than **[match=("_adj" "_adv")]**. |
| --- |
