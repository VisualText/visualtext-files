# getconval

## Purpose

Fetch the concept represented by a KB value object.

## Syntax

```
valueConcept = getconval(aValue)
```

```
valueConcept - type: con

aValue - type: val
```

## Returns

parentConcept - type: con

## Remarks

Given a KB VAL object, fetch the concept that it houses.

## Example

In this example, we create a concept like noun and assign it as the value of a word's attribute. First, create the concepts named **words** and **noun** as children to the root of the KB (**concept**), and then make the concept **book** a child of **words**.

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

[addconval](addconval.md), [conval](conval.md), [findvals](findvals.md), [conceptname](conceptname.md), [getfltval](getfltval.md), [Knowledge Base Functions](Table_of_Knowledge_Base_Functions.md)
