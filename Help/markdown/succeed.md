# succeed

## Purpose

In CHECK Region and CODE Region, succeed without executing further code.

## Syntax

```
NULL = succeed()
```

## Returns

## Remarks

Constrained to appear directly in the CHECK region, not within functions defined in the DECL region.

## Example

```
@CHECK

succeed();

@@CHECK
```

## See Also

[or](or.md), [fail](Functions/Miscellaneous_Functions/fail.md), [exitpass](exitpass.md), [Special Functions](Table_of_Special_Functions.md), [CHECK Actions](NLP_PP_Stuff/AT-CHECK_Actions.md)
