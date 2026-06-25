[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# $xmltext

## Purpose

Fetch 'cleaned up' text covered by the node from the text buffer, converting special characters to HTML and XML. Leading and trailing spaces are removed and separators are converted to single space.

## Syntax

```
returnedString = variableType("$xmltext"[, number])
```

```
returnedString - type: str

variableType - type: N or X

number - type: int
```

## Returns

Returns the cleaned-up text covered by the node as a string, the same as $raw but with characters special to HTML and XML converted (e.g., "<" becomes "&lt;").

## Remarks

## Example

"<" is converted to "&lt;".

```
@POST
    "output.xml" << N("$xmltext",1) << "\n";
@@POST

@RULES
_phrase <- _word [plus] @@
```

## See Also

[$treetext]($treetext.md), [$treeraw]($treeraw.md),  [$text]($text.md), [Special Variables](NLP_PP_Stuff/Special_Variables.md#table)
