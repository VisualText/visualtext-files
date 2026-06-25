[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# $end

## Purpose

Check if the referenced node has a right sibling in the parse tree.

## Syntax

```
returnedBoolean = variableType("$end"[, number])
```

```
returnedBoolean - type: bool

variableType - type: N or X

number - type: int
```

## Returns

Evaluates to **0** if the node has a right sibling and **1 **if the referenced node does not have a right sibling.

## Remarks

## Example

```
@POST
    if (N("$end",1))
        N("lastchild",1) = 1;
@@POST

@RULES
_word <- _xWILD [one] @@
```

## See Also

[$start]($start.md), [Special Variables](NLP_PP_Stuff/Special_Variables.md#table)
