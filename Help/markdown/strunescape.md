[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# strunescape

## Purpose

Unescape the characters in a string.  In strunescape syntax, **str** is an input string, **escapedCharsStr** is a string of chars to unescape when found in str, and **escapeStr** is a one character string that is used as the escape character.

## Syntax

```
returnedString = strunescape(str,
 escapedCharsStr, escapeStr)
```

```
    returnedString
 - type:  str

```

```
    str
 - type:  str

```

```
    escapedCharsStr
 - type:  str

```

```
    escapeStr
 - type:  str

```

## Returns

The string with the escape character removed from before each occurrence of any character listed in escapedCharsStr.

## Remarks

Unescaping removes the escape char preceding each instance of the escaped chars.

## Example

```
@CODE
G("out") = strunescape("a\\,b\\,c", ",", "\\");
"output.txt" << G("out") << "\n";
# writes: a,b,c
@@CODE
```

## See Also

[strescape](strescape.md)
