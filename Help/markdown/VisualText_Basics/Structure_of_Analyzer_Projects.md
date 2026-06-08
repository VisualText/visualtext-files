# Structure of Analyzer Projects

When an analyzer is created and saved in VisualText™, a directory structure is created in the working directory (e.g. C:\apps). This structure is referred to as the **analyzer** **project**. The analyzer project stores the analyzer and its related files.

An analyzer project is organized by a single **analyzer project file**. The analyzer project file is automatically created when you create an analyzer. The name of the analyzer project file is the name you give the analyzer project appended with a **.ana** extension. The analyzer project file, also called the .ana (pronounced "dot ana") file, is used to load the analyzer.

**NOTE 2.0.1.x and later:** Run, KB, and user DLL files are now renamed and moved to the \bin folder when they are compiled.  (And these must be compiled manually.)

The folders and files in the analyzer project are outlined below.

| **Folder or File** | **Description** |
| --- | --- |
| bin | Executables and libraries. Stores the kb.dll compiled knowledge base library. **NEW in 2.0.1.x and later:** DLLs have been renamed and moved to bin: kb.dll, kbu.dll, run.dll, runu.dll, user.dll, useru.dll |
| data | Miscellaneous data files created or used by the app. |
| logs | Directory for the analyzer log file. |
| input | Input file tree. |
| kb | The interpreted and compiled KBs (**kb.dll**) are stored here. |
| output | Directory for output files, dump files, log files, intermediate output files, and so on. |
| rfa | Output for the RFA, which parses the RFB analyzer definition. |
| rfb | Output for the RFB, which parses pass files. |
| run | Directory for the compiled analyzer library, **run.dll**. |
| spec | Directory for the analyzer sequence file and pass files. |
| user | Directory for the **user** MS Visual C++ project. Can be used to write new NLP++ functions and passes. |
|   |   |
| cgerr.log | KB error log file. |
| gui.kb | KB command file that stores analyzer sequence and input folder hierarchy. |
| main.cpp | Code file for a standalone driver program to call the analyzer. |
| NAME.ana | The project file for the current analyzer app. |
| Uanalyze.cpp | Code file for standalone driver program. |
| Uanalyze.h | Code file for standalone driver program. |

This folder structure houses all the information needed to run the analyzer, including folders for input and output, a folder for the knowledge base, etc.
