# lookup

## Purpose

Look up the values of named global variable *var* in the file named *fileName* and modify the named flag *flag*.

## Syntax

```
lookup(var, fileName, flag)
```

```
var - type: str

fileName - type: str

flag - type: str
```

## Returns

## Remarks

Old-style, slated for overhaul.  For most purposes, we recommend using the **spellword** function to see if something is a dictionary word.

This is a highly specialized word lookup. **Global **variable **var** has multiple words as values (assumed to be alphabetically sorted and unique). **fileName** is a file of strings, one per line. **flag** tells which bit-flag of the word's symbol table entry to modify.  See also the **unknown** function.

## Example

The code **lookup("Words", "dict.words", "word")** looks up all the values in the **Words** variable in the **dict.words** file and modifies the **word** bit-flag (which says whether the word is a proper English word).

```
@CODE

G("Words")[0] = "aardvark";

G("Words")[1] = "abacus";

gtolower("Words");

sortvals("Words");

guniq("Words");

lookup("Words","dict.words","word");



@PRE

<1,1> unknown();

@POST

N("unknown word") = 1;

@RULES

_xNIL <- _xALPHA @@
```

## See Also

[spellword](spellword.md), [unknown](unknown.md), [gtolower](gtolower.md), [guniq](guniq.md), [CODE Actions](NLP_PP_Stuff/AT-CODE_Actions.md#tables_of_code)
