[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# rmconcept

## Purpose

Remove a concept from the Knowledge Base.

## Syntax

```
NULL = rmconcept(concept)
```

```
concept - type: con
```

## Returns

Nothing

## Remarks

Removes concept and its entire subhierarchy.  If a bad concept is passed (e.g., a string, not a handle to a concept), an NLP++ error is thrown and is written to the output log.

## Example

```
G("myConcept") = makeconcept(findroot(),"a concept");

rmconcept(G("myConcept"));
```

## See Also

[rmchild](rmchild.md), [rmchildren](rmchildren.md), [rmword](rmword.md), [Knowledge Base Functions](Table_of_Knowledge_Base_Functions.md)
