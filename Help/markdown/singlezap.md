[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# singlezap

## Purpose

Perform a single tier reduction. Excise all the nodes in the matched phrase.

## Syntax

```
singlezap()
```

## Returns

Nothing is returned to NLP++. As a side effect, a single new node (named for the rule's suggested element) replaces the matched phrase, and all of the original matched nodes are excised (removed) from the parse tree.

## Remarks

Useful for things like retokenizing or replacing parse tree nodes with new nodes.

## Example

# Replace the hyphenated "moti-vate" with "motivate". @POST  singlezap(); @RULES motivate <- moti \- vate @@

## See Also

[singlex](singlex.md), [singler](singler.md), [single](single.md), [noop](noop.md), [POST Actions](NLP_PP_Stuff/AT-POST_Actions.md#table_of_@POST_Actions)
