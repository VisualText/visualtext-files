# rmattr

## Purpose

Remove the named attribute *attrNameStr* (and its values) of a concept *aConcept*.

## Syntax

```
returnedBoolean = rmattr(aConcept, attrNameStr)
```

```
returnedBoolean - type: bool

aConcept - type: con

attrNameStr - type: str
 
```

## Returns

1 if removed, 0 otherwise.

## Remarks

Removes named attribute of the given concept. Differs from `rmattrs` in that `rmattrs` removes all attributes of the argument concept, while `rmattr` removes only the specified attribute .

## Example

This example creates the concept apple, then creates two attributes of apple, then deletes both of them. Finally, we add both of the attributes back and then delete only one.

```
if(findconcept(findroot(), "apples"))

rmconcept(findconcept(findroot(), "apples"));

G("apples") = makeconcept(findroot(), "apples");

addstrval(G("apples"), "color", "red");

addstrval(G("apples"), "taste", "good");
```

```
# remove all attributes

rmattrs(G("apples"));

addstrval(G("apples"), "color", "red");

addstrval(G("apples"), "taste", "good");
```

```
# only remove named attribute

rmattr(G("apples"),"color");
```

The KB Editor should look like this:

```
![](../helps/KB_Functions_Images/rmattrs_kb.gif)
```

## See Also

[rmattrs](rmattrs.md), [Knowledge Base Functions](Table_of_Knowledge_Base_Functions.md)
