# dbexecstmt

## Purpose

Execute a statement with the currently open statement handle.

## Syntax

```
return_bool = dbexecstmt(command_str)
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

Unlike **dbexec**(), **dbexecstmt**() assumes there is a currently open statement handle.  NLP++ currently allows only a single statement handle to be active at a time.

## Example

```
@CODE
```

```
dbopen("test","root","mypassword");
```

```
dballocstmt();
```

```
dbexecstmt("INSERT INTO abc (name, number) VALUES('Jane','0011');");
```

```
dbexecstmt("INSERT INTO abc (name, number) VALUES('Joe','0013');");
```

```
dbfreestmt();
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
