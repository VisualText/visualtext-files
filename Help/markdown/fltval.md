# fltval

## Purpose

Fetch the float-value of a kb attribute *attrName *belonging to concept* concept*.  If there are multiple numeric values, only the first value is returned.

## Syntax

```
returnedNum = fltval(concept, attrName);
```

```
returnedNum - type: float

concept - type: con

attrName - type: str
```

## Returns

A floating point number, *returnedNum*.

## Remarks

Concepts can have zero or more attributes. Each attribute can have zero or more values. This function takes a concept and attribute name as input arguments and returns the first value associated with the attribute name, which must be a float.

## Example

```
@CODE

L("pi") = makeconcept(findroot(), "pi");

replaceval(L("pi"),"val",3.14);

"output.txt" << "pi = " << fltval(L("pi"), "val") << "\n";
```

Prints out the following to output.txt:

```
pi = 3.14
```

## See Also

[numval](numval.md), [Knowledge Base Functions](Table_of_Knowledge_Base_Functions.md)
