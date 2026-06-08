# Analyzer Templates

VisualText analyzers are built from initial **templates**.  A template is a starter or skeletal analyzer that can be copied and modified.

The templates contain a sequence of passes designed to help you perform certain tasks.  The Database template for example, is an analyzer with passes that will allow you to import an existing database into the knowledge base.  The Bare template is used to create the basic or minimal analyzer.  It contains only the tokenize pass.  All templates start with the tokenize pass.

## Template Types

The templates currently available are outlined below:

| Name | **Description** |
| --- | --- |
| Bare | Minimal or basic analyzer. Contains default system pass, tokenize only. |
| Database | Analyzer with sequence of passes to import records from an existing database into the VisualText knowledge base. (Passes also available as library passes.) |
| DatesPlusNumbers | Analyzer with sequence of passes to recognize simple and compound numeric words, numeric sequences and lists, various character formatting such as punctuation and contractions, telephone numbers, and dates. (Passes also available as library passes.) |
| **EnglishLexicon** | Analyzer with a built-in English lexicon of 180,000 words. Lexical entries are coded with part of speech information. Lexicon is stored in the knowledge base in the dict subhierarchy. |
| HTML | Analyzer with a sequence of passes to recognize HTML formatting elements, text tagging, special HTML characters, and tagging structures. (Passes also available as library passes.) |
| XML | XML analyzer. (Passes also available as library passes.) |
| XML DTD | Analyzer with a sequence of passes to recognize an XML document type definition (DTD) file. (Passes also available as library passes.) |

| **Note**: Passes in the Database, Date Plus Numerics, HTML, XML and XML DTD templates are also available as Library Passes. For example, you can create an analyzer with the Bare template and choose to add the sequence of passes from the Add > Library Pass menu in the Ana Tab. For general information on library passes, see Library Passes. To learn how to add these passes as library passes, see Adding Library Passes. |
| --- |

## Selecting Template Type

You set the type of analyzer you want to build when you create a new analyzer.

For analyzer templates that contain a sequence of passes, note that the relative ordering of passes in the sequence should not be changed.  If the sequence of passes is changed, the analyzer may not work as designed.

## See Also

[Creating Analyzers](Using_VisualText/Analyzers/Creating_analyzers.md)
