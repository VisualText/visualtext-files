[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# batchstart

## Purpose

Check if a batch analysis process has just begun.

## Syntax

```
returnedBool = batchstart()
```

```
returnedBool - type: bool
```

## Returns

True if we're processing the first file in a batch, as signaled by the Batch Toggle in the VisualText GUI.

## Remarks

## Example

```
@CODE

G("startflag") = batchstart();

@@CODE
```

## See Also

[Special Functions](Table_of_Special_Functions.md)
