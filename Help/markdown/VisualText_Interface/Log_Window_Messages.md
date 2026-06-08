# Log Window Messages

Two types of messages are given in the Log Window: [informational](#info_messages) messages and [error](#error_messages) messages.

The Log Window is divided into two parts: Events and Details.

## Informational Messages

Here are some of the most common informational messages displayed in the [Log Window](../Log_Window.md).

| **Message** | **Description** |
| --- | --- |
| Loading stat: Initializing time | Time basis for start of boot sequence timing. |
| Loading stat: “Auto-load” analyzer turned off | Time required to load IDE without an analyzer. (See the General Preferences for auto-loading an analyzer at startup.) |
| Loading stat: Total time | Time required to load IDE. |
| Loading stat: Loading "analyzerName" KB - NUM | Time required to load the KB for analyzer called analyzerName. |
| Loading stat: Loading "analyzerName" Analyzer - NUM | Time required to load the analyzer. |
| Loading stat: Finalizing - NUM | Time required to finish load sequence. |
| Loading stat: Total time: NUM | Total time required to load knowledge base and analyzer. |
| Analyzer Load: 0 0 [Date: Day, Month, Time, Year] | Day, date and time analyzer is loaded. |
| Analyzer Load: 0 0 [Read analyzer sequence from kb.] | Indicates analyzer is being read from the knowledge base. |
| Analyzer Load: 0 0 [Build analyzer time=NUM sec] | Total time to build analyzer. |
| Analyzing (NUM) TextFile | Name of text currently being analyzed. |
| Time = NUM | Time required to process text. |
| Analysis done (NUM) FilePath | Name and directory path of analyzed file. |

## Error Messages

Error and warning messages are displayed in the Log Window. These messages provide you with a way of seeing what is happening when the analyzer is run. They can be a valuable tool when debugging your analyzer. Some of the most common error messages are given below.

| **Message** | **Description** |
| --- | --- |
| RightMatchSpecial unimplemented | Indicates _xWILD may have been used at the beginning and/or end of a rule's phrase. This is currently not supported. Try _xANY instead. Or try _xWILD in combination with _xSTART and/or _xEND such that _xWILD does not occur at the beginning or end of the phrase. |
| No Rule Reduce: Can’t attach semantic data | Indicates that an S variable will be discarded, since the rule does not create a suggested node. |
| Check: Error in NLP++. Code actions: Error in NLP++. Post actions: Error in NLP++. | Indicates a runtime error in a CODE, CHECK, or POST region of a pass file. Possible errors are an NLP++ syntax error or a mismatch between the code and the rules that it applies to. For example, if an optional rule element matched no nodes, but the code attempts to assign a variable to the element's node, this error message will appear. |
| Error. Analyzer pass '<NAME>' is uninterned | Indicates that a pass in the analyzer sequence contains syntax errors and is being skipped over. |
| Pat pass given no rules | Indicates possible syntax error in a rule of the pass file. Check for missing CODE Region labels. |
