[← Help Contents](../index.md) | [📘 NLP++ Textbook](../NLP++_Textbook.md)

# Data Types

NLP++ data types are shown in the following table.

Numeric overflow and underflow are not flagged.  For example, the maximum **int** is 2147483647 in Windows and must be checked by the programmer as needed.  For large numbers, the **float** type should be used.

| **NAME** | **ABBREVIATION** | **CHARACTERISTICS** |
| --- | --- | --- |
| string | **STR** | Sequence of characters: e.g., **G("name") = "w3c";** |
| integer | **INT** | 32-bit integers: e.g., **G("num") = 32776;** |
| float | FLOAT | 32-bit floating point numbers: e.g., **G("flt") = 123.456;** |
| boolean | **BOOL** | 1 or 0. (Boolean implemented as a numeric nonzero for true and the numeric 0 for false.) |
| ostream | **OSTREAM** | Output stream. **G(*****filename) << expr;*** prints by referring to the ostream value of ***G(filename)***. See the **openfile** NLP++ function. |
| concept | **CON** | Concepts are the main object in the knowledge base. They have string names, and optionally have one or more attributes. e.g. **G("myConcept") = makeconcept(G("root"),"My Name");** |
| attribute | **ATTR** | Attributes are associated with concepts and KB nodes. They have string names, and optionally have one or more values. e.g. **G("myAttribute") = addattr(G("myConcept"),"is");** |
| value | **VAL** | Values are the values of KB attributes. They can be strings, numerics, or concepts: e.g. **addconval(G("myConcept"), "is", "John Smith");** |
| phrase | **PHR** | A phrase is a sequence of nodes owned by a single concept. E.g., create the first node of a phrase: **G("USPhrase") = makephrase(G("US"),"United"); **Add the last node of the phrase:** addcnode(G("US"), "States");** |
| node | **NODE** | Node in the KB. Differs from a concept in that it is not in the KB hierarchy, but rather in a concept's phrase. A node serves as a "proxy" or "instance" of a concept. |
| array | **ARRAY** | The values of an array, or multi-valued variable, can be any simple values. Note that nested ARRAY types are not currently supported. |
| pnode | **PNODE** | Parse tree node. Unrelated to a KB node. |

## Parse Tree Nodes

NLP++ can also reference the nodes of a parse tree directly. For example, **N(2)** refers to the (first) node that matched the 2nd element of a rule's right-hand-side phrase. **X(3)** refers to the 3rd node in the current context path as specified by @PATH. These constructs are used in functions that deal with the parse tree.  For more information on parse tree functions, see [Parse Tree Functions](../Table_of_Parse_Tree_Functions.md).

| **Note**: Knowledge base nodes are unrelated to parse tree nodes. The former are called NODE and the latter PNODE. |
| --- |

See [Special Node References](About_NLP++_Variables.md#Special_Node_References) for more on referencing parse tree nodes.

## Arrays

Arrays can consist of combinations of simple types. Nested array types are not implemented. An example follows.

```
# Create an array and step through it.

G("counter") = 0;

G("array_size") = 10;

# Arrays can optionally be "declared" by padding them with 0.

G("int_array")[G("array_size") - 1] = 0;



while ( G("counter") < G("array_size") ) {

G("int_array")[G("counter")] = G("counter");

"output.txt" << G("int_array")[G("counter")] << "\n";

G("counter") ++;

}

# print it out all at once

"output.txt" << G("int_array") << "\n";.

# copy it all at once:

G("another_array") = G("int_array");
```

## See Also

[Code Syntax](Code_Syntax.md)

[Tokens](Tokens.md)

[Variables](About_NLP++_Variables.md)

[Special Variables](Special_Variables.md)

[Functions and Actions](Functions_and_Actions.md)

[Operators and Expressions](Operators_and_Expressions.md)

[Statements and Blocks](Statements_and_blocks.md)
