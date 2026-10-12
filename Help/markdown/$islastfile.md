[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# $islastfile

## Purpose

Checks to see if the current file is the last file being analyzed in a directory or in an `nlp -STDIN` stream.

## Syntax

```
returnedBoolean = variableType("$islastfile")
```

```
returnedBoolean - type: int

variableType - type: G
```

## Returns

Returns 1 if the current file is the last file, 0 if not.

## Remarks

Use `$islastfile` to write results collected across every file of a directory run, since the knowledge base carries over from file to file (see [$isdirrun]($isdirrun.md)). For a single-file run `$islastfile` is also 1.

**NEW 4.2.6** In an `nlp -STDIN` stream, the last file is the one before the blank line or end of input that ends the stream. The engine reads one line ahead so it can set `$islastfile` before that file is analyzed.

## Example

```
@CODE
    if (G("$islastfile")) {
        "summary.txt" << "Done processing all files.\n";
    }
@@CODE
```

## See Also

[$isdirrun]($isdirrun.md), [$isfirstfile]($isfirstfile.md), [$inputpath]($inputpath.md), [Special Variables](NLP_PP_Stuff/Special_Variables.md#table)
