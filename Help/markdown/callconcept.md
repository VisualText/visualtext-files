[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# callconcept

## Purpose

In an analyzer run by [callanalyzer](callanalyzer.md), get the concept it was given for its results.

## Syntax

```
returnedConcept = callconcept()
```

```
returnedConcept - type: concept
```

## Returns

The concept passed to [callanalyzer](callanalyzer.md) by the analyzer that called this one.

When the analyzer is not being called, it returns the concept named `callanalyzer` under the root of the knowledge base, which is created if it does not exist.

## Remarks

A called analyzer shares its caller's knowledge base, so `callconcept()` is the caller's concept itself, not a copy. Whatever the called analyzer adds under it is in place as soon as the call returns.

When the analyzer runs on its own, from VisualText or the command line, `callconcept()` still returns a concept, so you can develop and test the analyzer and inspect its results in the knowledge base before another analyzer calls it.

## Example

```
@POST
addstrval(callconcept(),"color",strtolower(N("$text",1)));

@RULES
_xNIL <- _xALPHA @@
```

## See Also

[callanalyzer](callanalyzer.md), [findroot](findroot.md), [Special Functions](Table_of_Special_Functions.md)
