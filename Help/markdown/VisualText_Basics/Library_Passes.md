[← Help Contents](../index.md) | [📘 NLP++ Textbook](../NLP++_Textbook.md)

# Library Passes

To help you get started building your text analyzer, VisualText comes with several pre-built pass files.  These pre-built pass files are called **library passes**.  They are available within Add menu item of the Ana Tab popup menu.

Library passes contain NLP++ rules and code to recognize common or generic types of data. Generic data includes telephone numbers, email addresses, different types of money formats, dates, etc.  VisualText also provides library passes for importing existing databases into the knowledge base.

## Types of Library Passes

There are two types of library passes:  those that are used by themselves and those that are part of a series of passes.

Below is a summary of available library passes.  Where library passes are part of a series of passes, the total number of passes is indicated next to the library pass name.

| Library Pass Name | **Description** |
| --- | --- |
| Database (10) | Import a database into the KB hierarchy. Passes can import database with both text and numeric fields. Assumes first line of database file is a list of field names. To add a large database, it is more efficient to split up the database file into smaller files. If splitting large database into smaller files, the first line of each file should include the list of field names. |
| Date Plus Numerics (9) | Recognize simple and compound numeric words, numeric sequences and lists, various character formatting such as punctuation and contractions, telephone numbers, and dates. |
| Emails | Recognize email addresses. |
| HTML (5) | Recognize HTML formatting elements, text tagging, special HTML characters, and tagging structures. |
| Lines |   |
| Numerics (7) | Recognize simple and compound numeric words, numeric sequences and lists, various character formatting such as punctuation and contractions, and telephone numbers. |
| Remove Blank Lines | Remove blank lines. |
| Remove White Space | Remove white spaces. |
| Trends | Count the occurrence of words and phrases in a text. |
| XML DTD (14) | XML document type definition. DTD is used to define the XML document structure. DTDs can be contained in the XML document, or can be referenced from an external document. |
| Xml (21) | Process XML files. |

## Using Library Passes

Library passes can be added to any part of your analyzer sequence.  Note however, that they may not be inserted before the system pass, tokenize.  When a library pass is composed of a series of passes, all of the passes in the sequence are added.

The insertion of library passes into an existing analyzer may not be completely "seamless."  That is, the developer may need to reorder passes and edit contexts within pass files (e.g., the list within a **@NODES** context selector) in order to get the analyzer working properly with the added library passes.

## Location of Library Passes

The set of library passes that accompanies VisualText is stored in the spec folder of the installation directory.  If you installed the VisualText software on your c drive for example, the library passes are contained in the following directory:

```
c:\Program Files\TextAI\VisualText\data\spec
```

You can create your own library passes and add them to the spec directory.  They will automatically appear in the Library Passes submenu of the Ana Tab popup menu.

## See Also

[Adding passes to the analyzer sequence](../Using_VisualText/Analyzer_Sequence/Hand-Built_Pass_Files/Adding_passes.md)
