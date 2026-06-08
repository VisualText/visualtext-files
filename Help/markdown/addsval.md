[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# addsval

## Purpose

Add numeric value *number* as a string to concept *concept*'s attribute named *nameString*.

## Syntax

```
addsval(concept, nameString, number)
```

```
concept - type: con

nameString - type: str

number - type: int
```

## Returns

Nothing.

## Remarks

If the attribute has not been created yet, `addsval` will create it.

Sometimes it is convenient to treat a number like a string. In this case, you can perform numeric operations in the number field of this function, but then have the result stored in the KB as a string.

## Example

```
@CODE
```

```
G("Malibu") = makeconcept(findroot(), "Malibu");

addsval(G("Malibu"),"Route",1+2);
```

## See Also

[addstrval](addstrval.md), [addnumval](addnumval.md), [addconval](addconval.md), [Knowledge Base Functions](Table_of_Knowledge_Base_Functions.md)
