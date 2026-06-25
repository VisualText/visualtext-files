[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# print

## Purpose

**OBSOLETE.**  Print the literal **string** to standard output.

## Syntax

```
print(string)
```

```
string - type: str
```

## Returns

Writes **string** to the current output file if one is open, otherwise to standard output.  This action returns no value.

## Remarks

Old-style.  Use NLP++ syntax such as

"output.txt" << "string...\n";

## Example

```
@CODE

print("Hello, world!\n");
```

## See Also

[printr](printr.md), [prlit](prlit.md), [prrange](prrange.md), [startout](startout.md), [stopout](stopout.md), [CODE Actions](NLP_PP_Stuff/AT-CODE_Actions.md#tables_of_code), [POST Actions](NLP_PP_Stuff/AT-POST_Actions.md#table_of_@POST_Actions)
