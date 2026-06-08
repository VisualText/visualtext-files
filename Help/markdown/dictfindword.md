[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# dictfindword

## Purpose

Find dictionary concept *wordString* in the dictionary hierarchy of KB, return handle to concept.

## Syntax

```
returnedConcept = dictfindword(wordString)
```

```
returnedConcept - type: con

wordString - type: str
```

## Returns

Handle to the word concept if *wordString* is found in the dictionary, NULL otherwise.

## Remarks

The dictionary is a specialized part of the KB hierarchy used to store and lookup word forms. You can see it with the KB editor, under **concept > sys > dict**.

## Example

```
@CODE

"output.txt" << "1 " << conceptname(addword("hello")) << "\n";

"output.txt" << "2 " << conceptname(wordindex("hello")) << "\n";

"output.txt" << "3 " << findwordpath("hello") << "\n";

"output.txt" << "4 " << findwordpath("olleh") << "\n";

"output.txt" << "5 " << wordpath("foobaz") << "\n";

"output.txt" << "6 " << conceptname(dictfindword("hello")) << \n";

rmword("foobaz");
```

Prints out:

```
1 hello

2 he

3 "concept" "sys" "dict" "a" "h" "he" "hello"

4

5 "concept" "sys" "dict" "a" "f" "fo" "foobaz"

6 hello
```

## See Also

[findwordpath](findwordpath.md), [wordindex](wordindex.md), [wordpath](wordpath.md), [Knowledge Base Functions](Table_of_Knowledge_Base_Functions.md)
