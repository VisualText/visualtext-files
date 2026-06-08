[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# exitpass

## Purpose

Exit from the current pass file immediately, without performing rule matching (if any).

## Syntax

```
NULL = exitpass()
```

## Returns

## Remarks

`exitpass` can be called from the CODE, POST, and CHECK Regions, but won't work as desired from inside a user-defined function. It can be used (a bit crudely) to support conditional execution of passes in the analyzer.

For example, you could build an analyzer that handles both HTML and plain text. If the input has no HTML tags, then skip each HTML pass with `exitpass`. If it does have HTML tags, then analyze them first.

It can also serve to exit a pass in the middle of rule matching, e.g., if a special situation or pattern is recognized.

## Example

```
@CODE

exitpass(); # Exit the current pass file immediately.

@@CODE
```

## See Also

[fail](Functions/Miscellaneous_Functions/fail.md), [succeed](succeed.md), [Special Functions](Table_of_Special_Functions.md)
