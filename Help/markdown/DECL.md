[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# DECL Region

The DECL Region is where you define your own functions in NLP++.  It is delimited by @DECL and optionally by @@DECL.  When present, it must be the first region in a pass file.

With VisualText 1.2 and later, functions can take parameters with the **L** local variable, as well as return values and call themselves recursively.  In addition, you may use the special NLP++ variable references to pass information to and from functions.  Depending on where a function is called from, it can appropriately handle the **S**, **N**, and **X** variable references in addition to the global, or **G**, variable reference.  The return type of functions can vary dynamically -- in fact, the same function could return different types at different times.  Multi-valued variables (i.e., arrays) can be used to have a function return multiple values.

Recursive functions work as expected.  Also, you may call a function in an earlier pass than the pass in which it is defined (i.e., forward reference is ok).  NLP++ functions have syntax similar to C/C++ functions.

<function definition> ::= <id> \( <local vars>  \)   \{ <statements> \} <local vars> ::= <local vars> \, <local var>  | <local var>  |  (empty) <local var> ::= 'L' \( <string> \) <statement> ::= <return statement> <return statement> ::= 'return' <expr> \;   |   'return' \;

An example follows.

**@DECL** myfunction(**L**("var"))    # Define your function. { "output.txt" << "Entering myfunction." << "\n";** G**("tmp") = **L**("var");   # Assign value to global variable.** L**("tmp") = **L**("var");   # Assign value to local variable. return **L**("tmp") * 2;   # Return a value. }

@CODE

"output.txt" << myfunction(3) << "\n";   # Call your function.** @@CODE**

This function call returns and outputs the number "6" to the file "output.txt".

## See Also

[Declare Zone](Declare.md)
