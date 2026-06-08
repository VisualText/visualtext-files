# getconcept

## Purpose

Get or make concept named *conceptNameString* under concept *parentConcept*.

## Syntax

```
returnedConcept = getconcept(parentConcept, conceptNameString)
```

```
returnedConcept - type: con

parentConcept - type: con

conceptNameString - type: str
```

## Returns

returnedConcept - type: con

## Remarks

All concepts have names (see `makeconcept`) and need to be rooted in the concept hierarchy. This function returns a concept given its name and its parent concept. If the parent concept is bad, an error appears in the log output window. If the parent concept does not have a child concept named conceptNameString, this function creates one with that name. If the parent concept does have a child concept named conceptNamestring, this function returns that concept.

## Example

In this example, we show how we can create a concept like noun and assign it as the value of a word's attribute. We create the concepts named **words** and **noun** as children to the root of the KB (**concept**), and then make the concept **book** a child of **words**.

```
G("words") = makeconcept(findroot(), "words");

G("noun") = makeconcept(findroot(),"noun");

G("noun_book") = makeconcept(G("words"),"book");
```

The KB editor at this point looks like:

![](../helps/Image%20Files/addconval.gif)

Next, give **book** the attribute "**is a"** and make the concept **noun** be the value of **book**'s attribute "**is a**":

```
G("an_attr") = addattr(G("noun_book"),"is a");

addconval(G("noun_book"), "is a", G("noun"));
```

The remaining code finds the first child of **words** named **book,** gets the concept which is the value of the attribute **"is a" **and prints out its name ('noun') to output.txt:

```
G("aConcept") = getconcept(G("words"),"book");

G("anotherConcept") = getconval(findvals(G("aConcept"),"is a"));

"output.txt" << conceptname(G("anotherConcept")) << "\n";
```

## See Also

[makeconcept](makeconcept.md), [conceptname](conceptname.md), [Knowledge Base Functions](Table_of_Knowledge_Base_Functions.md)
