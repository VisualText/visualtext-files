# dbexec

## Purpose

Execute a statement on the currently open database.

## Syntax

```
return_bool = dbexec(command_str)
```

```
return_bool - True if successful, else false
```

```
command_str - Statement to send to the database 
```

## Returns

True if successful.

## Remarks

Unlike **dbexecstmt**(), **dbexec**() executes a statement in modular fashion anytime a database is open.  It allocates a statement handle, sends the statement, then closes its statement handle.

## Example

```
@CODE
```

```
dbopen("test","root","mypassword");
```

```
dbexec("INSERT INTO abc (name, number) VALUES('Joe','0013');");
```

```
dbclose();
```

```
@@CODE
```

## See Also

[Table of Database Functions](Table_of_Database_Functions.md)

[Database1 Analyzer](Sample_Analyzers/Database1_Analyzer.md)
