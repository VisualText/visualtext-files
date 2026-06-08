[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# Table of Spelling Functions

The NLP++ functions used to check spelling are listed here in table form for easy reference.  For examples of these functions, refer to the individual function pages included in the Spelling Functions section.

Return types can be **STR** (string), **INT** (integer) or **BOOL** (Boolean).  Boolean type is currently implemented by integer **1** (or non-zero) for **true** and **0** for **false**.

| **FUNCTION NAME** | **RETURNS** | **DESCRIPTION** |
| --- | --- | --- |
| [**spellcandidates(word_str)**](spellcandidates.md) | **STR** | Make a list of space separated candidates for spell-correcting given word. |
| [**spellcorrect(word_str)**](spellcorrect.md) | **STR** | Correct spelling of word. If word is not known, returns best spelling guess. |
| [**spellword(word_str)**](spellword.md) | **BOOL** | Check if word is a known English word. |
| [**strspellcandidate(word_str, list_str)**](strspellcandidate.md) | **STR** | Select best spell-correct candidate for a word, given a list of space-separated candidates (as returned by spellcandidates, e.g.) |
| [**strspellcompare(str1, str2)**](strspellcompare.md) | **INT** | Measure spelling "distance" between two given words. The smaller the number, the fewer the corrections to get from one to the other. |

## See Also

[Special Functions](Table_of_Special_Functions.md)

[Knowledge Base Functions](Table_of_Knowledge_Base_Functions.md)

[Formatting and I/O Functions](Table_of_Formatting_and_I_O_Functions.md)

[Parse Tree Functions](Table_of_Parse_Tree_Functions.md)

[String Functions](Table_of_String_Functions.md)
