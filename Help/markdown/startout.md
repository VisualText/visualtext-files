[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# startout

## Purpose

Divert standard output to the main output file, set by the caller of the analyzer.

## Syntax

```
startout()
```

## Returns

Nothing. This is a side-effecting CODE action: it opens the caller-supplied main output file (for appending) and diverts file-less output to it; if no output file was supplied, file-less output goes to standard output. It returns no value to NLP++.

## Remarks

Old-style. The default output file is **output.txt.**

## Example

```
@CODE

startout();           # Divert file-less output to the main output file.

print("done\n");      # Goes to the diverted output file.

stopout();            # Stop diverting.
```

## See Also

[fileout](fileout.md), [stopout](stopout.md), [CODE Actions](NLP_PP_Stuff/AT-CODE_Actions.md#tables_of_code)
