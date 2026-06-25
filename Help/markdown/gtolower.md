[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# gtolower

## Purpose

Convert the strings in multi-string valued **global** variable to lower case.

## Syntax

```
gtolower(varname)
```

```
varname - type: str
```

## Returns

Nothing. This is a side-effecting CODE action: it lowercases the string values held in the global variable **varname** in place and returns no value to NLP++.

## Remarks

Old-style function slated for replacement.

## Example

```
@CODE

G("strs") = "abc";

G("strs")[1] = "def";

gtolower("strs");

"output.txt" << G("strs") << "\n";
```

## See Also

[lookup](lookup.md), [CODE Actions](NLP_PP_Stuff/AT-CODE_Actions.md#tables_of_code)
