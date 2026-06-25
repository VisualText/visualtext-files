[← Help Contents](../index.md) | [📘 NLP++ Textbook](../NLP++_Textbook.md)

# CODE Action

The CODE Actions in this section predate the NLP++ language, but are retained because they are still useful. In subsequent releases, these actions may be modified.

## Types of CODE Actions

CODE Actions are divided into two groups:

- Variable Actions

- Print Actions

## Tables of CODE Actions

Actions available in the CODE Region are provided in the tables below.  For examples on using these actions, refer to the individual action topics in the @CODE Actions section.

## Variable Actions

| **ACTION(ARG1,ARG2...)** | **DESCRIPTION** |
| --- | --- |
| [**varstrs(varname)**](../varstrs.md) | Create an empty multi-string-valued **global** variable with name **varname**. The POST Action **addstrs()** adds values to this type of variable. |
| [**sortvals(varname)**](../sortvals.md) | Sort the strings in multi-string-valued **global** variable **varname**. |
| [**gtolower(varname)**](../gtolower.md) | Convert the strings in multi-string valued **global** variable to lower case. |
| [**guniq(varname)**](../guniq.md) | Remove redundancies in a sorted, multi-string valued **global** variable. |
| [**lookup(var,file,flag)**](../lookup.md) | Specialized word lookup. **Global **variable **var** has multiple words as values. **file** is a file of strings, one per line. **flag** tells which bit-flag of the word's symbol table entry to modify. E.g., **lookup("Words", "dict.words", "word")** looks up all the values in the **Words** variable in the **dict.words** file and modifies the **word** bit-flag (which says whether the word is a proper English word). |

## Print Actions

| CODE Action | Description |
| --- | --- |
| [**print(str)**](../print.md) | Print str to the standard output (usually the console or DOS window). (See ***startout*** below). |
| [**printvar(var)**](../printvar.md) | Print the values of the **global** variable named **var** to standard output. (See ***startout*** below). |
| [**fprintvar(file, var)**](../fprintvar.md) | Print the values of the **global** variable named **var** to **file**. |
| [**prlit(file, str)**](../prlit.md) | Print the literal string **str** to **file**. |
| [**gdump(filename)**](../gdump.md) | Dump the all the global variables and their values to the given filename. |
| [**fileout(file)**](../fileout.md) | Open **file** for appending. **File** becomes a variable useable in print actions with a file argument, e.g. **prlit()**. |
| [**startout(0)**](../startout.md) | Divert standard output to the main output file, set by the caller of the analyzer (default is **output.txt**). |
| [**stopout(0)**](../stopout.md) | Stop diverting standard output to the main output file. Subsequent file-less output is to standard output. |

## See Also

[PRE Action](AT-PRE_Actions.md)

[CHECK Action](AT-CHECK_Actions.md)

[POST Action](AT-POST_Actions.md)
