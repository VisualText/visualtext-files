[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# $text

## Purpose

Fetch the 'cleaned up' text covered by the node. Leading and trailing spaces are removed and separators are converted to single space.

## Syntax

```
returnedString = variableType("$text"[, number])
```

```
returnedString - type: str

variableType - type: N or X

number - type: int
```

## Returns

Returns the cleaned-up text covered by the node as a string, gathered from the original input text buffer.

## Remarks

Uses the original text buffer, rather than the subtree under the node, in order to gather text.

## Example

```
@POST
    "output.txt" << N("$text",1) << "\n";
@@POST

@RULES
_phrase <- _word [plus] @@
```

## See Also

[$treetext]($treetext.md), [$raw]($raw.md), [$treeraw]($treeraw.md), , [$xmltext]($xmltext.md), [phraseraw](phraseraw.md), [phrasetext](phrasetext.md), [Special Variables](NLP_PP_Stuff/Special_Variables.md#table)
