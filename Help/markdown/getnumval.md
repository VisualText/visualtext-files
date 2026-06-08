# getnumval

## Purpose

Fetch the number from a numeric value.

## Syntax

```
returnedNum = getnumval(aValue);
```

```
returnedNum - type: int

aValue - type: val
```

## Returns

A number, *returnedNum*.

## Remarks

Concepts can have zero or more attributes. Each attribute can have zero or more values. This function takes a value as argument and returns the number associated with the input argument value. Differs from `getstrval`, in that `getsval` handles either numerical or string values in aValue, while `getstrval` expects a string. Differs from `getstrval` in that `getnumval` expects a number in aValue. If passed a bad argument value, the function writes an error message to the output log.

## Example

```
@CODE

# create a range

G("range") = makeconcept(findroot(), "range");

addnumval(G("range"),"min",33);

addnumval(G("range"),"max",118);

# access data

"output.txt" << "range = " <<

  getnumval(findvals(G("range"), "max")) -

  getnumval(findvals(G("range"), "min")) << "\n";

# clean up

rmconcept(G("range"));
```

This prints the following to output.txt:

```
range = 85
```

## See Also

[getstrval](getstrval.md), [getsval](getsval.md), [getconval](getconval.md), [getfltval](getfltval.md), [Knowledge Base Functions](Table_of_Knowledge_Base_Functions.md)
