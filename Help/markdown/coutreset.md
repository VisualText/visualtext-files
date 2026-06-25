[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# coutreset

## Purpose

Rebind the output stream cout to a given file.

## Syntax

```
returnedOstream = coutreset(fileNameStr)
```

```
returnedOstream - type: ostream
```

```
fileNameStr - type: string
```

## Returns

The output stream bound to the given file (opened in append mode). Returns no value if the file could not be opened.

## Remarks

In VisualText, a way to bind where outputs to cout() are sent.

## Example

```
@CODE
```

```
# In VisualText, output to a file.  Outside VisualText, output to user-supplied stream.
```

```
if (interactive())
```

```
   coutreset("out.txt");
```

```
cout() << "Hello output stream!" << "\n";
```

```
@@CODE
```

## See Also
