[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# eltnode

## Purpose

Fetch the first node that matched the nth element of a rule.

## Syntax

```
returnedPnode = eltnode(elt_num)
```

```
returnedPnode - type: pnode

elt_num - type: int          Nth element number
```

## Returns

Returns the first parse tree node that matched the elt_numth element of the current rule. Returns nothing if that element matched no nodes (for example, an optional element that was skipped).

## Remarks

Must appear in a @CHECK or @POST region. The element number must be greater than zero. Use [lasteltnode](lasteltnode.md) to fetch the last node that matched an element.

## Example

```
@POST

L("first") = eltnode(2);     # First node matched by the 2nd rule element.

@RULES

_np <- _det _noun @@
```

## See Also

[lasteltnode](lasteltnode.md), [varinlist](varinlist.md), [Parse Tree Functions](Table_of_Parse_Tree_Functions.md)
