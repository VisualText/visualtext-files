# Table of String Functions

The NLP++ functions used to operate on strings are listed here in table form for easy reference.  For examples of these functions, refer to the individual function pages included in the String Functions section.

The return types include:  **STR** (string), **STR ARRAY** (string array), **INT** (integer), and **BOOL** (Boolean).  Boolean type is currently implemented by integer **1** (or non-zero) for **true** and **0** for **false**.

| **FUNCTION NAME** | **RETURNS** | **DESCRIPTION** |
| --- | --- | --- |
| [deaccent(str)](deaccent.md) | STR | Convert string to replace accented characters. |
| [**dejunk(str)**](dejunk.md) | STR | Convert string to replace all but simple ASCII chars. **New in 2.6.0.3.** |
| [flt(str)](flt.md) | FLOAT | Convert string or int to float, if possible. |
| [l**evenshtein(str1,str2)**](levenshtein.md) | INT | Levenshtein edit-distance between two strings.** New in 2.0.2.9** |
| [**num(str)**](num.md) | **INT** | Convert string to number, if possible. (Also accepts num arg). |
| [split(str, char_str)](split.md) | STR ARRAY | Split a string using the given char as separator. |
| [stem(str)](stem.md) | STR | Compute stem of noun and verb. Return lowercase string. |
| [**strchar(str, num)**](strchar.md) | **STR** | Index to numth char of string |
| [**strchr(str, ch_str)**](strchr.md) | **STR** | Find first occurrence of char in string. Return string headed by char. |
| [strchrcount(str, ch_str)](strchrcount.md) | INT | Count the occurrences of a character in a string. |
| [**strclean(str)**](strclean.md) | **STR** | Remove leading, trailing, and repeat whitespace separators. |
| [**strcontains(str1,str2)**](strcontains.md) | **BOOL** | Check if str1is contained in str2. |
| [**strcontainsnocase(str1,str2)**](strcontainsnocase.md) | **BOOL** | Check if str1 is contained in str2, ignoring letter case. |
| [**strendswith(str, suffix_str)**](strendswith.md) | **BOOL** | Does given str ends with given suffix_str |
| [**strstartswith(str, suffix_str)**](strstartswith.md) | **BOOL** | Does given str starts with given suffix_str |
| [**strequal(str1,str2)**](strequal.md) | **BOOL** | Check if str1 is identical to str2. |
| [**strisalpha(str)**](strisalpha.md) | **BOOL** | Check if str is all alphabetic chars. |
| [**strisdigit(str)**](strisdigit.md) | **BOOL** | Check if str is all numeric chars. |
| [strislower](strislower.md) | BOOL | Check if first char of string is lowercase |
| [strisupper](strisupper.md) | BOOL | Check if first char of string is uppercase. |
| [striscaps](striscaps.md) | BOOL | Check if the entire string is uppercase. |
| [**strnotequal(str1,str2)**](strnotequal.md) | **BOOL** | Check if str1 differs from str2. |
| [**strequalnocase(str1,str2)**](strequalnocase.md) | **BOOL** | Check if str1 is identical to str2, ignoring letter case. |
| [**strnotequalnocase(str1,str2)**](strnotequalnocase.md) | **BOOL** | Check if str1 differs from str2, ignoring letter case. |
| [**strlessthan(str1,str2)**](strlessthan.md) | **BOOL** | Check if str1 is lexically before str2. |
| [**strgreaterthan(str1,str2)**](strgreaterthan.md) | **BOOL** | Check if str1 is lexically after str2. |
| [**strlength(str)**](strlength.md) | **INT** | Return length of string. |
| [**strpiece(str, start_num, end_num)**](strpiece.md) | **STR** | Fetch substring of string from start_num to end_num indexes. Zero-based |
| [**struniquechars(str)**](struniquechars.md) | **STR** | Find all the unique characters in a string. |
| [**strrchr(str, ch_str)**](strrchr.md) | **STR** | Find last occurrence of char in string. Return string headed by char |
| [**strsubst(str, old_str, new_str)**](strsubst.md) | **STR** | Replace substring old_str of a string str with new_str. |
| [**strtolower(str)**](strtolower.md) | **STR** | Convert string to lowercase. |
| [**strtotitle(str)**](strtotitle.md) | **STR** | Convert string to title capitalization. |
| [**strtoupper(str)**](strtoupper.md) | **STR** | Convert string to uppercase. |
| [**strtrim(str)**](strtrim.md) | **STR** | Remove leading and trailing whitespace from str. |
| [**strwrap(str, num)**](strwrap.md) | **STR** | Break string at specified length. |
| [**str(num)**](str.md) | STR | Convert numeric value to string. (Also accepts string arg). |
| [strescape(str, charsToEscapeStr, escapeStr)](strescape.md) | STR | Escape characters in string. |
| [**strunescape(str, escapedCharsStr, escapeStr)**](strunescape.md) | **STR** | Unescape characters in string. |
| [suffix(wordStr, suffixStr)](suffix.md) | BOOL | True if suffixStr may be the suffix of wordStr. |
| [unpackdirs(dir_str)](unpackdirs.md) | STR ARRAY | Unpack directory names from a full directory path string. |
| [xmlstr(str)](xmlstr.md) | STR | Convert chars to appropriate chars for an XML/HTML file. |
|   |   |   |

## See Also

[Special Functions](Table_of_Special_Functions.md)

[Knowledge Base Functions](Table_of_Knowledge_Base_Functions.md)

[Formatting and I/O Functions](Table_of_Formatting_and_I_O_Functions.md)

[Parse Tree Functions](Table_of_Parse_Tree_Functions.md)

[Spelling Functions](Table_of_Spelling_Functions.md)
