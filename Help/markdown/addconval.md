# addconval

## Purpose

Add the concept value *valueConcept* to the attribute *attrNameString* belonging to the concept *concept*.

## Syntax

```
addconval(concept, attrNameString, valueConcept)
```

```
concept - type: con

attrNameString - type: str

valueConcept - type: con
```

## Returns

Nothing

## Remarks

Concepts can have zero or more attributes, and attributes can have zero or more values. Values of attributes can be strings, numbers or other concepts. This function adds a concept to the value of other another concept's attribute. All concepts need to be rooted in the concept hierarchy, so first you need to create them before you can assign them as values of attributes to other concepts.

If the attribute doesn't exist yet, addconval will create it. If the concept or the value concept is bad, an error appears in the log output window.

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

The remaining code finds the first child of words named book, gets the concept which is the value of the attribute "is a" and prints out its name ('noun') to output.txt:

```
G("aConcept") = getconcept(G("words"),"book");

G("anotherConcept") = getconval(findvals(G("aConcept"),"is a"));

"output.txt" << conceptname(G("anotherConcept")) << "\n";
```

## See Also

[addsval](addsval.md), [addstrval](addstrval.md), [addnumval](addnumval.md), [Knowledge Base Functions](Table_of_Knowledge_Base_Functions.md)
