[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# mkdir

## Purpose

Create a new directory (i.e., folder).

## Syntax

```
returnedBool = mkdir(directoryStr)
```

```
returnedBool - type: bool

directoryStr- type: str
```

## Returns

True (1) if the directory exists afterwards, whether **mkdir** made it or it was already there. False (0) if it could not be made, for example because the path has a character the file system does not allow.

## Remarks

**mkdir** makes any missing parent directories too, the same way on Windows, Linux and macOS. Forward slashes work on every platform. Spaces in the path need no quoting.

From 4.2.31, **mkdir** creates the directory directly. Before 4.2.31 it ran the operating system's `mkdir` command, which caused these problems:

- On Windows a path with forward slashes, such as `G("$apppath") + "/output"`, made nothing.
- A path with spaces broke.
- Characters such as `&` in the path were run as commands.
- It returned true even when nothing was made.

## Example

```
@CODE

if (!mkdir(G("$apppath") + "/output/by date"))
    "output.txt" << "Could not make the output directory\n";

@@CODE
```

## See Also

[system](system.md), [today](today.md), [Special Functions](Table_of_Special_Functions.md)
