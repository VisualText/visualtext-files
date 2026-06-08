# attrchange

## Purpose

Replace all matching attribute-value pairs *attrStr*-*oldValStr* in the KB belonging to the concept *aConcept* to new attribute-value pairs *attrStr*-*newValStr*.

## Syntax

```
returnedBoolean = attrchange(aConcept, attrStr, oldValStr, newValStr)
```

```
returnedBoolean - type: bool

aConcept - type: con

attrStr - type: str

oldValStr - type: str

newValStr - type: str
```

## Returns

1 if at least one pair is changed, 0 otherwise.

## Remarks

Think of this as a global replace. If passed a bad concept, the function writes an error to the output log.

## Example

```
# if you find apples in the concept hierarchy

if (findconcept(findroot(),"apple"))

# kill them (to start fresh)

rmconcept(findconcept(findroot(),"apple"));

# Create the apple concept

G("apple") = makeconcept(findroot(),"apple");

# Apple's color's red

addstrval(G("apple"),"color","red");

# MacIntosh apples are also red

addstrval(makeconcept(G("apple"),"MacIntosh"),"color","red");

# Print out apple's attribute and value

if(attrname(findattrs(G("apple")))){

"output.txt" << "1) apples " << attrname(findattrs(G("apple")));

"output.txt" << " "

<< getstrval(attrvals(findattrs(G("apple")))) << "\n";

}

# Test for a given attribute and value

"output.txt" << "2) are apples red? "

<< attrwithval(G("apple"), "color", "red") << "\n";

"output.txt" << "3) are apples blue? " <<

attrwithval(G("apple"), "color", "blue") << "\n";

# Change a value of a given attribute to another value.

attrchange(findroot(), "color", "red", "blue");

"output.txt" << "4) are apples blue now? " <<

attrwithval(G("apple"), "color", "blue") << "\n";
```

The code above writes the following to output.txt:

```
1) apples color red

2) are apples red? 1

3) are apples blue? 0

4) are apples blue now? 1
```

Since attrchange operates on all children of the parent concept, the resulting KB looks like:

![](../helps/Image%20Files/attrchange.gif)

## See Also

[replaceval](replaceval.md), [Knowledge Base Functions](Table_of_Knowledge_Base_Functions.md)
