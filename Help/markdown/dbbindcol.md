[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# dbbindcol

## Purpose

Bind a database table's column to an NLP++ variable.

## Syntax

```
return_bool = dbbindcol(column_num, type_str, size_num, &var, &flag_var)
```

```
return_bool - True if successful, else false
```

```
column_num - Database column number
```

```
type_str - Database type for the given column.  See table below
```

```
size_num - For some database types, indicates the required storage size for retrieving the data
```

```
&var - (call by reference). NLP++ variable to receive the fetched column value.
```

```
&flag_var - (call by reference).  NLP++ variable to indicate whether the column had a value.

 
```

## Returns

True if successful.

## Remarks

The associated function **dbfetch** fetches a database table row, filling all the bound variables.

## Database Types and Conversion

The supported database types (those not in parentheses) and their conversion to NLP++ types are listed here:

| DATABASE TYPE | **NLP++ TYPE** | SPECIFY SIZE? |
| --- | --- | --- |
| BIGINT | NUM | no |
| BINARY | STR | yes |
| BIT | NUM | no |
| (BLOB) | --- | --- |
| CHAR | STR | yes |
| DATE | STR | no |
| DATETIME | STR | no |
| DECIMAL | FLOAT | no |
| DOUBLE | FLOAT | no |
| ENUM | STR | yes |
| FLOAT | FLOAT | no |
| INT | NUM | no |
| INTEGER | NUM | no |
| (LONGBLOB) | --- | --- |
| LONGVARBINARY | STR | yes |
| (MEDIUMBLOB) | --- | --- |
| MEDIUMINT | NUM | no |
| NUMERIC | FLOAT | no |
| REAL | FLOAT | no |
| SET | STR | yes |
| SMALLINT | NUM | no |
| TIME | STR | no |
| TIMESTAMP | STR | no |
| TINYBLOB | STR | yes |
| TINYINT | NUM | no |
| VARBINARY | STR | yes |
| VARCHAR | STR | yes |
| YEAR | STR | no |
|   |   |   |

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
