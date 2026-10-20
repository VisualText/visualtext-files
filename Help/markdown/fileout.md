[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# fileout

## Purpose

Open **fileName** for appending. **FileName** becomes a variable useable in print actions with a file argument, e.g. **prlit()**.

## Syntax

```
fileout(fileName)
```

```
fileName - type: str
```

## Returns

Nothing. This is a side-effecting CODE action: it opens **fileName** for appending in the current output area and registers a variable named **fileName** holding that output stream, which print actions (e.g. **prlit**) can then target. It returns no value to NLP++.

## Remarks

Old-style.  Use NLP++ syntax such as

"file.txt" << "hello\n";

to create files in the current output area.  An absolute path is used as given, so `L("f") = G("$apppath") + "/out.txt"; L("f") << "hello\n";` writes to the analyzer folder (engine 4.2.39: it used to write nothing). If the file can't be opened, the engine says so once, in `err.log` and on standard error.  Or, use **openfile** to place files anywhere on your file system.

## Example

```
@CODE

fileout("companies.txt");        # Open companies.txt for appending.

prlit("companies.txt","Acme\n"); # Write a line to it.
```

## See Also

[openfile](openfile.md), [startout](startout.md), [stopout](stopout.md), [prlit](prlit.md), [CODE Actions](NLP_PP_Stuff/AT-CODE_Actions.md#tables_of_code)
