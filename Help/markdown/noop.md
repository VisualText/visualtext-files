[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# noop

## Purpose

Perform no POST Action. This is a convenience to disable the default **single()** reduce action.

## Syntax

```
noop()
```

## Returns

Nothing is returned to NLP++, and no action is performed on the parse tree. Its only effect is to mark the rule as a no-op so that the default **single()** reduce does not run, leaving the matched nodes unchanged.

## Remarks

## Example

# Increment the count of nouns, # without reducing _noun to anything. @CHECK ++G("noun count"); @POST  noop();  # If absent, then _noun will reduce to _xNIL. @RULES _xNIL <- _noun @@

## See Also

[single](single.md), [POST Actions](NLP_PP_Stuff/AT-POST_Actions.md#table_of_@POST_Actions)
