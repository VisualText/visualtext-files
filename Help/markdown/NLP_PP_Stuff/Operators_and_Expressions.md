[← Help Contents](../index.md) | [📘 NLP++ Textbook](../NLP++_Textbook.md)

# Operators and Expressions

## Operators

Most NLP++ operators are modeled on the C programming language. The main addition is the ***confidence operator, %%***. This enables convenient accumulation of evidence in terms of percent confidence. Following is an operator precedence table, with highest precedence at the top.

| **OPERATOR** | **DESCRIPTION** | **ASSOCIATIVITY** |
| --- | --- | --- |
| **++ --** | Post increment, decrement | Left to right |
| **++ --** | Pre increment, decrement | Right to left |
| **!** | Logical NOT (unary) | Right to left |
| **+ -** | Unary plus, minus | Right to left |
| **% * / %%** | Remainder, multiplication, division, confidence | Left to right |
| **+ -** | Addition, subtraction | Left to right |
| ** ****< > <= == != >=** | Relational operators | Left to right |
| **&& \|\|** | Logical AND, OR | Left to right |
| **=** | Assignment | Right to left (multiple assignment works) |
| ***= /= += -= %%=** | Shorthand assignment (unimplemented) | Right to left |
| **<<** | Output operator | Left to right |

## Output Operator

The << output operator is modeled on the C++ operator. One form is:

**filename << expression << expression .... ;

Example:

```
"output.txt" << "Hello, NLP++!" << "\n";
```

NOTES: The file named by filename should have been created by a call to openfile(filename...) or a prior fileout(filename) code action. If that hasn't been done, then the output operator will create the global variable G(filename) with the output stream as its value. The default output mode for the file is append, which can't be modified by the user at present. Also, the default output directory is the log directory for the current input file -- also not under user control at present.

## Confidence Operator

Say that you have 80% confidence that you've found a name. You could write this into a global variable as

```
G("name confidence") = 80;
```

Now you want to account for a new piece of evidence. Say the standalone confidence of that evidence is 70%. You could combine this as

```
G("name confidence") = G("name confidence") %% 70;
```

which will yield a new percent confidence between 80% and 100%.

The %% operator guarantees that "adding" or "subtracting" confidence will always stay within the range of 0 to +100, providing an intuitive way to gather evidence and compare confidences using a single scale of measurement.

## String Catenation Operator

The plus '+' operator, when given string args, serves as a built-in string catenation operator.

## Expressions

NLP++ expressions are modeled on the C/C++ programming languages and can be nested arbitrarily and grouped using parentheses ( ).

Assignment expressions can be nested, just as in C/C++. For example

G("a") = G("b") = 0;

sets the global variables named "a" and "b" to 0.

## See Also

[Code Syntax](Code_Syntax.md)

[Tokens](Tokens.md)

[Variables](About_NLP++_Variables.md)

[Data Types](Variable_types.md)

[Special Variables](Special_Variables.md)

[Functions and Actions](Functions_and_Actions.md)

[Statements and Blocks](Statements_and_blocks.md)
