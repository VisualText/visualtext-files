[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# system

## Purpose

Execute string *commandStr* as operating system command.

## Syntax

```
returnedBool = system(commandStr)
```

```
returnedBool - type: bool

commandStr - type: str
```

## Returns

True if successful execution of command.

## Remarks

An "escape to the shell" from inside NLP++.

## Example

```
@CODE

system("dir > c:\\listing.txt"); # List contents of current working directory.

@@CODE
```

## See Also

[Special Functions](Table_of_Special_Functions.md)
