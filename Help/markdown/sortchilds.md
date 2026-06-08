[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# sortchilds

## Purpose

Sort concept's immediate children in alphabetic order.

## Syntax

```
None = sortchilds(aConcept);
```

```
aConcept - type: con
```

## Returns

## Remarks

## Example

L("con") = getconcept(findroot(),"top"); getconcept(L("con"),"32"); getconcept(L("con"),"3"); getconcept(L("con"),"33"); sortchilds(L("con"));

Before sorting, the children of "top" are ordered 32, 3, 33. After sorting, the order is changed to 3, 32, 33.

## See Also

[sorthier](sorthier.md),  [Knowledge Base Functions](Table_of_Knowledge_Base_Functions.md)
