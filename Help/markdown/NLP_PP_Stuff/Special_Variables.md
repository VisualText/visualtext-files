# Special Variables

To get useful information from the parse tree and other sources when analyzing a text, some special variable names have been provided. All start with a dollar sign (**$**). No such variable names are usable with suggested (**S**) variables, at present.

## Notes on Special Variables

1. Special variable names must be quoted. E.g., N("$text", 2).

1. You should not assign to or create your own "dollar" variables. NLP++ reserves all variable names that start with a dollar sign.

## Types of Special Variables

These special variables have been organized into the following four groups:

- File Variables

- Letter Case Variables

- Test Variables

- Text Variables

A consolidated table of NLP++ special variables is provided below. Each item in the table is also detailed in individual topics in the Special Variables section.

## Table of Special Variables

| **VARIABLE NAME** | **VARIABLE TYPES** | **DESCRIPTION** |
| --- | --- | --- |
| **$treetext** | **N, X** | Fetch the 'cleaned up' (removing leading and trailing, convert separators to single space) text gleaned from a node's subtree. Uses the parse tree as input, not text buffer. Analogous to $text. Difference between $treetext and $text is $text returns text from the input text buffer while $treetext returns text from the parse tree. So, if you have removed some nodes from a tree with an excise(), $treetext returns the text minus the excised elements, while $text returns everything in the input text buffer, including the text under excised nodes. |
| **$text** | **N, X** | Fetch the text covered by the node. Cleanup whitespace (removing leading and trailing, convert separators to single space). Uses the original text buffer, rather than the subtree under the node, in order to gather text. See also $treetext and $treeraw. |
| **$treeraw** | **N, X** | Fetch the text covered by the node from the parse tree. Text is not 'cleaned up'. Analogous to $treetext. See also $treetext and $raw. |
| **$raw** | **N, X** | Fetch the 'cleaned up' text covered by the node from the text buffer. See also $treetext, $treeraw and $text. |
| **$xmltext** | **N, X** | Same as $raw***,*** but converts characters that are special to HTML and XML. E.g., "<" is converted to "&lt;". |
| **$length** | **N, X** | Get the length of node's text. |
| **$ostart** | **N, X** | Start offset of the referenced node in the input text. |
| **$oend** | **N, X** | End offset of the referenced node in the input text. |
| **$start** | **N, X** | Check if referenced node has left sibling in parse tree. Evaluates to 1** **if the referenced node has no left sibling, else 0. |
| **$end** | **N, X** | Check if referenced node has right sibling in parse tree. Evaluates to 1** **if referenced node has no right sibling, else 0. |
| **$apppath** | **G** | Get base directory path for current application. E.g., "D:\dev\apps\Resume". |
| **$anaspath** | **G** | Get parent directory for the analyzers. **NEW 2.1.0** |
| **$kbpath** | **G** | Get base directory path for the kb / user directory. E.g., "D:\dev\apps\Resume\kb\user". **NEW 1.27.0** |
| **$input** | **G** | Get full input file. E.g., "D:\apps\Resume\input\Dev1\rez.txt" |
| **$inputparent** | **G** | $inputparent returns "Dev1" assuming input file is "D\apps\Resume\input\Dev1\text.txt". **NEW 1.26.0** |
| **$inputpath** | **G** | Get input file path. E.g., "D:\apps\Resume\input\Dev1" |
| **$inputname** | **G** | Get input file name. E.g., "rez.txt" |
| **$inputhead** | **G** | Get input file head. E.g., "rez" |
| **$inputtail** | **G** | Get input file tail. E.g., "txt" |
| $passnum | G | Get current pass number. **NEW 2.0.2.4** |
| $rulenum | G | Get current rule number within current pass. **NEW 2.0.2.4** |
| $isdirrun | G | Check if the engine is processing a directory of files instead of an individual file. Returns 1 if it is analyzing a directory, else 0. **NEW 1.26.0** |
| $isfirstfile | G | Check if is first file processed in a directory. Returns 1 if it is the first file, else 0. **NEW 1.24.0** |
| $islastfile | G | Check if is last file processed in a directory. Returns 1 if it is the last file, else 0. **NEW 1.24.0** |
| **$allcaps**** $uppercase** | **N** | Check if token underlying node is all uppercase. Returns 1 if token is all uppercase. If multiple words (even if all are all-caps), returns 0. WARN: Not identical to the **uppercase**() PRE Action. |
| **$lowercase** | **N** | Check if token underlying node is all lowercase. Returns 1 if token is all lowercase If multiple words (even if all are all-caps), returns 0. WARN: Not identical to the **lowercase**() PRE Action. |
| **$cap** | **N** | Check if token underlying node is a capitalized word. Returns 1 if token is a capitalized word. WARN: Not identical to the **cap**() PRE Action. |
| **$mixcap** | **N** | Check if token underlying node is a mixed-capitalized word. Returns 1 if token is a mixed-capitalized word. Examples: "MIchigan", "abcD". |
| **$exists** | **N** | Check if node exists in parse tree. Returns 1 if node exists, else 0. |
| **$unknown** | **N** | Check if token underlying node is an unknown word. Returns 1 if token underlying node is unknown. WARN: Not identical to the **unknown**() PRE Action. Requires a **lookup**() CODE Action prior to any use of this special variable. |

| **Notes**: The $uppercase, $lowercase, $cap, and $unknown differ from the analogous PRE Actions in that they all traverse down to the "leafiest" node they can find, in order to perform their check. The corresponding PRE Actions only chain down if the [s] flag is present in the associated phrase element(s). Also, the $ variables are not stopped by a [base] attribute in a node. |
| --- |

## See Also

[Variables](About_NLP++_Variables.md)
