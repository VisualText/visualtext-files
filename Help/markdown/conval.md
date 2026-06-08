[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# conval

## Purpose

Fetch concept-value of attribute *attrNameString* (must be first)* *belonging to* *concept *concept*.

## Syntax

```
returnedConcept = conval(concept, attrNameString)
```

```
returnedConcept - type: con

concept - type: con

attrNameString - type: str
```

## Returns

returnedConcept - type: con

## Remarks

An attribute's value can be a concept, and conval returns attribute values of this type.  If an attribute has multiple values, it only fetches the first.  If it can't fetch a concept value, it returns 0.

## Example

First, create the concepts named words and noun as children to the root of the KB, then make the concept book a child of **words**.

```
G("words") = makeconcept(findroot(), "words");

G("noun") = makeconcept(findroot(),"noun");

G("noun_book") = makeconcept(G("words"),"book");
```

The KB editor at this point looks like:

![](../helps/Image%20Files/addconval.gif)

Next, give book the attribute "is a" and make the concept noun be the value of book's attribute "is a":

```
G("an_attr") = addattr(G("noun_book"),"is a");

addconval(G("noun_book"), "is a", G("noun"));
```

The remaining code fetches the value of the "is a" attribute, i.e., the noun concept, and prints its name:

```
G("bConcept") = conval(G("noun_book"),"is a");
```

```
"output.txt" << conceptname(G("bConcept")) << "\n";
```

This prints the following to output.txt:

```
noun
```

## See Also

[numval](numval.md), [strval](strval.md), [getconval](getconval.md), [Knowledge Base Functions](Table_of_Knowledge_Base_Functions.md)
