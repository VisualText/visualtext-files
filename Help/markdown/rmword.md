# rmword

## Purpose

Remove dictionary concept *wordString* from the KB dictionary hierarchy.

## Syntax

```
NULL = rmword(wordString)
```

```
wordString - type: str
```

## Returns

Nothing.

## Remarks

The dictionary is a specialized part of the KB hierarchy used to store and lookup words.

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

[addword](addword.md), [Knowledge Base Functions](Table_of_Knowledge_Base_Functions.md)
