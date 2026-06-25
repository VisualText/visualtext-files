[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# fprintxvar

## Purpose

**OBSOLETE.**  To **fileName**, print the value of the variable **var** in the **ord**th context node.

## Syntax

```
fprintxvar(fileNname, var, ord)
```

```
fileName - type: str

var - type:

ord - type:
```

## Returns

Writes the value of variable **var** stored on the **ord**th context node to **fileName**.  This action returns no value.

## Remarks

The output file (**fileName**) must be set up in advance using **openfile**, **fileout** or an output statement.

## Example

```
@POST
  fprintxvar("output.txt", "number", 1);
@@POST

@RULES
_item <- _noun @@
```

## See Also

[fprintgvar](fprintgvar.md), [fprintnvar](fprintnvar.md), [openfile](openfile.md), [fileout](fileout.md), [POST Actions](NLP_PP_Stuff/AT-POST_Actions.md#table_of_@POST_Actions)
