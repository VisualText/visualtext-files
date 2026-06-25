[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# today

## Purpose

Format the current date and time as a string.

## Syntax

```
returnedStr = today()
```

```
returnedStr - type: str
```

## Returns

Return the current date and time as a string.

## Remarks

`today()` takes no arguments and returns the current local date and time. It does not invoke the operating-system shell; for that, use [system](system.md).

## Example

```
@CODE

"output.txt" << today() << "\n";

@@CODE
```

## See Also

[Special Functions](Table_of_Special_Functions.md), [Formatting and I/O Functions](Table_of_Formatting_and_I_O_Functions.md)
