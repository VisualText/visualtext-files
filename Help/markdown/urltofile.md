[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# urltofile

## Purpose

Fetch a page from the web using the given URL and writing to the given file name.

## Syntax

```
returnedStr = urltofile(urlStr, fileStr)
```

```
returnedStr - type: str
```

```
urlStr - type: str
```

```
fileStr - type: str
```

## Returns

On success, returns a non-empty string identifying the fetched resource (and writes the page to fileStr); on failure, returns no value (an empty result).

## Remarks

This function can serve as the basis for a web traversal capability. Web fetching is gated by a build-time web option and is not implemented in the Linux build (where it returns no value).

## Example

@CODE

urltofile("http://www.textai.com", "c:\\textai_com.htm");

## See Also

[Web Functions](Table_of_Web_Functions.md)
