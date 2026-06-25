[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# debug

## Purpose

Place a C++ breakpoint at a particular rule, for VisualText / engine developers. Used as a PRE action it succeeds unconditionally (a no-op); it may also be called as a statement.

## Syntax

```
<fromRuleEltNumber,toRuleEltNumber> debug;
```

```
debug();
```

```
fromRuleEltNumber - type: int

toRuleEltNumber - type: int
```

## Returns

Nothing. `debug()` succeeds unconditionally and performs no action at runtime.

## Remarks

`debug` can appear in the PRE, CHECK, and POST regions. It lets a developer set a breakpoint in the engine's C++ source (e.g. in MS Visual C++) that is hit when a particular rule is evaluated.

## Example

```
@PRE

<1,1> debug();

@RULES

_xNIL <- _xALPHA @@
```

## See Also

[Special Functions](Table_of_Special_Functions.md), [PRE Actions](NLP_PP_Stuff/AT-PRE_Actions.md)
