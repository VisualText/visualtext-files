# pnvarnames

## Purpose

Fetch all a node's variable names into an array (i.e., a multi-valued variable).

## Syntax

```
returnedArray = pnvarnames(aPnode)
```

```
returnedArray - type: array of strings

aPnode - type: pnode
 
```

## Returns

## Remarks

A quick way to get a node's variables.

## Example

```
# Print out variable name followed by
 its values, for each variable in each _TEXTZONE node.
```

```
@POST
```

```
  "output.txt"
 << N("$text",1) << "\n";
```

```
  S("names")
 = pnvarnames(N(1));
```

```
  "output.txt"
 << S("names") << "\n";
```

```
  while
 (S("names")[++G("ii")])  #
 Traverse node's variables.
```

```
    {
```

```
    "output.txt"
 << S("names")[ G("ii") ] << ": ";
```

```
    G("val")
 = pnvar(N(1),S("names")[ G("ii") ]);
```

```
    "output.txt"
 << G("val") << "\n";     #
 Print variable's values.
```

```
    }
```

```
  "output.txt"
 << "\n";
```

```
@RULES
```

```
_xNIL <- _TEXTZONE @@
```

## See Also
