[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# $raw

## Purpose

Fetch 'cleaned up' text covered by the node from the text buffer. Leading and trailing spaces are removed and separators are converted to single space.

## Syntax

```
returnedString = variableType("$raw"[, number])
```

```
returnedString - type: str

variableType - type: N or X

number - type: int
```

## Returns

Returns the cleaned-up text covered by the node as a string, gathered from the input text buffer.

## Remarks

## Example

```
@POST
    "output.txt" << N("$raw",1) << "\n";
@@POST

@RULES
_phrase <- _word [plus] @@
```

## See Also

[$treetext]($treetext.md), [$treeraw]($treeraw.md),  [$text]($text.md), [$xmltext]($xmltext.md), [phraseraw](phraseraw.md), [phrasetext](phrasetext.md), [Special Variables](NLP_PP_Stuff/Special_Variables.md#table)
