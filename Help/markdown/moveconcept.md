[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# moveconcept

## Purpose

Move a concept, with all its children, attributes and phrase, so that it becomes the last child of another concept.

## Syntax

```
returnedConcept = moveconcept(aConcept, newParent);
```

```
returnedConcept - type: con
aConcept - type: con
newParent - type: con
```

## Returns

The moved concept, or 0 if it was not moved.

## Remarks

The concept is moved, not copied. Everything under it comes along, and variables that already point to it, or to anything under it, still do.

Nothing is changed, and 0 is returned, when:

- *aConcept* is the root of the knowledge base;
- *newParent* is *aConcept* itself or one of its descendants;
- *newParent* already has a child with *aConcept*'s name.

Moving a concept within its current parent makes it that parent's last child. To move a concept one place among its siblings, use [movecleft](movecleft.md) or [movecright](movecright.md).

**NEW 4.2.21**

## Example

```
@CODE
L("top") = makeconcept(findroot(), "top");
L("a") = makeconcept(L("top"), "a");
L("b") = makeconcept(L("a"), "b");
makeconcept(L("b"), "b1");
L("c") = makeconcept(L("top"), "c");

moveconcept(L("b"), L("c"));
"output.txt" << conceptpath(findconcept(L("b"), "b1")) << "\n";
```

This writes `"concept" "top" "c" "b" "b1"`: `b` and its child `b1` are now under `c`, and `a` has no children.

## See Also

[movecleft](movecleft.md), [movecright](movecright.md), [renameconcept](renameconcept.md), [Knowledge Base Functions](Table_of_Knowledge_Base_Functions.md)
