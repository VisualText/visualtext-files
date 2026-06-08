[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# prunephrases

## Purpose

Remove all phrases from a KB subhierarchy.

## Syntax

```
returnedBoolean = prunephrases(hierarchyCon)
```

```
returnedBoolean - type: bool

hierarchyCon - type: con
```

## Returns

Nothing.

## Remarks

Phrases may be used to implement arbitrary sequential knowledge. For example, the Gram Tab implementation utilizes phrases to represent the samples of a rule concept. Each node in the phrase belonging to a rule concept represents one user-highlighted sample. The node's name itself is used to represent the sample's text.

## Example

```
@CODE

# Warning: Exit VisualText without saving, after running this example, or your Gram Tab

# hierarchy will lose all its samples!

G("root") = findroot(); # Get the root concept of the KB.

G("gram") = findconcept(G("root"), "gram"); # Get root of Gram hierarchy.



prunephrases(G("gram")); # Remove all the samples in the Gram hierarchy!

@@CODE
```

## See Also

[Knowledge Base Functions](Table_of_Knowledge_Base_Functions.md)
