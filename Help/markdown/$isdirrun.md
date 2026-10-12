[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# $isdirrun

## Purpose

Check if the engine is processing a directory of files instead of an individual file. Returns 1 if it is analyzing a directory or a stream of files from `nlp -STDIN`, else 0.

## Syntax

```
returnedBoolean = variableType("$isdirrun")
```

```
returnedBoolean - type: int

variableType - type: G
```

## Returns

Returns 1 if processing a directory or an `-STDIN` stream, 0 if not.

## Remarks

A directory run loads the analyzer and its knowledge base once and then analyzes every file in the directory. The knowledge base is not reloaded between files, so whatever one file adds to it is still there for the next. Use [$isfirstfile]($isfirstfile.md) to reset knowledge-base state at the start of a run and [$islastfile]($islastfile.md) to write out results gathered across all the files.

**NEW 4.2.6** `nlp -STDIN` does the same for files that are not all known up front. The engine loads once, then reads one input file path per line from standard input until a blank line or end of input, and analyzes each file as a directory run would: `$isdirrun` is 1 and the knowledge base carries over from file to file.

```
dir /b /s C:\corpus\*.txt | nlp -ANA myanalyzer -WORK C:\nlp-engine -STDIN
find corpus -name '*.txt' | nlp -ANA myanalyzer -WORK ~/nlp-engine -STDIN
```

Only the line after a file says whether it was the last one, so each file is analyzed once the next line (or the end of input) has been read. That suits piping in a list of files; a caller that waits for one file's results before sending the next path will wait forever. A path that does not exist is reported and skipped, and a relative path that is not found as given is looked for in the analyzer's `input` folder.

Loading a large analyzer takes several seconds, so this matters most for many small files: five short documents through the parse-en-us analyzer took 40.8 seconds as five separate runs and 8.0 seconds as one `-STDIN` run.

## Example

```
@CODE
    if (G("$isdirrun")) {
        "summary.txt" << "Processing a directory of files.\n";
    }
@@CODE
```

## See Also

[$isfirstfile]($isfirstfile.md), [$islastfile]($islastfile.md), [$inputpath]($inputpath.md), [Special Variables](NLP_PP_Stuff/Special_Variables.md#table)
