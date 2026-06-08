[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# regexp

## Purpose

Match text to a regular expression pattern.

## Syntax

```
<fromRuleEltNumber,toRuleEltNumber>regexp(patternStr);
```

```
fromRuleEltNumber - type: int

toRuleEltNumber - type: int

patternStr - type: string
```

## Returns

Succeeds if the pattern matches, else fails.

## Remarks

A pattern consists of text and the special characters ? and *. ? matches any single character, and * matches any zero or more characters.  (There is no way to currently escape ? and *).  Matching is case sensitive.

## Example

# This will match words such as junk, junks, junky, junkyard. @PRE <1,1> regexp("junk*"); @POST group(1,1,"_junkword"); @RULES _xNIL <- _xALPHA @@

## See Also

[regexpi](regexpi.md), [PRE Actions](NLP_PP_Stuff/AT-PRE_Actions.md)
