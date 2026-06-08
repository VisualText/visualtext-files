[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# sorthier

## Purpose

Sort concept's subhierarchy in alphabetic order.  Each concept's children in the subhierarchy are ordered alphabetically.

## Syntax

```
None = sorthier(aConcept);
```

```
aConcept - type: con
```

## Returns

## Remarks

## Example

L("con") = getconcept(findroot(),"top"); getconcept(L("con"),"32"); getconcept(L("con"),"3"); getconcept(L("con"),"33");

# Another layer. getconcept(L("33"),"c"); getconcept(L("33"),"b"); getconcept(L("33"),"a"); sortchilds(L("con"));

sorthier(L("con"));

Before sorting, the children of "top" are ordered 32, 3, 33.  The children of 33 are ordered c b a. After sorting, the order is changed to 3, 32, 33 under top, and a b c under 33.

## See Also

[sortchilds](sortchilds.md),   [Knowledge Base Functions](Table_of_Knowledge_Base_Functions.md)
