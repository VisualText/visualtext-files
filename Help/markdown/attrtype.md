[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# attrtype

## Purpose

Fetch an attribute's type

## Syntax

```
type = attrtype(concept,attr_name);
```

```
type - type: int

concept - type: con

attr_name - type: str
```

## Returns

Returns 0 for string, 1 for number, 2 for concept, and 3 for float.

## Remarks

This allows for calling the correct function, either getstrval, getnumval, or getconval.

## Example

```
@CODE

G("apple") = makeconcept(findroot(),"apple");

addstrval(G("apple"),"color","red");

# prints 0 (string)

"output.txt" << "type = " << attrtype(G("apple"),"color") << "\n";
```
