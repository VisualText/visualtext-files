[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# prtree

## Purpose

Look for **name** anywhere under the node matching rule element **number**. Print its text to **fileName**, if found.

## Syntax

```
prtree(fileName, number, name)
```

```
fileName - type: str

number - type: int

name - type: str
```

## Returns

If a node named **name** is found anywhere in the subtree under rule element **number**, writes that node's matched input text to **fileName**.  If no such node is found, nothing is written.  This action returns no value.

## Remarks

The output file (**fileName**) must be set up in advance using **openfile**, **fileout** or an output statement.

## Example

```
@POST
  prtree("output.txt", 1, "_date");
@@POST

@RULES
_event <- _name _clause @@
```

## See Also

[prchild](prchild.md), [prxtree](prxtree.md), [openfile](openfile.md), [fileout](fileout.md), [POST Actions](NLP_PP_Stuff/AT-POST_Actions.md#table_of_@POST_Actions)
