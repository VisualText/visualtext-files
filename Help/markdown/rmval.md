# rmval

## Purpose

Remove value *aValue* of an attribute named *anAttribute*.

## Syntax

```
returnedBoolean = rmval(anAttribute, aValue)
```

```
returnedBoolean - type: bool

anAttribute - type: attr

aValue - type: val
```

## Returns

1 if removed, 0 otherwise.

## Remarks

Removes a single value given an attribute. Differs from `rmvals` in that `rmvals` removes all values of the attribute, while rmval only removes the one given. Also, note difference in arguments - `rmval` takes an attribute and a value as input args, while `rmvals` takes a concept and an attribute name string as input.

## Example

```
# create the concept

if(findconcept(findroot(),"myConcept"))

rmconcept(findconcept(findroot(),"myConcept"));

G("aConcept") = makeconcept(findroot(), "myConcept");

# remove values of existing attribute.

G("result") = rmvals(G("aConcept"),"myAttr");

"output.txt" << "G(result) should be 0, is " << G("result") << "\n"; addstrval(G("aConcept"),"myAttr","myVal1");

addstrval(G("aConcept"),"myAttr","myVal2");

G("anAttr") = findattr(G("aConcept"),"myAttr");

G("aVal") = attrvals(G("anAttr"));

G("result") = rmval(G("anAttr"), G("aVal"));
```

## See Also

[rmvals](rmvals.md), [rmattrval](rmattrval.md), [rmattrs](rmattrs.md), [Knowledge Base Functions](Table_of_Knowledge_Base_Functions.md)
