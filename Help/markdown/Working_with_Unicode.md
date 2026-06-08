# Working with Unicode

Starting with VisualText 2.0.1, a Unicode VisualText executable is available with every release.

Unicode is well-documented on the web.  Basically, Unicode is a character set that supports the major languages and character sets.  To do this, characters consist of two bytes, rather than the ANSI or ASCII representation of characters with one byte.

While the advantages of Unicode are tremendous, it also adds substantial complexity and headaches to programs that use it.  Also, Unicode is necessarily processed more slowly than single-byte character representations.

VisualText support for Unicode is an ongoing enterprise.  The 2.0.1 release provides default tokenization for the world's character sets (or "scripts"), as well as supporting Unicode characters in NLP++ strings, in the GUI, in knowledge bases, compiled analyzers, and the like.

In subsequent releases, we plan to add NLP++ functions that will help characterize and manipulate Unicode constructs in text, parse trees, strings, and the knowledge base.

## Windows and Unicode

To display and input Unicode fonts, you'll need to consult your Microsoft Windows documentation.  For example, in Windows XP, select

Start Button > Settings > Control Panel > Regional and Language Settings

The Languages tab there lets you install fonts for complex and East Asian character sets.  The Details button within the Languages tab lets you set up input in various character sets, and so on.

## NOTES

[1] If using English only or small Western alphabets (e.g., French, Spanish, German), consider staying with ANSI VisualText.

[2] An analyzer should be used with Unicode or ANSI VisualText, but not both.

[3] Unicode VisualText writes files out using the UTF-8 format and expects to read files in the same format.  If an input file contains Unicode characters, then VisualText expects it to have the Byte Order Marker (BOM) as required of Windows files.  A nice thing about UTF-8 is that normal ANSI or ASCII files are automatically in the right format, with or without a BOM header.

![](../helps/Tutorials/GO.gif) If a file does not appear to be read correctly by VisualText, then it may have come from a non-Windows source.  Try opening the file in an application such as WordPad, add a character, then remove the character, then save the file as UTF-8.  This should automatically add the BOM head to the beginning of the file.

[4] KB dictionary indexing.  We'll be providing analyzer templates specific for Unicode.  You can also manually add dictionary indexes to the knowledge base (by editing the **kb\user\hier.kb** file).  Contact us at support@textanalysis.com for help with these issues.

add hier "concept" "sys" "dict" "a" "z" "zy" add hier "concept" "sys" "dict" "a" "あ" add hier "concept" "sys" "dict" "a" "あ" "あ"

Basically, you'll want to add lines like the second and third above, in order to have Unicode characters distributed well within the KB dictionary.

[5] No particular updates have been made yet to RUG (Automated Rule Generation) for Unicode VisualText.
