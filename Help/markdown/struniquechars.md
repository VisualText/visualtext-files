[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# struniquechars

## Purpose

Find all the unique characters in a string.

## Syntax

```
returnedString = strpiece(string)
```

```
returnedString - type: str
endNumber - type: int
```

## Returns

Return a string of all the unique characters in a string. They are returned in the order they are found.

## Remarks

## Example

```
@CODE
G("uniq") = struniquechars("mississippi");
"output.txt" << G("uniq") << "\n";
# Writes "misp"
@@CODE
```

## See Also

[strsubst](strsubst.md), [strcontains](strcontains.md), [strcontainsnocase](strcontainsnocase.md), [strendswith](strendswith.md), [strendswith](strendswith.md), [String Functions](Table_of_String_Functions.md)
