[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# makeconcept

## Purpose

Make a new concept with name *conNameStr* and attach it under the parent concept *parentCon*. *positionInt* is an optional argument for specifying the 'birth order' (where the concept is attached vis a vis siblings) of the new child. *positionInt* of 0 or absent places the new concept at the end of the list of children.

## Syntax

```
returnCon = makeConcept(parentCon, conNameStr, [positionInt])
```

```
returnCon - type: con

parentCon - type: con

conNameStr - type: str

positionInt - type: int (optional)
```

## Returns

A handle to the newly created concept.

## Remarks

If a bad concept is passed (e.g., a string, not a handle to a concept), an NLP++ error is thrown and is written to the output log starting with "arg must be sem object" then processing aborts. If the second argument is not a string (e.g., an integer), an NLP++ error is thrown and written to the output log starting with "arg must be string" and processing aborts. If the third argument is greater than the number of existing children plus 1, nothing happens.

## Example

```
G("myConcept") = makeconcept(findroot(),"a concept");
```

```
or
```

```
G("myConcept") = makeconcept(findroot(),"a concept", 3);
```

## See Also

[getconcept](getconcept.md), [conceptname](conceptname.md), [Knowledge Base Functions](Table_of_Knowledge_Base_Functions.md)
