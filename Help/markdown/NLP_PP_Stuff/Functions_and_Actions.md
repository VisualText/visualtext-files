[← Help Contents](../index.md) | [📘 NLP++ Textbook](../NLP++_Textbook.md)

# Functions and Actions

## Functions

NLP++ supports function calls, which have a similar form to other programming languages (such as C/C++):

**functionName(arg1, .... argN)**

where functionName is constrained to be alphabetic and where each argument to the function may be an NLP++ expression.

Only call-by-value arguments are supported at present.  That means that when a variable is used as an argument, its value is not changed by a change to the local variable that it becomes associated with in the function.

Functions have no template or declaration -- only a definition.  Even so, you may use a function in one pass and define it in a subsequent pass (forward reference).  The parameters to functions take arbitrary data types that may vary dynamically.  Return statements similarly return arbitrary data types.  The same function could return a numeric value in one call and a string in another.  We discourage the abuse of this extreme flexibility, however!  The new **L** variable reference has been introduced to support formal function parameters as well as local variables within a function body.  Recursive functions are also possible.  The example below illustrates the definition and use of user-defined functions in NLP++.

```
@DECL
```

xuf(**L**("var"))

{

"output.txt" << **L**("var") << "\n";

**L**("local") = 3;   `# create a local variable.`

"output.txt" << **L**("local") << "\n";

**return **1+2;

}

facto(**L**("num"))  `# recursive factorial function.`

{

**if **(**L**("num") <= 0)

**return **1;

**return ****L**("num") * facto(**L**("num") - 1);

}

```
@@DECL
```

```
@CODE
```

**G**("x")[2] = 3;

"output.txt" << **G**("x") << "\n";

xuf(**G**("x"));

"output.txt" << "4! = " << facto(4) << "\n";

```
@@CODE
```

The code above prints out

0 0 3

0 0 3

3

4! = 24

## Actions

Actions, e.g., **single**, are specialized functions that don't take generalized NLP++ expressions as arguments.  Though some actions have been upgraded and now take NLP++ arguments (e.g. **group**), some actions have not been upgraded and the argument must be a literal value.

A unique feature of actions in the PRE Region is that they have a mandatory range.  The syntax is as follows:

**<num,num> pre_action_name(args....)**

The action applies to each rule element in the <num, num> range individually.

See [Actions](Actions.md) as a starting point for per-page descriptions for actions.

## Case Sensitivity

NLP++ function and action names are case-sensitive.

## Defining New Functions

In VisualText 1.2 and later, user-defined NLP++ functions are fully supported, including parameter lists, return statements, recursive calls, and compilation of these.  Functions are specified in the @DECL region, which must appear first within a pass file, if present.

New NLP++ functions can also be defined with C++ code, within an application's **user** project. User-defined function calls must be preceded by the '*user*' scope qualifier, e.g., *user::myfunction*. (Interpreted NLP++ will find the correct function and issue a warning, but user functions without the scope qualifier will be compiled incorrectly.)

## See Also

[Actions](Actions.md)

[Functions](Functions.md)
