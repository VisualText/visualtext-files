# Rule Element Modifiers

Each rule element can be followed by **optional** **element modifiers**.  Element modifiers can be used for **both** the **suggested element** (_SUGG) and the **phrase of elements** (_PHRASE) on the right-hand side of a rule.

Element modifiers place constraints on how elements in a rule are matched. For example, if you want to specify that the rule matcher should match a specific element in the phrase of elements on a rule's right-hand side first, you would use the **trigger** element modifier with the rule element.

The modifier must be enclosed in square brackets **[ ]** **after** the element. The element modifier is made up of a **key** (the modifier name itself) and sometimes a **value**. A value can be a parenthesized list, a name or number. Some element modifiers do not have values. Some examples follow:

_xWILD [s one match=(_adj _noun \n)]

hello [rename=_hello]

For a list of element modifiers used with the suggest rule element, see [Suggested Element Modifiers](Suggested_element_modifiers.md). For a list of element modifiers for the phrase of elements, see [Phrase Element Modifiers](Phrase_element_modifiers.md).

| **WARNING**: When writing lists for an element modifier, we recommend not enclosing them in double quotes, since they are not treated as strings. E.g., write **[match=(_adj _adv)] **rather than **[match=("_adj" "_adv")]**. |
| --- |

## See Also

[Rule Syntax](Rule_syntax.md)
