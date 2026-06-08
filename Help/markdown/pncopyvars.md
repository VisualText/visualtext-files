[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# pncopyvars

## Purpose

Copy a node's variables to the suggested node of a rule match or to a concept. Must be called from the POST Region and can be considered a new-style NLP++ **action**.

## Syntax

```
NULL = pncopyvars(Pnode1,Pnode2)

NULL = pncopyvars(Pnode1,Pnode2)

NULL = pncopyvars(Pnode1,aConcept)

NULL = pncopyvars(aPnode)

NULL = pncopyvars(positionNum)

NULL = pncopyvars(0)
```

```
aPnode - type: pnode
```

```
positionNum - type: int
```

## Returns

## Remarks

The first form copies variables from node 1 to node 2, or copies from node 1 to a concept in the hierarchy.  The second form copies node variables from a given node. The third form copies variables from the first node matching the positionNumth element of the current rule. The fourth form copies from the node matching the last element of the rule.

## Example

```
@POST

pncopyvars(N(2)); # Copy head _noun variables to _np node.

single();

@RULES

_np <- _det [s] _noun [s] @@
```

## See Also

[POST Actions](NLP_PP_Stuff/AT-POST_Actions.md#table_of_@POST_Actions), [Parse Tree Functions](Table_of_Parse_Tree_Functions.md)
