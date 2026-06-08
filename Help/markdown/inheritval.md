# inheritval

## Purpose

Find a string attribute *attrNameStr* in the hierarchy starting at the concept *childConcept, *searching upwards*.  *Search for attribute continues until attribute is found or the concept named *topConcept* is reached.

## Syntax

```
returnedAttrValStr = inheritval(childConcept, attrNameStr, topConcept)
```

```
returnedAttrValStr - type: str

childConcept - type: con

attrNameStr - type: str

topConcept - type: con
```

## Returns

If the attribute is found, if it has a value, the string value is returned. Else the function returns NULL.

## Remarks

If topConcept is 0, keeps searching until the root of the hierarchy (**concept**) is reached.

## Example

```
@CODE

if (findconcept(findroot(),"ontology"))

rmconcept(findconcept(findroot(),"ontology"));

G("ontology") = makeconcept(findroot(), "ontology");

G("animal") = makeconcept(G("ontology"),"animal");

G("human") = makeconcept(G("animal"),"human");

G("man") = makeconcept(G("human"),"man");

addstrval(G("man"),"gender", "male");

G("bachelor") = makeconcept(G("man"),"bachelor");

G("result") = inheritval(G("bachelor"), "gender", G("man"));

"output.txt" << "bachelor's gender: " << G("result") << "\n";
```

Prints the following to output.txt:

```
bachelor's gender: male
```

## See Also

[Knowledge Base Functions](Table_of_Knowledge_Base_Functions.md)
