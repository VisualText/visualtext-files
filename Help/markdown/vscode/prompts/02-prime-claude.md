Prime Claude for NLP++
<!-- desc: Paste this into a fresh Claude session before asking for any NLP++ help — it is everything Claude needs to know to work on your analyzers: the installed engine, example, and template paths, the conventions that keep it on the rails (use the Knowledge Base template as intended, build results into a KB and emit JSON with JsonKB, and run with -WORK pointing at the engine), and the engine facts that trip up newcomers. No task to fill in — once Claude has read this, ask it for whatever you need. -->
This is everything you need to know to help me work on NLP++ analyzers. NLP++ is a rule-based programming language for natural language processing, run by the NLP engine. Read this in full before we start — afterward I will ask you to build a new analyzer, extend an existing one, write dictionaries and knowledge bases, generate test inputs, or debug why a rule fires. Everything you need is already installed on this machine at the paths below:

- NLP engine executable (run analyzers with this): {{engineExe}}
- NLP engine command-line switches (how to run, compile, set the working directory, etc.): https://github.com/VisualText/nlp-engine/blob/master/README.md#switches
- Example analyzers (study these for patterns and the pass sequence): {{analyzersDir}}
- Analyzer templates (good starting points): {{templatesDir}}
- VisualText support files: {{visualTextDir}}
    - Library functions and language dictionaries / knowledge bases: {{languagesDir}}
    - Misc library functions: {{miscDir}}

An NLP++ analyzer is a folder containing: spec/ (the .nlp passes plus analyzer.seq, the ordered pass sequence), input/ (text files to analyze), and kb/ (the knowledge base). Before writing anything, read several of the example and template analyzers above to learn the analyzer.seq format, the pass regions (@CODE, @NODES/@PATH, @RULES, @PRE/@POST, @DECL), the rule and wildcard syntax, and the KB/library functions available in the languages and misc directories.

Build the analyzer by copying an appropriate template from the templates directory to the workspace and renaming it. When your analyzer needs to accumulate results and emit them, copy the **Knowledge Base** template and follow its intended design rather than bypassing it:

- Keep its scaffolding — spec/KBFuncs.nlp, spec/kbinit.nlp, and spec/output.nlp. Your grammar passes accumulate results into a knowledge base (a global root concept created in kbinit), and the output pass serializes that KB with the library's SaveKB and JsonKB functions. Do NOT hand-roll JSON with string writes.
- To make JsonKB emit a JSON array, store repeated items as numbered sibling concepts (item1, item2, ...) with their data in attributes; numbered concepts sharing a base name become a JSON array automatically. Name them directly with makeconcept rather than via MakeCountCon, so no "_count" bookkeeping attribute leaks into the JSON.
- The KB persists between runs, so in kbinit clear (rmconcept) any result concept left over from a previous run before rebuilding it.

Useful engine facts:

- Tokenization (dicttok) splits alphabetic vs numeric vs punctuation and keeps whitespace as separate tokens, but does NOT split on internal case — so a mixed-case word like "NaCl" arrives as a single alpha token. $text preserves original case; adjacent tokens with no whitespace between them are contiguous, and a _xWILD [plus match=(_xALPHA _xNUM)] run stops at whitespace or punctuation.
- Dictionaries: a .dict file placed in kb/user (flat "word attr=val ..." format, one word per line) is auto-loaded by the tokenizer, tagging matching tokens with its attributes. dictfindword("Word") looks a word up from code and is case-sensitive.

Run an analyzer with:

    nlp.exe -ANA <analyzer dir> -IN <input file> -WORK <ENGINE DIR> -DEV

-WORK must point at the engine directory (the folder containing nlp.exe), NOT the analyzer folder — otherwise the engine prints "ERROR IN ANALYZER INIT", silently runs only the tokenizer, and no passes execute. Per-input output (and .tree debug files under -DEV) appears in input/<file>.txt_log/.

Study a couple of the example and template analyzers now to learn the conventions, then tell me you are ready and I will describe the task. When we work, build the passes, run the analyzer over the input files, and show me the output so we can check it together.
