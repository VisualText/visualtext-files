[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# sortvals

## Purpose

Sort the strings in multi-string-valued **global** variable **varname**.

## Syntax

```
sortvals(varname)
```

```
varname - type: str
```

## Returns

Nothing. This is a side-effecting CODE action: it sorts the string values held in the global variable **varname** in place and returns no value to NLP++.

## Remarks

## Example

```
@CODE

G("xx") = "abacus";

G("xx")[1] = "aardvark";

sortvals("xx");

"output.txt" << G("xx") << "\n";
```

## See Also

[guniq](guniq.md), [CODE Actions](NLP_PP_Stuff/AT-CODE_Actions.md#tables_of_code)
