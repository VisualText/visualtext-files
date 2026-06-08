# attrexists

## Purpose

Find attribute *attrStr* with value *valStr, *searching in the subhierarchy of concept *parentConcept*.

## Syntax

```
returnedBoolean = attrexists(parentConcept, attrStr, valStr)
```

```
returnedBoolean - type: bool

parentConcept - type: con

attrStr - type: str

valStr - type: str
```

## Returns

1 if any concept below *parentConcept* has the attribute-value pair, 0 otherwise. Passed a bad concept, the function writes an error to the output log.

## Remarks

The search starts at the named concept, and continues down its entire subhierarchy. Contrast this with *attrwithval*, which is limited to only the argument concept.

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

"output.txt" << "2) are apples red? " <<

attrwithval(G("apple"), "color", "red") << "\n";

"output.txt" << "3) are apples blue? " <<

attrwithval(G("apple"), "color", "blue") << "\n";

# Change a value of a given attribute to another value.

attrchange(findroot(), "color", "red", "blue");

"output.txt" << "4) are apples blue now? " <<

attrwithval(G("apple"), "color", "blue") << "\n";

"output.txt" << "5) " << attrexists(findroot(), "color", "blue");
```

The code above writes the following to output.txt:

```
1) apples color red

2) are apples red? 1

3) are apples blue? 0

4) are apples blue now? 1

5) 1
```

## See Also

[attrwithval](attrwithval.md), [Knowledge Base Functions](Table_of_Knowledge_Base_Functions.md)
