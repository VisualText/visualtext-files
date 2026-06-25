[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# strsubst

## Purpose

Replace substring of a string with a newstring.

## Syntax

```
returnedString = strsubst(string, oldString, newString)
```

```
returnedString - type: str

string - type: str

oldString - type: str

newString - type: str
```

## Returns

A copy of `string` with occurrences of oldString replaced by newString.

## Remarks

## Example

```
@CODE
G("fixed") = strsubst("a-b-c", "-", "_");
"output.txt" << G("fixed") << "\n";
# Writes "a_b_c"
@@CODE
```

## See Also

[strpiece](strpiece.md), [strcontains](strcontains.md), [strcontainsnocase](strcontainsnocase.md), [strendswith](strendswith.md), [strendswith](strendswith.md), [String Functions](Table_of_String_Functions.md)
