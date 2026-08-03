[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# refind

## Purpose

Find a regular expression match and its capture groups.

## Syntax

```
returnedArray = refind(str, patternStr)
returnedArray = refind(str, patternStr, flagsStr)
```

```
returnedArray - type: str array

str - type: str

patternStr - type: str

flagsStr - type: str
```

## Returns

An array in which element 0 is the whole match and elements 1..n are the capture groups, in the order their opening parentheses appear in the pattern. Returns an empty array if the pattern does not match.

## Remarks

This is how a pass pulls pieces **out** of a string. Before `refind`, extracting something like the digits after a dash meant walking the string a character at a time with [strchar](strchar.md).

Only the **first** match is returned. A group that took part in no match, such as an unmatched alternative or an optional group that did not fire, comes back as an empty element.

Full ECMAScript syntax, as with [rematch](rematch.md). Pass `"i"` as the flags argument to ignore case.

Test the result before indexing it. Check the **first element**, not the count: assigning an empty array to a variable collapses it back to no value, and [arraylength](arraylength.md) reports 1 for a variable holding no value, so a count test would read 1 on a failed match.

```
L("g") = refind(L("s"),"([a-z]+)-([0-9]+)");
if (strlength(L("g")[0])) {
    L("word") = L("g")[1];
    L("num")  = num(L("g")[2]);
}
```

Calling [rematch](rematch.md) with the same pattern is an equally good guard, and costs little because the compiled pattern is cached and shared between the two calls.

Patterns are compiled once and cached. A malformed pattern writes a warning to the log and returns no value.

## Example

```
@CODE

# Pull the key and value out of a "name = widget" configuration line.
L("g") = refind(L("line"),"^([a-z]+) *= *(.+)$");

if (strlength(L("g")[0])) {
    "out.txt" << "key="   << L("g")[1]
              << " value=" << L("g")[2] << "\n";
}

@@CODE
```

## See Also

[rematch](rematch.md), [resubst](resubst.md), [split](split.md), [strpiece](strpiece.md), [String Functions](Table_of_String_Functions.md)
