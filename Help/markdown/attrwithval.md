[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# attrwithval

## Purpose

Check *concept* to see if it has attribute *attrStr* with value *valStr*.

## Syntax

```
returnedBoolean = attrwithval(concept, attrStr, valStr)
```

```
returnedBoolean - type: bool (1 or 0)

concept - type: con

attrStr - type: str

valStr - type: str
```

## Returns

1 if the concept has the attribute-value pair, 0 otherwise. Passed a bad concept, the function writes an error to the output log.

## Remarks

If an attribute has multiple values, returns true if one of the values matches *valStr*.  Limited to string-valued attributes.

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
```

The code above writes the following to output.txt:

```
1) apples color red

2) are apples red? 1

3) are apples blue? 0

4) are apples blue now? 1
```

## See Also

[attrexists](attrexists.md), [attrvals](attrvals.md),  [Knowledge Base Functions](Table_of_Knowledge_Base_Functions.md)
