[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# pnsingletdown

## Purpose

Fetch the child of a parse tree node, obeying rules about going down a "singlet chain." That is, get child only if no branching and if not going down past node with BASE flag set.

## Syntax

```
returnedPnode = pnsingletdown(aPnode)
```

```
returnedPnode - type: pnode

aPnode - type: pnode
```

## Returns

Returns the child reached by descending the "singlet chain" below the node. Descent stops (and returns nothing further) at branching, or at a node whose BASE flag is set. Returns nothing if there is no such child.

## Remarks

## Example

```
# Example shows a way to "layer" semantics in parse tree.

@POST

  G("last") = lasteltnode(4);               # Get last noun node.

  G("noun sem") = pnsingletdown(G("last")); # Get semantic node under _noun.

  if (G("noun sem")                         # If got a semantic guy, eg "_house",

      && (G("name") = pnname(G("noun sem")))# (and get the name of the node)

      && strchr(G("noun sem"),"_") )        # and it's nonliteral.

     {

     group(1,4,G("name"));                  # "Promote" the sem, eg, "_house".

     group(1,1,"_np");  # Now layer on the np.  Note numbering has changed.

     }

  else

     group(1,4,"_np");        # No semantic guy, just build noun phrase.

@RULES

_xNIL <- _det [s] _quan [s] _adj [s plus] _noun [s plus] @@
```

## See Also

[pndown](pndown.md), [pnup](pnup.md), [pnprev](pnprev.md), [pnnext](pnnext.md), [Parse Tree Functions](Table_of_Parse_Tree_Functions.md)
