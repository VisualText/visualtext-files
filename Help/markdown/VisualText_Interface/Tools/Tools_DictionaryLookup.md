[← Help Contents](../../index.md) | [📘 NLP++ Textbook](../../NLP++_Textbook.md)

# Dictionary Lookup

## Function

The Dictionary Lookup Tool allows you to access and search specified online dictionaries.  It can be a handy tool when doing lexical work.  You can feed Dictionary Lookup a list of words or phrases and it will return html files containing the results for the search for each of the words on the list.  The html files are placed in folders in the Text Tab.  You can also use Dictionary Lookup as a reference source to search for words in the online dictionary directly from VisualText.

## Accessing

Dictionary Lookup can be accessed from several places within VisualText.  It can be accessed from the main [Tools Menu](../Main_Tools_Menu.md), the [Text Tab Popup Menu](../../Text_Tab_Popup.md) under Tools, and from the Tools menu in the [Text File Popup Menu](../Popups/Text_File_Popup.md). Dictionaries can also be accessed from the [Attribute Editor](Attribute_Editor.md).

## Setting Dictionary Lookup Preferences

Access to the online ontology WordNet is provided by default.  To add other online dictionaries to Dictionary Lookup, you must specify the dictionary path in the [Dictionary Lookup tab](../Main_File_Menu.md#dictionaryLookup_pref) in VisualText preferences located under the File Menu.  For more information on creating path names to online dictionary sources, see [URLs for Dictionary Lookup](../../HowToBuild/DictLookupURL/DictionaryLookup.md).

| **Note**: Access to WordNet relies on a fixed webpage CGI to WordNet. If the WordNet page changes, the path for WordNet must be changed in the preferences dialog. |
| --- |

## Using Dictionary Lookup

**To create dictionary files from a word list**:

Dictionary Lookup expects a file that consists of a list of words, one per line with no spaces after the word.

1. Select the **file** in the Text Tab.

1. Right-click and select **Dictionary** > **Lookup** from the Text Tab Popup, and choose the online dictionary from the list.  Html files for each of the words on the list are created in a folder in the input directory.  The name of the folder is filename_DictionaryName.

**To use Dictionary Lookup to find words in an online dictionary**:

1. Highlight a **word** in an open text file in the Workspace.  (If you do not highlight a word, you will be prompted with a dialog box.)

1. Right-click and select **Dictionary** > **Lookup** from the Text File Popup, and choose the online dictionary from the list.  The word is displayed in a browser window.

## See Also

[Dictionary Lookup Preferences](../Main_File_Menu.md#dictionaryLookup_pref)

[URLs for Dictionary Lookup](../../HowToBuild/DictLookupURL/DictionaryLookup.md)
