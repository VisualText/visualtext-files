# exittopopup

## Purpose

Cause current pass to exit and invoke a popup window in VisualText.

## Syntax

```
return_bool = exittopopup(message_str, type_str)
```

```
return_bool - True if successful, else false
```

```
message_str - Message for popup to display
```

```
type_str - Type of action for popup to perform ("askfortext" or "yesno")

 
```

## Returns

True if successful.

## Remarks

**exittopopup**() causes the current analyzer pass to exit and invokes a popup when in VisualText. The **[interactive](interactive.md)**() function can help the analyzer act according to whether it's inside VisualText or not.  The associated function **[getpopupdata](getpopupdata.md)()** fetches the data typed in by the user.  The Database1 sample analyzer makes use of this to query a database interactively from VisualText.

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

[getpopupdata](getpopupdata.md)

[interactive](interactive.md)
