[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# $treeraw

## Purpose

Fetch the text covered by the node from the parse tree. Leading and trailing spaces are not removed and separators are not converted to single space.

## Syntax

```
returnedString = variableType("$treeraw"[, number])
```

```
returnedString - type: str

variableType - type: N or X

number - type: int
```

## Returns

Returns the text covered by the node from the parse tree as a string, without cleanup of leading/trailing spaces or separators.

## Remarks

Analogous to $treetext.

## Example

```
@POST
    "output.txt" << N("$treeraw",1) << "\n";
@@POST

@RULES
_phrase <- _word [plus] @@
```

## See Also

[$treetext]($treetext.md), [$text]($text.md), [$raw]($raw.md), , [$xmltext]($xmltext.md), [phraseraw](phraseraw.md), [phrasetext](phrasetext.md), [Special Variables](NLP_PP_Stuff/Special_Variables.md#table)
