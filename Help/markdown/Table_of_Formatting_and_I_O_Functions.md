[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# Table of Formatting and I/O Functions

The NLP++ functions used formatting and performing input and output operations are listed here in table form for easy reference.  For examples of these functions, refer to the individual function pages included in the Formatting and I/O Functions section.

The return types include:**  STR** (string), **OSTREAM** (output stream) and **BOOL** (Boolean).  Boolean type is currently implemented by integer **1** (or non-zero) for **true** and **0** for **false**.

| **FUNCTION NAME** | **RETURNS** | **DESCRIPTION** |
| --- | --- | --- |
| [cbuf()](cbuf.md) | OSTREAM | Output to buffer that user supplied for the current parse (standalone or embedded only). |
| [cout()](cout.md) | OSTREAM | Output to standard output or user-supplied stream (the latter in standalone or embedded only). |
| [coutreset(fileNameStr)](coutreset.md) | OSTREAM | Bind cout() stream to the given filename. |
| [**closefile(fileOstream)**](closefile.md) | BOOL | Close the output file stream. |
| [inputrangetofile(start_n,end_n,out_ostr)](inputrangetofile.md) | BOOL | Print a range of chars from the input text to an output stream. (Listed with Parse Tree Functions) |
| [**LJ(num, fieldsize_num)**](LJ.md) | **STR** | Left-justify num in given field size. |
| [**openfile(fileNameStr)**](openfile.md) | OSTREAM | Open output file stream. |
| [**percentstr(numerator_num, denominator_num)**](percentstr.md) | **STR (" 0" to "100")** | Format a percentage (right-justified in field of 3 chars). |
| [**rightjustifynum(num, fieldsize_num)**](rightjustifynum.md) | **STR** | Right-justify num in given field size. |
| [**today()**](today.md) | STR | Format the current date and time as a string. |

## See Also

[Special Functions](Table_of_Special_Functions.md)

[Knowledge Base Functions](Table_of_Knowledge_Base_Functions.md)

[Parse Tree Functions](Table_of_Parse_Tree_Functions.md)

[String Functions](Table_of_String_Functions.md)

[Spelling Functions](Table_of_Spelling_Functions.md)
