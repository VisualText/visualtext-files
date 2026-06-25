[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# prrange

## Purpose

Print the text under a range of rule elements **number1** to **number2** to** fileName**.

## Syntax

```
prrange(fileName, number1, number2)
```

```
fileName - type: str

number1 - type: int

number2 - type: int
```

## Returns

Writes the matched input text spanning rule elements **number1** through **number2** to **fileName**.  This action returns no value.

## Remarks

The output file (**fileName**) must be set up in advance using **openfile**, **fileout** or an output statement.

## Example

```
@POST

prrange("output.txt", 1, 3);


@@POST
```

```
@RULES
_company <- _name [s] _suffix @@
```

```
@@RULES
```

## See Also

[print](print.md), [printr](printr.md), [prlit](prlit.md), [openfile](openfile.md), [fileout](fileout.md), [POST Actions](NLP_PP_Stuff/AT-POST_Actions.md#table_of_@POST_Actions)
