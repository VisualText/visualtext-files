# rmchildren

## Purpose

Remove all children of a concept *parentCon*.

## Syntax

```
returnedBoolean = rmchildren(parentCon)
```

```
returnedBoolean - type: boolean

parentCon - type: con
```

## Returns

1 if parentCon has the children concepts that are removed, 0 otherwise.

## Remarks

Differs from `rmchild` in that `rmchild` deletes a named child concept, while `rmchildren` deletes all children of argument concept.

## Example

This example creates two children concepts then deletes them both. Then it creates them again and deletes one by name:

```
if(findconcept(findroot(),"a concept"))

rmconcept(findconcept(findroot(),"a concept"));

G("aParent")= makeconcept(findroot(),"a concept")

G("aChild") = makeconcept(G("aParent"),"a child");

G("aChild") = makeconcept(G("aParent"),"a sibling");

rmchildren(G("aParent"));

G("aChild") = makeconcept(G("aParent"),"a child");

G("aChild") = makeconcept(G("aParent"),"a sibling");

rmchild(G("aParent"),"a sibling");
```

## See Also

[rmchild](rmchild.md), [rmconcept](rmconcept.md), [Knowledge Base Functions](Table_of_Knowledge_Base_Functions.md)
