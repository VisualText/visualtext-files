From scratch: chemical formulas
<!-- desc: Worked from-scratch example — gathers Wikipedia chemistry excerpts, then builds an NLP++ analyzer that finds chemical formulas and breaks each into its elements and atom counts, emitting JSON. A good first prompt to watch an analyzer built end to end. -->
I want you to help me write a prototype NLP++ analyzer. NLP++ is a rule-based programming language for natural language processing, run by the NLP engine. Everything you need is already installed on this machine at the paths below:

- NLP engine executable (run analyzers with this): {{engineExe}}
- NLP engine command-line switches (how to run, compile, set the working directory, etc.): https://github.com/VisualText/nlp-engine/blob/master/README.md#switches
- Example analyzers (study these for patterns and the pass sequence): {{analyzersDir}}
- Analyzer templates (good starting points): {{templatesDir}}
- VisualText support files: {{visualTextDir}}
    - Library functions and language dictionaries / knowledge bases: {{languagesDir}}
    - Misc library functions: {{miscDir}}

An NLP++ analyzer is a folder containing: spec/ (the .nlp passes plus analyzer.seq, the ordered pass sequence), input/ (text files to analyze), and kb/ (the knowledge base). Run an analyzer by invoking the engine executable above on an input file.

Create a folder of text files from the internet — short excerpts from Wikipedia chemistry articles that are full of chemical formulas — and save them under the analyzer's input/ directory.

Then build an NLP++ analyzer that finds the chemical formulas in the text and breaks each one into its elements and atom counts, emitting the results as JSON.

Study a couple of the example and template analyzers first to learn the conventions, then build it, run it over the files, and show me the output.
