[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# $passnum

## Purpose

Get the number of the pass currently being executed.

## Syntax

```
returnedInt = variableType("$passnum")
```

```
returnedInt - type: int

variableType - type: G
```

## Returns

The current pass number (the position of the running pass in the analyzer sequence).

## Remarks

Pass numbering reflects the order of passes in the analyzer sequence. See also [$rulenum]($rulenum.md) for the current rule number within the pass.

## Example

```
@CODE
    L("file") = "output.txt";
    L("file") << "Pass: " << G("$passnum") << "\n";
@@CODE
```

## See Also

[$rulenum]($rulenum.md), [Special Variables](NLP_PP_Stuff/Special_Variables.md#table)
