[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# deaccent

## Purpose

Convert string to remove accented characters.

## Syntax

```
returnedString = deaccent(string)
```

```
returnedString - type: str

string - type: str
```

## Returns

String with accented characters converted to non-accented variants.

## Remarks

## Example

```
@CODE
G("out") = deaccent("café résumé");
"output.txt" << G("out") << "\n";
# writes: cafe resume
@@CODE
```

## See Also

[String Functions](Table_of_String_Functions.md)
