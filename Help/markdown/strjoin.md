[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# strjoin

## Purpose

Join the elements of an array into a single string.

## Syntax

```
returnedStr = strjoin(array, separatorStr)
```

```
returnedStr - type: str

array - type: array

separatorStr - type: str
```

## Returns

The elements run together with the separator between each pair. Returns no value if the array is empty or every element is empty.

## Remarks

This is the inverse of [split](split.md). Without it, building a delimited string meant a loop plus a "first time through" flag to decide whether to emit a separator.

The separator goes only **between** elements, never before the first or after the last. An array of one element comes back unchanged, with no separator at all.

Numeric and float elements are rendered as text, so an array of mixed types still joins sensibly. Empty elements contribute nothing but are still separated, so joining `a`, ``, `c` with `,` gives `a,,c`.

## Example

```
@CODE

L("parts") = split("a b c"," ");
"out.txt" << strjoin(L("parts"),"-") << "\n";      # a-b-c

# Round trip: re-join what split took apart, with a new separator.
L("csv") = strjoin(readlines(L("path")),",");

@@CODE
```

## See Also

[split](split.md), [arraylength](arraylength.md), [arraysort](arraysort.md), [String Functions](Table_of_String_Functions.md)
