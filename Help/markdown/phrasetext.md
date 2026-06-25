[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# phrasetext

## Purpose

Fetch the text that matched the right-hand side phrase of a rule. This function is analogous to $text.

## Syntax

```
returnedString = phrasetext()
```

```
returnedString - type: str
```

## Returns

Returns the cleaned-up text spanned by the nodes that matched the rule's right-hand side. Returns nothing if the rule matched no nodes.

## Remarks

Must appear in a @CHECK or @POST region.

## Example

```
@POST

G("text") = phrasetext();     # Text matched by the whole right-hand side.

@RULES

_np <- _det _noun @@
```

## See Also

[phraseraw](phraseraw.md), [$raw]($raw.md), [$text]($text.md), [$treetext]($treetext.md), [$treeraw]($treeraw.md), [Parse Tree Functions](Table_of_Parse_Tree_Functions.md)
