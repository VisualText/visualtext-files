[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# lasteltnode

## Purpose

Fetch the last node that matched the nth element of a rule.

## Syntax

```
returnedPnode = lasteltnode(elt_num)
```

```
returnedPnode - type: pnode

elt_num - type: int             Nth element of the rule
```

## Returns

Returns the last parse tree node that matched the elt_numth element of the current rule. Returns nothing if that element matched no nodes (for example, an optional element that was skipped).

## Remarks

Must appear in a @CHECK or @POST region. The element number must be greater than zero. Use [eltnode](eltnode.md) to fetch the first node that matched an element.

## Example

```
@POST

L("last") = lasteltnode(2);     # Last node matched by the 2nd rule element.

@RULES

_np <- _det _noun [plus] @@
```

## See Also

[eltnode](eltnode.md), [phrasetext](phrasetext.md), [Parse Tree Functions](Table_of_Parse_Tree_Functions.md)
