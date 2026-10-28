[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# $datum

## Purpose

Get the string the caller passed with `nlp -DATUM value`, or with `datum=` from Python or Node.js. Use it to let one analyzer serve several callers: the output format they want, a mode, a customer name.

## Syntax

```
returnedString = variableType("$datum")
```

```
returnedString - type: str

variableType - type: G
```

## Returns

The string passed with `-DATUM`, or 0 if none was passed.

## Remarks

The value is set for one run (from the command line) or one `analyze()` call (from Python or Node.js); it does not carry over to the next call.

## Example

```
@CODE
    if (G("$datum") == "json")
        G("format") = "json";
    else
        G("format") = "text";
@@CODE
```

```
nlp -ANA myanalyzer -WORK C:\nlp-engine -DATUM json input\text.txt
```

```
NLPPlus.analyze(text, "myanalyzer", datum="json")
```

## See Also

[Command Line](vscode/commandline.md), [$dev]($dev.md), [Special Variables](NLP_PP_Stuff/Special_Variables.md#table)
