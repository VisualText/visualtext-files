[← Help Contents](../index.md) | [📘 NLP++ Textbook](../NLP++_Textbook.md)

# About the Knowledge Base

The Knowledge Base Management System (KBMS) used in VisualText™ is based on a knowledge representation framework developed by Text Analysis International, called Conceptual Grammar™ (CG). CG represents knowledge in terms of concepts, phrases, and their attributes. Everything "hangs" off a hierarchy of concepts. Because CG can represent concepts, phrases, attributes, and their interrelationships, it allows diverse types of knowledge to be stored flexibly within a single framework. See also the [Introduction to the Knowledge Base](../VisualText_Interface/Knowledge_Base.md).

The [KB Editor](../VisualText_Interface/Tools/KB_Editor.md) and the [Attribute Editor](../VisualText_Interface/Tools/Attribute_Editor.md) can be used to manipulate portions of the KB.

## KB Location

The KB is stored under an application's kb folder. For example, for the tutorials, the folder

```
C:\apps\myAnalyzerFolder\myAnalyzer\kb
```

has a folder called **user**. The **user** folder stores data specific to the analyzer in question. The KB for an analyzer is defined by the four files in the kb\user folder: **attr.kb**, **hier.kb**, **phr.kb** and **word.kb**.

## KB Objects

The KB consists of a hierarchy of **concepts**. **Attributes** can be associated with each concept . An attribute consists of a **key** (or **slot**, or **name**) and zero or more **values**. A value can be a string, an integer, or another concept. Each attribute can have multiple values, each with a distinct type.  (Note that a **value**, or **val**, is a type of knowledge base object.)

A concept can also have an associated **phrase** of **nodes**. A node is similar to a concept in most respects, except that a node is not placed directly in the knowledge base hierarchy. Rather, nodes serve as "proxies" or references to concepts that reside in the hierarchy. Phrases can be used to implement idioms, patterns, samples, rules -- in short, any sequential information.

Advanced Notes: An attribute key itself is actually a concept, rather than a string, so that multiple attributes with the same "name" can coexist peacefully within the same concept. To add further flexibility (or complexity, depending on your view), multiple attributes with identical keys can reside within a single concept. For many applications, referring to attribute keys by name is just fine, so most of the implemented NLP++ functions that you'll encounter refer to attributes by name.

## Knowledge Base Functions

See the [Table of KB Functions](../Table_of_Knowledge_Base_Functions.md) and page-per-function in the Knowledge Base Functions section.

## Saving the Knowledge Base

The knowledge base can be changed manually by using the KB Editor.  Analyzers can also be programmed to update the knowledge base automatically, for example to accumulate information across a set of documents.

Some analyzers are geared to load up a relatively empty knowledge base and then populate it temporarily.  Some analyzers are built primarily to grow a large knowledge base.  When exiting VisualText, the user is asked to save the changes to the knowledge base or discard them.  Unless your purpose is specifically to build or modify a knowledge base, then you can opt not to save the modified knowledge base.  Some distinctions to be aware of:

Save KB - Saves the knowledge base into command files. Compile KB - Saves the knowledge base into a file system. Load interpreted KB - read kb command files into the knowledge base on loading an analyzer. Load compiled KB - load or use the compiled kb file or file system.

## QDBM-Based Knowledge Base

With the 2.1.0.0 version and later, VisualTextQ provides a knowledge base manager based on the QDBM freeware.  This supports growing very large knowledge bases in VisualText, by virtue of replacing the old kb.dll file with the QDBM file system.  With this variant, loading the interpreted version reads the knowledge base command files into the QDBM database.  Saving the knowledge base writes out command files, as before.  Compiling the knowledge base saves off a copy of the QDBM database.

Loading the compiled knowledge base copies the QDBM database to a temporary folder (kb\tmp) for use in the current session.  If the session is closed without saving the kb, then the changes made in the tmp area are discarded.  If the kb is "compiled", then the tmp area is merely copied to the permanent store (kb\qdbm).

In this way, the same knowledge base management commands work as before, but under the hood the QDBM system replaces the kb.dll file for the compiled version of the knowledge base.  As always, BEFORE UPGRADING to the new VisualText version, it is important to save any knowledge base that is important -- this will create command files that will automatically load in any newer version of VisualText.  For questions about kb management, please contact our support.
