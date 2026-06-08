[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# conceptname

## Purpose

Fetch the string value name of a concept.

## Syntax

```
returnedString = conceptname(concept)
```

```
returnedString - type: str

concept - type: con
```

## Returns

Name of concept as a string.

## Remarks

You cannot directly print out the name of a concept by referring to its handle, but instead must use this function to access its string valued name. If the concept is bad, an error appears in the log output window.

## Example

```
@CODE
```

```
"output.txt" << conceptname(makeconcept(findroot(),"test"));
```

Prints out the following in output.txt

```
test
```

## See Also

[attrname](attrname.md), [Knowledge Base Functions](Table_of_Knowledge_Base_Functions.md)
