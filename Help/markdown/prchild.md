[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# prchild

## Purpose

**OBSOLETE.**  Look for **name** immediately under the node matching rule element **number**. Print its text to **fileName**, if found.

## Syntax

```
prchild(fileName, number, name)
```

```
fileName - type: str

number - type: int

name - type: str
```

## Returns

If a node named **name** is found immediately under rule element **number**, writes that node's matched input text to **fileName**.  If no such child is found, nothing is written.  This action returns no value.

## Remarks

The output file (**fileName**) must be set up in advance using **openfile**, **fileout** or an output statement.

## Example

```
@POST
  prchild("output.txt", 1, "_name");
@@POST

@RULES
_company <- _org @@
```

## See Also

[prtree](prtree.md), [prxtree](prxtree.md), [openfile](openfile.md), [fileout](fileout.md), [POST Actions](NLP_PP_Stuff/AT-POST_Actions.md#table_of_@POST_Actions)
