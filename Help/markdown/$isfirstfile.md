[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# $isfirstfile

## Purpose

Checks to see if the current file is the first file being analyzed in a directory or in an `nlp -STDIN` stream.

## Syntax

```
returnedBoolean = variableType("$isfirstfile")
```

```
returnedBoolean - type: bool

variableType - type: G
```

## Returns

Returns 1 if the current file is the first file, 0 if not.

## Remarks

The knowledge base is loaded once for a directory run or a `-STDIN` stream and is not reloaded between files (see [$isdirrun]($isdirrun.md)). Do once-per-run setup when `$isfirstfile` is 1, such as clearing a knowledge-base concept the run will fill in or writing a header. For a single-file run `$isfirstfile` is also 1.

## Example

```
@CODE
    if (G("$isfirstfile")) {
        "summary.txt" << "Header\n";
    }
@@CODE
```

## See Also

[$isdirrun]($isdirrun.md), [$islastfile]($islastfile.md), [$inputpath]($inputpath.md), [Special Variables](NLP_PP_Stuff/Special_Variables.md#table)
