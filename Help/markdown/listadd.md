[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# listadd

## Purpose

Add a new node to a list node's children. If the item occurs after the list (***olist*** < ***oitem***), it is added as the last child. If the item occurs before the list, it is added as the first child. The optional **keep** arg can be "true" or "false". If "true", it keeps the nodes between the list and the item as children of list. If "false", it excises all the intervening nodes.

## Syntax

```
listadd(olist, oitem[,keep])
```

## Returns

## Remarks

## Example

```
# Add a capitalized word

# to the _caps list, discarding

# the whitespace between them.

@POST

listadd(1,3, "false");

@RULES

_xNIL <- _caps _xWHITE _xCAP @@
```

```
@POST

listadd(3,1,"false");

@RULES

_xNIL <- _xCAP _xWHITE _caps @@
```

## See Also

[POST Actions](NLP_PP_Stuff/AT-POST_Actions.md#table_of_@POST_Actions)
