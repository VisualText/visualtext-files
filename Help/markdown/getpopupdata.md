# getpopupdata

## Purpose

Get data from a popup window invoked by a call to [exittopopup](exittopopup.md)() in a preceding pass of an analyzer.

## Syntax

```
return_str = getpopupdata()
```

```
return_str - Data the user typed into the popup window 
```

## Returns

The data from user type-in.

## Remarks

The Database1 sample analyzer illustrates use of this function to interactively query a database.  The **[interactive](interactive.md)**() function is useful for determining if the analyzer is running inside VisualText or not.

## Example

```
# A pass of the analyzer.
```

```
@CODE
```

```
if (interactive())
```

```
  exittopopup("Enter database statement:","askfortext");
```

```
@@CODE
```

```
# A subsequent pass of the analyzer.
```

```
@CODE
```

```
if (interactive())
```

```
  G("command") = getpopupdata();
```

```
else
```

```
  G("command") = "SELECT * FROM table33;";
```

```
@@CODE
```

## See Also

[Database1 Analyzer](Sample_Analyzers/Database1_Analyzer.md)

[exittopopup](exittopopup.md)

[interactive](interactive.md)
