[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# single

## Purpose

Perform the DEFAULT single tier reduction. This reduces the entire set of nodes that matched a rule phrase.

## Syntax

```
single()
```

## Returns

## Remarks

## Example

# Since @POST is non-empty, you must explicitly specify reduction. @POST  ++G("nouns");  single();  # NEEDED, or computer will not reduce to _noun. @RULES _noun <- computer @@ # In this case, @POST is empty, so single() occurs by default. @POST @RULES _noun <- sheep @@

## See Also

[singler](singler.md), [singlex](singlex.md), [singlezap](singlezap.md), [noop](noop.md), [POST Actions](NLP_PP_Stuff/AT-POST_Actions.md#table_of_@POST_Actions)
