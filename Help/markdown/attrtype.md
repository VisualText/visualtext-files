# attrtype

## Purpose

Fetch an attribute's type

## Syntax

```
type = attrtype(concept,attr_name);
```

```
returnedValue(s) - type: number

anAttribute - type: attr
```

## Returns

Returns 0 for string, 1 for number, 2 for concept, and 3 for float.

## Remarks

This allows for calling the correct function, either getstrval, getnumval, or getconval.

## Example
