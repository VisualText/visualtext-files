[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# fprintvar

## Purpose

Print the values of the **global** variable **varName** to **fileName**.

## Syntax

```
fprintvar(fileName, varName)
```

```
fileName - type: str

varName - type: str
```

## Returns

Writes the value(s) of the global variable **varName** to **fileName**.  If the variable has multiple values, they are written separated by spaces.  This action returns no value.

## Remarks

Old-style.  Use NLP++ syntax such as

"output.txt" << G("varname") << "\n";

## Example

```
@CODE

fprintvar("companies.txt", "company");
```

## See Also

[printvar](printvar.md), [gdump](gdump.md), [startout](startout.md), [stopout](stopout.md), [CODE Actions](NLP_PP_Stuff/AT-CODE_Actions.md#tables_of_code)
