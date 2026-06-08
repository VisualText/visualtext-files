# regexpi

## Purpose

Match text to a regular expression pattern (case insensitive).

## Syntax

```
<fromRuleEltNumber,toRuleEltNumber>regexpi(patternStr);
```

```
fromRuleEltNumber - type: int

toRuleEltNumber - type: int

patternStr - type: string
```

## Returns

Succeeds if the pattern matches, else fails.

## Remarks

A pattern consists of text and the special characters ? and *. ? matches any single character, and * matches any zero or more characters.  (There is no way to currently escape ? and *).  Matching is case insensitive.

## Example

# This will match words such as JUNK, junks, junky, JunkYard. @PRE <1,1> regexpi("junk*"); @POST group(1,1,"_junkword"); @RULES _xNIL <- _xALPHA @@

## See Also

[regexp](regexp.md), [PRE Actions](NLP_PP_Stuff/AT-PRE_Actions.md)
