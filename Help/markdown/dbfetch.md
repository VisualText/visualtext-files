[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# dbfetch

## Purpose

Fetch a row from the current database result.

## Syntax

```
return_bool = dbfetch()
```

```
return_bool - True if successful, else false
```

## Returns

True if successful.

## Remarks

Assumes that preceding calls to dbbindcol() have bound NLP++ variables to database columns of the table that has been queried.

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
dbexecstmt("SELECT * FROM employee;");
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
