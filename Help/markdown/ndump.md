[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# ndump

## Purpose

Dump all the variables in the **ord**th phrase element's node and their values to **fileName**.

## Syntax

```
ndump(fileName, ord)
```

```
fileName - type: str

ord - type:
```

## Returns

Writes the matched text of the **ord**th phrase element's node (as a `$text=` line) followed by every variable on that node and its value(s) to **fileName**.  If **ord** is 0 or omitted, the node of the last phrase element is used.  This action returns no value.

## Remarks

The output file (**fileName**) must be set up in advance using **openfile**, **fileout** or an output statement.

## Example

```
@POST
  ndump("nodes.txt", 1);
@@POST

@RULES
_item <- _noun @@
```

## See Also

[gdump](gdump.md), [xdump](xdump.md), [sdump](sdump.md), [openfile](openfile.md), [fileout](fileout.md), [POST Actions](NLP_PP_Stuff/AT-POST_Actions.md#table_of_@POST_Actions)
