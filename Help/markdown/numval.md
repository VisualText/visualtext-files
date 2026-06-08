# numval

## Purpose

Fetch the numeric-value of a kb attribute *attrName *belonging to concept* concept*.  If there are multiple numeric values, only the first value is returned.

## Syntax

```
returnedNum = numval(concept, attrName);
```

```
returnedNum - type: int

concept - type: con

attrName - type: str
```

## Returns

A number, *returnedNum*.

## Remarks

Concepts can have zero or more attributes. Each attribute can have zero or more values. This function takes a concept and attribute name as input arguments and returns the first number associated with the attribute name. Difference vis getsval: getsval expects string values in aValue, or converts numbers to strings. Difference vis getnumval: getnumval expects a number in aValue, and has only one input argument, a value which has already been found, while numval takes two input arguments and finds the attribute by name. If passed a bad argument value, the function writes an error message to the output log.

## Example

```
@CODE

# create a range

G("range") = makeconcept(findroot(), "range");

addnumval(G("range"),"min",33);

addnumval(G("range"),"min",34);

addnumval(G("range"),"max",118);



# access data

"output.txt" << "range = " <<

getnumval(findvals(G("range"), "max")) -

getnumval(findvals(G("range"), "min")) << "\n";

"output.txt" <<

numval(G("range"),"min") << "\n";
```

Prints out the following to output.txt:

```
range = 85

33
```

## See Also

[conval](conval.md), [strval](strval.md), [getnumval](getnumval.md), [Knowledge Base Functions](Table_of_Knowledge_Base_Functions.md)
