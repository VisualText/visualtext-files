# urltofile

## Purpose

Fetch a page from the web using the given URL and writing to the given file name.

## Syntax

```
returnedBool = urltofile(urlStr, fileStr)
```

```
returnedBool - type: bool (0 or 1)
```

```
urlStr - type: str
```

```
fileStr - type: str
```

## Returns

True if fetched the web page successfully.

## Remarks

This function can serve as the basis for a web traversal capability.

## Example

@CODE

urltofile("http://www.textai.com", "c:\\textai_com.htm");

## See Also

[Web Functions](Table_of_Web_Functions.md)
