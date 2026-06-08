[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# findattr

## Purpose

Fetch the attribute named *nameString* belonging to the concept *concept*.

## Syntax

```
returnedAttribute = findattr(concept, nameString);
```

```
returnedAttribute - type: attr

concept - type: con

nameString - type: str
```

## Returns

An attribute if the concept has an attribute named nameString. If nameString is not a attribute of concept, findattr returns 0.

## Remarks

If a bad concept is passed, a warning is written to output log file - "warning: given no concept."

## Example

```
G("myConcept") = makeconcept(findroot(),"a concept");

G("myAttr") = addattr(G("myConcept"),"an attribute");

"output.txt" << attrname(findattr(G("myConcept"),"an attribute")) << "\n";

G("junk") = findattr(G("myConcept"),"duh");

"output.txt" << "junk = " << G("junk");
```

This prints the following to output.txt:

```
an attribute

junk = 0
```

## See Also

[findattrs](findattrs.md), [Knowledge Base Functions](Table_of_Knowledge_Base_Functions.md)
