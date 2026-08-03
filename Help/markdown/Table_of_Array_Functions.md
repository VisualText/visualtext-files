[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# Table of Array Functions

Arrays and lists are treated equivalently in NLP++, and we'll continue to call them both "arrays" for conciseness.

The current section is meant to round out the treatment of list-like capabilities such as pushing a value to the front.  Up to now, arrays were grown mainly by indexing to the last element.

Arrays can also be assigned and manipulated with parse tree functions and kb functions.

| **FUNCTION NAME** | **RETURNS** | **DESCRIPTION** |
| --- | --- | --- |
| [**arraylength(array)**](arraylength.md) | **INT** | Number of elements in an array. |
| [**arrayreverse(array)**](arrayreverse.md) | **ARRAY** | The same elements, last to first. |
| [**arrayslice(array, start_num [, end_num])**](arrayslice.md) | **ARRAY** | Elements from start up to but not including end. Zero based; omit end to run to the end. |
| [**arraysort(array [, numeric_bool [, descending_bool]])**](arraysort.md) | **ARRAY** | Sort an array. Lexical and ascending by default; stable. |
| [**arrayunique(array)**](arrayunique.md) | **ARRAY** | Keep the first of each distinct element, in the original order. |
| [**push(value, array)**](push.md) | **ARRAY** | Push a value to the front of an array. Allows mixed types (string, num, flt, concept...), allows redundant values, does not check uniqueness. NOTE: This alters the array indexing; the pushed item becomes the 0th element. |
| [**split(str, char_str)**](split.md) | **ARRAY** | Split a string into an array on a separator character. |
| [**strjoin(array, separator_str)**](strjoin.md) | **STR** | Join an array's elements into one string. The inverse of split. |

These functions never modify the array given to them; each returns a new array.

### Testing for an empty result

The functions that can find nothing — `arrayslice`, `arrayunique`, [refind](refind.md), [dirlist](dirlist.md), [readlines](readlines.md) — return an **empty array**. Note that assigning an empty array to a variable collapses it back to no value, and `arraylength` reports **1** for a variable holding no value. So guard a loop by testing the first element, not the count:

```
L("hits") = arrayslice(L("rows"),1);
if (strlength(L("hits")[0])) {
    # ... safe to loop over L("hits") ...
}
```

## See Also
