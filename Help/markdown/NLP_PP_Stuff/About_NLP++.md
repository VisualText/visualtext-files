[← Help Contents](../index.md) | [📘 NLP++ Textbook](../NLP++_Textbook.md)

# About NLP++

NLP++™ is a general purpose programming language that integrates extensions for natural language processing (NLP). In addition to a C++ -like code syntax, NLP++ embodies a syntax for pass files, contexts, rules, and actions. Similar to LISP, NLP++ is a loosely-typed language.  In addition to integer, string, and array data types, NLP++ includes parse tree and knowledge base data types. In this way, the user can naturally address the rules, parse trees, and the knowledge base, while using C++ -like code to embed heuristics. Integration with the parse tree makes it possible to manipulate nodes and to manage semantic information within them. Integration with the knowledge base makes it possible to dynamically create and manage complex data structures. Integration with rules makes it possible to control every aspect of rule matching, to exploit context, and to elaborate the actions that follow rule matching.

NLP++ supports Concept Oriented Programming (COP), enabling you to focus on heuristics, the domain, and the task, rather than the underlying data structures. Because VisualText supports an interpreted environment, you can modify and test without having to wait for code to compile, which accelerates the development of text analyzers.

NLP++ is an evolving language but is already rich and robust.

## Text Analyzers and NLP++

As implemented in VisualText, a text analyzer consists of:

- the analyzer sequence, which specifies the order of passes, their types, and their associated pass files

- the pass files themselves

- the associated knowledge base

- miscellaneous code and data

NLP++ code and rules occur entirely within pass files. Everything contained within a pass file is considered to be part of the NLP++ language, including region markers (e.g., @RULES and @@RULES), specialized regions, code, actions, rules, and comments.

## NLP++ Syntax

NLP++ combines several types of syntax:

- Pass file markers such as @RULES

- Code syntax

- Rule syntax

One region of pass files, the PRE Region also has an element range construct, e.g., "<1, 3>" that is not found elsewhere. We strive to keep the syntax sets as integrated as possible. For example, double quoted "abc" is a string in every context, and C/C++ conventions for backslashed characters are used everywhere. # is used for comments throughout, and a token starting with an underscore (e.g., "_noun") denotes a nonliteral everywhere.

## See Also

[Code Syntax](Code_Syntax.md)

[Rule Syntax](Rule_syntax.md)

[Pass File Layout](About_Pass_Files.md)
