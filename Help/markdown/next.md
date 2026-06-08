[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# next

## Purpose

Fetch the next sibling concept of current concept.

## Syntax

```
returnedConcept = next(currentConcept)
```

```
returnedConcept - type: con

currentConcept - type: con
```

## Returns

Next sibling concept.

## Remarks

If currentConcept is a bad concept, a warning is written to output log. If there is no next sibling of currentConcept, a warning is written to the output log.

## Example

![](../helps/Image%20Files/naveg.gif)

Run the following code using the KB shown above:

```
@CODE

# Find 'mother' in the KB

G("First") = findhierconcept("mother", findroot());

# goto parent concept (female)

G("Second") = up(G("First"));

"output.txt" << conceptname(G("Second")) << "\n";

# go back down to 'mother'

G("First") = down(G("Second"));

"output.txt" << conceptname(G("First")) << "\n";

# find mother's first sibling, which should be 'daughter'

G("Second") = next(G("First"));

"output.txt" << conceptname(G("Second")) << "\n";

# find daughter's previous sibling, which should be mother

G("First") = prev(G("Second"));

"output.txt" << conceptname(G("First")) << "\n";
```

The output should look like:

```
female

mother

daughter

mother
```

## See Also

[prev](prev.md), [down](down.md), [up](up.md), [Knowledge Base Functions](Table_of_Knowledge_Base_Functions.md)
