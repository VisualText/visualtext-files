[← Help Contents](../index.md) | [📘 NLP++ Textbook](../NLP++_Textbook.md)

# Basic steps for creating a text analyzer

This topic outlines the basic steps for creating and running a text analyzer using VisualText. Since VisualText can be used to create many different types of text analyzers, we will give a rough outline of the overall process of creating, running and defining a text analyzer.

**Creating a new analyzer project**:

1. From the **File** menu, select **New Analyzer**.

1. In the **New Analyzer** dialog, provide the following information:

- **Analyzer Name**: This name will be used to organize the analyzer project. VisualText automatically assigns a .ana extension to the name to mark it as the analyzer project file. You use the .ana file to open the analyzer project.

- **Location: **Select the default location or navigate to the drive and folder that you would like to save the analyzer project in.

- **Template**: Select "Bare". (Currently, the only template available is Bare.) Bare is the absolute basic or minimal analyzer.)

1. Click **OK**.

**Creating text files to be analyzed**:

1. In the **Text** Tab, right click and select **Add** > **New Text File**.

1. In the dialog box, give the text file a **name**.

1. Click **OK**. The newly created text file opens up in the Workspace. (The text file is stored in the **input** folder of the analyzer project. You can also add files to be analyzed directly into the input folder.)

**Adding and saving text to a text file**:

1. Double click on the a file in the **Text** Tab to open it in the **Workspace**.

1. Add text to the file.

1. Save the file by right-clicking on the file and selecting **Save**. You can also use the save icon on the Main Toolbar. ![](../../helps/Toolbar_buttons/save_button.gif)

**Defining the analyzer sequence**:

The analyzer sequence, made up of **passes**, is viewed and managed in the **Ana Tab**. A pass is a discrete step in the analyzer sequence that has its own pass algorithm. Each analyzer project comes with a built-in pass in the analyzer sequence. The default pass **tokenize** tokenizes each of the characters in an input file into token types, such as **alpha** for alphabetic, **num** for numeric, **punct** for punctuation, etc. As you build your analyzer, you add passes to the analyzer sequence after the tokenize pass. Each pass in the analyzer sequence is associated with a **pass file** that contains NLP++ code and rules which instruct the rule matcher what to do. Here is how you add passes to the analyzer sequence:

1. Select the pass in the analyzer sequence where you want to add a pass.

1. Right-click and select, **Add** > **New Pass**. (The pass is inserted AFTER the pass you selected.)

1. In the Pass Properties dialog, provide the following:

- **Name**: This is the name for the analyzer pass.

- **Type**: Select Pattern for a pattern-based pass and recursive for a recursive pass.

1. Click **OK**.

The new pass is created in the analyzer sequence. To edit the pass, double click on the pass to open the associated pass file in the Workspace. For a description on editing pass files, see the Developer's section.

**Running an analyzer**:

1. Select a** **file in the **Text** **Tab**.

1. From the **Analyzer** Menu, select **Run**. You can also use the run icon from the Workspace toolbar. ![](../../helps/Toolbar_buttons/run_button.gif) A red checkmark on the file icon indicates that the file has been analyzed.

When an analyzer is run, a parse tree is created for the analyzed text. How you define your analyzer sequence and pass files will determine what kind of information will be displayed in the parse tree.

**Viewing the parse tree of an analyzed text**

1. Select the analyzed file in the **Text Tab**.

1. Click on the Parse Tree button. ![](../../helps/Toolbar_buttons/view_entire_tree_button.gif) You can also open the file in the Workspace, right-click on the file and select **View** > **Parse Tree**.

**Saving the Analyzer**:

1. Select **Save Analyzer** from the **File** menu. Save Analyzer saves the analyzer project and the associated Knowledge Base. (You should save your project often.)

1. Answer **Yes** to the prompt asking if you want to save the analyzer.
