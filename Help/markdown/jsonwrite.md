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

Only the digits at the end of a name count: `a1b1`, `a1b2` are the array `a1b` with ids `1` and `2`. Adjacent counted siblings with different base names (`item1`, `item2`, `thing1`) make separate arrays. An all-digit name such as `12` is an ordinary object.

One long-standing quirk of the NLP++ original is reproduced exactly, because existing analyzers' output files depend on it: indentation for level *n* is `max(1,n)` steps rather than *n*.

**FIXED 4.2.37:** an array followed by a plain sibling (`item1`, `item2`, `name`) was written with a stray `}` and no comma after the `]`, so the file was not JSON. Adjacent arrays with different base names were merged into one, an array element with no attributes or children ended in a trailing comma, and a name with interior digits was split in the wrong place (`a1b2` became array `a1`, id `12`). `JsonKB` in `KBFuncs.nlp` was fixed the same way, so the two still produce identical output; refresh an analyzer's copy of `KBFuncs.nlp` to get it.

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
