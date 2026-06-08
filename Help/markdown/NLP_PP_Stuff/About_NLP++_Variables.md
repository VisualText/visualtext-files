[← Help Contents](../index.md) | [📘 NLP++ Textbook](../NLP++_Textbook.md)

# Variables

There are two broad classes of variables in NLP++:

- **general variables**

- **parse tree node variables**

**Global variables **and** local variables** are the only general class implemented to date. Globals are referenced by the special **G** function.  Local variables are denoted by **L**, and currently specify parameter lists and appear within user-defined NLP++ function definitions in the @DECL region.

**Parse tree node variables**, or **node variables** for short, are attached to particular nodes in the parse tree, and serve to decorate the tree with semantic information. The special functions **N**, **X**, and **S** refer to parse tree nodes in the context of a matched rule.

The special NLP++ functions that reference variables are tabulated below:

| **VARIABLE** | **DESCRIPTION** |
| --- | --- |
| **G(varname)** | Global variable. |
| **S(varname)** | Variable belonging to the **suggested** concept of a rule. |
| **X(varname [,num])** | Variable belonging to the ***num***th **context** node starting at the root of the parse tree. Usually used to refer to the ***num***th node of the @PATH select list. With @NODES, the preferred form is X(varname). |
| N(varname [,num]) | Variable belonging to a **node** that matched the ***num***th element of a rule phrase. |
| **L****(varname])** | Local variable, specifies user-defined NLP++ function parameters and appears in function body. |
|   |   |

The shorthand notations **N(varname)** and **X(varname)** refer to the last element of the phrase and the last context node, respectively. The former is convenient for rules that have only one element in their phrase. The latter is convenient when using the @NODES selector. **N(varname, 0)** and** X(varname, 0)** have the identical meaning.

There is no notion of a local variable or pointer, at this time. **S** variables are often used as an idiom for local variables (the difference is that they "hang around" if a new node is suggested by the current rule).

| **Note**: Variable names must be quoted. E.g., N("unknown word", 2) |
| --- |

**WARNING:** **X(varname,num)** does **NOT** refer to the **num**th member of a @NODES list. That list is not a path in the parse tree. We recommend using **X(varname)** with @NODES, to avoid "blindly" traversing down the parse tree. Using X(varname,2), for example, implies that you know what the nodes immediately below the root are. Such a use should be clearly documented.

## Special Variable Names

To get useful information from the parse tree and other sources when analyzing a text, some special variable names have been provided. All start with a dollar sign (**$**). No such variable names are usable with suggested (**S**) variables, at present.

Note the following about using special variables:

1. Special variable names must be quoted. E.g., N("$text", 2).

1. You should not assign to or create your own "dollar" variables. NLP++ reserves all variable names that start with a dollar sign.

1. The $uppercase, $lowercase, $cap, and $unknown differ from the analogous PRE Actions in that they all traverse down to the "leafiest" node they can find, in order to perform their check. The corresponding PRE Actions only chain down if the [s] flag is present in the associated phrase element(s). Also, the $ variables are not stopped by a [base] attribute in a node.

See[Special NLP++ Variables](Special_Variables.md) for a listing of the special variables.

## Special Node References

**N**, **X**, and **S** can, in addition to referring to a node's variables, refer to the node itself. Thus **N**(2) refers to the first node that matched element 2 of the matched rule. **N**() and **N**(0) refer to the last rule element's (first or only) node. Similarly, **X**(2) refers to the second context node in the @PATH dominating the current rule. **S**() refers to the suggested concept.

## Variable Types

NLP++ is a *loosely typed* language.  The same variable can be assigned an integer in one statement and a string in the next.  Type is determined by usage -- there are no type declarations for variables.

**G**("tmp") = 123;

**G**("tmp") = "abc";

Variables can take multiple values, in which case they are called **arrays**.  Each value in an array can be of an arbitrary data type:

**G**("tmp")[0] = 123;

**G**("tmp")[1] = "abc";

See the [Data Types](Variable_types.md) topic for more details about arrays and other data types.

## See Also

[Code Syntax](Code_Syntax.md)

[Tokens](Tokens.md)

[Data Types](Variable_types.md)

[Special Variables](Special_Variables.md)

[Functions and Actions](Functions_and_Actions.md)

[Operators and Expressions](Operators_and_Expressions.md)

[Statements and Blocks](Statements_and_blocks.md)
