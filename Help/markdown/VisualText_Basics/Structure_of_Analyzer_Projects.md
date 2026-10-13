[← Help Contents](../index.md) | [📘 NLP++ Textbook](../NLP++_Textbook.md)

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

## Log files

A run writes logs in three places. Each file is rewritten on every run, so none of them grows across runs. Two files are both named `dbg.log` but hold different things.

**`logs/`: building the analyzer.** Written when the engine loads the analyzer, before any text is analyzed.

| File | Contents |
|---|---|
| make_ana.log | Errors and warnings from reading the pass files, each as `<pass> <line> [message]`. A syntax error in a rule file shows up here. |
| cgerr.log | Knowledge base loading: which `kb/user` files were read, and KB errors. |
| dbg.log | How long each step of parsing the analyzer's own rule files took (`tokenize`, `retok`, `bigtok`, ...). Not the analysis timings. |
| file.log | The input files analyzed in this run, one `File=` line each. |

**`input/<file>_log/`: analyzing one input file.** One folder per input file, next to it.

| File | Contents |
|---|---|
| err.log | Errors from running the analyzer on this file, each as `<pass> <line> [message]`. The VS Code extension shows these as squiggles in the pass files. |
| dbg.log | How long each analyzer pass took on this file, with the slowest passes ranked at the end. |
| final.tree | The parse tree after the last pass. |
| ana001.tree, ... | The parse tree after each pass. Only with `-DEV`, and costly to write. |
| missing-words.log | Words not found in a lazily loaded `*full.dict` or `*full.kbb`, when the analyzer has one. |

Files the analyzer itself writes, such as `out.txt` or a `.kbb` from `SaveKB`, go here too.

**`output/`: engine startup.** `init.log` records loading the optional `bin/user.dll` extension library. `dbg.log` and `def.log` are opened at startup but nothing is written to them; they are always empty.
