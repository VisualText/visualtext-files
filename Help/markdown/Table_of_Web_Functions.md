[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# Table_of_Web_Functions

NLP++ functions are provided to help process web pages.

**Note:** The User Project within each analyzer project includes the functions user::analyzefile and user::analyzebuf.  In concert with the NLP++ web functions, a web traversal capability can be built and run within VisualText.  (E.g., a web crawler or web spider.)  By integrating web traversal with HTML web page analysis, one may construct a focused or intelligent web crawler.

| **FUNCTION NAME** | **RETURNS** | **DESCRIPTION** |
| --- | --- | --- |
| [resolveurl(base_str,embed_str)](resolveurl.md) | STR | Create an absolute URL from embed_str, using base_str as a base URL. |
| [**urlbase(url_str)**](urlbase.md) | **STR** | (Superseded by resolveurl) Fetch a normalized, partial URL ending in a directory path. Aids in resolving relative URLs within a web page.** (New in 1.6)** |
| [**urltofile(url_str,file_str)**](urltofile.md) | NONE | Fetch the web page specified by the url_str into a file located at file file_str on the local machine. **(New in 1.6)** |
|   |   |   |

## See Also

[Functions](NLP_PP_Stuff/Functions.md)
