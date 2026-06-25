[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# strgreaterthan

## Purpose

Check if string 1 is lexically after string 2.

## Syntax

```
returnedBoolean = strgreaterthan(string1, string2)
```

```
returnedBoolean - type: bool

string1 - type: str

string2 - type: str
```

## Returns

True if string1 sorts lexically (alphabetically) after string2, otherwise false.

## Remarks

## Example

```
@CODE
G("after") = strgreaterthan("banana", "apple");
"output.txt" << G("after") << "\n";
# prints 1 because "banana" sorts after "apple"
@@CODE
```

## See Also

[strlessthan](strlessthan.md), [String Functions](Table_of_String_Functions.md)
