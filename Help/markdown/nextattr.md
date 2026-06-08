[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# nextattr

## Purpose

Fetch the next attribute in a list of attributes.

## Syntax

```
returnedAttr = nextattr(anAttr);
```

```
returnedAttr - type: attr

anAttr - type: attr
```

## Returns

A list of values.

## Remarks

Concepts can have zero or more attributes. Each attribute can have zero or more values. This function takes an attribute as argument and returns the next attribute associated with the attribute. If there are no next attributes of the attribute (i.e., no younger siblings), the function returns NULL.

## Example

To demonstrate nextattr, we first need to build a KB:

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

# Apple's weigh 3 something or others

addnumval(G("apple"),"weight",3);

# Apple's color is also green and yellow

addstrval(G("apple"),"color","green and yellow");
```

The code creates a KB like this:

```
![](../helps/Image%20Files/attrvals.gif)
```

(To launch Attribute Editor, select the concept in the KB Editor, right mouse click and select Attributes from the popup menu).

The following code accesses the KB's attributes and values:

```
"output.txt" << "Apple's attrs 'n vals:\n";

# Find apple's attribute's

G("attrList") = findattrs(G("apple"));

# cycle through all of apple's attributes

G("attr counter") = 1;

while(G("attrList")){

"output.txt" << G("attr counter") << ")\t" <<

attrname(G("attrList")) << "\n";

# get the attribute's list of values

G("valList") = attrvals(G("attrList"));

# cycle through all the values

G("val counter") = 1;

while(G("valList")) {

"output.txt" << "\t" << G("val counter") << ")\t" <<

getsval(G("valList")) << "\n";

G("valList") = nextval(G("valList"));

G("val counter")++;

}

# get the next attribute

G("attrList") = nextattr(G("attrList"));

G("attr counter")++;

}
```

```
The output looks like this:
```

```
![](../helps/Image%20Files/attrsnvalsoutput.gif)
```

## See Also

[findattrs](findattrs.md), [Knowledge Base Functions](Table_of_Knowledge_Base_Functions.md)
