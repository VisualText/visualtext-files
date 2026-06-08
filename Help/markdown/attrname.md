[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# attrname

## Purpose

Fetch the name of an knowledge base attribute.

## Syntax

```
returnedString = attrname(anAttribute);
```

```
returnedString - type: str

anAttribute - type: con
```

## Returns

A string which is the name of the passed attribute.

## Remarks

If you try to print out an attribute directly, you'll get an error. This function returns the string value name of an attribute. If a bad attribute is passed, an error is written to output log file.

## Example

```
G("myConcept") = makeconcept(findroot(),"a concept");

G("myAttr") = addattr(G("myConcept"),"an attribute");

"output.txt" << attrname(G("myAttr")) << "\n";
```

This prints out

```
an attribute
```

## See Also

[conceptname](conceptname.md), [Knowledge Base Functions](Table_of_Knowledge_Base_Functions.md)
