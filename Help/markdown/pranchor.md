# pranchor

## Purpose

**OBSOLETE.**  Print a web URL to **fileName**. Treat the range (**number1, number2**) as a URL.

## Syntax

```
pranchor(fileName, number1, number2)
```

```
fileName - type: str

number1 - type: int

number2 - type: int
```

## Returns

## Remarks

Use the global variable named **Base** to resolve and print complete relative URLs. (A prior pass must find the <base> HTML tag and set **Base** appropriately. NOT yet using the file's URL, so not handling cases where <base> itself is a relative URL.)

The output file (**fileName**) must be set up in advance using **openfile**, **fileout** or an output statement.

## Example

## See Also

[openfile](openfile.md), [fileout](fileout.md), [POST Actions](NLP_PP_Stuff/AT-POST_Actions.md#table_of_@POST_Actions)
