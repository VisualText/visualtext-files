[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# arrayunique

## Purpose

Remove duplicate elements from an array.

## Syntax

```
returnedArray = arrayunique(array)
```

```
returnedArray - type: array

array - type: array
```

## Returns

A new array holding the first occurrence of each distinct element. Returns an empty array if the argument is not an array.

## Remarks

The array does **not** have to be sorted first. `arrayunique` keeps the first of each set of equal elements and preserves the original order, so `a b a c b` gives `a b c`.

Elements are compared by their text, so a numeric 2 and a string `"2"` count as the same value.

The source array is not modified; a new array comes back.

## Example

```
@CODE

L("seen") = split("a b a c b"," ");
"out.txt" << strjoin(arrayunique(L("seen")),",") << "\n";   # a,b,c

# Compose: distinct values, sorted.
"out.txt" << strjoin(arraysort(arrayunique(L("seen"))),",") << "\n";

@@CODE
```

## See Also

[arraysort](arraysort.md), [arrayreverse](arrayreverse.md), [arrayslice](arrayslice.md), [Array Functions](Table_of_Array_Functions.md)
