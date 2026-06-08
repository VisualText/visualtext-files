[← Help Contents](../../../index.md) | [📘 NLP++ Textbook](../../../NLP++_Textbook.md)

# Adding Passes

When you add a pass to the analyzer sequence you are also creating the pass file that is associated with the pass. You can associate existing pass files from another analyzer project with a new pass in the analyzer sequence.

VisualText also comes with a set of **library passes** that can be added to the analyzer sequence.  Library passes are pre-built passes that contain code to recognize telephone numbers, email addresses, dates, money and other common patterns. Some library passes are available as VisualText analyzer templates.

**To add a new pass to the analyzer sequence**:

1. In the **Ana Tab**, click on the pass in the sequence where you want to insert the pass. The new pass will be added AFTER the pass you select.

1. With the mouse in the Ana Tab, right-click and select **Add** > **New Pass**.

1. In the **Pass Properties** dialog box, give the pass file a **name**. (For pass names with multiple words, we recommend using an underscore between the words.)  For **Type**, select Pattern for a pattern based pass or Recursive for a recursive one. By default the pass is set with the **Active** flag, meaning the pass will be processed the next time the analyzer is run. (To inactivate the pass, see [Inactivating a pass](../../Hand_Building_Pass_Files/Inactivating_a_pass.md).)

1. Click **OK** to finish creating the pass. The newly pass is added to analyzer sequence.

**To associate an existing pass file with a pass in the analyzer sequence**:

1. In the **Ana Tab**, click on the pass in the sequence where you want to insert the pass. The new pass will be added AFTER the pass you select.

1. Right-click and select **Add** > **Pass from File**.

1. Navigate to the directory where the pass file exists.  (For example, c:\apps\myAnalyzer\spec.)

1. Select the **pass file** and click **Open**.  The pass is added to the analyzer sequence.  The name of the pass defaults to the name of the existing pass file.

**To add a library pass to the analyzer sequence**:

1. In the **Ana Tab**, click on the pass in the sequence where you want to insert the pass. The new pass will be added AFTER the pass you select.  If a library pass contains more than one pass in the sequence, all passes are added to the Ana Tab.  The number following the library pass name indicates the total number of passes in the sequence.

1. Right-click and select **Add** > **Library Pass**.

1. Select the **pass** from the menu.

| **Library Pass** | Pass Name |
| --- | --- |
| Date Plus Numerics | RecursiveCharPatterns NumericLists |
| HTML | HTML_TagStructure |
| Xml | XML_DeclarationConstructors2 XML_TagStructure |
| XML DTD | XML_DTD_DeclarationConstructors2 |

| **Tip**: You can add pass files to TextAI\VisualText\data\spec directory located in the install directory to create your own set of library of passes. |
| --- |

## See Also

[Editing Pass Files](Editing_pass_files.md)

[Moving Passes](Moving_passes.md)

[Analyzer Templates](../../../Analyzer_Templates.md)
