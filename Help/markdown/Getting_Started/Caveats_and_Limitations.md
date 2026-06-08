[← Help Contents](../index.md) | [📘 NLP++ Textbook](../NLP++_Textbook.md)

# Programming Notes and Issues

This document details issues with VisualText™ and NLP++™. Additional information about the current release can be found in the [New in Current Version](../New_in_Current_Version.md) page and in the Release Report, located by default at

C:\Program Files\TextAI\VisualText\Docs\ReleaseReport.txt.

#### DOCUMENTATION ISSUES

·         Zipped tutorial analyzers may be missing in some versions, so you'll have to start working them from Tutorial number 1.

·         Documentation for Linux is not provided in the present Help.  Workaround: contact our customer support for assistance.

#### INSTALLATION

·         On rare occasions, the installation program may hang.  Please try another computer, and contact our customer support for workarounds.

#### RUNNING ANALYZERS

·         Analyzers cannot be run on files with the .log extension.

·         VisualText is optimized for processing large numbers of relatively small text files. Input files larger than **1MB** may substantially slow processing, and it is inadvisable to process individual files larger than **4 MB**.  Workaround: a program may split large texts into buffers and submit them to an analyzer one at a time, using the knowledge base to manage information across segments of a document.

·         Scale Up issues.  A variety of scale-up issues have been addressed in VisualText 2.x.  If you are experiencing problems, contact us.

·         Knowledge base DLL file.  For huge knowledge bases, the KB.DLL compiled knowledge base can become extremely large (100s of MB).  VisualText QDBM addresses this, but is too slow for commercial-grade use at this time.

#### GUI ISSUES

·         It is safest to edit the **gram** subhierarchy using the Gram Tab only, rather than the KB Editor. Where feasible, use the Gram Concept Properties dialog (available from Gram Tab popup > Properties) to edit attributes of **gram** concepts. Use the Attribute Editor only to edit attributes that are not accessible from the Gram Concept Properties dialog.

·         Editing the **sys** hierarchy can easily corrupt the Knowledge Base.  Before editing the **sys** hierarchy (either manually or programmatically), you are advised to create a backup copy of your project.  A KB Safe Mode is provided in the VisualText preferences for those who want to disable inadvertent manual editing of the sys hierarchy.

·         Size Dynamically in VisualText display preferences is currently working for the KB Editor window only.

·         Currently, folders are not part of the Ana Tab. Descriptions for Ana Tab folders in the Ana Tab Popup Menu are for future enhancements.

#### WRITING CODE AND RULES

·         NLP++** **is an evolving language.  If constructs that you would like to see in the language are absent, you may often create them yourself by writing a user-defined NLP++ function or a C++ version within the **User Project** for an analyzer.  We appreciate your feedback about capabilities to incorporate in the language, both to provide you with faster execution of the functions and to enhance NLP++ and VisualText as a development environment.

·         One way to implement a new type of pass algorithm is to define a new NLP++ function in the user project and invoke that function from the **code** region of a pass. The user function may traverse the parse tree, interface to third party code, and so on.  (Now the same can be done with an NLP++ function defined in a @DECL region).

·         Some data types are not yet implemented, including **bool**, and **char**. Nonzero integer values are used for Boolean **true** and zero is used for Boolean **false**, analogous to the C Programming Language.  We recommend NOT explicitly comparing the returns of functions documented as bool with 1 and 0.  For example, write if (batchstart()) rather than if (batchstart() == 1).

·         Numeric overflow and underflow are not flagged.  For example, the maximum **int** is 2147483647 in Windows and must be checked by the programmer as needed.  For large numbers, the **float** type should be used.

·         POST Actions should operate on rule elements from right to left (or bottom to top, if written one element per line).

When the POST region includes group and excise actions, the numbering of rule elements is affected. For example, if element 3 is to be excised, then referring to elements 4, 5, etc. subsequently is invalid. Therefore, operations on rule elements should proceed from right to left, that is from high-numbered rule elements to lower-numbered elements. For example, the following POST actions will work as expected:

N("status",4) = "good"; excise(2,3);

The node matching element 4 gets a variable named "status" with value "good", after which the nodes matching elements 2 and 3 are excised. But if written this way:

excise(2,3); N("status",4) = "good";

there may no longer be an element 4 after the excise action, or a different rule element may be referred to than expected. Conditionally excising rule elements would further complicate the tracking of rule element numbers.

·         Stacking POST Actions should be avoided.

While group actions may be repeated in a POST Region (*but see below*), the user should avoid writing multiple actions (e.g., single, excise, singler, singlex) that modify the parse tree within a single POST Region. After an action such as **single**, the elements of the current rule may no longer available.

·         GROUP action differs in compiled versus interpreted versions of an analyzer In interpreted NLP++, a group action such as **group(5,7,"_list")** collapses elements 5 through 7 under a new node called _list, which is numbered 5, with the subsequent element (which was numbered 8) now numbered as 6.  But in compiled code, 5 through 7 are collapsed as before, but now elements 6 and 7 are retained with zero nodes, and numbering is *unchanged*.  That is, element 8 is still number 8.  This discrepancy will be fixed in a subsequent version.

·         Some NLP++ actions will not accept general NLP++ expressions as arguments. For example, **singler**(1,3) is valid, but singler(G("lo"),G("hi")) will result in a syntax error.

·         Partly constrained wildcards don’t work in some cases.  The following example

@PRE <2,2> var(“lower”); @RULES _NP <-   _The   _xWILD [plus]   _Bears   @@

will match nodes to the wildcard regardless of whether they have a nonzero variable called “lower”.  A workaround is to write the rule as

@PRE <2,2> var(“lower”); @RULES _NP <-   _The   _xWILD [plus fail=(_Bears)]   _Bears   @@

This will work as specified. Only nodes with a nonzero variable called “lower” will match the _xWILD element.

·         Infinite loops.  As in most grammar systems, it is possible to write "grammar loops" in NLP++.  Also, a lone rule such as

@POST

singler(1,1);

@RULES

_np <- noun [opt] prep [lookahead] @@

where everything is optional except the lookahead elements, can cause an infinite loop.

·         Modifying the lookahead region.  Reducing or grouping a node at or past the [lookahead] keyword can cause a pass to silently stop matching rules, as below:

@POST

single();  #  Correct would be singler(1,4);

@RULES

_np <- _det _quan _adj _noun _prep [lookahead] @@

·         In recursive analyzer passes, an infinite loop occurs with rules having one right-hand-side element with singlet mode:

_adjlist <- _adj [s] @@

Here, _adj is found "inside" repeatedly.  Two ways to fix this are shown below.

_adjlist [**base**] <- _adj [s] @@

_adjlist <- _adj   @@

In the first, case, _adj is found "inside" the current parse tree node only once, since the **base** attribute placed on the _adjlist keeps the internal _adj from being found inside it.  In the second case, _adj only matches when it labels the current "top level" parse tree node being examined.  Once it is reduced to _adjlist, the internal _adj is no longer visible.

·         KB Phrase.  A knowledge base PHRASE is implemented merely as the first element in the phrase.  Thus, fetching the phrase and then adding a new first element requires re-fetching the phrase.

`G("phrase") = findphrase(G("some concept"));  # Fetch the "phrase", i.e., the first node.`

`addnode(G("phrase"),"nodename", 1);           # Add a new first node of phrase.`

In the above, G("phrase") no longer points to the first node in the phrase.  A workaround is to track the first node in a phrase, or to re-fetch the phrase as needed using findphrase, as below

` `

`G("phrase") = findphrase(G("some concept"));  # Fetch the "phrase", i.e., the first node.`

`addnode(G("phrase"),"nodename", 1);           # Add a new first node of phrase.`

`G("phrase") = findphrase(G("some concept"));  # Re-fetch the first node of phrase.`
