[← Help Contents](../index.md) | [📘 NLP++ Textbook](../NLP++_Textbook.md)

# NLP++

[Note: This topic is slated for removal. Refer also to the NLP++ section.]

NLP++**ï¿½** is a novel programming language developed by Text Analysis International, Inc. It enables a developer to focus on the conceptual task of building a text analyzer while minimizing the need to delve into compiled programming languages. NLP++ combines a C++ -like syntax (called the *code* part) with a rule syntax (described in the [Pass Files](../NLP_PP_Stuff/Pass_Files.md) topic). The current topic is concerned primarily with the code part.

One use of NLP++ is dynamic semantics, that is, to create and use information "on the fly". Another is to embed heuristics and algorithms into the text analyzer under construction.

## Regions

The NLP++ language can currently appear in the @CHECK, @CODE and @POST regions of a pass file. In a @CHECK region, the functions **succeed** and **fail** can be used to accept or reject a rule match, respectively.

The @PRE region, which operates during the pattern matching of a rule, does not yet allow NLP++ constructs.

**WARNINGS:** [1] The developer must keep in mind that actions that modify the parse tree, such as single(), will disable references to the nodes of a phrase and otherwise affect the execution of NLP++ code. It is recommended that tree-modifying actions follow references to node variables. [2] If the developer must reference a newly created node, e.g., by the **group** action, he must manually figure out the new element number of the created node. Note that following an action such as **group**, element numbers to the right of the grouped node will also change.

## Tokens

See the Pass File section on [Tokens](../NLP_PP_Stuff/Pass_Files.md#pass_file_tokens).

## Variables

NLP++ currently supports global variables and variables associated with particular nodes of the parse tree. The syntax for these variables is as follows:

| **VARIABLE** | **DESCRIPTION** |
| --- | --- |
| **G(varname)** | Global variable. |
| **S(varname)** | Variable belonging to the suggested concept of a rule. |
| **X(varname [,num])** | Variable belonging to the ***num***th context node starting at the root of the parse tree. Usually used to refer to the ***num***th node of the @PATH select list. With @NODES, the preferred form is X(varname). |
| **N(varname [,num])** | Variable belonging to a node that matched the ***num***th element of a rule phrase. |

The shorthand notations **N(varname)** and **X(varname)** refer to the last element of the phrase and the last context node, respectively. The former is convenient for rules that have only one element in their phrase. The latter is convenient when using the @NODES selector. **N(varname, 0)** and** X(varname, 0)** have the identical meaning.

There is no notion of a local variable or pointer, at this time. **S** variables are often used as an idiom for local variables (the difference is that they "hang around" if a new node is suggested by the current rule).

**NOTE****:** Variable names must be quoted. E.g., N("unknown word", 2)

**WARNING:** **X(varname,num)** does **NOT** refer to the **num**th member of a @NODES list. That list is not a path in the parse tree. We recommend using **X(varname)** with @NODES, to avoid "blindly" traversing down the parse tree. Using X(varname,2), for example, implies that you know what the nodes immediately below the root are. Such a use should be clearly documented.

## Special Variable Names

To get useful information from the parse tree and other sources when analyzing a text, some special variable names have been provided. All start with a dollar sign (**$**). No such variable names are usable with suggested (**S**) variables, at present.

| **VARIABLE NAME** | **VARIABLE TYPES** | **DESCRIPTION** |
| --- | --- | --- |
| **$treetext** | **N, X** | Fetch the 'cleaned up' (removing leading and trailing, convert separators to single space) text gleaned from a node's subtree. Uses the parse tree as input, not text buffer. Analogous to $text. Difference between $treetext and $text is $text returns text from the input text buffer while $treetext returns text from the parse tree. So, if you have removed some nodes from a tree with an excise(), $treetext returns the text minus the excised elements, while $text returns everything in the input text buffer, including the text under excised nodes. |
| **$text** | **N, X** | Fetch the text covered by the node. Cleanup whitespace (removing leading and trailing, convert separators to single space). Uses the original text buffer, rather than the subtree under the node, in order to gather text. See also $treetext and $treeraw. |
| **$treeraw** | **N, X** | Fetch the text covered by the node from the parse tree. Text is not 'cleaned up'. Analogous to $treetext. See also $treetext and $raw. |
| **$raw** | **N, X** | Fetch the 'cleaned up' text covered by the node from the text buffer. See also $treetext, $treeraw and $text. |
| **$xmltext** | **N, X** | Same as $raw***,*** but converts characters that are special to HTML and XML. E.g., "<" is converted to "&lt;". |
| **$length** | **N, X** | Get the length of node's text. |
| **$ostart** | **N, X** | Start offset of the referenced node in the input text. |
| **$oend** | **N, X** | End offset of the referenced node in the input text. |
| **$start** | **N, X** | Evaluates to **1 **if the referenced node has no left sibling in the parse tree, else **0**. |
| **$end** | **N, X** | Evaluates to **1 **if the referenced node has no right sibling in the parse tree, else **0**. |
| **$apppath** | **G** | Get base directory path for current application. E.g., "D:\dev\apps\Resume". |
| **$input** | **G** | Get full input file. E.g., "D:\apps\Resume\input\Dev1\rez.txt" |
| **$inputpath** | **G** | Get input file path. E.g., "D:\apps\Resume\input\Dev1" |
| **$inputname** | **G** | Get input filename. E.g., "rez.txt" |
| **$inputhead** | **G** | Get input file head. E.g., "rez" |
| **$inputtail** | **G** | Get input file tail (i.e., extension). E.g., "txt" |
| **$allcaps**** $uppercase** | **N** | Returns 1 if the token underlying the node is all uppercase. If multiple words (even if all are all-caps), returns 0. WARN: Not identical to the uppercase() pre action. |
| **$lowercase** | **N** | Returns 1 if the token underlying the node is all lowercase If multiple words (even if all are all-caps), returns 0. WARN: Not identical to the lowercase() pre action. |
| **$cap** | **N** | Returns 1 if the token underlying the node is a capitalized word. WARN: Not identical to the cap() pre action. |
| **$mixcap** | **N** | Returns 1 if the token underlying the node is a mixed-capitalized word. Examples: "MIchigan", "abcD". |
| **$exists** | **N** | Returns 1 if the node exists, 0 otherwise. |
| **$unknown** | **N** | Returns 1 if the token underlying the node is an unknown word. WARN: Not identical to the unknown() pre action. Requires a **lookup**() code action prior to any use of this special variable. |

**NOTE****:** [1] Special variable names must be quoted. E.g., N("$text", 2). [2] You should not assign to or create your own "dollar" variables. NLP++ reserves all variable names that start with a dollar sign. [3] The $uppercase, $lowercase, $cap, and $unknown differ from the analogous pre actions in that they all traverse down to the "leafiest" node they can find, in order to perform their check. The corresponding pre actions only chain down if the [s] flag is present in the associated phrase element(s). Also, the $ variables are not stopped by a [base] attribute in a node.

## Parse Tree Nodes

NLP++ can also reference the nodes of a parse tree directly. For example, **N(2)** refers to the (first) node that matched the 2nd element of a rule's right-hand-side phrase. **X(3)** refers to the 3rd node in the current context path as specified by @PATH. These constructs are used in functions that deal with the parse tree (see the Parse Tree Functions section below). (Note that knowledge base nodes are unrelated to parse tree nodes. The former are called NODE and the latter PNODE, as in the Types section below.)

## Types

The types of NLP++ variables available are shown in the following table.

| **NAME** | **ABBREVIATION** | **CHARACTERISTICS** |
| --- | --- | --- |
| **string** | **STR** | Alpha-numerics: e.g. **G("foobar") = "w3c";** |
| **integer** | **INT** | 32-bit integers: e.g. **G("foorbar") = 32776;** |
| **boolean** | **BOOL** | 1 or 0 (Boolean implemented as a numeric 1 for true and the numeric 0 for false.) |
| **ostream** | **OSTREAM** | C++ output stream.*** fileout(filename)*** creates a variable with ostream value and ***filename << expr;*** prints by referring to the ostream value of ***G(filename)***. See also the **ofile** NLP++ function. |
| **concept** | **CON** | Concepts are the main object in the kb and appear in the kb hierarchy. They have string names, and optionally have one or more attributes. e.g. **G("myConcept") = makeconcept(G("root"),"My Name");** |
| **attribute** | **ATTR** | Attributes are associated with concepts and kb nodes. They have string names, and optionally have one or more values. e.g. **G("myAttribute") = addattr(G("myConcept"),"is");** |
| **value** | **VAL** | Values are the values of kb attributes. They can be strings, integers or concepts: e.g. **addconval(G("myConcept"), "is", "John Smith");** |
| **phrase** | **PHR** | A phrase is a sequence of nodes owned by a single concept. E.g., create the first node of a phrase: **G("USPhrase") = makephrase(G("US"),"United"); **Add the last node of the phrase:** addcnode(G("US"), "States");** |
| **node** | **NODE** | Node in the KB. Differs from a concept in that it is not in the KB hierarchy, but rather in a concept's phrase. A node can serve as a "proxy" for a concept. |
| **array** | **ARRAY** | The values of an array, or multi-valued variable, can be any single value (i.e., any type other than a nested ARRAY). |
| **pnode** | **PNODE** | Node in the parse tree. Unrelated to a KB node. |

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

**The << output operator is modeled on the C++ operator. Only the following form is supported, currently:**

**filename << expression << expression .... ;

Example:

```
"output.txt" << "Hello, NLP++!" << "\n";
```

NOTES: The file named by filename should have been created by a prior fileout(filename) code action. If that hasn't been done, then the output operator will create the global variable G(filename) with the output stream as its value. The default output mode for the file is append, which can't be modified by the user at present. Also, the default output directory is the log directory for the current input file -- also not under user control at present.

## Confidence Operator

Say that something in the parse tree gives you 80% confidence that you've found a name. You could write this into a global variable as

```
G("name confidence") = 80;
```

Now you want to account for a new piece of evidence. Say the standalone confidence of that evidence is 70%. You could combine this as

```
G("name confidence") = G("name confidence") %% 70;
```

which will yield a new percent confidence between 80% and 100%.

The %% operator guarantees that "adding" or "subtracting" confidence will always stay within the range of -100 to +100, providing an intuitive way to gather evidence and compare confidences using a single scale of measurement. (Actually, %% bottoms out at 0%. A planned change to the operator will enable it to bottom out at -100%, which can be thought of as 100% confidence against something.)

## Expressions

NLP++ expressions are modeled on the C/C++ programming languages and can be nested arbitrarily and grouped using parentheses ( ).

One useful enhancement: addition with string arguments or string variables equates to string catenation.

## Functions and Actions

NLP++ supports function calls. Actions, e.g., single, are specialized functions that don't take generalized NLP++ expressions as arguments (see [Pass Files](../NLP_PP_Stuff/Pass_Files.md) in the Developers section). Currently, new NLP++ functions must be defined with C++ code, within an application's user project. User-defined functions must be preceded by the '*user*' scope qualifier, e.g., *user::myfunction*. (Interpreted NLP++ will find the correct function and issue a warning, but user functions without the scope qualifier will be compiled incorrectly.)

## Statements and Blocks

This too is modeled after the C programming language. Curly braces { and } delimit blocks of statements. Statements should end with a semicolon (;). A statement can be an arbitrary expression, a block, or fully nested if-else statements.

## While Loop

The only loop construct current supported is the while loop. Here's an example that prints out 0 thru 9:

```
G("counter") = 0;

G("loop_limit") = 10;

while( G("counter") < G("loop_limit")) {

"output.txt" << "Loop counter = " << G("counter") << "\n";

G("counter")++;

}
```

## Parse Tree Functions

| FUNCTION NAME | RETURNS | DESCRIPTION |
| --- | --- | --- |
| arraylength(VAR) | INT | Return number of values in given variable or expr. (Like a call-by-reference) |
| lasteltnode(elt_num) | PNODE | Get the last node that matched the elt_numth element of a rule. |
| phrasetext() | STR | Get the text that matched the right hand side phrase of a rule. Analogous to $text. |
| phraseraw() | STR | Get the raw text that matched the right hand side phrase of a rule. Analogous to $raw |
| pndeletechilds(pnode) | None | Delete children of given pnode. |
| pnname(pnode) | STR | Return pnode's name. |
| pnnext(pnode) | PNODE | Return pnode's right sibling, if any. |
| pnprev(pnode) | PNODE | Return pnode's left sibling, if any. |
| pnrename(pnode, str) | STR | Rename given pnode. Returns the interned name. |
| pnroot() | PNODE | Return root of parse tree |
| pnsingletdown(pnode) | PNODE | Return pnode's child, obeying rules about going down a "singlet chain." I.e., get child only if no branching and if not going past node with BASE flag set. |
| pnup(pnode) | PNODE | Return pnode's parent, if any. Only leftmost pnode in a list has a parent. |
| pnvar(pnode, var_str) | (var values) | Get pnode's variable value(s). |
| varinlist(var_str, elt_num) | (var values) | Get var_str variable's value(s) in any pnode that matched elt_numth element |

## String Functions

| FUNCTION NAME | RETURNS | DESCRIPTION |   |
| --- | --- | --- | --- |
| strchar(str, num) | STR | Index to numth char of string |   |
| strchr(str, ch_str) | STR | Find first occurrence of char in string. Return string headed by char. |   |
| strclean(str) | STR | Remove leading, trailing, and repeat whitespace separators. |   |
| strcontains(str1,str2) | BOOL | Is str1 contained in str2. |   |
| strcontainsnocase(str1,str2) | BOOL | Is str1 contained in str2, ignoring letter case. |   |
| strendswith(str, suffix_str) | strstartswith(str, suffix_str) | BOOL | Does given str end with given suffix_str |
| strequal(str1,str2) | BOOL | Is str1 identical to str2. |   |
| strisalpha(str) | BOOL | Is str all alphabetic chars. |   |
| strisdigit(str) | BOOL | Is str all numeric chars. |   |
| strnotequal(str1,str2) | BOOL | Does str1 differ from str2. |   |
| strequalnocase(str1,str2) | BOOL | Is str1 identical to str2, ignoring letter case. |   |
| strnotequalnocase(str1,str2) | BOOL | Does str1 differ from str2, ignoring letter case. |   |
| strlessthan(str1,str2) | BOOL | Is str1 lexically before str2. |   |
| strgreaterthan(str1,str2) | BOOL | Is str1 lexically after str2. |   |
| strlength(str) | INT | Return length of string. |   |
| strpiece(str, start_num, end_num) | STR | Return substring from start_num to end_num indexes. Zero-based |   |
| strrchr(str, ch_str) | STR | Find last occurrence of char in string. Return string headed by char |   |
| strsubst(str, old_str, new_str) | STR | In str, substitute instances of old_str with new_str. |   |
| strtolower(str) | STR | Return lowercase form of string. |   |
| strtotitle(str) | STR | Capitalize string as in a title or header. |   |
| strtoupper(str) | STR | Return uppercase form of string |   |
| strtrim(str) | STR | Remove leading and trailing whitespace from str. |   |
| unpackdirs(dir_str) | STR ARRAY | Unpack directory names from a full directory path string. |   |
| strwrap(str, num) | STR | Fold string successively at every numth character. |   |
| num(str) | NUM | Convert string to number, if possible. (Also accepts num arg). |   |
| str(num) | STR | Convert numeric value to string. (Also accepts string arg). |   |

## Miscellaneous Functions

| FUNCTION NAME | RETURNS | DESCRIPTION |
| --- | --- | --- |
| fail() | None | In @CHECK region, abort the rule that has just matched. Noop elsewhere. |
| succeed() | None | In @CHECK and @CODE region, succeed without performing further code actions in that region. |
| batchstart() | BOOL | True if current file is first in a batch run. |
| debug() | BOOL | No op. Convenient breakpoint for debugging from C++ compiler. |
| hitconf(hits_num, total_num, fudge_num) | 0 to 100 | Percent confidence for hits. Fudge factor is typically 3 to 20. |
| LJ(num, fieldsize_num) | STR | Left-justify num in given field size. |
| ofile(path_str [, mode_str [, mode_str [, mode_str]]] ) | OSTREAM | Open an output file for the given path; analogous to C++ open file function. Zero to three mode strings selected from: 1) "app" = append; 2) "ate" = special C++ append; 3) "binary" = open in binary mode (text is default). WARNINGS: Default mode is OVERWRITE, not APPEND. Unlike fileout(), does not create a global variable for the file stream. [Upgraded doc to conform to standard C++ i/o libraries.] |
| percentstr(numerator_num, denominator_num) | STR (" 0" to "100") | Format a percentage (right-justified in field of 3 chars). |
| rightjustifynum(num, fieldsize_num) | STR | Format a percentage (right-justified in field of 3 chars). |
| spellcandidates(word_str) | STR | Return list of space separated candidates for spell-correcting given word. |
| spellcorrect(word_str) | STR | If known word, return as-is. If not, return best spelling guess. |
| spellword(word_str) | BOOL | See if given word is a known English word. |
| strspellcandidate(word_str, list_str) | STR | Choose best spell-correct candidate for a word, given a list of space-separated candidates (as returned by spellcandidates, e.g.) |
| strspellcompare(str1, str2) | INT | Return spelling "distance" between two given words. The smaller the number, the fewer the corrections to get from one to the other. |
| system(str) | BOOL | Execute str as operating system command |

Note: It is necessary to escape the directory delimiter backslash ('\') with another ('\'). For example, suppose you wanted to echo characters to a file and then copy that file to some other directory. Here's some example code:

## System Function Example

```
@NODES _ROOT

@POST

# echo.txt is put in your default console location, which for

# me happens to be D:\WINNT\Profiles\Administrator\Desktop

system("echo this is a test > echo.txt");

# echo1.txt ends up in D:\WINNT\Profiles\Administrator\Desktop

system("copy echo.txt echo1.txt");

# echo2.txt ends up on D:

system("copy echo1.txt D:\\echo2.txt");

# echo3.txt ends up on D:\apps

system("copy D:\\echo2.txt D:\\apps\\echo3.txt");

"output.txt" << "copy.\n" ;

noop();

@@POST

@RULES

_xNIL <- _xALPHA @@
```
