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

True if successful execution of command.

## Remarks

Mkdir depends on the machine or operating system in use.  Recommended to create one "level" of a directory path at a time, to assure that the code is portable.

## Example

```
@CODE

mkdir("c:\abc\myfolder"); # This will work on Windows OS even if abc doesn't exist.

@@CODE
```

## See Also

[system](system.md), [today](today.md), [Special Functions](Table_of_Special_Functions.md)
