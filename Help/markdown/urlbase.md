# urlbase

## Purpose

Extract a normalized directory path from a URL.

## Syntax

```
returnedStr = urlbase(urlStr)
```

```
returnedStr - type: str
```

```
urlStr - type: str
```

## Returns

The normalized URL ending in directory path.

## Remarks

As an aid to converting relative URLs to absolute URLs when processing a web page.

## Example

@CODE

"output.txt" << urlbase("http://www.x.com/pqr/a.txt") << "\n";

"output.txt" << urlbase("http://www.abc.com/") << "\n";

"output.txt" << urlbase("http://www.x.com/pqr/") << "\n";

prints out:

http://www.x.com/pqr

http://www.abc.com

http://www.x.com/pqr

## See Also

[Web Functions](Table_of_Web_Functions.md)
