# Compiled and Standalone Analyzers

This section is concerned with configuring and using text analyzers outside the VisualText™ environment. It covers:

- Standalone analyzer

- Command-line arguments for an analyzer

- Analyzer and knowledge base APIs

- Compiling the analyzer

- Compiling the knowledge base

- Extending NLP++ functionality

- UPDATING ANALYZERS

We assume that an analyzer has been built using VisualText, and that Microsoft Visual C++ is available to the developer.

**Linux and Gnu C++.**  Analyzers built with VisualText can be configured to run on Linux with Gnu C++.  TAI periodically upgrades the port to the VisualText runtime libraries.  The libraries are not currently bundled with the VisualText release, and you may inquire about them by contacting us at info@textanalysis.com .

## Overview

The *interpreted* text analyzer constructed with VisualText consists partly of the definition files within the application's **spec** folder. The spec folder contains the analyzer sequence file (**analyzer.seq**) that defines the order of text-analysis passes, as well as the pass files (**.pat** files) that specify the rules and code to be executed at each pass. The analyzer engine and knowledge base management system (KBMS) are implemented as DLLs that execute the interpreted knowledge within the spec folder and within the **kb** folder, respectively. In addition, the app's **user** project is available for adding new NLP++ functionality to the core functions provided with VisualText.

When the user compiles the analyzer, C++ code is generated, placed in the app's **run** folder, and compiled using MS Visual C++. When the user compiles the knowledge base, the app's **kb** folder is similarly updated.

C++ code files are also provided for a default standalone analyzer. The user creates an empty project and adds the C++ files at the application's top level folder (**main.cpp** and so on). The default standalone analyzer exemplifies the way in which a VisualText application can be embedded in larger programs.

The following sections provide further details about these topics.

## Standalone Analyzer

Analyzer templates (such as Bare) come with prebuilt Microsoft Visual C++ project files **prog.dsw** and **prog.dsp**, which contain most of the project settings described below.  You should be able to just modify the line in main.cpp and compile this project to have a standalone version of your analyzer.

Instructions for creating and running the standalone analyzer:

1. Make sure that your app folder (e.g., C:\apps\chatter) has the latest versions of the code files, by comparing with the files in the directory VisualText\Templates\Bare. The files include main.cpp, Uanalyze.cpp, Uanalyze.h, and possibly others.

2. Use MS Visual C++ to create a standalone application in the app folder (e.g., an empty Win32 Console Application). Use the name of the app folder to name the project and create the project within the app folder.

3. Add the code files in the app folder to the project.

4. Edit the Project Settings: In *Project Settings > C/C++ tab > Category: Preprocessor > Additional include directories:* add the filler ***$(VISUALTEXT)\include\Api***

In *Project Settings > C/C++ tab > Category: Code Generation > Use run-time library:* select

(in Release config) ***Multithreaded***

*** ***   (in Debug config) ***Debug Multithreaded***

In *Project Settings > C/C++ tab > Category: General > Debug info:* select

(in Release config) ***None***

(in Debug config) ***Program Database***

In *Project Settings > Link tab > Category: Input > Additional library path:* add the filler ***$(VISUALTEXT)\lib***

In *Project Settings > Link tab > Object/library modules:* append the text   (in release config:) ***libconsh.lib lite.lib libprim.lib***

(*if available*: in debug config:) ***libconshd.lib lited.lib libprimd.lib***

In *Project Settings > Debug tab*: you may want to set up an input text file to process for testing purposes.

5. In main.cpp, edit the name of the application. e.g., **appname = "chatter";  **This name must conform to the name of the top-level folder of the analyzer project.

6. Build the program in the standard fashion within the MS Visual C++ environment.

## Command Line Arguments

Invoking a standalone analyzer (built as above) looks like

*analyzer-executable* [/INTERP][/COMPILED][/IN *infile*] [/OUT *outfile*] [/DEV] [*infile* [*outfile*]]

The various arguments are

| ARGUMENT | DESCRIPTION |
| --- | --- |
| /INTERP | Run the interpreted analyzer (this is the default). |
| /COMPILED | Run the compiled analyzer (run.dll). |
| /IN *infile* | Specify the input file to be analyzed |
| /OUT *outfile* | Specify the output file [SEE NOTES] |
| /DEV | Developer's verbose mode (e.g., output intermediate logs). |
| [*infile* [*outfile*]] | Unmarked args are input file followed by output file. |
|   |   |

## Analyzer and Knowledge Base APIs

The code files in the top level folder of an analyzer project demonstrate API calls to load and run the analyzer and knowledge base.  The API header files are located by default in

C:\Program Files\TextAI\VisualText\include\API

and its subfolders.  The main API header files are

**API\lite\nlp.h**, which specifies function calls for creating an NLP object to manage an analyzer and run it on input text files or buffers, and

**API\consh\cg.h**, which specifies function calls for creating a CG object to manage, access, and modify the knowledge base.

The header documentation in nlp.h is repeated here for reference.

```
THE MAIN API FUNCTIONS
 ARE:
```

```
NLP              =
 Create the NLP object to manage analyzer.
```

```
make_analyzer    =
 Create and load a text analyzer.
```

```
API CALLS FOR NORMAL
 RUNNING OF ANALYZER ON A TEXT:
```

```
analyze          =
 Run analyzer on a single text.
```

```
API CALLS FOR STEPPING
 THROUGH ONE PASS AT A TIME:
```

```
apiInitAnalyzer  =
 Initialize stepwise interp analysis of a text.
```

```
apiStepAnalyzer  =
 Execute next pass in the analysis of a text.
```

```
apiCleanAnalyzer =
 Clean up stepwise analysis of a text.
```

We describe the call to analyze(), which is the main function that you'll call outside VisualText to analyze a text.  Note that an example of the use of the API calls *NLP*, *make_analyzer*, and *analyze* is found in the main.cpp file of any analyzer project.

```
void
 analyze(
```

```
   char
 *input,         //
 INPUT FILE PATH.
```

```
   char
 *output,        //
 OUTPUT FILE PATH.
```

```
   char
 *appdir,        //
 ANALYZER APPLICATION TOP DIR.
```

```
   bool
 flogfiles,      //
 OUTPUT INTERMEDIATE LOGS.
```

```
   char
 *outdir = 0,    //
 DIRECTORY FOR OUTPUT.
```

```
   char
 *inbuf = 0,     //
 IF ANALYZING A BUFFER, SUPPLY IT HERE
```

```
   long
 len = 0,        //
 LENGTH OF INPUT BUFFER
```

```
   bool
 compiled=false, // RUN COMPILED ANALYZER
```

```
   ostream
 *os = 0,     //
 STANDARD OUTPUT STREAM
```

```
   char
 *outbuf = 0,    //
 OUTPUT BUFFER TO BIND TO cbuf STREAM
```

```
   long
 outlen = 0,     //
 MAXIMUM LENGTH OF cbuf OUTPUT BUFFER
```

```
   char
 *datum          //
 STRING OF PARAMETERS TO ANALYZER [NEWLY DOCUMENTED 2.4.0.1]
```

```
   );
```

```
You have a choice of
 specifying input from a file or a buffer.  If
 inbuf and len
 are zero, then analyze() assumes that input comes from the input
 file argument.
```

```
Output is more flexible
 in that during the analysis of a text, you can send output to a file,
 a user-supplied stream, and a user-supplied buffer.  output
 specifies the default output file, outbuf
 and its length outlen specify
 an output buffer, and os specifies
 an output stream.  In
 NLP++, you may also send outputs to additional files (see discussion of
 output statements).
```

```
The compiled
 flag, if true, specifies that you are running a compiled version of the
 analyzer (run.dll, see below).  If
 false, then you are running the same interpreted analyzer definition that
 you have developed within VisualText.
```

```
OUTPUT
 FILE. The output argument leads nowhere in current-day NLP++. (That
 is, there's no built-in NLP++ function such as cbuf() that writes to it.)
  But you
 can manually add it to the DATUM argument to pass it to the analyzer.
```

```
DATUM
 STRING. This arg has been available for many 2.x VisualText versions,
 but hasn't been documented prior to 2.4.0.1.  It
 is a string that gets passed to the G("$datum") global variable
 of the called analyzer.  Typically,
 one can separate values with a pipe character ('|') in the datum string,
 and use something like
```

```
    L("arr")
 = split(G("$datum"),"|");
```

```
to read each parameter into an array element.
  One can
 use the parameters to set up output files, assign tasks, and pass information
 to the called analyzer.
```

## Compiling the Analyzer

Instructions for compiling the analyzer and running compiled vs interpreted mode in the standalone analyzer. (Currently VisualText doesn't provide a way to run the compiled analyzer.) Can only compile the analyzer during load of VisualText, at present. (Could also compile it from a C++ program, if desired.)

1. Invoke VisualText.

2. Depress the toggle for compiling the analyzer:  ![Compile Analyzer](../../helps/Toolbar_buttons/compile_analyzer_button.gif)

3. Load the analyzer to be compiled. C++ code gets generated and compiled (in the app\run folder) during analyzer load. NOTE: In version 2, you will need to go to the run folder of your analyzer and manually upgrade and compile the project.  For example, in version 2.3 and later, files are generated for each pass of an analyzer.

Running the compiled analyzer

Examine the API call for creating an analyzer, in main.cpp of the current application folder:

nlp->make_analyzer(seqfile, appdir, develop, 0, compile-on-load, **compiled**);

The **compiled** flag will load the compiled analyzer if true. (Note: the interpreted analyzer is ALWAYS loaded as well.) You can also specify that code be generated when making the analyzer, by setting the compile-on-load argument to true.

To run the compiled analyzer, set **compiled** to true in the call to analyze, as below.

nlp->analyze(infile,outfile,appdir,true,0,line,0,**compiled**);

## Compiling the KB

Unlike the analyzer, which can only be compiled during load, the knowledge base can be compiled at any time by clicking the compile kb button:  ![Compile KB](../../helps/Toolbar_buttons/compile_kb_button.gif)

NOTE: In version 2, you will need to go to the kb folder of your analyzer and manually upgrade and compile the project, after the above.  You may also need to add all the .cpp and .h files in that folder to the kb project in order for it to compile.

The user can save an interpreted version of the KB with the Save KB button at anytime as well: ![Save KB](../../helps/Toolbar_buttons/save_kb_button.gif)

Compiling very large KBs or loading interpreted KBs can take a long time.  A hint for managing very large KBs is to load the compiled version, an option that can be set in the File > Preferences menu item.  Then, the NLP++ functions **[kbdumptree](../kbdumptree.md)** and **[take](../take.md)** can be used to dump and load subhierarchies of the kb that are being worked on.  (Also available is: in the KB Editor window, select a concept whose tree is to be dumped or reloaded.  Right-click and select Modular > Dump to dump the subtree to a .kb command file, or Modular > Load to browse to a .kb file to be loaded.)

The knowledge base can also be compiled from a C++ program.  In the main.cpp file of the standalone app, add the API call

**cg->genKb();**

This will generate and compile C++ code for the knowledge base, creating a kb.dll file in kb\Debug or kb\Release, as appropriate.

## Extending NLP++ with the User Project

The **user** C++ project created with a new analyzer provides an example of a user-defined NLP++ function, in the Ucode.cpp file. An interpreted as well as compiled variant of the function is exemplified. Methods for processing the function's arguments, as well as accessing the parse tree and knowledge base, are illustrated.

One way to define a new NLP++ function is within the @DECL region, which must be first in a pass file, if present.  Another way is to create a C++ function in the User project, as exemplified with the function called **testfn** in the file user\Ucode.cpp.  The assumption is that a user-defined function must participate in NLP++ expressions, and so it must process arguments in the same way that other NLP++ functions process arguments.  It must also return values by a special mechanism involving a **retVal** object, as exemplified in the testfn example.  From a pass file, the function must be called with a user:: prefix.  E.g.,  **user::testfn()**.

Just after an analyzer is loaded, the function **ucodeIni()** is called, and just before an analyzer is closed, **ucodeFin()** is called.  These functions are available in the User project and may be filled with user-defined initializations and cleanups.

## UPDATING ANALYZERS

To update your analyzers to Version 2.0, you will mainly need to regenerate and recompile the code in your projects.  First, compare your code with that in the top level, kb folder, run folder, and user folder of the Bare analyzer in c:\Program Files\TextAI\VisualText\Templates\Bare.  You may need to add the code lines

#include <windows.h> #include <tchar.h> #include <my_tchar.h> #include <streamclasses.h>

to your StdAfx.h file, or

#include "vtapi.h"

as appropriate, in order to succesfully compile.  Then, regenerate run and kb code, if you're using the compile version of the analyzer and kb.  Similarly, recompile the user project for your analyzer, especially if you are using functions there or adding new ones to extend NLP++.
