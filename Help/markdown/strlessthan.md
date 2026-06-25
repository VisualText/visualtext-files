[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# strlessthan

## Purpose

Check if string 1 is lexically before string 2.

## Syntax

```
returnedBoolean = strlessthan(string1, string2)
```

```
returnedBoolean - type: bool

string1 - type: str

string2 - type: str
```

## Returns

True if string1 sorts lexically (alphabetically) before string2, otherwise false.

## Remarks

## Example

```
@CODE
G("first") = strlessthan("apple", "banana");
"output.txt" << G("first") << "\n";
# prints 1 because "apple" sorts before "banana"
@@CODE
```

## See Also

[strgreaterthan](strgreaterthan.md), [String Functions](Table_of_String_Functions.md)
