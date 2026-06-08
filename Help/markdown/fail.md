# fail

## Purpose

Exit from a region or rule in a pass file.

## Syntax

```
NULL = fail()
```

## Returns

## Remarks

Constrained to appear directly in the CHECK region, not within functions defined in the DECL region.

## Example

```
@CHECK

fail(); # Reject the current rule match.

@@CHECK
```

## See Also

[exitpass](exitpass.md), [succeed](succeed.md), [or](or.md), [Phrase Element Modifier fails](fails.md)
