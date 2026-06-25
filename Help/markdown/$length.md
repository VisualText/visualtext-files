[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# $length

## Purpose

Get the length of node's text.

## Syntax

```
returnedNumber = variableType("$length"[, number])
```

```
returnedNumber - type: int

variableType - type: N or X

number - type: int
```

## Returns

Returns the length of the node's text as an integer.

## Remarks

## Example

```
@POST
    if (N("$length",1) > 3)
        N("long",1) = 1;
@@POST

@RULES
_word <- _xWILD [one] @@
```

## See Also

[Special Variables](NLP_PP_Stuff/Special_Variables.md#table)
