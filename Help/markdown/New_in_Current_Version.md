[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# MAJOR RELEASE (2.0 NON-UNICODE + UNICODE BETA)

[1] **VisualText executables.** Version 2.0.1.X and later include both Unicode and non-Unicode (or ANSI) executables.

bin\VisualText.exe          Non-Unicode ANSI version bin\VisualTextU.exe        Unicode BETA version (only works with Unicode input files)

With 2.1.0.0 and later, the following is also supplied:

bin\VisualTextQ.exe        Non-Unicode ANSI version that uses QDBM database manager under the hood.  Note that this is a beta version for growing arbitrarily large knowledge bases, but is not yet optimized for speed.

The ANSI version shares the same source code with the Unicode version, but replicates the same basic functionality as earlier versions of VisualText.

[2] **Upgrading.**  As always, care must be taken to upgrade or update existing analyzers and their knowledge bases.  We have added the topic [Updating Analyzers and KBs](Updating_Analyzers_and_KBs.md), which you should read and follow **BEFORE** uninstalling an older VisualText and installing the latest.   Also, analyzer project structure has changed slightly.  See [Structure of Analyzer Projects](VisualText_Basics/Structure_of_Analyzer_Projects.md).

[3] **Unicode hints.**  We've added the topic[Working with Unicode](Working_with_Unicode.md) to help here.

**Linux and Gnu C++.**  Analyzers built with VisualText can be configured to run on Linux with Gnu C++.  TAI periodically upgrades the port to the VisualText runtime libraries.  The libraries are not currently bundled with the VisualText release, and you may inquire about them by contacting us at info@textanalysis.com .

## Miscellaneous

(2.7.2.0) Rework of crawling functions eg [urltofile](urltofile.md), to handle HTTPS as well as HTTP. (2.7.0.9) New function [pnmove](pnmove.md) to enable moving nodes within the parse tree. (2.7.0.0) Overhauls, optimizations, and bug fixes focusing on the recursive NLP++ pass algorithm. (2.6.0.3) New function [dejunk](dejunk.md) to clean out non-ASCII and extended ASCII characters (sometimes replacing with a question mark character). (2.6.0.0) Important fix to NLP++ pattern matcher re feature-based match with wildcards.  **dicttokz** pass, a variant of dicttok that removes whitespace from parse tree at the outset, puts in attributes NOSP (no space before), NL (new line before).  Adds capitalization attributes to parse tree as well.  (This will be an ongoing development in 2.6.x.x). (2.5.0.0) New [dicttok black-box tokenization pass](VisualText_Basics/About_the_analyzer_sequence.md) that uses KB from TAIParse to put part-of-speech tags on parse tree automatically. See [DictTok_Sample](DictTok_Sample.md) analyzer. (2.4.x.x) Maintenance releases, various fixes in feature-based matching, compiled analyzers, etc. (2.3.2.0) In text windows ctrl-A now is Select All. ctrl-G is Find Again. (2.3.1.9) Maintenance release. Fixes to error reporting and recovery, compiled vs interpreted analyzers.. [group](group.md) now returns the new "reduce" node that it creates, an important convenience.  [group](group.md) also reports when it is including the [lookahead](lookahead.md) node -- an error.  [listadd](listadd.md) no longer treats the list node as the "reduce" node. (2.3.1.8) [xmlstr](xmlstr.md) now converts characters to &#123; where 123 is a character number, rather than to strings such as &frac14;. (2.3.1.6) Added special rule elements **[_xLET](_xLET.md)** and **[_xCAPLET](_xCAPLET.md)** to conveniently match single-character words. (2.3.1.0) VISUAL BASIC .NET API for calling VisualText analyzers.  See the sample program called [VB_to_VT](VB_to_VT.md), which also lists the API functions. (2.3.0.0) Compiling analyzers now generates separate code files for each pass, enabling large analyzers to be compiled into C++.  For example, the latest versions of TAIParse should now compile.  Note that a Microsoft Visual Studio project may now need to have files added to it, within an analyzer's RUN folder. (2.2.2.13) New PRE actions called [regexp](regexp.md) for matching using regular expressions, with [regexpi](regexpi.md) case insensitive version. (2.2.2.11) New function for sorting a knowledge base concept's hierarchy and children: [sorthier](sorthier.md) and [sortchilds](sortchilds.md). (2.2.2.8) Compiling analyzers once again generates PRETTY, or human-readable, code.  We tried very long lines to circumvent the 65K file line limit of some compilers, but too-long lines are an issue as well.  In subsequent versions, we'll be splitting files as needed.  For now, huge analyzers may need their generated C++ code (in the RUN folder) to be tweaked manually in order to compile. (2.2.2.5) EXITPASS, SUCCEED, and FAIL.  These functions have been restored in that they are allowed in practically any context without triggering error messages.  The compiled analyzer version uses C++ exception handling mechanisms in order to instantly handle these in deeply embedded contexts (function within a function, etc.)  Parse tree display ("yellow box") now places node variables in two columns for convenient viewing of long variable lists. Parse tree nodes now point back to rules that renamed them via [xrename](xrename.md) and [pnrename](pnrename.md).  Compile-during-analyzer-load popup of MS DOS window has been removed.  Interpreted user functions improperly returned a non-zero value in the absence of a return statement. (2.2.2.4) Incorrect VisualText TAB SIZE in Vista has been fixed. SAVE KB and COMPILE KB default popup answer is now NO.  (Unless you are explicitly trying to build a KB, then you don't want to save the KB.)  Parse tree for lone underscore character is now a terminal punctuation char.  Listadd in recursive passes when building a list right-to-left now fixed (compiled version hang fixed). [excise](excise.md) forbids deleting a lookahead node. (2.2.2.2) The functions [exitpass](exitpass.md), [succeed](succeed.md), [fail](fail.md), can appear only at the top level of code regions in compiled analyzers (**FIXED**. See 2.2.2.5 above).  Fixes to NLP++ syntax relating to negation.  A fix to float conversion.  Further fixes to optimized recursive pass algorithm. (2.2.2.1) Further fixes to align compiled and interpreted analyzers (fixes to zeroed items in relational operators and others).  Fix of an annoying VisualText crash when brought into focus from the background.  A substantial fix to the optimized recursive NLP++ pass algorithm in both the interpreted and compiled analyzer frameworks. (2.2.1.1) New function [pninsert](pninsert.md) for programmatically inserting nonliteral nodes into the parse tree. (2.2.1.0) NEW. A parse tree view mode that reflects items removed from the parse tree, such as HTML tags.  See [Tree Text Mode in the View Menu](VisualText_Interface/Main_View_Menu.md). Fix to some NLP++ compiled functions to enable zero (0) as a null string.  E.g., strsubst("ab,c",",",0); will replace commas by empty string in a compiled analyzer. Note that this behavior already works as expected in interpreted analyzers, e.g., those that run inside VisualText. (2.2.0.0) A substantially cleaned up VisualText release (see 2.1.0.9 notes below).  Tree Text view does not leave everything expanded on reentering VisualText, but remembers what folders have been closed up in the view. The RUN NEXT button behaves better. (2.1.0.9) A CLEANUP RELEASE.  ALIGNED INTERPRETED AND COMPILED ANALYZERS, FIXED MISC BUGS AND LEAKS.  Fixed a substantial bug that hobbled compiled analyzers.  Memory leaks plugged in eltnode and lasteltnode.  The PROG project or sample driver for analyzers now sets the BATCHSTART flag at the start of a run, to enable a compiled analyzer to test the NLP++ batchstart() function/flag. (So that an analyzer can perform initializations when it runs the first file of a batch of files.) DEFAULT configuration of VisualText is now full screen, kb safe mode off, toolbars in a standard configuration.  TIP OF THE DAY offers real suggestions. Fixed bugs in the PROG driver of each analyzer, for the analysis of multiple files and folders. (2.1.0.8) Fix to functions like resolveurl, strchr, strrchr. Fix to parse tree nodes with large string-valued variables.  Fixes to Tab Window and Find Window show/hide bugs.  Change to VisualText naming in the Windows registry.  Fixed a memory leak in rmattrs. (2.1.0.6) Fixes to file and directory handling.  (See the PROG project of a newly created analyzer project.) (2.1.0.3) Misc fixes, including parse tree display and return of arrays in NLP++ user-defined functions. (2.1.0.0) In order to support huge knowledge bases, a VisualTextQ version is provided that utilizes the QDBM database management freeware under the hood.  For backward compatibility, one can treat the knowledge base built in this way as the "compiled" knowledge base.  Loading the interpreted knowledge base will read kb command files into a QDBM file system.  "Compiling" the kb will save the latest version of the QDBM files -- not compiling the changes will discard the latest modifications to the kb. Other notes: Removed the Windows MS-DOS Command Prompt popups from most system calls. (2.0.2.9) The [levenshtein](levenshtein.md) edit-distance computation is provided. (2.0.2.8) Optimizations to string manipulation using L (local) variables.  These are not interned, as with S,X,G,N variables.  Locally assigned strings are completely freed when a scope (function, @CODE, @CHECK) is exited, while globally assigned strings are interned and persist throughout a text analysis.  Analyzers can be optimized by using local L variables wherever feasible. (2.0.2.7) [fltval](fltval.md) knowledge base value fetch. (2.0.2.5) Linux upgrade. (2.0.2.4) New variables **[G**("$passnum")](%24passnum.md) and **[G**("$rulenum")](%24rulenum.md) e.g. to track rule context and performance. (2.0.2.3) New NLP++ function [eltnode](eltnode.md), analogous to lasteltnode. (2.0.2.2) Recovery from very long tokens. (2.0.2.1) Refix of an infrequent crash in using $treetext. (2.0.2.0) Optimization to recursive passes. (2.0.1.1) Fixes to the **Find in Files** popup menu.  Bugs were introduced in VisualText 2.0: (a) missing patterns that start at the beginning of a line, (b) incorrect display of capitalization in found patterns.

# NEW IN CURRENT VERSION (2.0 NON-UNICODE BETA)

VisualText 2.0 is the first to be compiled with Microsoft Visual Studio .NET.  Within a few releases, Unicode support will be featured as well.

Professional version: While code generation is still automated, compiling analyzers and KBs will need to be done manually for version 2.  Similarly, user projects and other code will need to be upgraded to .NET and compiled, in order to work properly.  See the topic [VisualText Basics > Compiled and Standalone Analyzers](VisualText_Basics/Compiled_and_Standalone_Analyzers.md) for further guidelines.  Similarly for updating existing analyzers to version 2.

A new feature is the deaccent element modifier, which allows alphabetics to be matched without regard to accents on characters.  **NOTE:** Within a rule element, the deaccent keyword must precede any match, fail, and except lists, in order to work correctly.

Miscellaneous

(beta) The analyzer sequence can include folders, for organization and readability.  Passes can be dragged into the folders.

Fix to NOOP rule matches in recursive pass.  Matching continues after last node matched by such a rule.

Better infinite loop tracking in recursive passes, to catch A -> B and B -> A grammar loops ("2-state tracking").

FEATURE-BASED PATTERN MATCHING.  The functions below enable matching based on whether a node has a variable with a particular value.

[var](var.md)(var_name)    # If var has nonzero value. [varz](varz.md)(var_name)  # If zero or no var. [vareq](vareq.md)(var_name,str)  # If var equals str. [vareq](vareq.md)(var_name,num)  # If var equals num. [varne](varne.md)(var_name,str)  # If var not equal str. [varne](varne.md)(var_name,num)  # If var not equal num.

# NEW IN CURRENT VERSION (1.8)

NLP++ now features initial [mathematical functions](Table_of_Math_Functions.md).

# NEW IN CURRENT VERSION (1.7)

The 1.7 release includes various enhancements to VisualText.  Attention has been given to compiling and running analyzers within the Microsoft .NET environment.  Also, enhancements have been made to scalability: for example, the analysis of each text now uses and frees up local tables, so that analyzers should not grow as new texts are successively analyzed.  (Of course, an analyzer may save things to the KB, in which case overall memory size will increase.)

The knowledge base files in the kb\user directory are now managed in a new way, to better support scale up in the interpreted KB.  A main.kb top-level file invokes the other command files in that directory in order to load the interpreted knowledge base.  Also, the attr.kb file has been replaced by multiple files named attr1.kb, attr2.kb, and so on, depending on the size of the interpreted knowledge base.  Old-style knowledge base directories will automatically be upgraded whenever a knowledge base is saved.

See [Sample Analyzers > POStagger](POStagger.md) for an example analyzer that integrates a 3rd party part-of-speech tagger.

**Important:** See the Analyzer Upgrade Note for 1.6, below, regarding upgrading existing analyzers.

## Miscellaneous GUI

GUI behaviors have been changed.  Questions about compiling and saving the KB will be encountered as appropriate.  Also, when the analyzer sequence or properties are changed, a popup will ask to save those changes.

The GUI no longer uses the gui.kb file to record the analyzer sequence and the input file hierarchy.  Rather, the input file hierarchy is obtained from the file system, and the analyzer sequence definition is fetched from the analyzer's spec\analyzer.seq human-readable file.  The GUI still uses the KB to store this information on a temporary basis when the analyzer is loaded.

Some log files accessible in the Text Tab are now tracked by the Page Mode mechanism.  That is, their display will automatically update in tandem with the input file selected in the Text Tab.

Timing data for each pass of an analyzer is available in the dbg.log file.

The Finder Window now presents matches using the order of files in the current analyzer sequence.

Browser and input text type-in windows can now accept up to 1024 characters.

Some stale or broken pointers to VisualText Help topics have been fixed.

By default, new analyzers have the Verbose and Logs Toggle turned off.

## Miscellaneous NLP++

Scalability enhancement: Separate information tables are built and removed for the analysis of each input text.  This enables analyzers to run large numbers of texts without slowing down and without consuming extra memory (depending on whether the analyzer updates the KB).

Incompatible changes to API header files, User project, and standalone sample code.  Existing analyzers must be upgraded and recompiled.  Standalone code upgraded to recursively process directories of input files.  user::loadanalyzer fixed to create globally managed knowledge base.  NLP, CG, and VTRUN objects created and deleted only within the runtime libraries via API calls in VisualText\include\Api\lite\vtrun.h.

Storage tables in NLP++ and the Conceptual Grammar KBMS have been enlarged and their performance has been enhanced.  The differences can be substantial for larger input files.

Some automatic infinite loop monitoring is performed in passes with the ***recursive*** algorithm type set.

A bug in the ***fail*** plus ***except*** keyword logic has been fixed, within rule element modifiers.

Missing KB functions for floating point data type have been installed, as well as some missing compiled variants of NLP++ functions.

Some table sizes have been increased, e.g., for buffers returned by an analyzer called with **user::analyzefile** and **user::analyzebuf**.

Enhancements to analyzer error statements.  More warnings are issued if an NLP++ function is called with too many arguments.  Correct pass and line numbers have been added to many error messages.

The [dictgetword](dictgetword.md) function finds a dictionary word-concept, else makes a new one.  A renaming of [addword](addword.md).

The [take](VisualText_Basics/About_KB_Command_Files.md) command now handles relative paths.

The [sqlstr](sqlstr.md) function converts strings to a format for SQL entry into a database.  (Merely converts single quote to two single quotes.)

Bug fixes in compiled versions, string catenation and string functions, both in scaled up string sizes and 0 as a string.  Removed some null string warnings.

A compiled vs interpreted issue is that C/C++ conditional evaluation works in compiled but not interpreted.  So in expressions like A && B, assume that both the A and the B sides will always be evaluated.

(1.7.4) New analyzers now come with a prebuilt Microsoft Visual C++ user project, including the files **prog.dsw** and **prog.dsp**.  For professional version users, these enable convenient setup of a standalone sample analyzer.  See the Help topic [VisualText Basics > Compiled and Standalone Analyzers](VisualText_Basics/Compiled_and_Standalone_Analyzers.md).

(1.7.4.5)

Fixed **_xSTART** rule element modifier within a match list.

Fixed rare race condition in opting to not save knowledge base when exiting VisualText.

Fixed handling of inactive passes and changing active/inactive pass property.

Fixed [split](split.md) function to handle large string, added compiled variant of function.

Better handling of "composite" literals formed by rules such as:  redo <- re \- do @@

Fixed returns of some string processing functions.  Fixed crash on catenating null strings.

New function: [deaccent](deaccent.md) replaces accented characters in strings with unaccented characters.

Improved error checking in the @DECL region.

Fixed parse tree display for analyzing binary files.

GUI convenience: When logs turned off, clicking passes in Ana Tab will not redraw the parse tree.  Nicer to work with large input files now.

Fixed display of parse tree view for binary input files.

(1.7.4.6)

Fixed parse tree display of variables in yellow node popup when Node Variables toggle is off.

(1.7.5)

Added a new sample analyzer called POStagger (in VisualText\apps), which invokes an external part-of-speech tagger.  This analyzer shows how one can extend VisualText with 3rd party software.  See the [Sample Analyzers > POStagger](POStagger.md) description for more details.

Implemented the [setlookahead](setlookahead.md) action, allowing dynamic setting of the lookahead node after a rule match.

(1.7.6)

Housekeeping: Further alignment of compiled and interpreted. Fixed compiled-version of splice action and _xSTART in a match list.  Fixed Save KB crashes due to long concept names.  Fixed infinite loop on some optional rules with lookahead.

Added error messages for fully optional rules, range errors in NLP++ actions.

(1.7.7)

Fixed crashes with catenating empty strings.

Some fixes to the third party POS tagging handshake, handles paths with space characters.

The [permuten](permuten.md) function is useful for permuting lists of values.

# NEW IN VERSION (1.6)

**Analyzer Upgrade Note:**  Analyzers built with prior versions of VisualText will not load properly with the 1.6 version.  To upgrade existing analyzers, you'll want to compare and merge your existing analyzer project files with those within the VisualText\Templates\Bare analyzer template.  (If an analyzer was built using another template, best to compare with that one.)  After merge, you'll want to recompile the analyzer, knowledge base, user projects, and stand-alone driver program, if any.  Important places to look for mergeable files are:

- Files in the top level folder of the analyzer project (e.g., main.cpp)

- Kb folder code files (but do not overwrite your knowledge base files in Kb\user).

- Run folder

- User folder (not Kb\user).

**Warning:** Prior to any merge, we strongly recommend (1) making a safe copy of all your existing analyzers; (2) doing Save KB for analyzers that have a compiled knowledge base, in order to save the interpreted form of the KB; (3) making a comparison with each existing analyzer and the Bare template (or other template that you started with), using a tool such as WinDiff that comes with Microsoft Visual C++.

**Simple merge:** If you have only modified the analyzer sequence and pass files, then the merge is simple.  Copy everything in VisualText\Templates\Bare ***EXCEPT*** the **spec** folder, **kb** folder and **.ana** file, if any, to your existing analyzer project.  Then copy the top-level files in the Bare **kb** folder, ***EXCLUDING*** the **user** sub-folder, to your existing analyzer project.

## External and Multiple Analyzers

The NLP++ runtime system now enables analyzers to invoke other analyzers and allows multiple analyzers and knowledge bases to cleanly operate within the same executable program.

In the User project of an analyzer, the sample function User\Ucode.cpp\useranalyzefile may be called from an analyzer, e.g.,

G("buffer for result from analyzer") = user::analyzefile("analyzername","c:\\forexample\\inputfile.txt", "data to pass to analyzer via $datum variable", G("ostream"));

to invoke another analyzer (assumed to be in the area defined by the APPS environment variable). The called analyzer may grab the data from the 3rd argument via the special variable G("$datum").  Writing to the cbuf() stream enables the called analyzer to return data to the calling analyzer.

Another function, user::useranalyzebuf(), illustrates calling a second analyzer, as follows

G("result") = user::analyzebuf("analyzername", "input buffer...", "info for $datum special variable", G("ostream"))

so that a buffer can be processed by a called analyzer, which returns a buffer result to the calling analyzer.

The VisualText programmer's API has been enhanced to enable multiple analyzers to be loaded into memory once, while invoking each other multiple times.  Creating an NLP() object now takes an optional name string, so that analyzers may register themselves in memory and call each other by name.  The function [findana](findana.md) will help load once and run many times within VisualText itself.  (This capability is still under development.)

In order to enable load one and run many times for an analyzer, we also supply the function user::loadanalyzer(analyzername_str).  Thus one can set up to call a second analyzer as follows:

G("analyzer handle") = user::loadanalyzer("myanalyzer");

G("result") = user:analyzefile(G("analyzer handle"), G("input file"), G("stuff to pass down to $datum variable"), G("ostream"));

The second statement could be placed in a loop in order to analyze a set of input files, thereby saving on analyzer and knowledge base load time.

Note that the first argument to analyzefile and analyzebuf can be the analyzer name or the "handle", which currently are equivalent.  In anticipation of VisualText allowing multiple instances of the same analyzer, we recommend using the "handle" returned by loadanalyzer.

New: analyzefile and analyzebuf now also take an ostream argument (which can be 0), enabling the calling analyzer to specify an output stream for the called analyzer.

**Caveats:** Recursive calls to the same analyzer are not supported in the current version.  They may clobber some working areas such as the knowledge base and the output folder of an analyzer project.  Infinite calling loops must be guarded against (e.g., by passing down a counter).

## Compiling Knowledge Base

If automated compilation of an analyzer's knowledge base is failing, we recommend defining the user environment variable (in Start Button > Control Panels > System > Advanced > Environment Variables):

VCBIN = C:\Program Files\Microsoft Visual Studio\VC98\bin

This assures that the correct linker (named LINK.EXE) will be invoked by the makefile that compiles an analyzer's knowledge base.  (If your computer has several development programs on it, such as Visual Basic or Symantec Visual Cafe, then the wrong program named LINK.EXE may be found inadvertently by the system when linking C++ programs.  The above environment variable is used by VisualText to eliminate this conflict.)

## Miscellaneous

HOURGLASS CURSOR BUG - On some machines, especially new or fast machines, analyzing a file in VisualText may have led to a hung VisualText session.  This bug, due to a race condition between two threads, has been fixed.

Runtime Library Upgrades - Knowledge base and runtime libraries have been upgraded to remove global variables and install object-oriented programming constructs.

Compilation of larger analyzers has been enhanced by changes to the C++ code generated from pass files.  Some internal table sizes also have been enlarged.

Global string and hash tables used by the analyzer have been enlarged.

For display purposes, the new menu item Edit > Change Fonts... allows a user to bring up a standard font selection popup window.  In this way, text files may be displayed using fonts loaded in the computer  (e.g., Japanese fonts).

Some important fixes to problems with multi-valued NLP++ variables, e.g., going into and out of user-defined functions.

Deployment - The /silent command line option for standalone analyzers now eliminates extraneous outputs to the console.

Some fixes have been made to the error messages printed in the VisualText log window.  This overhaul is still in progress, and so some error messages may still not point to the file and line of code that led to a syntax or runtime error.

The [exitpass](exitpass.md) function has been upgraded to work in the @POST region.  It also works within if-else statements, lists of statements, and while-statements.  It should not be used within user-defined NLP++ functions, however.

Compiled variants of NLP++ code have been fixed, including *exitpass* and assignment statements (where an OSTREAM is being assigned to a variable).  *rightjustifynum* was fixed to handle null values identically in compiled and interpreted variants.

**L** local variables may now be used in the @CODE, @POST, and @CHECK regions.  They go out of scope when execution of code in a region is completed.

A bug has been fixed in matching rules that contained a triggered element along with wildcard elements to its left.  (Appeared only in compiled analyzers.)

When a browser window with a local HTML file was left open on exiting VisualText, the file could not be found when reloading the analyzer in VisualText.  This bug has been fixed.

The new function [nodeowner](nodeowner.md) has been implemented, usurping the functionality of of [nodeconcept](nodeconcept.md).  The former fetches the concept that owns the current phrase, while the latter fetches the concept that the given node is a proxy for.

The new function [sortconsbyattr](sortconsbyattr.md) sorts an array of KB concepts by comparing one of their attributes.

The new function [inputrange](inputrange.md) conveniently fetches substrings of the input text. For efficient printing of such ranges, [inputrangetofile](inputrangetofile.md) is provided.

The new function [strchrcount](strchrcount.md) counts the occurrences of a character in a string.

The new functions [dictfirst](dictfirst.md) and [dictnext](dictnext.md) enable convenient traversal of the words in the KB dictionary hierarchy.

The new Perl-like function [split](split.md) enables splitting a string into a multi-valued variable (i.e., an NLP++ array) using a given character as a separator.

New functions in support of web page processing: [urltofile](urltofile.md) fetches a web page as a file and [resolveurl](resolveurl.md) converts a relative URL to an absolute URL.  In conjunction with analyzers calling analyzers, these functions support web navigation (crawling, spidering, searching) within VisualText.  urltofile now has reasonable timeouts set for fetching a page from the web (but user cannot modify the timeout setting).

The new function [xmlstr](xmlstr.md) converts characters in a string appropriately for outputting XML or HTML files (e.g., converts "hello&bye" to "hello&amp;bye").

Fix to the [splice](splice.md) NLP++ action.  Developers should avoid addressing rule elements after actions such as *splice* and *merge,* because numbering is element numbering is unpredictable after such actions.

Variants of the NLP++ [strpiece](strpiece.md) function have been fixed.

Fixes to NLP++ expressions that compare non-numeric types with 0.  E.g. "G("str") == 0".  String catenation with one empty argument has been fixed (e.g., "hello" + 0).

Assignments involving OSTREAM data types have been fixed in the compiled version.

Many error messages have been fixed, but due to overhauls, the pass and line number are not always available to an error message.

Compiled rules with a trigger element and wildcards to its left have been fixed.  Compiled versions of Boolean testing for knowledge base data types, e.g., in an if-statement, have been fixed.

Local files in the Browser window now display properly when loading an analyzer.

Some enhancements have been made to "retokenization".  For example, one can write rules like

oversight <- over sight @@

in which the suggested concept is a literal, and have the new "oversight" node in the parse tree matched by _xALPHA.  Getting the text from N("$treeraw") will also work (though not from N("$text")).

In some 1.6 versions, cout() does not work.  This has been fixed.

# NEW IN VERSION (1.5)

Version 1.5 is primarily concerned with housekeeping.

Changes to the VisualText user interface behaviors make it more convenient to work with analyzers.  When you click the Run button, the cursor immediately changes to an hourglass.  In viewing parse trees regardless of settings, the yellow popup box for a node always displays its variables and values.  When Logs are turned off, the parse tree always displays the final parse tree.  When commenting text in the Editor, only highlighted lines get commented (fixing the "extra line commented" feature).

The runtime system for compiled analyzers has received major treatment.  For example, the compiled and interpreted versions of the latest TAIParse can have their intermediate log files and output files compared on a file-by-file basis using a program such as WinDiff.  Because interpreted/compiled analyzers are now well-aligned, it is easy to find any differences between the versions, as a debugging aid.  Missing compiled variants of NLP++ functions have been added and debugged.

# NEW IN VERSION (1.4)

## Database Connectivity

NLP++ now features database connectivity functions, more or less mirroring the standard set of ODBC functions.  All database types other than BLOBS are handled.  Values returned from a database are mapped to string, numeric, and float NLP++ types, as appropriate.  See [Database Functions.](Table_of_Database_Functions.md)

A sample analyzer illustrating connection to a database and other new features is in **Samples\database1**.  See also [Database1 Analyzer](Sample_Analyzers/Database1_Analyzer.md).

## Attribute Editor Enhancements

The [Attribute Editor](VisualText_Interface/Tools/Attribute_Editor.md) has been substantially overhauled.  Management of the knowledge base value types (string, concept, and numeric) is more coherent.  Methods have been introduced for specifying and viewing a concept as the value of an attribute.  Up and down navigation arrows have been added, enabling convenient perusal of the knowledge base while staying within the Attribute Editor.

## Miscellaneous

An analyzer may now cause the creation of a popup window within VisualText, with the new functions **exittopopup**() and **getpopupdata**().

The built-in database function **[dbbindcol](dbbindcol.md)**() is the first to employ call-by-reference within NLP++.  User-defined functions may not use call-by-reference at this time.

A **silent** flag in standalone analyzer API calls minimizes the amount of debugging and logging output produced during the operation of a text analyzer.

A function for gathering command line arguments has been placed within the sample standalone code, e.g., in **Bare\main.cpp**.

# NEW IN VERSION 1.3.1

## Miscellaneous

The VisualText GUI now highlights contiguous text regions with alternating dark and light colors.  That is, dark blue and light blue alternate to display new nodes built in a pass, while dark and light green alternate to show nodes matched in a pass.

The conversion functions [num()](num.md) and [str()](str.md) now handle floating point.

A call-by-reference capability has been implemented for NLP++ builtin functions.  Not yet available to user-defined NLP++ functions.

**ind wattr**, a command for more conveniently adding knowledge to the kb via command files.  See [About KB Command Files](VisualText_Basics/About_KB_Command_Files.md).

Fixed an overflow buf in spelling functions.

# NEW IN VERSION 1.3

## Output to User-Supplied Stream and Buffer

In standalone/embedded analyzers, users may now provide an output stream and an output buffer to the analyzer.  Output to these is enabled by the new NLP++ functions [cout()](cout.md) and [cbuf()](cbuf.md).  [coutreset()](coutreset.md) enables rebinding the output stream to a file, while [interactive()](interactive.md) checks to see if the analyzer is running in an interactive environment, e.g., within VisualText.  Further documentation is available in the topic [Compiled and Standalone Analyzers](VisualText_Basics/Compiled_and_Standalone_Analyzers.md).

# NEW IN VERSION 1.2

## Enhanced User-Defined NLP++ Functions

In version 1.1, we introduced the @DECL region and user-defined function definitions within NLP++.  With Version 1.2, support for NLP++ functions is much improved, including parameter lists, arguments, return statements, recursive function calls, and compilation of all the above.  To implement parameters, we introduce the local variable reference **L**, similar to the **S**, **X**, **N**, and **G** variable references that are key to NLP++.  **L** is used not only for parameters, but can define variables local to the function body.

# NEW IN VERSION 1.1.2

## Event-Based Functions in User Project

The functions **ucodeIni()** and **ucodeFin()** are available in the User project of an analyzer.  The analyzer developer may place initializations in ucodeIni that operate immediately after the analyzer is loaded.  Analogously, cleanups may be placed in ucodeFin, which operates immediately before the analyzer is closed.

## Improved Checking on Overly Large Input Texts

Enhancements are in progress that check against an overly large input text file.  More generally, when the analyzer has expended all available space resources, then the system will degrade more gracefully rather than crashing.  It is recommended that an input file of about 1MB maximum be run through a typical text analyzer.

As always, huge texts will need to be split up into buffers or multiple files before presentation to a text analyzer, in general.  The VisualText knowledge base can serve to manage information across multiple segments of a huge document.

# NEW IN VERSION 1.1

## User-Defined NLP++ Functions

VisualText 1.1 introduces user-defined NLP++ functions.  Up to now, users could only add functions via the C++ **user **project associated with each analyzer project, or by requesting that a function be added by TAI to the NLP++ builtin functions.

The current version is a pre-release of the user-defined function capability.  No return statements and no parameter lists can be written in functions yet.  Nor are there templates that define the inputs and outputs to a function, nor is overloading of function names allowed.  Even so, the new capability substantially enhances the power of NLP++ for complex tasks.  Rather than repeating the same code in many places, functions enable the code to be written in a single centralized location.

Functions are placed in the new @DECL region, which must be the first region in a pass file, when present.  Functions may be called from passes that precede the function definition (i.e., forward reference).   A sample is

@DECL

# User-defined function definitions.

myfunction() { "output.txt" << "Entering myfunction." << "\n";** G**("tmp") = 3; }

@CODE myfunction();   # A call to user-defined function.

An interesting feature of NLP++ functions is that their operation can optionally depend on the region they are called from.  For example, in functions called from a @POST region, the user may use the **S**, **N**, and **X** variable references as though the function's code were placed directly within the region.

## Double-Click Parse Tree Node

A new backtrace and debugging capability is the following.  In a Parse Tree window, double-click on a node, and the pass file that created that node will open in the Workspace.  Further, the cursor will be placed at the start of the precise rule that created the node.
