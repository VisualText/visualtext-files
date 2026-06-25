[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# prlit

## Purpose

**OBSOLETE.**  Print the literal string **string** to **fileName**.

## Syntax

```
prlit(fileName, string)
```

```
fileName - type: str

string - type: str
```

## Returns

Writes the literal string **string** to **fileName**.  This action returns no value.

## Remarks

Old-style.  The output file (**fileName**) must be set up in advance using **openfile**, **fileout** or an output statement.

## Example

```
@POST
  prlit("output.txt", "found a match\n");
@@POST
```

## See Also

[print](print.md), [prrange](prrange.md), [printr](printr.md), [openfile](openfile.md), [fileout](fileout.md), [CODE Actions](NLP_PP_Stuff/AT-CODE_Actions.md#tables_of_code), [POST Actions](NLP_PP_Stuff/AT-POST_Actions.md#table_of_@POST_Actions)
