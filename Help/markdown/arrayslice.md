[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# arrayslice

## Purpose

Take a run of elements out of an array.

## Syntax

```
returnedArray = arrayslice(array, startNum)
returnedArray = arrayslice(array, startNum, endNum)
```

```
returnedArray - type: array

array - type: array

startNum - type: int

endNum - type: int
```

## Returns

A new array holding the elements from startNum up to but not including endNum. Returns an empty array if the argument is not an array or if the range selects nothing.

## Remarks

Indexes are zero based. **start is included and end is not**, so the number of elements taken is end - start. Omit end to run to the end of the array.

Out-of-range values are clamped rather than reported as errors, so slicing past the end simply yields fewer elements and an empty range yields an empty array.

The source array is not modified; a new array comes back.

## Example

```
@CODE

L("abcd") = split("a b c d"," ");

"out.txt" << strjoin(arrayslice(L("abcd"),1,3),",")  << "\n";   # b,c
"out.txt" << strjoin(arrayslice(L("abcd"),2),",")    << "\n";   # c,d
"out.txt" << strjoin(arrayslice(L("abcd"),3,99),",") << "\n";   # d
"out.txt" << strjoin(arrayslice(L("abcd"),2,2),",")  << "\n";   # (empty)

# Drop a header line off a data file.
L("rows") = arrayslice(readlines(L("path")),1);

@@CODE
```

## See Also

[arraysort](arraysort.md), [arrayunique](arrayunique.md), [arrayreverse](arrayreverse.md), [arraylength](arraylength.md), [Array Functions](Table_of_Array_Functions.md)
