[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# push

## Purpose

Add a value to the front of an array.

## Syntax

```
returnedArray = push(value, array)
```

```
returnedArray - type: array

array - type: array

value - type: str, num, flt or concept
```

## Returns

A new array with value as element 0, followed by every element of the original array. Returns an empty array if the first argument is not an array.

## Remarks

Up to now arrays were grown mainly by indexing past the last element. `push` adds at the **front** instead.

The pushed value keeps its own type, so strings, numbers, floats and concepts can all be pushed, and mixed-type arrays are allowed. Uniqueness is not checked; pushing a value already in the array simply adds it again.

Note that this changes the array's indexing: the pushed value becomes element 0 and every existing element shifts up by one.

The source array is not modified; a new array comes back.

## Example

```
@CODE

L("abc") = split("a b c"," ");
"out.txt" << strjoin(push("z",L("abc")),",") << "\n";   # z,a,b,c

@@CODE
```

## See Also

[arrayslice](arrayslice.md), [arrayreverse](arrayreverse.md), [arraylength](arraylength.md), [Array Functions](Table_of_Array_Functions.md)
