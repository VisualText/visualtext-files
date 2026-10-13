[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# $os

## Purpose

Find out which operating system the engine is running on.

## Syntax

```
returnedString = variableType("$os")
```

```
returnedString - type: str

variableType - type: G
```

## Returns

`windows`, `linux` or `macos`.

## Remarks

Use it where an analyzer has to do something differently per platform, such as building a file path or choosing the command for [system](system.md).

**NEW 4.2.15**

## Example

```
@CODE
if (G("$os") == "windows")
    system("dir > listing.txt");
else
    system("ls > listing.txt");
@@CODE
```

## See Also

[$dev]($dev.md), [system](system.md), [Special Variables](NLP_PP_Stuff/Special_Variables.md#table)
