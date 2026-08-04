[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# jsonparse

## Purpose

Parse a JSON document into knowledge base concepts.

## Syntax

```
returnedBool = jsonparse(jsonStr, parentConcept)
```

```
returnedBool - type: bool (1,0)

jsonStr - type: str

parentConcept - type: concept
```

## Returns

1 if the document parsed, else 0.

## Remarks

The inverse of [jsonwrite](jsonwrite.md). The members of the JSON object become children and attributes of parentConcept.

Pair it with [readfile](readfile.md) to load a file:

```
jsonparse(readfile(G("$apppath") + "/data/config.json"), G("kb"));
```

Before this existed, the way to get JSON into an analyzer was the `json2kbb` Python library pass, which converts `kb/user/*.json` to `.kbb` before the tokenizer. That still works, but it requires Python on the machine — which the npm and pypi distributions of the engine do not provide — and it will not overwrite an existing `.kbb`, so editing the `.json` appears to do nothing until you delete the `.kbb`. `jsonparse` has neither problem.

The mapping is the one `json2kbb` documents:

| JSON | knowledge base |
| --- | --- |
| an object | a concept |
| `"key": <primitive>` | an attribute `key=value` |
| `"key": { ... }` | a child concept named `key` |
| `"key": [ ... ]` | counted children `key1`, `key2`, ... |
| a primitive array element | `keyN` with a `value` attribute |

An integer becomes a num, a number containing `.`, `e` or `E` becomes a float, `true` and `false` become 1 and 0, and `null` becomes an empty string. String escapes are resolved, including `\uXXXX` with surrogate pairs combined.

A top-level object is required, and trailing content after it is an error, so a truncated or doubled document is reported rather than half-loaded. Inside an array element, an `"id"` member is skipped: [jsonwrite](jsonwrite.md) generates it from the concept's name, so keeping it would duplicate it on the next write.

## Example

```
@CODE

L("text") = readfile(G("$apppath") + "/data/settings.json");
G("cfg")  = makeconcept(findroot(),"cfg");

if (jsonparse(L("text"),G("cfg"))) {
    G("threshold") = numval(findvals(findconcept(G("cfg"),"tuning"),"threshold"));
}

@@CODE
```

## See Also

[jsonwrite](jsonwrite.md), [readfile](readfile.md), [makeconcept](makeconcept.md), [Knowledge Base Functions](Table_of_Knowledge_Base_Functions.md)
