[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# findroot

## Purpose

Find the root, or top, of the knowledge base (KB). The root is the entry point into the KB for searches and manipulations. There is only one root in the KB, and you can see it in the KB editor labelled **concept**.

## Syntax

```
returnConcept = findroot();
```

```
returnConcept - type: con
```

## Returns

A handle on the newly created concept.

## Remarks

There is one and only one root in the KB. You need to call this function at least once before you can do anything else with the KB. Do not delete the root.

## Example

```
G("the root") = findroot();
```

## See Also

[Knowledge Base Functions](Table_of_Knowledge_Base_Functions.md)
