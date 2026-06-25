[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# interactive

## Purpose

See if analyzer is operating in an interactive environment (e.g., in VisualText)

## Syntax

```
returnedBool = interactive()
```

```
returnedBool - type: bool
 
```

## Returns

True if analyzer is in an interactive environment.

## Remarks

In standalone or embedded analyzer, can call **nlp->setInteractive(bool)** to set this (see the NLP.h API file in VisualText/include/API/lite/nlp.h).

## Example

```
@CODE
```

```
# In VisualText, send output to a file, but outside of VisualText, direct outputs to a user-supplied buffer.
```

```
if (interactive())
```

```
   G("out") = "buf.txt";
```

```
else
```

```
   G("out") = cbuf();
```

```
G("out") << "Hello output!" << "\n";
```

```
@@CODE
```

## See Also

[cbuf](cbuf.md), [cout](cout.md), [Special Functions](Table_of_Special_Functions.md)
