[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# $ostart

## Purpose

Start offset of the referenced node in the input text.

## Syntax

```
variableType("$ostart"[, number])
```

```
variableType - type: N or X

number - type: int
```

## Returns

Returns the start offset of the referenced node in the input text as an integer.

## Remarks

## Example

```
@POST
    "output.txt" << N("$ostart",1) << "\n";
@@POST

@RULES
_word <- _xWILD [one] @@
```

## See Also

[$oend]($oend.md), [Special Variables](NLP_PP_Stuff/Special_Variables.md#table)
