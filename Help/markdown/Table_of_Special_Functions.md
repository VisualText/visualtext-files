# Table of Special Functions

NLP++ has a set of special functions.  These have been listed here in table form for easy reference.  For examples of these functions, refer to the individual function pages included in the Special Functions section.

The return types include:  **STR** (string), **INT** (integer), and **BOOL** (Boolean). Boolean type is currently implemented by integer **1** (or non-zero) for **true** and **0** for **false**.  **NONE** indicates nothing is returned.

| **FUNCTION NAME** | **RETURNS** | **DESCRIPTION** |
| --- | --- | --- |
| [**batchstart()**](batchstart.md) | **BOOL(1,0)** | Check if start of a batch analysis. True if current file is first in a batch run. |
| [**debug()**](debug.md) | **BOOL(1,0)** | No op. Convenient breakpoint for debugging from C++ compiler. |
| [exitpass()](exitpass.md) | NONE | Exit from the current pass file immediately, without performing rule matching (if any). |
| [exittopopup(message_str, type_str)](exittopopup.md) | BOOL(1,0) | Exit from current pass, invoking a popup if within VisualText. |
| [**fail()**](fail.md) | NONE | In CHECK Region, abort the rule that has just matched. Noop elsewhere. See succeed(). |
| [findana](findana.md) | STR | See if named project is already resident in memory. **(New in 1.6)** |
| [getpopupdata()](getpopupdata.md) | STR | Get the data typed in by a call to **exittopopup**(). |
| [hitconf(hits_num, total_num, fudge_num)](hitconf.md) | INT (0 to 100) | Calculate the keyword density. Fudge factor is typically 3 to 20. |
| [interactive()](interactive.md) | BOOL(1,0) | True if analyzer is being run in an interactive environment, e.g., inside VisualText. |
| [mkdir(dir_str)](mkdir.md) | BOOL(1,0) | Create a directory. Operating system-dependent. |
| [permuten(tot_num)](permuten.md) | INT ARR | Permute integers 0 to (tot_num - 1) such that array element k will never be equal to k. |
| [**succeed()**](succeed.md) | NONE | In CHECK Region and CODE Region, succeed without executing further code. See fail(). |
| [**system(str)**](system.md) | BOOL(1,0) | Execute str as operating system command. |
| [**today()**](today.md) | **STR** | Format the current date and time as a string. |
|   |   |   |

## See Also

[Knowledge Base Functions](Table_of_Knowledge_Base_Functions.md)

[Formatting and I/O Functions](Table_of_Formatting_and_I_O_Functions.md)

[Parse Tree Functions](Table_of_Parse_Tree_Functions.md)

[String Functions](Table_of_String_Functions.md)

[Spelling Functions](Table_of_Spelling_Functions.md)
