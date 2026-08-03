[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# rematch

## Purpose

Test a string against a regular expression.

## Syntax

```
returnedBool = rematch(str, patternStr)
returnedBool = rematch(str, patternStr, flagsStr)
```

```
returnedBool - type: bool (1,0)

str - type: str

patternStr - type: str

flagsStr - type: str
```

## Returns

1 if the pattern matches, else 0.

## Remarks

`rematch` uses full ECMAScript regular expression syntax, so character classes, anchors, quantifiers, alternation and groups all work. This is not the case for the older [regexp](regexp.md), which is a `*`/`?` glob, understands no other metacharacter, and can only be written in a `@PRE` region. `rematch` is an ordinary function and can be called anywhere NLP++ code can be written.

`rematch` **searches** the string: the pattern may match anywhere inside it. Anchor with `^` and `$` to require the whole string to match.

Pass `"i"` as the flags argument to ignore case. It is the only flag defined; anything else is an error.

Patterns are compiled once and cached, so calling `rematch` from inside a rule loop does not recompile the pattern on every node.

A malformed pattern writes a warning to the log and yields 0 rather than aborting the pass.

## Example

```
@CODE

# Anchored, so the whole token must be an ISBN-looking string.
if (rematch(N("$text"),"^[0-9]{3}-[0-9]{10}$")) {
    N("isbn") = 1;
}

# Unanchored search, ignoring case.
if (rematch(L("line"),"error|warning","i")) {
    G("problems")++;
}

@@CODE
```

## See Also

[refind](refind.md), [resubst](resubst.md), [regexp](regexp.md), [strcontains](strcontains.md), [String Functions](Table_of_String_Functions.md)
