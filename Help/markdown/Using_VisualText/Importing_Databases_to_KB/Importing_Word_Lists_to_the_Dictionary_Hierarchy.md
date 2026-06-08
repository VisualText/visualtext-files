[← Help Contents](../../index.md) | [📘 NLP++ Textbook](../../NLP++_Textbook.md)

# Importing Word Lists to the Dictionary Hierarchy

The Knowledge Base comes with a specialized concept called **dict** (for dictionary) which stores information about words.

There are several ways to incorporate a word list into the dict hierarchy.  One is to create a simple analyzer to read in and add the list of words to the hierarchy.  You can also add a pass to an existing analyzer project in order to add the word list.  The pass can look like

@POST L("text") = strtolower(N("$text")); addword(L("text")); @RULES _xNIL <- _xALPHA @@

Note that you can copy a knowledge base folder to a minimal analyzer having the pass above, run the analyzer on your word file, then Save KB.  Then you can copy the KB folder back to your main analyzer.  In this way, knowledge bases can be conveniently moved around and modified with data sources as they become available.  Some analyzers can thus be dedicated to building or augmenting knowledge bases.  (Things are somewhat more complex with a compiled knowledge base.  Mainly, you want to modify the analyzer preferences to load the interpreted knowledge base, when making upgrades as described here.)
