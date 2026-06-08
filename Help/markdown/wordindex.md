[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# wordindex

## Purpose

Fetch index entry for dictionary concept.  This finds where a word should be inserted into the dictionary.

## Syntax

```
returnIndexCon = wordindex(wordString)
```

```
returnIndexCon - type: con

wordString - type: str
```

## Returns

Handle on the concept location of where *wordString* belongs in dictionary.

## Remarks

The dictionary is a specialized part of the KB hierarchy used to store and lookup words. You can see it with the KB editor, under **concept** > **sys** > **dict**. In order to speed up access to the dictionary, it is indexed by letters of the alphabet. The function `wordindex` finds the index of a word, whether or not it is already in the dictionary.

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

[addword](addword.md), [dictfindword](dictfindword.md), [findwordpath](findwordpath.md), [wordpath](wordpath.md), [Knowledge Base Functions](Table_of_Knowledge_Base_Functions.md)
