[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# arrayreverse

## Purpose

Reverse the order of an array's elements.

## Syntax

```
returnedArray = arrayreverse(array)
```

```
returnedArray - type: array

array - type: array
```

## Returns

A new array holding the same elements last to first. Returns an empty array if the argument is not an array.

## Remarks

The source array is not modified; a new array comes back.

Combine with [arraysort](arraysort.md) only when you need something other than a plain descending sort — for a descending sort, pass 1 as arraysort's third argument instead of reversing afterwards.

## Example

```
@CODE

L("abc") = split("a b c"," ");
"out.txt" << strjoin(arrayreverse(L("abc")),",") << "\n";   # c,b,a

@@CODE
```

## See Also

[arraysort](arraysort.md), [arrayunique](arrayunique.md), [arrayslice](arrayslice.md), [Array Functions](Table_of_Array_Functions.md)
