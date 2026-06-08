[← Help Contents](../../index.md) | [📘 NLP++ Textbook](../../NLP++_Textbook.md)

# Workspace Toolbar

![](../../../helps/VisualText_Interface/Toolbars/workspaceToolbar.gif)

The Workspace Toolbar provides access to the analyzer, knowledge base and controls various functions with the display of parse tree information.

| **Button** | **Name** | **Description** |
| --- | --- | --- |
| ![Attribute Editor](../../../helps/Toolbar_buttons/attr_edit_button.gif) | Attribute Editor | Launches the Attribute Editor |
| ![KB Editor](../../../helps/Toolbar_buttons/kb_editor_button.gif) | KB Editor | Launches the KB Editor. |
| ![Move Concept Up](../../../helps/Toolbar_buttons/move_concept_up_buttong.gif) | Move Concept Up | Moves a selected concept in the concept hierarchy 'up' one position. |
| ![Move Concept Down](../../../helps/Toolbar_buttons/move_concept_down_button.gif) | Move Concept Down | Moves selected concept in the concept hierarchy down one position. |
| ![Save KB](../../../helps/Toolbar_buttons/save_kb_button.gif) | Save KB | Makes changes to the KB permanent. Changes made during a VisualText™ session are stored in memory. If KB is not saved, all changes made are lost upon exiting |
| ![Compile KB](../../../helps/Toolbar_buttons/compile_kb_button.gif) | Compile KB | Compiles the Knowledge Base. Action results in the creation of a KB.DLL. Preferences to load the compiled Knowledge Base can be set in Preferences from the File Menu. The KB.DLL library can be used with either an interpreted or compiled VisualText-built analyzer. |
| ![Compile Analyzer](../../../helps/Toolbar_buttons/compile_analyzer_button.gif) | Compile Analyzer | Turning on this toggle, followed by loading an analyzer, results in compiling the analyzer while it is being loaded. This results in the creation of a RUN.DLL library, which can be called from an external program. Currently, VisualText does not load the compiled analyzer library. The Compile Analyzer toggle is turned off after an analyzer is loaded. |
| ![Generate Dirty](../../../helps/Toolbar_buttons/generate_dirty_button.gif) | Generate Dirty | Generates rules only for those rule concepts in the Gram Tab that have the **Dirty** attribute set. This attribute is set by the system, for example, when new sample data is added to the concept. This is a "quick-and-dirty" rule generation that most often works well, but may not always agree with the Generate Rules > All option. It is used for rapid prototyping. See Mark for Generation in the Gram Tab Popup Menu, where the Dirty attribute can be set. |
| ![Slog](../../../helps/Toolbar_buttons/slog_button.gif) | Slog | Does a Generate Rules All, followed by a Run on the currently selected input. |
| ![Run](../../../helps/Toolbar_buttons/run_button.gif) | **Run** | Runs the analyzer on the currently selected input file. (Analyzers can not be run on files with a .log extension.) |
| ![Run Next](../../../helps/Toolbar_buttons/run_next_button.gif) | Run Next | Runs the analyzer file on the next file in the directory after the currently selected file. |
| ![Stop Analyzer](../../../helps/Toolbar_buttons/stop_analyzer_button.gif) | Stop Analyzer | Stops the current analyzer. |
| ![Toggle Highlight Mode](../../../helps/Toolbar_buttons/toggle_highlight_mode_button.gif) | **Toggle Highlight Mode** | When selected, enables highlighting of words or phrases in a text file matching selected pass in the Ana Tab or selected concept in the Gram Tab. Must be enabled before an analyzer is run over text. This tool allows you to quickly see whether and where a rule is applying. |
| ![Toggle Generate Logs](../../../helps/Toolbar_buttons/toggle_gen_logs_button.gif) | **Toggle Generate Logs** | When selected, enables generation of intermediate logs for each pass in the analyzer sequence. Must be enabled before an analyzer is run over text. This function gives you the ability to display and inspect the intermediate parse trees, one for each pass, and the final tree. It may slow the parse substantially in many-pass analyzers, since all intermediate trees are written to disk. If the function is not enabled, only the final tree is available for display. |
| ![Toggle Verbose Mode](../../../helps/Toolbar_buttons/toggle_verbose_mode_button.gif) | Toggle Verbose Mode | Enables the display of details from the loading of the analyzer. Results are displayed in the Log Window. |
| ![Toggle Batch Mode](../../../helps/Toolbar_buttons/toggle_batch_mode_button.gif) | Toggle Batch Mode | Instructs VisualText to analyze groups of files in an efficient mode. VisualText does not save intermediate and output files in batch mode. The text analyzer must explicitly create a location for output that is to be retained in batch mode. The NLP++™ function called batchstart() enables a text analyzer to check when the first text in a batch run is being analyzed. |
