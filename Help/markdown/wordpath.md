# wordpath

## Purpose

Get the entire path of dictionary concept *wordString.*

## Syntax

```
returnPathString = wordpath(wordString)
```

```
returnPathString - type: str

wordString - type: str
```

## Returns

If *wordString* is in the dictionary, return the path to it. If it is not, add it and return the path.

## Remarks

The dictionary is a specialized part of the KB hierarchy used to store and lookup words. You can see it with the KB editor, under **concept** > **sys** > **dict**. In order to speed up access to the dictionary, it is indexed by letters of the alphabet. `findwordpath` is different from `wordpath` in that `wordpath` will create the entry in the dictionary if it is not there already, while `findwordpath` will not create the entry.

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

[addword](addword.md), [dictfindword](dictfindword.md), [findwordpath](findwordpath.md), [wordindex](wordindex.md), [Knowledge Base Functions](Table_of_Knowledge_Base_Functions.md)
