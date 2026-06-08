# pathconcept

## Purpose

Fetch concept given its string path.

## Syntax

```
returnedConcept = pathconcept(pathString)
```

```
returnedConcept - type: con

pathString - type: str
```

## Returns

Concept.

## Remarks

If pathString does not 'point to' a concept, function returns NULL. If pathString is not a string, a warning is written to the output log window.

## Example

```
if (findconcept(findroot(),"parent"))

rmconcept(findconcept(findroot(),"parent"));

G("childConcept") = makeconcept(makeconcept(findroot(),"parent"),"child");

G("the path") = conceptpath(G("childConcept"));

"output.txt" << "The path is: " << G("the path") << "\n";

G("the concept") = pathconcept(G("the path"));

"output.txt" << "The concept is: " << conceptname(G("the concept")) << "\n";

G("garbage") = pathconcept("foo bar");

"output.txt" << "garbage is: " << G("garbage");
```

Writes the following to output.txt:

```
The path is: "concept" "parent" "child"

The concept is: child

garbage is: 0
```

## See Also

[conceptpath](conceptpath.md), [Knowledge Base Functions](Table_of_Knowledge_Base_Functions.md)
