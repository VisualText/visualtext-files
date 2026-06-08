[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# split

## Purpose

Split a string into pieces using a separator character.

## Syntax

```
returnedArray = str(str, charString)
```

```
returnedArray - type: array of str
```

```
str - type: str
```

```
charString - type: str
```

## Returns

An array of strings, each of which is a component of the given string.

## Remarks

Similar to the Perl *split* function.

## Example

@CODE

L("arr") = split("ab|cd|efg", "|");

"output.txt" << L("arr") << "\n";

"output.txt" << L("arr")[2] << "\n";

prints out:

ab cd efg

efg

## See Also

[String Functions](Table_of_String_Functions.md)
