[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# split

## Purpose

Split a string into pieces using a separator character.

## Syntax

```
returnedArray = split(str, charString)
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

Similar to the Perl *split* function. Each character in *charString* is a delimiter.

With an empty *charString*, `split` returns the string's characters: `split("héllo", "")` is `h`, `é`, `l`, `l`, `o`. Characters are whole characters, not bytes, so an accented letter or emoji stays one element. **NEW 4.2.15** (it used to be an error).

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
