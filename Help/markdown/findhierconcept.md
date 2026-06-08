# findhierconcept

## Purpose

Find a concept named *conceptNameStr* in the KB, starting in the subhierarchy of the concept *startCon*. Use this function when your not sure exactly where the concept is in the hierarchy, but you know enough to limit the search to some part of it.

## Syntax

```
returnedCon = findhierconcept(conceptNameStr, startCon)
```

```
returnedCon - type: con

conceptNameStr - type: str

startCon - type: con
```

## Returns

The concept, if found. If not, NULL.

## Remarks

If *startCon* is 0, start at root of KB. If a bad concept is passed to the function in *startCon*, a warning is written to the output log window.

## Example

To demonstrate findhierconcept, we first need to build a KB. The code below finds the root of the KB (**concept**) and creates the child concept **ontology** under it. It then creates the child concept **female** under the ontology concept. Finally, under the female concept, it says to create two children concepts **mother** and **daughter**.

```
G("root") = findroot();

G("onto") = makeconcept(G("root"), "ontology");

G("female") = makeconcept(G("onto"), "female");

makeconcept(G("female"), "mother");

makeconcept(G("female"), "daughter");
```

![](../helps/Image%20Files/naveg.gif)

Now that we have our database, we can see how findhierconcept works. The first line of code says to look for a concept named **mother** starting in the **ontology** subhierarchy. The second line of code, says if the concept named mother is found, to print out "**Mother concept=**" followed by the concept's name (**mother**) to output.txt. If a concept named mother is not found, the third line of code gives the instruction to write "**No mother found**" to output.txt.

```
G("mother") = findhierconcept("mother", G("onto"));

if (G("mother"))

"output.txt" << "Mother concept=" << conceptname(G("mother")) << "\n";

else

"output.txt" << "No mother found\n";
```

This code prints out the following to output.txt:

```
Mother concept=mother
```

## See Also

[findconcept](findconcept.md), [Knowledge Base Functions](Table_of_Knowledge_Base_Functions.md)
