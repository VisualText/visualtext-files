[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# phraseraw

## Purpose

Fetch the raw text that matched the right-hand side phrase of a rule. This function is analogous to $raw.

## Syntax

```
returnedString = phraseraw()
```

```
returnedString - type: str
```

## Returns

Returns the raw (uncleaned) input text spanned by the nodes that matched the rule's right-hand side. Unlike phrasetext, the text is not whitespace-cleaned. Returns nothing if the rule matched no nodes.

## Remarks

Must appear in a @CHECK or @POST region.

## Example

```
@POST

G("raw") = phraseraw();     # Raw text matched by the whole right-hand side.

@RULES

_np <- _det _noun @@
```

## See Also

[phrasetext](phrasetext.md), [$raw]($raw.md), [$text]($text.md), [$treetext]($treetext.md), [$treeraw]($treeraw.md), [Parse Tree Functions](Table_of_Parse_Tree_Functions.md)
