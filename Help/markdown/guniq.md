[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# guniq

## Purpose

Remove redundancies in a sorted, multi-string valued **global** variable.

## Syntax

```
guniq(varname)
```

```
varname - type: str
```

## Returns

## Remarks

Old-style, slated for replacement.

## Example

```
@CODE

G("strs") = "abc";

G("strs")[1] = "def";

gtolower("strs");

"output.txt" << G("strs") << "\n";

guniq("strs");

"output.txt" << G("strs") << "\n";
```

## See Also

[sortvals](sortvals.md), [CODE Actions](NLP_PP_Stuff/AT-CODE_Actions.md#tables_of_code)
