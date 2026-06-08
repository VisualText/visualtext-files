[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# dballocstmt

## Purpose

Allocate statement handle for the currently open database.

## Syntax

```
returnedBool = dballocstmt()
```

```
returnedBool - type: bool
 
```

## Returns

True if successful.

## Remarks

NLP++ database functions assume only one statement handle is open at a time.  In addition, one can call **dbexec**() to execute a statement in a separate fashion.

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
dbexecstmt("INSERT INTO employee (name, age) VALUES('John Smith','32');");
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

[Database1 Sample Analyzer](Sample_Analyzers/Database1_Analyzer.md)
