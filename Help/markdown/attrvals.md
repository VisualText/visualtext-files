# attrvals

## Purpose

Fetch attribute's list of values.

## Syntax

```
returnedValue(s) = attrvals(anAttribute);
```

```
returnedValue(s) - type: val

anAttribute - type: attr
```

## Returns

A list of values.

## Remarks

Concepts can have zero or more attributes. Each attribute can zero or more values. This function takes an attribute as argument and returns the list of values associated with the attribute. If there are no values of the attribute, the function returns NULL.

## Example

To demonstrate attrvals, we first need to build a KB:

```
@CODE

# if you find apples in the concept hierarchy

if (findconcept(findroot(),"apple"))

# kill them (to start fresh)

rmconcept(findconcept(findroot(),"apple"));

# Create the apple concept

G("apple") = makeconcept(findroot(),"apple");

# Apples have color

addstrval(G("apple"),"have","color");

# Apple's color is red

addstrval(G("apple"),"color","red");

# Apple's color is also green and yellow

addstrval(G("apple"),"color","green and yellow");
```

The code creates a KB like this:

```
![](../helps/Image%20Files/apple.gif)
```

The following code accesses the KB's attributes and values:

```
# Find apple's attribute list

G("attrList") = findattrs(G("apple"));

# Find the list of values of the first attribute

G("valList") = attrvals(G("attrList"));

# print out the first attribute's name and value

if(attrname(G("attrList"))){

"output.txt" << "1) first attribute of apple is: "

<< attrname(G("attrList")) << "\n";

"output.txt" << "2) first value of that attribute is: "

<< getstrval(G("valList")) << "\n";}

# get the next attribute

G("nextAttr") = nextattr(G("attrList"));

if(attrname(nextattr(G("attrList"))))

"output.txt" << "3) next attribute of apple is: "

<< attrname(G("nextAttr")) << "\n";

# get the list of values of the second attribute

G("valList") = attrvals(G("nextAttr"));

# print the first value's name

"output.txt" << "4) first value of that attribute is: "

<< getstrval(G("valList")) << "\n";

# print the second value of the second attribute

"output.txt" << "5) second value of that attribute is: "

<< getstrval(nextval(G("valList"))) << "\n";
```

```
The output looks like this:
```

```
![](../helps/Image%20Files/attrvalout.gif)
```

## See Also

[attrexists](attrexists.md), [attrwithval](attrwithval.md), [findvals](findvals.md), [Knowledge Base Functions](Table_of_Knowledge_Base_Functions.md)
