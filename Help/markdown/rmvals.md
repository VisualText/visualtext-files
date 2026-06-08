[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# rmvals

## Purpose

Remove the values of an attribute named *attributeNameString* belonging the concept* aConcept*.

## Syntax

```
returnedBoolean = rmvals(aConcept, attributeNameString)
```

```
returnedBoolean - type: bool

aConcept - type: con

attributeNameString - type: str
```

## Returns

1 if removed, 0 otherwise (e.g., attribute does not exist with that name under *aConcept*).

## Remarks

If a bad concept is passed (e.g., a string, not a handle to a concept), an NLP++ error is thrown and is written to the output log.

## Example

```
# create the concept

if(findconcept(findroot(),"myConcept"))

rmconcept(findconcept(findroot(),"myConcept"));

G("aConcept") = makeconcept(findroot(), "myConcept");

# create an attribute named 'myAttr' and give it the value 'myVal.'

addstrval(G("aConcept"),"myAttr","myVal");

# attempt to remove values of non-existent attribute.

G("result") = rmvals(G("aConcept"),"foo bar");

"output.txt" << "G(result) should be 0, is " << G("result") << "\n";

# remove values of existing attribute.

G("result") = rmvals(G("aConcept"),"myAttr");

"output.txt" << "G(result) should be 1, is " << G("result") << "\n";
```

## See Also

[rmval](rmval.md), [rmattrval](rmattrval.md), [rmattrs](rmattrs.md), [Knowledge Base Functions](Table_of_Knowledge_Base_Functions.md)
