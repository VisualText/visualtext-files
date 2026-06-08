# Statements and Blocks

## Expression Statement

NLP++ expressions can be treated as statements by terminating them with a semicolon.

## Statements and Blocks

This too is modeled after the C programming language. Curly braces **{** and **}** delimit blocks of statements. Statements should end with a semicolon (**;**). A statement can be an arbitrary expression, a block, or fully nested **if-else** statements.

## Assignment Statement

Assignment is treated as an expression rather than as a statement. As in C/C++, assignments can be chained.

## If-Else Statement

NLP++ supports if-else statement syntax identical to C/C++.

## While Statement

The only loop construct currently supported is the **while** loop. Here's an example that prints out 0 thru 9:

```
G("counter") = 0;

G("loop_limit") = 10;

while( G("counter") < G("loop_limit")) {

"output.txt" << "Loop counter = " << G("counter") << "\n";

G("counter")++;

}
```

## See Also

[Code Syntax](Code_Syntax.md)

[Tokens](Tokens.md)

[Variables](About_NLP++_Variables.md)

[Data Types](Variable_types.md)

[Special Variables](Special_Variables.md)

[Functions and Actions](Functions_and_Actions.md)

[Operators and Expressions](Operators_and_Expressions.md)
