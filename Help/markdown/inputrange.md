[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# inputrange

## Purpose

Fetch a substring of the input text, as specified by start and end offsets.

## Syntax

```
returnedStr = inputrange(start_num,end_num)
```

```
returnedStr - type: str

start_num - type: num
```

```
end_num - type: num
```

## Returns

Returns a substring copied from the input text.

## Remarks

While this function isn't strictly necessary, it represents a convenience and an optimization.  (One could fetch the text of the root node and use strpiece to fetch the desired substring.)

Offsets are zero based.

## Example

G("str") = inputrange(0,9);   # Fetch the first 10 characters of the input text as a string.

## See Also

[Parse Tree Functions](Table_of_Parse_Tree_Functions.md)
