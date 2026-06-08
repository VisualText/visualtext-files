[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# rmchild

## Purpose

Remove a concept's child by name or by number.

## Syntax

```
returnedBoolean = rmchild(parentCon, childConceptNameStr)
```

```
returnedBoolean - type: bool

parentCon - type: con

childConceptNameStr - type: str
```

```
returnedBoolean = rmchild(parentCon, childConceptNumber)
```

```
returnedBoolean - type: bool

parentCon - type: con

childConceptNumber - type: int
```

## Returns

1 if parentCon has the child concept and it is removed, 0 otherwise.

## Remarks

This is a dangerous function in that you can inadvertently remove pieces of your brain with it. Be very careful not to delete parts of the KB you didn't mean to, because this will lead to loss of analyzer integrity. For example, you could remove the gram or sys concepts.

Child concepts are rank ordered by birth order, unless re-arranged. Indexing starts at 1. Passing numerical argument 0 selects the last child concept. If you try to index outside of the range of children concepts, a warning is written to the output log and the function returns 0. If a bad concept is passed (e.g., a string, not a handle to a concept), an NLP++ error is thrown and is written to the output log.

Differs from `rmchildren` in that `rmchild` deletes a named child, while `rmchildren` deletes all children.

## Example

This example creates and deletes a child concept by name:

```
G("myConcept") = makeconcept(findroot(),"a concept");

G("result") = rmchild(G("myConcept"),"a concept");
```

This one does it by number:

```
G("aParent")= makeconcept(findroot(),"a concept")

G("aChild") = makeconcept(G("aParent"),"a child");

G("result") = rmchild(G("aParent"),1);
```

## See Also

[rmchildren](rmchildren.md), [rmconcept](rmconcept.md), [Knowledge Base Functions](Table_of_Knowledge_Base_Functions.md)
