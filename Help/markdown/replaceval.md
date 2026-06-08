# replaceval

## Purpose

Replace the values of an attribute.  There are three variants of `replaceval`, one each for replacing the value of  a concept *concept'*s attribute named *attrNameStr* with either integer *valueInt*, string *valueString* or concept values *valueConcept*.

## Syntax

```
None = replaceval(concept, attrNameStr, valueInt)
```

```
concept - type: con

attrNameString - type: str

valueInt - type: int
```

```
None = replaceval(concept, attrNameStr, valueString)
```

```
concept - type: con

attrNameString - type: str

valueString - type: str
```

```
None = replaceval(concept, attrNameStr, valueConcept)
```

```
concept - type: con

attrNameString - type: str

valueConcept - type: con
```

## Returns

Nothing

## Remarks

If the attr-val pair arguments do not exist under the concept, `replaceval` creates new ones. If passed a bad *concept* argument, a warning is written to the output log. If passed a value like G("foo") that does not refer to a concept, the value is written as a string.

Differs from `addnumval`, `addstrval` and `addconval` in that `replaceval` replaces existing values, while `add*` adds new attr-val pairs. If the attr-val pairs do not exist already, `replaceval`*` `*acts like the `add*` functions.

Differs from `attrchange` in a number of respects. First, `attrchange` takes four arguments (e.g., `attrchange(concept, attrNameString, oldValString, newValString)`) while `replaceval`*` `*takes three. Second, `attrchange`*` `*only operates on strings, while `replaceval`*` `*operates on strings, integers or concepts as values. Third, recall a concept can have zero or more attributes, and each attribute can have zero or more values. If there is more than one concept listed as values of an attribute (e.g., apples having many colors, each color being a concept unto itself) then `replaceval`*` `*will replace them all with the new one (i.e., delete the existing old concept values). `attrchange`, on the other hand, is able to 'hone in' on a specific value. However, `attrchange`*` `*only operates on strings as values of attributes, not concepts as values of attributes.

## Example

```
@CODE

if(findconcept(findroot(),"apples"))

rmconcept(findconcept(findroot(),"apples"));

G("apples") = makeconcept(findroot(),"apples");



if(findconcept(findroot(),"color"))

rmconcept(findconcept(findroot(),"color"));

G("color") = makeconcept(findroot(),"color");

G("red") = makeconcept(G("color"),"red");

G("blue") = makeconcept(G("color"),"blue");



addnumval(G("apples"),"weight", 3);

addstrval(G("apples"),"name", "MacIntosh");

addconval(G("apples"),"color", G("red"));



"output.txt" << "apples weight = "

<< numval(G("apples"),"weight") << "\n";

"output.txt" << "apples name = "

<< strval(G("apples"),"name") << "\n";

"output.txt" << "apples color = "

<< conceptname(conval(G("apples"),"color")) << "\n";



"output.txt" << "Replacing apple's attr vals:\n";

replaceval(G("apples"),"weight", 4);

replaceval(G("apples"),"name", "Granny Smith");

replaceval(G("apples"),"color", G("blue"));



"output.txt" << "apples weight = "

<< numval(G("apples"),"weight") << "\n";

"output.txt" << "apples name = "

<< strval(G("apples"),"name") << "\n";

"output.txt" << "apples color = "

<< conceptname(conval(G("apples"),"color")) << "\n";
```

The code above should print out:

```
apples weight = 3

apples name = MacIntosh

apples color = red

Replacing apple's attr vals:

apples weight = 4

apples name = Granny Smith

apples color = blue
```

## See Also

[attrchange](attrchange.md), [rmval](rmval.md), [rmvals](rmvals.md), [rmattr](rmattr.md), [rmattrs](rmattrs.md), [Knowledge Base Functions](Table_of_Knowledge_Base_Functions.md)
