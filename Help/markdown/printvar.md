[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# printvar

## Purpose

Print the values of the **global** variable **varName** to standard output.

## Syntax

```
printvar(varName)
```

```
varName - type: str
```

## Returns

Writes the value(s) of the global variable **varName** to the current output file if one is open, otherwise to standard output.  If the variable has multiple values, they are written separated by spaces.  This action returns no value.

## Remarks

Old-style.

## Example

```
@CODE

printvar("count");
```

## See Also

[fprintvar](fprintvar.md), [gdump](gdump.md), [startout](startout.md), [stopout](stopout.md), [CODE Actions](NLP_PP_Stuff/AT-CODE_Actions.md#tables_of_code)
