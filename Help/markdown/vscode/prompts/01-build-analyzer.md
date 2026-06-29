NLP++ local install — build an analyzer
I want you to help me write a prototype NLP++ analyzer. NLP++ is a rule-based programming language for natural language processing, run by the NLP engine. Everything you need is already installed on this machine at the paths below:

- NLP engine executable (run analyzers with this): {{engineExe}}
- NLP engine command-line switches (how to run, compile, set the working directory, etc.): https://github.com/VisualText/nlp-engine/blob/master/README.md#switches
- Example analyzers (study these for patterns and the pass sequence): {{analyzersDir}}
- Analyzer templates (good starting points): {{templatesDir}}
- VisualText support files: {{visualTextDir}}
    - Library functions and language dictionaries / knowledge bases: {{languagesDir}}
    - Misc library functions: {{miscDir}}

An NLP++ analyzer is a folder containing: spec/ (the .nlp passes plus analyzer.seq, the ordered pass sequence), input/ (text files to analyze), and kb/ (the knowledge base). Before writing anything, read several of the example and template analyzers above to learn the analyzer.seq format, the pass structure, and the library functions and KB conventions available in the languages and misc directories. Run an analyzer by invoking the engine executable above on an input file.

Create a folder of text files from the internet that (FILL IN YOUR DESCRIPTION) and create an analyzer that does (FILL IN YOUR DESCRIPTION OF THE ANALYZER).
