[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# resubst

## Purpose

Replace regular expression matches in a string.

## Syntax

```
returnedStr = resubst(str, patternStr, replacementStr)
returnedStr = resubst(str, patternStr, replacementStr, flagsStr)
```

```
returnedStr - type: str

str - type: str

patternStr - type: str

replacementStr - type: str

flagsStr - type: str
```

## Returns

The string with every match replaced. Returns no value if the input string is empty or if the result of the replacement is empty.

## Remarks

`resubst` replaces **every** match, where [strsubst](strsubst.md) replaces a fixed substring. Together with the pattern syntax that means one call can do work that previously took a loop.

The replacement string may refer back to the match:

| **FORM** | **MEANING** |
| --- | --- |
| **$1**, **$2** ... | The text of capture group 1, 2 ... |
| **$&** | The whole match |
| **$$** | A literal dollar sign |

Full ECMAScript syntax, as with [rematch](rematch.md). Pass `"i"` as the flags argument to ignore case.

Patterns are compiled once and cached. A malformed pattern or replacement writes a warning to the log and returns no value.

## Example

```
@CODE

# Collapse any run of whitespace to a single blank.
L("clean") = resubst(L("text")," +"," ");

# Normalize line endings so LF and CRLF files compare equal.
L("flat") = resubst(readfile(L("path")),"\r?\n","|");

# Swap the two halves of each token, using backreferences.
# "a1 b2 c3" becomes "1a 2b 3c".
L("swapped") = resubst("a1 b2 c3","([a-z])([0-9])","$2$1");

@@CODE
```

## See Also

[rematch](rematch.md), [refind](refind.md), [strsubst](strsubst.md), [strclean](strclean.md), [String Functions](Table_of_String_Functions.md)
