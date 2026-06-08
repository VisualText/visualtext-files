# Special Rule Elements

NLP++ has a set of predefined rule elements that make writing rules easier.  These **special rule elements** match various types of tokens such as alpha characters, punctuation, wildcards, etc.  For examples of these special rule elements, refer to the individual pages included in the Special Rule Elements section.

Special rule elements are given in the following table.

| **RULE ELEMENT** | **DESCRIPTION** |
| --- | --- |
| [_xWILD](../_xWILD.md) | Match anything. _xWILD is an unrestricted wildcard. Key-value pairs may add restrictions on number of nodes matched and on what is matched. (Note: with a *match* or *fail* list, _xWILD becomes an "OR" matching function.) |
| [_xANY](../_xANY.md) | Match any single node. (WARNING: A rule written with _xANY [max=0] will not work. _xANY is not implemented as a wildcard. Instead, the near equivalent _xANY _xWILD should be used.) |
| [_xNIL](../_xNIL.md) | Match nothing. _xNIL designates a suggested element when the rule performs a special action, such as removing the matched nodes from the parse tree. (_xNIL has no special action, but serves as documentation for the rule writer.) |
| [_xALPHA](../_xALPHA.md) | Match an alphabetic token, including accented and other extended ANSI chars. |
| [_xCTRL](../_xCTRL.md) | Match control and nonalphabetic extended ANSI characters. (See _xALPHA.) |
| [_xNUM](../_xNUM.md) | Match a numeric token. |
| [_xPUNCT](../_xPUNCT.md) | Match a punctuation token. |
| [_xWHITE](../_xWHITE.md) | Match a whitespace token, *including* newline. |
| [_xBLANK](../_xBLANK.md) | Match a whitespace token, *excluding* newline. Equivalent to ***_xWILD [match=(\ \t)]*** |
| [_xCAP](../_xCAP.md) | Match an alphabetic with uppercase first letter. |
| [_xCAPLET](../_xCAPLET.md) | Match an alphabetic consisting of a single capitalized letter. **NEW** |
| [_xLET](../_xLET.md) | Match an alphabetic consisting of a single letter. **NEW** |
| [_xVAR](../_xVAR.md) | Match a node that has the named attribute with a value. Form: ***_xVAR("attr")***. **NEW** |
| [_xEOF](../_xEOF.md) | Match the end of file. |
| [_xSTART](../_xSTART.md) | Match if at the start of a phrase (or "segment"). |
| [_xEND](../_xEND.md) | Match if at the end of a phrase (or "segment"). |

## See Also

[Phrase Element Modifiers](Phrase_element_modifiers.md) [Suggested Element Modifiers](Suggested_element_modifiers.md)

[Rule Syntax](Rule_syntax.md)
