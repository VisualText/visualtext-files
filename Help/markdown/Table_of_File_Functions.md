[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# Table of File Functions

NLP++ has a set of functions for querying and managing files and directories on disk. These have been listed here in table form for easy reference. For examples of these functions, refer to the individual function pages.

The return types include: **STR** (string), **INT** (integer), and **BOOL** (Boolean). Boolean type is currently implemented by integer **1** (or non-zero) for **true** and **0** for **false**. **NONE** indicates nothing is returned.

| **FUNCTION NAME** | **RETURNS** | **DESCRIPTION** |
| --- | --- | --- |
| [**deletefile(path_str)**](deletefile.md) | **BOOL(1,0)** | Delete a regular file. Never removes directories. |
| [**direxists(path_str)**](direxists.md) | **BOOL(1,0)** | True if the path is an existing directory. |
| [**fileexists(path_str)**](fileexists.md) | **BOOL(1,0)** | True if the path is an existing regular file. |
| [**filesize(path_str)**](filesize.md) | **INT** | Size of a regular file in bytes, or -1 if not a readable file. |
| [**mkdir(dir_str)**](mkdir.md) | **BOOL(1,0)** | Create a directory. Operating system-dependent. |

For reading and writing file contents, see the file-stream functions [openfile](openfile.md), [closefile](closefile.md), and [fileout](fileout.md) in the [Formatting and I/O Functions](Table_of_Formatting_and_I_O_Functions.md) table, and [urltofile](urltofile.md) in the [Web Functions](Table_of_Web_Functions.md) table.

## See Also

[Formatting and I/O Functions](Table_of_Formatting_and_I_O_Functions.md), [Web Functions](Table_of_Web_Functions.md), [Special Functions](Table_of_Special_Functions.md)
