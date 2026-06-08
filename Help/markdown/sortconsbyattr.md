[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# sortconsbyattr

## Purpose

Sort an array of knowledge base concepts by the value of one of their attributes.

## Syntax

```
returnArray_con = sortconsbyattr(array_con, attr_str, numeric_num, descending_num)
```

```
returnArray_con - type: array (multi-valued variable) of sorted KB concepts
```

```
array_con       - type: array of KB concepts
```

```
attr_str        - type: str.  The attribute name.
```

```
numeric_num     - type: num.  If 1, attr is numeric. If 0, attr is string.
```

```
descending_num  - type: num.  If 1, sort in descending order.  If 0, ascending.
```

## Returns

A new array of sorted concepts.

## Remarks

The given unsorted array is unchanged.

## Example

```
# Sort an array of concepts by comparing an attribute named "count", of numeric type,
```

```
# in ascending order.
```

```
G("sorted concepts") = sortconsbyattr(G("unsorted concepts"),"count",1,0);
```

```
G("unsorted concepts") = 0; # Explicitly remove the unsorted array.
```

## See Also

[Knowledge Base Functions](Table_of_Knowledge_Base_Functions.md)
