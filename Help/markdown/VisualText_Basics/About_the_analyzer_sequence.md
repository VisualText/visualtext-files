# About the Analyzer Sequence

## Passes

The analyzer sequence is a series of steps or **passes**, each containing its own pass algorithm. As the analyzer is run over the text, each pass is taken in the order it occurs in the sequence and executes the code and rules that are contained in it. The **Ana Tab** manages the analyzer sequence.

Analyzer passes use and modify a common data structure, called a **parse tree**.  They may also post and use shared information in the knowledge base.  VisualText analyzers can be very fast because they build a *single* parse tree per text.

## System and User Passes

There are two types of passes in the analyzer sequence: **system** or built-in passes and **user** passes. The first pass in the analyzer sequence is **tokenize** by default, which is a system pass that converts the input text to a parse tree. The tokenize pass, like all system passes, cannot be modified.

User passes employ either the **pattern** (or **pat**) and the **recursive** (or **rec**) algorithm.  Both employ a **pass file**, in which the user places NLP++ code and rules.

**NOTE:** VisualText does not provide a way to add system passes to the analyzer sequence.  You can do this manually by exiting VisualText and editing the **analyzer.seq** file in the project's **spec** folder.  **VisualText 2.5.x.x** and onward provides a new tokenize pass called **dicttok** that uses a knowledge base to automatically put part-of-speech information on the parse tree. (Grab the three kb.* files from **bin** folder of TAIParse, available at our website, and put them in a new analyzer project's **bin** folder).

If you need a customized tokenization pass to handle OCR output (already exists, commercially available in conjunction with http://www.XIEO.info)), convert HTML to plain text, or another specialized input format, TAI can help.  Contact us at support@textanalysis.com, 1-877-235-6259 USA toll free.

**dicttok** also puts a **CTRL** attribute on control characters to help manage control characters (e.g., using feature-based matching), as in the code snippet below.

**@PRE** <2,2> **vareq**(**"CTRL"**,128);  # Match ASCII 128 = €** @POST** "output.txt" << "Found ctrl = " << **N**("$text",2) << "\n";** @RULES**** _xNIL** <- â** _xCTRL**** _xALPHA**** @@**

will match the character (€) in the following text and output it.

â€œsmall

## Ordering of Passes

Since each pass in the analyzer typically builds upon the last one (via a common parse tree), careful attention should be given to the ordering of each pass in the sequence. When a pass creates a structure that is used by later passes, the pass is said to be **feeding** them. If it removes or hides information from successive passes, it is said to be **bleeding**. One nice feature of VisualText is that you can create an analyzer sequence, see how it works and easily change the sequence around to suit your needs. Since the ordering of rules *within* a pass file can also create, hide or destroy parse tree structure available for later rules and passes, careful attention should also be given to the ordering of rules within the pass file.

## Pass Types

Pattern - The *pattern* algorithm is the workhorse pattern-matching algorithm type used in VisualText. For each node in the currently selected phrase, each rule within the pass file is tried in turn. When a rule has matched, the pattern algorithm executes its associated code and actions, then moves onto the node following those that matched the current rule. (Notes: [1] when rules have a trigger, they are only tried if the triggered rule element will successfully match. [2] The next node to be tried after a rule match may be selected using the **lookahead** element action.)

Recursive - The *recursive* algorithm type implements a standard recursive-grammar algorithm. The nodes of the current phrase are in effect traversed repeatedly, as long as a rule in the current pass file matches. When no rules match in a phrase, then the next phrase in the parse tree is selected, till no more phrases remain to select. (Notes: [1] **noop** rule matches are counted as *failures* by the Recursive algorithm, so that they won't cause an infinite loop.)

## Adding Passes to the Analyzer Sequence

There are several ways to add passes to the analyzer sequence. One way is to create or add the pass yourself and the other way is to have VisualText create the pass for you. An analyzer will generally contain both types of passes.

#### Hand Building Passes

To create the pass yourself, you write NLP++ code and rules in the pass file used by the pass. It is also possible to add an existing pass file from another analyzer directly into your project. When you add your own passes, you use the Ana Tab. For more information on adding passes to the analyzer sequence yourself, see [Adding Pass Files](../Using_VisualText/Analyzer_Sequence/Hand-Built_Pass_Files/Adding_passes.md).

#### Automatically Generating Passes

When VisualText automatically creates a pass, it takes samples that you provide, makes generalizations from those samples and then creates the passes and the associated pass files. The automatically created passes are placed in a **stub region**.  The process of adding samples is called **sampling**. Automatically generated passes can be edited, but any edits will be lost the next time the automatic rule generation (RUG) is invoked. To make changes, you will have to go through the sampling process again. The Gram Tab is used for sampling. For more information on the automatic rule generation, see [About Automatic Rule Generation](About_Automated_Rule_Generation.md).

## Inactivating a Pass in the Sequence

As you add new passes to the Ana Tab, they become part of the stepwise sequence executed when the text analyzer runs on an input text. It is possible to have the analyzer **skip** a pass in the analyzer sequence by setting the pass properties for the pass. When you inactivate a pass, you tell the analyzer to ignore the code and rules included in the pass file associated with the pass. Skipping passes can be used as a tool to debug your analyzer. For more information, see [ctivating Passes](../Using_VisualText/Hand_Building_Pass_Files/Inactivating_a_pass.md).

## Icons Used in the Analyzer Sequence

- ![](../../helps/VisualText_Basics/dna-link.gif) A DNA link denotes a user pass (if recursive, includes a letter R). Inactivated passes are indicated by a break in the chain.

- ![](../../helps/VisualText_Basics/stub_region.gif) A red bead denotes a **stub region** start or end. A stub region holds automatically generated passes.

- ![](../../helps/VisualText_Basics/system_pass.gif) A vertical bar denotes a system pass (e.g., tokenize).
