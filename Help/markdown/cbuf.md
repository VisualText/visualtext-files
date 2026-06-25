[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# cbuf

## Purpose

Send output to user-supplied buffer.

## Syntax

```
returnedOstream = cbuf()
```

```
returnedOstream - type: ostream
```

## Returns

The user-supplied output buffer stream, for use with the `<<` output operator.

## Remarks

For use in embedded or standalone analyzers.  User may supply an output buffer to an API call such as nlp->analyze().  Then sending output to cbuf() will write to the user-supplied output stream.

## Example

```
@CODE
```

```
# In VisualText, output to a file.  Outside VisualText, output to user-supplied buffer.
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
G("out") << "Hello output buffer!" << "\n";
```

```
@@CODE
```

## See Also

[cout](cout.md), [coutreset](coutreset.md), [openfile](openfile.md), [interactive](interactive.md), [Formatting and I/O Functions](Table_of_Formatting_and_I_O_Functions.md)
