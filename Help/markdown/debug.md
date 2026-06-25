[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# debug

## Purpose

Enable C++ source code debugging for VisualText developers.

## Syntax

```
NULL = debug()
```

## Returns

Nothing. `debug()` is a no-op called as a statement.

## Remarks

Enables VisualText developers to set a breakpoint in a particular rule, from a C++ development environment, e.g. MS Visual C++.

## Example

```
@POST

debug();

@RULES

_xNIL <- _xNIL @@
```

## See Also

[Special Functions](Table_of_Special_Functions.md)
