[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# findvals

## Purpose

Fetch the list of values of a concept's attribute.

## Syntax

```
aValue = findvals(concept, attrNameString)
```

```
aValue - type: val

concept - type: con

attrNameString - type: str
```

## Returns

Value

## Remarks

Concepts can have zero or more attributes, and attributes can have zero or more values. Values of attributes can be strings, numbers or other concepts. This function finds the value (or list of values) that have the name *attrNameString*. In order to find the next value, use nextval. If the concept is bad, an error appears in the log output window.

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

[attrvals](attrvals.md), [nextval](nextval.md), [Knowledge Base Functions](Table_of_Knowledge_Base_Functions.md)
