[← Help Contents](../index.md) | [📘 NLP++ Textbook](../NLP++_Textbook.md)

# About KB Command Files

On examining the interpreted knowledge base in the kb\user folder of an analyzer project, you will find files with human-readable commands:

| main.kb | Invokes command files for loading the knowledge base. |
| --- | --- |
| hier.kb | Adds the concepts in the knowledge base hierarchy |
| word.kb | Adds the words in the dictionary |
| phr.kb | Adds phrases to concepts |
| attr#.kb | Adds attributes to concepts and phrase nodes |

When an interpreted KB is read as part of loading an analyzer, the commands in these four files are executed in the order given above.  (This ordering guarantees that concepts are added to the kb before they are used in phrases, and that all concepts and nodes are present before attaching attributes to them.)  Similarly, the gui.kb file at the top-level directory of an analyzer project defines the analyzer sequence and the input file hierarchy, as loaded into the knowledge base.

All these .kb files execute a batch command language for adding and editing the knowledge base.  A typical command looks like

add hier "concept" "sys"

**add hier <path>** specifies that a concept is to be added to the hierarchy, as specified by a path of concept names that starts at the root of the knowledge base hierarchy, called "concept."  Thus, the command above says to start at the root, named "concept," and to add a concept called "sys" under the root, if not already present.  Another example is

add word "xyz"

The **add word** command above adds the word "xyz" under its appropriate index-concept in the special dictionary hierarchy within the KB.

The command **ind phrase** is used to add a phrase of nodes to a concept.  Each concept can only have one phrase, with any number of nodes:

```
ind
 phrase
```

```
<concept>         ;
 The concept to which the phrase is being added.
```

```
<concept 1>       ;
 Concept referenced by 1st node of phrase.
```

```
<concept
 2>       ;
 Concept referenced by 2nd node of phrase.
```

```
...
```

```
end ind
```

An example that adds an attribute to a concept is

```
ind
 attr
```

```
"concept"
 "gram"
```

```
0
```

```
"concept"
 "sys" "dict" "a" "c" "co"
 "constrain"
```

```
pst
```

```
"true"
```

```
end
 ind
```

The command **ind attr** is a multi-line command for adding an attribute.  Its general form is

```
ind attr
```

```
<concept>         ;
 The concept to which an attribute is being added.
```

```
<concept index>
   ;
 0 means attr is to be added to the concept itself.  1
 = add attr to 1st
```

```
                  ;
 node of concept's phrase, etc.
```

```
<key concept>
     ;
 The attribute key (or name), specified by a concept in the kb.
```

```
<value type>
      ;
 The type of value:
```

```
                  ;
 (pst = string, pnum = integer, pfloat = float pcon = concept)
```

```
<value>           ;
 The value itself, according to its type.
```

```
...
```

```
<value type N>
    ;
 Can optionally add second value type, second value, and so on.
```

```
<value N>
```

```
end ind
```

Each command file should end with the **quit** command alone on a line.  Comments are indicated by a semicolon, as above.

Note that command files can be executed from an analyzer pass file, using the NLP++ **take** function (also available as an API function in include/API/consh/cg.h).  take(filename) executes the commands in the specified .kb file.  This is one way in which knowledge can be layered or imported into a knowledge base conveniently.  In addition, there's a **take** command, as in

take "kb\\user\\main.kb"

which accepts both an absolute and relative filename as argument, and executes the commands within the given filename.  Relative filenames assume the current application project as the root directory.

A variant to add attributes to a dictionary word concept has been implemented, called **ind wattr**.  Its format is identical with ind attr, except that instead of a concept, a word may be specified for convenience.

```
ind
 wattr
```

```
<word>            ;
 A string.  The
 dictionary word to which an attribute is being added.
```

```
0                 ;
 This line is kept merely to match the format of ind attr.
```

```
<key concept>
     ;
 The attribute key (or name), specified by a concept in the kb.
```

```
<value type>
      ;
 The type of value:
```

```
                  ;
 (pst = string, pnum = integer, pfloat = float pcon = concept)
```

```
<value>           ;
 The value itself, according to its type.
```

```
...
```

```
<value type N>
    ;
 Can optionally add second value type, second value, and so on.
```

```
<value N>
```

```
end ind
```

Additional batch commands exist, but the most important ones have been mentioned here.
