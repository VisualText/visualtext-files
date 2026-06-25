[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# printr

## Purpose

**OBSOLETE.**  Print the text for the rule element range from **number1** to **number2** to standard output.

## Syntax

```
printr(number1, number2)
```

```
number1 - type: int

number2 - type: int
```

## Returns

Writes the matched input text spanning rule elements **number1** through **number2** to standard output.  This action returns no value.

## Remarks

Output always goes to standard output, not to a file.  Use **prrange** to print a rule element range to a file.

## Example

```
@POST
  printr(1, 3);
@@POST

@RULES
_company <- _name [s] _suffix @@
```

## See Also

[print](print.md), [prlit](prlit.md), [prrange](prrange.md), [POST Actions](NLP_PP_Stuff/AT-POST_Actions.md#table_of_@POST_Actions)
