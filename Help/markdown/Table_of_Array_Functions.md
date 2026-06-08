# Table of Array Functions

Arrays and lists are treated equivalently in NLP++, and we'll continue to call them both "arrays" for conciseness.

The current section is meant to round out the treatment of list-like capabilities such as pushing a value to the front.  Up to now, arrays were grown mainly by indexing to the last element.

Arrays can also be assigned and manipulated with parse tree functions and kb functions.

| **FUNCTION NAME** | **RETURNS** | **DESCRIPTION** |
| --- | --- | --- |
| [**push(var)**](push.md) | ARRAY | Push a value to the front of a variable's value(s). Allows mixed types (string, num, flt, concept...), allows redundant values, does not check uniqueness. NOTE: This will alter the array indexing, pushed item will be the 0th element of array index. **UNIMPLEMENTED** |
|   |   |   |

## See Also
