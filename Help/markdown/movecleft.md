# movecleft

## Purpose

Move a concept *childConcept* before previous sibling.  (Moves the concept to the 'left' or 'higher' in the pecking order.)

## Syntax

```
None = movecleft(childConcept)
```

```
childConcept - type: con
```

## Returns

Nothing.

## Remarks

If you try to move a concept beyond the first concept, a message is written to the output log.

## Example

```
@CODE

"output.txt" << "move\n";

G("alpha") = makeconcept(findroot(),"first");

G("beta") = makeconcept(findroot(),"second");

G("gamma") = makeconcept(findroot(),"third");

movecleft(G("gamma"));

movecright(G("alpha"));
```

This prints the following to output.txt:

```
move
```

After this code is executed, the KB Editor looks like this:

```
![](../helps/KB_Functions_Images/movecleft_kb.gif)
```

## See Also

[movecright](movecright.md), [Knowledge Base Functions](Table_of_Knowledge_Base_Functions.md)
