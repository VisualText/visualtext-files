[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# fail

## Purpose

Exit from a region or rule in a pass file.

## Syntax

```
NULL = fail()
```

## Returns

Nothing. `fail()` is called as a statement; in the CHECK region it flags the current rule match to be rejected. Elsewhere it is a no-op.

## Remarks

Constrained to appear directly in the CHECK region, not within functions defined in the DECL region.

## Example

```
@CHECK

fail(); # Reject the current rule match.

@@CHECK
```

## See Also

[exitpass](exitpass.md), [succeed](succeed.md), [or](or.md), [CHECK Actions](NLP_PP_Stuff/AT-CHECK_Actions.md), [Phrase Element Modifier fails](fails.md)
