# Updating Analyzers and KBs

This topic applies to the latest version of VisualText.  You may want to read the topic [Compiled and Standalone Analyzers](VisualText_Basics/Compiled_and_Standalone_Analyzers.md) for background.

In case you need to merge code from your old analyzers, we recommend using **WinDiff** (available with MS Visual Studio 6.0).  Also, note the new include files referenced in the prog and user projects, as well as code changes that compile with both Unicode and non-Unicode configurations (see the API header file **Program Files\TextAI\include\Api\my_tchar.h** as well as studying the new code files).  Finally, note that the prog, kb, run, and user projects now all include Unicode_Release configurations which may need to be compiled for Unicode VisualText.

**WARNING: BEFORE** uninstalling an older VisualText and installing a later version, one should do steps [1] and [2] below.

**LIMITATION:** At present, we have no simple method for converting a Unicode KB to an ANSI KB.  You may need to manually edit out all Unicode characters.

[1] **Get interpreted KB.**  For each analyzer you want to update, you'll need to make sure it has an up-to-date INTERPRETED form of the knowledge base.  This is because compiled KBs (kb.dll) will not load with the new VisualText.

![](../helps/Tutorials/GO.gif) Simplest is to click the Save KB button (or select Save KB from the KB menu).  This assures that you generate the latest interpreted version of a knowledge base, whether you use a compiled analyzer or not.

[2] **Back up analyzers.**  Prior to upgrading the VisualText version, make a safe copy of your analyzers.  This will give you a fallback in case something goes wrong during the update process.

[3] **Install new VisualText.**

![](../helps/Tutorials/GO.gif) Follow the instructions provided to you with the latest version of VisualText.

[4] **Create new analyzer.**  In general, the best way to update an analyzer is to create a new version from scratch, then merge parts of the old analyzer into the new.

![](../helps/Tutorials/GO.gif) Rename the old analyzer, e.g. c:\apps\myAnalyzer to c:\apps\myAnalyzer_saf

![](../helps/Tutorials/GO.gif) Create a new analyzer of the same name by invoking VisualText, selecting File > New Analyzer, and selecting the Bare template.

![](../helps/Tutorials/GO.gif) If you will use a compiled KB, check the box at File > Preferences > Analyzer Dependent > Load Compiled KB. (Don't worry, if the analyzer doesn't find a compiled KB it will still load the interpreted KB.)

![](../helps/Tutorials/GO.gif) Exit VisualText.

Next we'll merge the old analyzer into the new, one piece at a time.

[5] **Merge KB.**

![](../helps/Tutorials/GO.gif) Copy the interpreted kb from your old analyzer, e.g., at **myAnalyzer_saf\kb\user**.

![](../helps/Tutorials/GO.gif) Paste this user folder into the new analyzer at **myAnalyzer\kb**.  (Yes to overwrite everything).

[6] **Merge Run.**  The analyzer's **\run** folder is automatically managed by VisualText, so don't muck around in here!  Once it's updated, you can manually compile the analyzer in here. (Professional version only.)

[7] **Merge Prog**.  Prog is a sample driver program that comes with an analyzer. (Usable in Professional version only.)

![](../helps/Tutorials/GO.gif) If you use the Prog driver, then follow instructions in the [Compiled and Standalone Analyzers](VisualText_Basics/Compiled_and_Standalone_Analyzers.md) topic.

![](../helps/Tutorials/GO.gif) If you've made your own modifications, you'll need to manually merge **\myAnalyzer_saf** files into **\myAnalyzer**.

![](../helps/Tutorials/GO.gif) Compile the Release or Unicode_Release configuration, as appropriate.

[8] **Merge User Project**.  An analyzer's user project is where extensions to the NLP++ language can be added, third party code can be integrated, and so on.

![](../helps/Tutorials/GO.gif) If you haven't modified the user proejct, then you're done.

![](../helps/Tutorials/GO.gif) If you have modified the user project, you'll need to merge your code from **myAnalyzer_saf\user** with **myAnalyze\user**.

![](../helps/Tutorials/GO.gif) Compile the Release or Unicode_Release configuration, as appropriate.

## NOTES:

[1] In 2.0.1.x and later, various analyzer DLLs have been moved and renamed.  In most cases, you'll find them in the **\bin** folder of a project, with names to distinguish Unicode from non-Unicode versions.

[2] Non-Unicode analyzers should be amenable to loading in the Unicode VisualText.  However, Unicode analyzers will not load correctly in the ANSI VisualText.

[3] We recommend using a particular analyzer with either ANSI VisualText or Unicode VisualText, not both.  Once you start placing Unicode characters in analyzers and knowledge bases, you can't then run them in the ANSI VisualText.

[4] We recommend naming analyzers according to whether they are Unicode or ANSI.
