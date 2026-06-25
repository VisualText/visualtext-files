[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# $oend

## Purpose

End offset of the referenced node in the input text.

## Syntax

```
variableType("$oend"[, number])
```

```
variableType - type: N or X

number - type: int
```

## Returns

Returns the end offset of the referenced node in the input text as an integer.

## Remarks

## Example

```
@POST
    "output.txt" << N("$ostart",1) << " - " << N("$oend",1) << "\n";
@@POST

@RULES
_word <- _xWILD [one] @@
```

## See Also

[$ostart]($ostart.md), [Special Variables](NLP_PP_Stuff/Special_Variables.md#table)
