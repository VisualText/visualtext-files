[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# dbclose

## Purpose

Close the currently open database.

## Syntax

```
return_bool = dbclose()
```

```
return_bool - True if successful, else false

 
```

## Returns

True if successful.

## Remarks

Close the currently open database.  NLP++ currently allows only one database to be open at a time.

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
