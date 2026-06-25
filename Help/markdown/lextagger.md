[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# lextagger

## Purpose

Invoke the third-party LexTagger part-of-speech tagger and update the current parse tree with its results.

## Syntax

```
returnedInt = lextagger()
```

```
returnedInt - type: int
```

## Returns

Returns 1 after invoking the tagger. On Linux this function is unimplemented and reports an error.

## Remarks

Lextagger takes no arguments and assumes the current parse tree has already been tokenized.

It locates the bundled tagger at `$VISUALTEXT\apps\LexTagger-1.0`, copies the current input file into the tagger's work area, runs the tagger via its `run.bat` script, then reads the tagger's output file and updates the parse tree with the resulting part-of-speech tags.

Because it shells out to an external program and relies on the `VISUALTEXT` environment variable and a Windows batch file, lextagger is Windows-only; the Linux build returns an error.

## Example

```
@CODE

lextagger();

@@CODE
```

## See Also

[findana](findana.md)

[mkdir](mkdir.md)

[system](system.md)

[today](today.md)
