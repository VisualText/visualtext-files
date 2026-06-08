[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# findwordpath

## Purpose

Find entire path of dictionary concept for the given string. (If not present, don't add the word.)

## Syntax

```
returnPathString = findwordpath(wordString)
```

```
returnPathString - type: str

wordString - type: str
```

## Returns

If it exists, return the path to it. If it does not, return an empty string.

## Remarks

The dictionary is a specialized part of the KB hierarchy used to store and lookup words. You can see it with the KB editor, under **concept **> **sys** > **dict**. In order to speed up access to the dictionary, it is indexed by letters of the alphabet. The function `findwordpath` finds the complete path to a word, if it is already in the dictionary, including the parent concept names in the KB hierarchy. `findwordpath` includes the whole path, whereas `wordindex` only finds the parent concept. `findwordpath` is different from `wordpath` in that `wordpath` will create the entry in the dictionary if it is not there already, while `findwordpath` will not create the entry.

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

[dictfindword](dictfindword.md), [wordindex](wordindex.md), [wordpath](wordpath.md), [Knowledge Base Functions](Table_of_Knowledge_Base_Functions.md)
