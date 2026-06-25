[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# fprintgvar

## Purpose

**OBSOLETE.**  To **fileName**, print the value of the global variable **var**.

## Syntax

```
fprintgvar(fileName, var)
```

```
fileName - type: str

var - type:
```

## Returns

Writes the value of the global variable **var** to **fileName**.  This action returns no value.

## Remarks

The output file (**fileName**) must be set up in advance using **openfile**, **fileout** or an output statement.

## Example

```
@POST
  fprintgvar("output.txt", "count");
@@POST
```

## See Also

[fprintnvar](fprintnvar.md), [fprintxvar](fprintxvar.md), [openfile](openfile.md), [fileout](fileout.md), [POST Actions](NLP_PP_Stuff/AT-POST_Actions.md#table_of_@POST_Actions)
