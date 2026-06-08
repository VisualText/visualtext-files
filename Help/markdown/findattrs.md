# findattrs

## Purpose

Fetch the list of attributes belonging to the concept named *concept*.

## Syntax

```
returnedAttribute = findattrs(concept)
```

```
returnedAttribute - type: attr

concept - type: con
```

## Returns

An attribute if the concept has an attribute. If the concept has no attributes, a null attribute structure is returned. You test to see whether anything was returned with code like:

```
G("result") = findattrs(G("foo"));

if(G("result"))

"output.txt" << "G(result) = " << attrname(G("result")) << "\n";
```

In this example, while G("foo") is a concept, it has no attributes.

## Remarks

Similar to findattr, except you don't pass the function the name of the attribute. So, if your application does not 'know' the attributes of a concept, use findattrs. If you know the specific concept you want, use findattr. If a bad concept is passed, such as a string instead of a concept, an error is written to the output log file.

## Example

In this example, we create the concept of *apples*, and give them the attribute *have *with value *color*. This is sort of like saying 'Apples have color.' Then we give apples the attribute *color* who's value is *red*, then the values of color *green* and *yellow*

```
G("root") = findroot();

# look for apples in the concept hierarchy

G("apple") = findconcept(G("root"),"apple");

# if you find them, kill them (to start fresh)

if (G("apple")) rmconcept(G("apple"));

# Apples exist

G("apple") = makeconcept(G("root"),"apple");

# Apples have color

addstrval(G("apple"),"have","color");

# Apple's color is red

addstrval(G("apple"),"color","red");

# Apple's color is also green and yellow

addstrval(G("apple"),"color","green and yellow");
```

```
# Now we access the attributes of the concept apple:
```

```
# Find apple's attribute list

G("attrList") = findattrs(G("apple"));

# Find the first attribute's name

G("attrName") = attrname(G("attrList"));

# Find the list of values of the attribute

G("valList") = attrvals(G("attrList"));

# get the first value

G("valName") = getstrval(G("valList"));

# print out the first attribute's name and value

If(G("attrName")){

"output.txt" << "first attribute of apple is: "

<< G("attrName") << "\n";

"output.txt" << "first value of that attribute is: "

<< G("valName") << "\n";

}

# get the next attribute

G("nextAttr") = nextattr(G("attrList"));

# get its name

G("attrName") = attrname(G("nextAttr"));

If(G("attrName")){

"output.txt" << "next attribute of apple is: "

<< G("attrName") << "\n";

}

# get the list of values of the second attribute

G("valList") = attrvals(G("nextAttr"));

# get the first value's name

G("valName") = getstrval(G("valList"));

# print it out

"output.txt" << "first value of that attribute is: "

<< G("valName") << "\n";

# get the second value of the second attribute

G("nextValName") = getstrval(nextval(G("valList")));

# print it out

"output.txt" << "second value of that attribute is: "

<< G("nextValName") << "\n";
```

This prints the following to output.txt:

```
first attribute of apple is: have

first value of that attribute is: color

next attribute of apple is: color

first value of that attribute is: red

second value of that attribute is: green and yellow
```

## See Also

[findattr](findattr.md), [Knowledge Base Functions](Table_of_Knowledge_Base_Functions.md)
