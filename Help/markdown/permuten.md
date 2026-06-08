# permuten

## Purpose

Randomly permute N integers 0 to N-1, such that none are in normal order.

## Syntax

```
returnedArr = permuten(totNum)
```

```
returnedArr - type: array of int

totNum - type: int
```

## Returns

Array of permuted integers.

## Remarks

Assures that array element k will not be the integer k.  Zero-based numbering from 0 to N-1.

## Example

```
@CODE

"output.txt" << "0 1 2 3 4" << "\n";

"output.txt" << permuten(5) << "\n";

@@CODE
```

```
Outputs something like:
```

```
0 1 2 3 4

3 0 4 1 2
```

## See Also

[Special Functions](Table_of_Special_Functions.md)
