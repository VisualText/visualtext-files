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

## Remarks

Uses the original text buffer, rather than the subtree under the node, in order to gather text.

## Example

```
@RULES
```

```
@@RULES
```

## See Also

[$treetext]($treetext.md), [$raw]($raw.md), [$treeraw]($treeraw.md), , [$xmltext]($xmltext.md), [phraseraw](phraseraw.md), [phrasetext](phrasetext.md), [Special Variables](NLP_PP_Stuff/Special_Variables.md#table)
