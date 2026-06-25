[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# prxtree

## Purpose

**OBSOLETE.**  To **fileName**, print the first node called **name** found in the **ord**th element's tree, preceded by **prestr** and followed by **poststr**. If named node is not found, nothing is printed out.

## Syntax

```
prxtree(fileName, prestr, ord, name, poststr)
```

```
fileName - type: str

prestr - type: str

ord - type:

name - type: str

poststr - type: str
```

## Returns

If a node named **name** is found in the subtree of the **ord**th rule element, writes **prestr**, then that node's matched input text, then **poststr** to **fileName**.  If no such node is found, nothing is written.  This action returns no value.

## Remarks

The output file (**fileName**) must be set up in advance using **openfile**, **fileout** or an output statement.

## Example

The code prxtree("out.txt", "date: ", 3, "_date", "\n") prints out a line like "date: 3/9/99 <cr>" if a _date node is found within the subtree of element 3.

## See Also

[prchild](prchild.md), [prtree](prtree.md), [openfile](openfile.md), [fileout](fileout.md), [POST Actions](NLP_PP_Stuff/AT-POST_Actions.md#table_of_@POST_Actions)
