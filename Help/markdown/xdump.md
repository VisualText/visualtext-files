[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# xdump

## Purpose

Dump all the variables in the **ord**th context node and their values to** fileName.**

## Syntax

```
xdump(fileName, ord)
```

```
fileName - type: str

ord - type:
```

## Returns

Writes every variable on the **ord**th context node and its value(s) to **fileName**.  If **ord** is 0 or omitted, the last context node is used.  This action returns no value.

## Remarks

The output file (**fileName**) must be set up in advance using **openfile**, **fileout** or an output statement.

## Example

```
@POST
  xdump("context.txt", 1);
@@POST

@RULES
_item <- _noun @@
```

## See Also

[gdump](gdump.md), [ndump](ndump.md), [sdump](sdump.md), [openfile](openfile.md), [fileout](fileout.md), [POST Actions](NLP_PP_Stuff/AT-POST_Actions.md#table_of_@POST_Actions)
