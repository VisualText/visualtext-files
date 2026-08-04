[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# jsonwrite

## Purpose

Write a knowledge base concept tree to a file as JSON.

## Syntax

```
returnedBool = jsonwrite(fileNameStr, concept)
```

```
returnedBool - type: bool (1,0)

fileNameStr - type: str

concept - type: concept
```

## Returns

1 if the file was written, else 0.

## Remarks

This is the built-in form of the `JsonKB` function in `KBFuncs.nlp`, with the same argument order and **byte-identical output**, so it is a drop-in replacement. `JsonKB` is now a one-line wrapper around it.

Serializing the knowledge base is where a knowledge-base analyzer spends most of its time. Measured on the date-time analyzer, its `output.nlp` — thirteen lines calling `JsonKB` and `SaveKB` — was **43.9%** of total runtime, all of it inside interpreted NLP++. The built-in is roughly **3x faster** on that pass.

A bare filename is written into the current input's log directory, the same place the [output operator](NLP_PP_Stuff/Operators_and_Expressions.md) `<<` writes. An absolute path is used as given.

The serialization is:

| knowledge base | JSON |
| --- | --- |
| a concept | an object |
| an attribute | a `"name": "value"` member |
| counted sibling concepts (`item1`, `item2`, ...) | an array under the shared base name, each element carrying an `"id"` |

Two long-standing quirks of the NLP++ original are reproduced exactly, because existing analyzers' output files depend on them: indentation for level *n* is `max(1,n)` steps rather than *n*, and a concept name containing interior digits is split at the wrong place when deciding whether it is a counted sibling.

## Example

```
@CODE

G("results") = makeconcept(findroot(),"results");
# ... passes accumulate into G("results") ...

jsonwrite("output.json",G("results"));

@@CODE
```

## See Also

[jsonparse](jsonparse.md), [readfile](readfile.md), [makeconcept](makeconcept.md), [Knowledge Base Functions](Table_of_Knowledge_Base_Functions.md)
