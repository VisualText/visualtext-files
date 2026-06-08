[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# findconcept

## Purpose

Find a concept in the knowledge base.  There are two variants, string and integer. The string variant finds and returns the concept with name **nameString** under the parent concept **parentConcept**. If a number is passed instead of **nameString**, the concept with that sibling order number is returned.

## Syntax

```
returnedConcept = findconcept(parentConcept, nameString);
```

```
returnedConcept - type: con

parentConcept - type: con

nameString - type: str
```

```
returnedConcept = findconcept(parentConcept,number)
```

```
returnedConcept - type: con

parentConcept - type: con

number - type: int
```

## Returns

String version: `findconcept` returns a concept if the **parentConcept** does have a child concept with name **nameString**. If **parentConcept** does not have child with name **nameString**, `findconcept` returns 0.

Numerical version: If a number is passed in instead of a string, the concept with that number is returned. Child concepts are numbered from 1 to N, where 1 is the first child added to a concept, and N is the last one added.

## Remarks

If **parentConcept** is not in the KB, that is, if you don't have a handle on a valid concept, an error is thrown in the output log window: "Arg must be Sem object." If an index is chosen outside of the set of existing concepts, findconcept returns 0.

## Example

```
# get a handle on the root

G("the root") = findroot();

# make the child concept

makeconcept(G("the root"),"child");

# do something else ...

# later on, get the string variant

G("the child") = findconcept(G("the root"),"child");

# fetch the numeric variant

G("same concept") = findconcept(G("the root"), 1);
```

## See Also

[getconcept](getconcept.md), [findhierconcept](findhierconcept.md), [Knowledge Base Functions](Table_of_Knowledge_Base_Functions.md)
