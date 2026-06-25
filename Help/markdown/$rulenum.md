[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# $rulenum

## Purpose

Get the number of the rule currently being executed within the current pass.

## Syntax

```
returnedInt = variableType("$rulenum")
```

```
returnedInt - type: int

variableType - type: G
```

## Returns

The current rule number within the current pass.

## Remarks

Rule numbering is relative to the pass currently executing. See also [$passnum]($passnum.md) for the current pass number.

## Example

```
@CODE
    L("file") = "output.txt";
    L("file") << "Pass " << G("$passnum") << " rule " << G("$rulenum") << "\n";
@@CODE
```

## See Also

[$passnum]($passnum.md), [Special Variables](NLP_PP_Stuff/Special_Variables.md#table)
