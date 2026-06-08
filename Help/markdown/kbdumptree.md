[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# kbdumptree

## Purpose

Create a dump file *file_str* of knowledge base concept *root_con*.

## Syntax

```
returnedBoolean
 = kbdumptree(root_con, file_str)
```

```
returnedBoolean - type: bool
```

```
root_con - type:  con
```

```
file_str
 - type:  str
```

## Returns

Returns **1** is true and **0** if false.

## Remarks

This function requires a filename ending in a ".kb" extension.

## Example

```
@CODE
```

```
G("root") = findroot();
```

```
G("conc") = makeconcept(G("root"),
 "companies");
```

```
makeconcept(G("conc"), "ford");
```

```
makeconcept(G("conc"), "gm");
```

```
kbdumptree(G("conc"), "c:\\companies.kb");
```

```
@@CODE
```

## See Also

[take](take.md) [Knowledge Base Functions](Table_of_Knowledge_Base_Functions.md)
