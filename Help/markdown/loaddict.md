[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# loaddict

## Purpose

Load a single dictionary file (`.dict`) from the analyzer's `kb/user` directory into the conceptual grammar (the KB currently in memory).

## Syntax

## `returnedBoolean = loaddict(file_str)`

```
returnedBoolean - type: bool (1 or 0)
```

```
file_str - type:  str
```

## Returns

Returns **1** if the file was loaded successfully and **0** otherwise (for example, if the file is not found in `kb/user`).

## Remarks

`file_str` is the **name of a file in the analyzer's `kb/user` directory**, not a full path. The file is resolved as `<app>/kb/user/<file_str>`.

A `.dict` file uses the flat `word attr=val ...` format, one word per line. `loaddict` adds those words and their attributes to the KB already in memory. If a `.kbb` file with the same stem exists in `kb/user`, its `dictionary` concept is used as the ambiguity KB for the words being added, mirroring how the engine pairs dictionaries with their KB during normal startup.

To load an indented hierarchy file instead, use [loadkbb](loadkbb.md).

## Example

```
@CODE
```

```
if (loaddict("extra.dict"))
    "loaded extra.dict" >> G("$apppath") + "\\load.log";
```

```
@@CODE
```

This loads `<app>/kb/user/extra.dict` into the conceptual grammar.

## See Also

[loadkbb](loadkbb.md) &nbsp;|&nbsp; [take](take.md) &nbsp;|&nbsp; [writekb](writekb.md) &nbsp;|&nbsp; [dictfindword](dictfindword.md) &nbsp;|&nbsp; [Knowledge Base Functions](Table_of_Knowledge_Base_Functions.md)
