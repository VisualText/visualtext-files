# hitconf

## Purpose

Calculate the keyword density.

## Syntax

```
returnedNum = hitconf(hitsNum, totalNum, fudgeNum)
```

```
returnedNum - type: int

hitsNum - type: int

totalNum - type: int

fudgeNum - type: int
```

## Returns

Returns a percent confidence as an integer between 0 and 100.

## Remarks

Useful as a way to convert density of hits in a file to a confidence value. For example, if the total words in a file were 100 and there were 5 hits of a certain topic, then hitconf could compute a confidence for that topic. The fudge factor typically varies from 3 to 20 or more. Empirically you can determine what works best.

## Example

```
@CODE

G("confidence") = hitconf(5, 100, 17);

@@CODE
```

## See Also

[Special Functions](Table_of_Special_Functions.md)
