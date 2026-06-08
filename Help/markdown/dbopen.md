# dbopen

## Purpose

Open a database.

## Syntax

```
return_bool = dbopen(db_str, user_str, password_str)
```

```
return_bool - True if successful, else false
```

```
db_str - Name of the database, as known to the ODBC manager
```

```
user_str - Name of database account (may be optional)
```

```
password_str - Password for database account (may be optional)

 
```

## Returns

True if successful.

## Remarks

Open a database connection.  NLP++ currently allows only one database to be open at a time.

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
dbexecstmt("SELECT * FROM table;");
```

```
dbbindcol(1,"varchar",50,&G("employee name"),&G("result1"));
```

```
while (dbfetch())
```

```
   {
```

```
   "output.txt" << "employee name: ";
```

```
   if (G("result1"))
```

```
      "output.txt" << G("employee name") << "\n";
```

```
   else
```

```
      "output.txt" << "NULL" << "\n";
```

```
   }
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
