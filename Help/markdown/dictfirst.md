# dictfirst

## Purpose

Fetch the first word in the KB dictionary hierarchy.

## Syntax

```
wordConcept = dictfirst()
```

```
wordConcept - type: con
```

## Returns

The first word-concept in lexicographic traversal of the KB dictionary hierarchy.

## Remarks

The dictionary is a specialized part of the KB hierarchy used to store and lookup words.  dictfirst and dictnext provide a convenient way to traverse the dictionary without worrying about the details of its implementation.  (I.e., the presence of layers of dictionary indexing concepts.)

## Example

```
@CODE
```

```
L("con") = dictfirst();
```

```
while (L("con"))
```

```
  {
```

```
  "output.txt" << conceptname(L("con") << "\n";
```

```
  L("con") = dictnext(L("con"));
```

```
  }
```

Prints a list of the dictionary entries, one per line.

## See Also

[dictnext](dictnext.md), [Knowledge Base Functions](Table_of_Knowledge_Base_Functions.md)
