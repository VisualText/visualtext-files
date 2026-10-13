[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# rmchars

## Purpose

Remove every occurrence of a set of characters from a string.

## Syntax

```
returnedString = rmchars(string, charsString)
```

```
returnedString - type: str

string - type: str

charsString - type: str
```

## Returns

*string* with every character that appears in *charsString* removed. If *charsString* is empty, *string* is returned unchanged.

## Remarks

Each character of *charsString* is removed wherever it occurs; order doesn't matter. Characters are whole characters, not bytes: `rmchars("héllo", "é")` is `hllo`.

To remove a multi-character substring instead, use [strsubst](strsubst.md) with an empty replacement.

**NEW 4.2.15**

## Example

```
@CODE
"output.txt" << rmchars("(555) 867-5309", "()- ") << "\n";
# Writes 5558675309
@@CODE
```

## See Also

[strsubst](strsubst.md), [split](split.md), [strclean](strclean.md), [String Functions](Table_of_String_Functions.md)
