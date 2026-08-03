[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

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

A pattern consists of text and the special characters ? and *. ? matches any single character, and * matches any zero or more characters.  (There is no way to currently escape ? and *).  Matching is case insensitive, for every element of the pattern.

The pattern must match the **whole** string, not a part of it. `regexpi("RUN")` does not match `running`, and `regexpi("AT")` does not match `cat`. Wrap the pattern in stars to search inside a word: `regexpi("*AT*")` matches `cat`.

## Example

# This will match words such as JUNK, junks, junky, JunkYard. @PRE <1,1> regexpi("junk*"); @POST group(1,1,"_junkword"); @RULES _xNIL <- _xALPHA @@

For a full regular expression — character classes, anchors, quantifiers, alternation and capture groups — and one that can be called from anywhere rather than only from a `@PRE` region, see [rematch](rematch.md) with the `"i"` flag, plus [refind](refind.md) and [resubst](resubst.md).

## See Also

[regexp](regexp.md), [rematch](rematch.md), [refind](refind.md), [resubst](resubst.md), [PRE Actions](NLP_PP_Stuff/AT-PRE_Actions.md)
