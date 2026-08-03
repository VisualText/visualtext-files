[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# arraysort

## Purpose

Sort the elements of an array.

## Syntax

```
returnedArray = arraysort(array)
returnedArray = arraysort(array, numericBool)
returnedArray = arraysort(array, numericBool, descendingBool)
```

```
returnedArray - type: array

array - type: array

numericBool - type: bool (1,0)

descendingBool - type: bool (1,0)
```

## Returns

A new array holding the same elements in sorted order. Returns an empty array if the argument is not an array.

## Remarks

The other sorts — [sortvals](sortvals.md), [sortchilds](sortchilds.md), [sorthier](sorthier.md), [sortphrase](sortphrase.md), [sortconsbyattr](sortconsbyattr.md) — are all knowledge-base or parse-tree oriented. `arraysort` sorts a plain array, such as what [split](split.md), [readlines](readlines.md) or [dirlist](dirlist.md) returned. The argument order follows [sortconsbyattr](sortconsbyattr.md).

By default the sort is lexical and ascending. Lexical order is **byte order**, so all uppercase letters sort ahead of all lowercase ones: `Banana` comes before `apple`. Lowercase the array first with a loop and [strtolower](strtolower.md) if you want dictionary order.

Pass 1 for numericBool to compare the elements as numbers instead, which is what you want for an array of digits — lexically, `100` sorts before `2`.

The sort is stable, so elements that compare equal keep their original relative order.

The source array is not modified; a new array comes back.

## Example

```
@CODE

L("words") = split("cherry apple banana"," ");
"out.txt" << strjoin(arraysort(L("words")),",")     << "\n";  # apple,banana,cherry

L("nums") = split("10 2 100"," ");
"out.txt" << strjoin(arraysort(L("nums"),1),",")    << "\n";  # 2,10,100
"out.txt" << strjoin(arraysort(L("nums"),1,1),",")  << "\n";  # 100,10,2

@@CODE
```

## See Also

[arrayunique](arrayunique.md), [arrayreverse](arrayreverse.md), [arrayslice](arrayslice.md), [sortconsbyattr](sortconsbyattr.md), [Array Functions](Table_of_Array_Functions.md)
