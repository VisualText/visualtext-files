[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# varstrs

## Purpose

Create an empty multi-string-valued **global** variable with name **varname**.

## Syntax

```
varstrs(varname)
```

```
varname - type: str
```

## Returns

## Remarks

Obsolete, slated for removal.  Use NLP++ array code instead, e.g., G("tmp") = 0; G("tmp") = "abc"; G("tmp")[1] = "def";

## Example

```
@CODE

varstrs("tmp");  # Create a global variable named "tmp".
```

## See Also

[CODE Actions](NLP_PP_Stuff/AT-CODE_Actions.md#tables_of_code)
