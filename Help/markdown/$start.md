[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# $start

## Purpose

Check if the referenced node has a left sibling in the parse tree.

## Syntax

```
returnedBoolean = variableType("$start"[, number])
```

```
returnedBoolean - type: bool

variableType - type: N or X

number - type: int
```

## Returns

Evaluates to **0** if the node has a left sibling and **1 **if the referenced node does not have a left sibling.

## Remarks

## Example

```
@POST
    if (N("$start",1))
        N("firstchild",1) = 1;
@@POST

@RULES
_word <- _xWILD [one] @@
```

## See Also

[$end]($end.md), [Special Variables](NLP_PP_Stuff/Special_Variables.md#table)
