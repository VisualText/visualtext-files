[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# $treetext

## Purpose

Fetch 'cleaned up' text gleaned from a node's subtree. Leading and trailing spaces are removed and separators are converted to single space.

## Syntax

```
returnedString = variableType("$treetext"[, number])
```

```
returnedString - type: str

variableType - type: N or X

number - type: int
```

## Returns

## Remarks

Uses the parse tree as input, not text buffer. $treetext is analogous to $text. The difference between $treetext and $text is $text returns text from the input text buffer while $treetext returns text from the parse tree. If you have removed some nodes from a tree with an excise(), $treetext returns the text minus the excised elements, while $text returns everything in the input text buffer, including the text under excised nodes.

## Example

```
@POST





@@POST
```

```
@RULES
```

```
@@RULES
```

## See Also

[$text]($text.md), [$treeraw]($treeraw.md), [$raw]($raw.md), , [$xmltext]($xmltext.md), [phraseraw](phraseraw.md), [phrasetext](phrasetext.md), [Special Variables](NLP_PP_Stuff/Special_Variables.md#table)
