[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# sortattrs

## Purpose

Sort a concept's attributes alphabetically by name.

## Syntax

```
returnedNum = sortattrs(aConcept);
```

```
returnedNum - type: int
aConcept - type: con
```

## Returns

1 if the sort succeeded, 0 otherwise.

## Remarks

Names are compared the way [sortchilds](sortchilds.md) compares child concepts, so the order ignores case. Each attribute keeps its values in their original order. Only the order in which the attributes are listed changes, so the order [findattrs](findattrs.md) and [nextattr](nextattr.md) walk them in, and the order they are saved in. Looking an attribute up by name gives the same result before and after.

**NEW 4.2.21**

## Example

```
@CODE
L("con") = makeconcept(findroot(), "word");
addstrval(L("con"), "zeta", "z");
addstrval(L("con"), "alpha", "2");
addstrval(L("con"), "alpha", "1");
addstrval(L("con"), "Mid", "m");
sortattrs(L("con"));
```

Before sorting, the attributes are listed as `zeta`, `alpha`, `Mid`. After sorting, they are `alpha`, `Mid`, `zeta`, and `alpha` still has the values `2`, `1` in that order.

## See Also

[sortchilds](sortchilds.md), [sorthier](sorthier.md), [findattrs](findattrs.md), [Knowledge Base Functions](Table_of_Knowledge_Base_Functions.md)
