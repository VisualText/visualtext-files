[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# take

## Purpose

Execute commands in a knowledge base command file (.KB file).

## Syntax

## `returnedBoolean = take(file_str)`

```
returnedBoolean - type: bool (1 or 0)
```

```
file_str - type:  str
```

## Returns

Returns **1** if successful and **0** otherwise.

## Remarks

If a relative path is supplied, then the current analyzer project folder is assumed to be the base.

## Example

```
@CODE
```

```
take("e:\\apps\\tester\\companies.kb");

take("\\data\\myadditions.kb"); # Starts from G("$apppath"),
 project folder.
```

```
@@CODE
```

where the companies.kb file might contain the following:

```
add hier "concept" "company"
```

```
add hier "concept" "company"
 "ford"
```

```
add hier "concept" "company
 "gm"
```

```
....
```

```
quit
```

## See Also

[kbdumptree](kbdumptree.md)

[About KB Command Files](VisualText_Basics/About_KB_Command_Files.md)
