[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# resolveurl

## Purpose

Convert a relative URL to an absolute URL.

## Syntax

```
str = resolveurl(baseurl_str, embeddedurl_str)
```

## Returns

An absolute URL built from the base URL and the embedded URL.

## Remarks

Supersedes urlbase

## Example

@CODE

"output.txt" << resolveurl("http://www.abcd.edu/x/y/z.html", "../gif/img1.gif")

<< "\n";

prints out:

http://www.abcd.edu/x/gif/img1.gif

## See Also

[Web Functions](Table_of_Web_Functions.md)
