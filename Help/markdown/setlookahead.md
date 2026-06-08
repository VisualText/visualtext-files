[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# setlookahead

## Purpose

Dynamically set the next node that the rule matcher will look at, after the current rule match is done.

## Syntax

```
setlookahead(ord_num)
```

## Returns

True if successful, else false.

## Remarks

The [lookahead](lookahead.md) element modifier is static, while the setlookahead function allows dynamic and conditional setting of the lookahead node.  The function overrides the lookahead modifier.  To avoid confusion, we recommend not using both in the same rule.

Not a reduce action per se, but works in tandem with reduce actions.

## Example

```
@POST

if (N(3))

 single();

else

 {

 # Discard the comma match,if any.

 setlookahead(2);

 singler(1,1);

 }

@RULES

_namewtitle <-

 Smith

 \, [opt]

 CEO [opt]

 @@
```

## See Also

[lookahead](lookahead.md) element modifier

[POST Actions](NLP_PP_Stuff/AT-POST_Actions.md#table_of_@POST_Actions)
