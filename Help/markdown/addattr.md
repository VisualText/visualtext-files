# addattr

## Purpose

Add an empty attribute named *nameString* (one with no value) to the concept named *concept*.

## Syntax

```
returnedAttribute = addattr(concept, nameString);
```

```
returnedAttribute - type: attr

concept - type: con

nameString - type: str
```

## Returns

A handle on the newly created attribute.

## Remarks

You may know an attribute before you know its value. With this function, you can create the attribute without mentioning a value. If a bad concept is passed, a warning is written to output log file - "Warning: Given no concept." Attribute names are unique, so if you try to add the same name more than once, i.e. if called repeatedly with the same arguments, the repeated call is ignored and only one attribute is added.

## Example

```
@CODE

G("myConcept") = makeconcept(findroot(),"a concept");

G("myAttr") = addattr(G("myConcept"),"an attribute");

"output.txt" << attrname(G("myAttr")) << "\n";
```

This prints out the following to output.txt:

```
an attribute
```

## See Also

[addconval](addconval.md), [addnumval](addnumval.md), [addstrval](addstrval.md), [addsval](addsval.md), [Knowledge Base Functions](Table_of_Knowledge_Base_Functions.md)
