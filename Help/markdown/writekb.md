[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# writekb

## Purpose

Dumps the entire KB currently in memory to the kb/user directory which includes a word.kb, attrs.kb, and main.kb file.

## Syntax

```
returnedBoolean = writekb(directory_str)
```

```
returnedBoolean - type: bool

directory_str - type: str
```

## Returns

Returns **1** if the KB was written successfully and **0** otherwise.

## Remarks

The entire KB currently in memory is written to the given directory as a set of files (word.kb, attrs.kb, and main.kb). If no directory argument is given, a warning is written to the output log.

## Example

```
@CODE

writekb(G("$apppath") + "\\kb\\user");
```

## See Also

[kbdumptree](kbdumptree.md) [take](take.md) [Knowledge Base Functions](Table_of_Knowledge_Base_Functions.md)
