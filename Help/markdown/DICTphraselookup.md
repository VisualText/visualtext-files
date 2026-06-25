[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# DICTphraselookup

## Purpose

Look up a phrase in the Knowledge Base dictionary by walking the parse tree from a starting node alongside a phrase hierarchy stored in the KB. Parse tree nodes that match the phrase hierarchy are annotated with match information.

## Syntax

```
DICTphraselookup(fromNode, keyStr, matchStr, listStr, skipPunctInt)
```

```
fromNode - type: node (parse tree node)

keyStr - type: str

matchStr - type: str

listStr - type: str

skipPunctInt - type: int (0 or 1)
```

## Returns

Nothing.

## Remarks

This function provides a hardwired form of dictionary phrase lookup. It assumes the KB contains a hierarchy of phrases that is reached through the *keyStr* concept attribute on dictionary words.

The arguments are:

* *fromNode* — the current parse tree node, used to match the start of the phrase.
* *keyStr* — the name of the concept attribute in the KB dictionary used to reach the phrase hierarchy. It is keyed from the LOWERCASE text of the current node.
* *matchStr* — the name of the "match" attribute in the phrase hierarchy that marks a full match.
* *listStr* — the name used for the gathered list of matches.
* *skipPunctInt* — a flag, **1** to skip punctuation during the walk or **0** not to. The flag must be 0 or 1; any other value writes an error to the output log. Whitespace in the parse tree is always skipped.

Internally the function lowercases the start node's text, finds the matching word concept in the KB dictionary, then follows the *keyStr* attribute to the start of the phrase hierarchy. It then walks parse tree nodes to the right in tandem with the phrase hierarchy (matching node text in uppercase, as the phrase hierarchy is assumed to be all uppercase), recording matches as it goes. Match information (such as `PARTMATCH`, the matched concept, the saved last node and concept, and the gathered match list named *listStr*) is stored as values on the affected parse tree nodes; the parse tree structure itself is not changed.

If the starting node has no dictionary word concept, or that word concept has no phrase-start concept under *keyStr*, the function simply returns having recorded nothing. A missing node, missing key string, or a first argument that is not a parse node writes an error to the output log.

## Example

```
DICTphraselookup(N("n"), "k", "k_match", "k_list", 1);
```

Here `N("n")` is the current parse tree node that begins a candidate phrase, `"k"` is the dictionary concept attribute that points into the phrase hierarchy, `"k_match"` is the attribute marking a full match, `"k_list"` is the name used to gather the matches, and `1` skips punctuation during the walk.

## See Also

[dictfindword](dictfindword.md), [findconcept](findconcept.md), [conval](conval.md), [findphrase](findphrase.md), [Knowledge Base Functions](Table_of_Knowledge_Base_Functions.md)
