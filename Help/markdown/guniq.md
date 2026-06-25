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

Nothing. This is a side-effecting CODE action: it removes redundant adjacent string values from the global variable **varname** in place and returns no value to NLP++.

## Remarks

Old-style, slated for replacement.

Operates like the Unix **uniq** utility: it only removes duplicates that are adjacent, so the values must already be sorted (e.g. with **sortvals**) for all redundancies to be eliminated.

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
