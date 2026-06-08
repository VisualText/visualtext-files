# singlezap

## Purpose

Perform a single tier reduction. Excise all the nodes in the matched phrase.

## Syntax

```
singlezap()
```

## Returns

## Remarks

Useful for things like retokenizing or replacing parse tree nodes with new nodes.

## Example

# Replace the hyphenated "moti-vate" with "motivate". @POST  singlezap(); @RULES motivate <- moti \- vate @@

## See Also

[singlex](singlex.md), [singler](singler.md), [single](single.md), [noop](noop.md), [POST Actions](NLP_PP_Stuff/AT-POST_Actions.md#table_of_@POST_Actions)
