[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# cout

## Purpose

Send output to standard output or user-supplied stream.

## Syntax

```
returnedOstream = cout()
```

```
returnedOstream - type: ostream
```

## Returns

The standard output stream (or the user-supplied stream, in standalone or embedded analyzers), for use with the `<<` output operator.

## Remarks

For use in embedded or standalone analyzers.  User may supply an output stream to an API call such as nlp->analyze().  Then sending output to cout() will write to the user-supplied output stream.

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
   G("out") = "out.txt";
```

```
else
```

```
   G("out") = cout();
```

```
G("out") << "Hello output stream!" << "\n";
```

```
@@CODE
```

## See Also
