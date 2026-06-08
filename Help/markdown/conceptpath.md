# conceptpath

## Purpose

Fetch entire path of given concept as a string.

## Syntax

```
returnedString = conceptpath(concept)
```

```
returnedString - type: str

concept - type: con
```

## Returns

Path of concept as a string.

## Remarks

If the concept is bad, an error appears in the output log window.

## Example

```
G("childConcept") = makeconcept(makeconcept(findroot(), "parent"), "child");

"output.txt" << conceptpath(G("childConcept"));
```

Writes the following to output.txt:

```
"concept" "parent" "child"
```

## See Also

[attrname](attrname.md), [findwordpath](findwordpath.md), [wordpath](wordpath.md), [Knowledge Base Functions](Table_of_Knowledge_Base_Functions.md)
