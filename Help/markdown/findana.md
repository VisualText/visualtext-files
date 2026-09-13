[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# findana

## Purpose

See if the given analyzer is loaded into memory.

## Syntax

```
returnedBool = findana(anaStr)
```

```
returnedBool - type: bool (0 or 1)
```

```
anaStr - type: str
```

## Returns

True if named analyzer is already loaded into memory.

## Remarks

Analyzer is named by its project (i.e., folder) name, and is assumed to reside in the area defined by the $APPS environment variable.

This was the first of a set of functions for loading an analyzer once and running it many times. [callanalyzer](callanalyzer.md) now does that from NLP++: it loads the named analyzer the first time it is called, and from then on findana returns true for that analyzer.

## Example

@CODE

L("ana present") = findana("TAIParse");

## See Also

[callanalyzer](callanalyzer.md), [system](system.md), [interactive](interactive.md), [Special Functions](Table_of_Special_Functions.md)
