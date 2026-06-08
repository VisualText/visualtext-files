[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# strval

## Purpose

Fetch the string-value of kb attribute *attrnameString *belonging to the concept *concept*.

## Syntax

```
returnedStr = strval(concept, attrNameString);
```

```
returnedStr - type: str

concept - type: con

attrNameString - type: attr
```

## Returns

String value of attribute named *attrNameString*. If there are no attributes of the concept, the function returns NULL. If the attribute exists, but does not have a value, the function returns NULL.

## Remarks

Concepts can have zero or more attributes. Each attribute can have zero or more values. This function takes a concept and name of an attribute as argument and returns first the string value associated with the attribute (if it exists). Different from getstrval, which takes (an already found) value as input argument, in that strval will find the named value.

## Example

```
# put attribute and value in the KB

if(findconcept(findroot(),"apple"))

rmconcept(findconcept(findroot(),"apple"));

G("apple") = makeconcept(findroot(), "apple");

addstrval(G("apple"),"color","red");



# access

"output.txt" << "getstrval = " <<

getstrval(findvals(G("apple"), "color")) << "\n";

"output.txt" << "strval = " <<

strval(G("apple"),"color") << "\n";

"output.txt" << "attrwithval = " <<

attrwithval(G("apple"), "color", "red") << "\n";



# change

attrchange(G("apple"), "color", "red", "blue")

"output.txt" << "changing apples' color from red to blue\n"

<< "attrwithval = " <<

attrwithval(G("apple"), "color", "blue") << "\n";



# remove attrs, vals and concept

rmattrval(G("apple"), "color", "red");

rmconcept(G("apple");
```

Outputs:

```
getstrval = red

strval = red

attrwithval = 1

changing apples' color from red to blue

attrwithval = 1
```

## See Also

[getstrval](getstrval.md), [numval](numval.md), [conval](conval.md), [Knowledge Base Functions](Table_of_Knowledge_Base_Functions.md)
