[← Help Contents](../index.md) | [📘 NLP++ Textbook](../NLP++_Textbook.md)

# Tokens

Following are some token types that occur in NLP++ code.

| **ITEM** | **DESCRIPTION** |
| --- | --- |
| **#** | Comment. Text till the end of the line is ignored. |
| **AAA or NNN** | Literal tokens. Completely alphabetic or completely numeric. |
| **_AAA** | Nonliteral tokens must begin with underscore. All the remaining letters MUST be alphabetic. Currently, only alphabetics are allowed after the initial underscore. |
| **"XXX"** | Strings get double quoted. Everything within string taken literally (except backslashed characters). |
| **\X** | Backslash any nonalphanumeric char you want taken literally. If X = one of a b n r f t v, these are special escapes analogous to C/C++. |
| **\\** | Literal backslash character. |

## See Also

[Code Syntax](Code_Syntax.md)

[Variables](About_NLP++_Variables.md)

[Data Types](Variable_types.md)

[Special Variables](Special_Variables.md)

[Functions and Actions](Functions_and_Actions.md)

[Operators and Expressions](Operators_and_Expressions.md)

[Statements and Blocks](Statements_and_blocks.md)
