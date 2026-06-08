[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# unpackdirs

## Purpose

Unpack directory names from a full directory path string.

## Syntax

```
str array = unpackdirs(dir_str)
```

## Returns

## Remarks

Now the split function is available also, for getting at the components of a file path.

## Example

```
# This code gets each component directory of the
```

```
# current input file path.
```

```
@CODE
```

```
G("array") = unpackdirs(G("$input"));
```

```
"output.txt" << "file=" << G("$input") << "\n";
```

```
"output.txt" << "dirs=" << G("array") << "\n";
```

```
"output.txt" << "split=" << split(G("$input"),"\\") << "\n";
```

```
@@CODE
```

```
A sample output looks like:
```

```
file=c:\apps\myanalyzer\input\misc\xxx.txt
```

```
dirs=apps myanalyzer input misc
```

```
split=c: apps myanalyzer input misc xxx.txt
```

## See Also

[String Functions](Table_of_String_Functions.md), [split](split.md)
