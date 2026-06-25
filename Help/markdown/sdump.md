[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# sdump

## Purpose

Dump all the variables in the suggested node and their values to **fileName**.

## Syntax

```
sdump(fileName)
```

```
fileName - type: str
```

## Returns

Writes every variable being built for the suggested node and its value(s) to **fileName**.  This action returns no value.

## Remarks

The output file (**fileName**) must be set up in advance using **openfile**, **fileout** or an output statement.

## Example

```
@POST
  sdump("suggested.txt");
@@POST
```

## See Also

[gdump](gdump.md), [xdump](xdump.md), [ndump](ndump.md), [openfile](openfile.md), [fileout](fileout.md), [POST Actions](NLP_PP_Stuff/AT-POST_Actions.md#table_of_@POST_Actions)
