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

This is the first of a set of functions under development for loading an analyzer once and running it many times.  While such functionality exists in the programmer's API, it is under development for running within VisualText as well.

## Example

@CODE

L("ana present") = findana("TAIParse");

## See Also
