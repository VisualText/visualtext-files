[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# stopout

## Purpose

Stop diverting standard output to the main output file. Subsequent file-less output is to standard output.

## Syntax

```
stopout()
```

## Returns

Nothing. This is a side-effecting CODE action: it closes the diverted main output file (unless output was going to standard output) and resets the output handle, so subsequent file-less output goes to standard output. It returns no value to NLP++.

## Remarks

Old-style. Reports an error if no output file is currently open (i.e. **startout** was not called first).

## Example

```
@CODE

startout();           # Divert file-less output to the main output file.

print("done\n");      # Goes to the diverted output file.

stopout();            # Stop diverting; close the file.
```

## See Also

[fileout](fileout.md), [startout](startout.md), [CODE Actions](NLP_PP_Stuff/AT-CODE_Actions.md#tables_of_code)
