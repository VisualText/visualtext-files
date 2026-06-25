[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# fprintnvar

## Purpose

**OBSOLETE.**  To **fileName**, print the value of the variable **var** in the **ord**th element's node.

## Syntax

```
fprintnvar(fileName, var, ord)
```

```
filename - type: str

var - type:

ord - type:
```

## Returns

Writes the value of variable **var** stored on the node of the **ord**th phrase element to **fileName**.  This action returns no value.

## Remarks

The output file (**fileName**) must be set up in advance using **openfile**, **fileout** or an output statement.

## Example

```
@POST
  fprintnvar("output.txt", "number", 1);
@@POST

@RULES
_item <- _noun @@
```

## See Also

[fprintgvar](fprintgvar.md), [fprintxvar](fprintxvar.md), [openfile](openfile.md), [fileout](fileout.md), [POST Actions](NLP_PP_Stuff/AT-POST_Actions.md#table_of_@POST_Actions)
