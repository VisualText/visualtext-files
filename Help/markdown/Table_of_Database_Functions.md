[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# Table of Database Functions

The NLP++ functions for interfacing with a database are listed here in table form for easy reference.  For examples of these functions, refer to the individual function pages included in the Database Functions section.  Also available is a sample analyzer illustrating connection to a database, in **Samples\database1**.  An introductory page is available at [Database1 Analyzer](Sample_Analyzers/Database1_Analyzer.md).

| **FUNCTION NAME** | **RETURNS** | **DESCRIPTION** |
| --- | --- | --- |
| [**dballocstmt()**](dballocstmt.md) | BOOL | Create a handle for an active database statement. (Stored internally, allows only one active handle at a time.) |
| [**dbbindcol(column_num, type_str, size_str, &var, &flag_var)**](dbbindcol.md) | BOOL | Bind the given database column number to the NLP++ variable **var**. **type_str** specifies the database data type being fetched. **size_str** specifies the size needed to store the database value being retrieved -- for some types, it is ignored. ** flag_var** is a second NLP++ variable used to flag whether the currently fetched row contains a value in the column being fetched. Calls to **dbbindcol** are followed by calls to **dbfetch** in order to fetch successive database rows. Note that the ampersands are needed to indicate call by reference, i.e., that values are being passed up to the two NLP++ variables. E.g., *dbbindcol(1,"string",255, &G("employee name"),&G("result flag"));* |
| [**dbclose()**](dbclose.md) | BOOL | Close the currently open database. (Only one database can be open at a time.) |
| [**dbexec(cmd_str)**](dbexec.md) | **BOOL** | Send a statement to the currently open database. A modular function that creates a statement handle, sends the command string, then closes the statement handle. |
| [**dbexecstmt(cmd_str)**](dbexecstmt.md) | **BOOL** | Send a statement using the currently open statement handle. Assumes a statement has been opened with **dballocstmt**. |
| [**dbfetch()**](dbfetch.md) | BOOL | Fetch a row from a database. Columns bound by previous calls to **dbbindcol** will get their variables filled with values from the columns in this database row. Returns 1 as long as rows successfully fetched, else 0. |
| [**dbfreestmt()**](dbfreestmt.md) | **BOOL** | Frees the statement handle allocated by **dballocstmt**. Only one statement handle can be active at a time. |
| [**dbopen(db_str [, user_str] [, password_str])**](dbopen.md) | **BOOL** | Open the given database name with user name and password. Depending on the database and account set up, the user name and password may be optional. |
|   |   |   |

## See Also

[Database1 Analyzer](Sample_Analyzers/Database1_Analyzer.md)
