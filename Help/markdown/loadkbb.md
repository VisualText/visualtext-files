[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# loadkbb

## Purpose

Load a single knowledge base binary file (`.kbb`) from the analyzer's `kb/user` directory into the conceptual grammar (the KB currently in memory).

## Syntax

```
returnedBoolean = loadkbb(file_str)
```

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

A `.kbb` file uses the indented "dictionary" format, where indentation expresses the concept hierarchy. `loadkbb` adds the concepts in the file to the KB already in memory, hanging them off the existing hierarchy. This is the same mechanism the engine uses when it loads `*.kbb` files during normal KB startup, exposed so an analyzer can pull in an additional `.kbb` on demand.

Lines, concept names, attribute names and values can be any length. Before engine 4.2.38 a line of 2,048 or more characters silently ended the load, a value of 512 or more characters crashed the engine, and every quoted value followed by more text on its line also loaded a stray number `0`. A `.kbb` that was loaded and then saved again before 4.2.38 has those `0` values written into it, so rebuild it from its source data.

To load a flat `word attr=val ...` dictionary file instead, use [loaddict](loaddict.md).

## Example

```
@CODE
```

```
if (loadkbb("extra.kbb"))
    "load.log" << "loaded extra.kbb\n";
```

```
@@CODE
```

This loads `<app>/kb/user/extra.kbb` into the conceptual grammar.

## See Also

[loaddict](loaddict.md) &nbsp;|&nbsp; [take](take.md) &nbsp;|&nbsp; [writekb](writekb.md) &nbsp;|&nbsp; [kbdumptree](kbdumptree.md) &nbsp;|&nbsp; [Knowledge Base Functions](Table_of_Knowledge_Base_Functions.md)
