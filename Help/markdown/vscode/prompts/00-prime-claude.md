Prime Claude for NLP++
<!-- desc: Paste this into a fresh Claude session before asking for any NLP++ help — it is everything Claude needs to know to work on your analyzers: the installed engine, example, and template paths, the conventions that keep it on the rails (use the Knowledge Base template as intended, build results into a KB and emit JSON with JsonKB, build on the library dictionaries and knowledge bases instead of hand-typed word lists, and run with -WORK pointing at the engine), and the engine facts that trip up newcomers. No task to fill in — once Claude has read this, ask it for whatever you need. -->
This is everything you need to know to help me work on NLP++ analyzers. NLP++ is a rule-based programming language for natural language processing, run by the NLP engine. Read this in full before we start — afterward I will ask you to build a new analyzer, extend an existing one, write dictionaries and knowledge bases, generate test inputs, or debug why a rule fires. Everything you need is already installed on this machine at the paths below:

- NLP engine executable (run analyzers with this): {{engineExe}}
- NLP engine command-line switches (how to run, compile, set the working directory, etc.): https://github.com/VisualText/nlp-engine/blob/master/README.md#switches
- Example analyzers (study these for patterns and the pass sequence): {{analyzersDir}}
- Analyzer templates (good starting points): {{templatesDir}}
- VisualText support files: {{visualTextDir}}
    - Library functions and language dictionaries / knowledge bases: {{languagesDir}}
    - Misc library functions: {{miscDir}}
- NLP++ help files — over 400 markdown pages, the reference documentation for the language and the tool: {{helpDir}}
    - {{helpDir}}/index.md — the master table of contents for the whole help system.
    - {{helpDir}}/vscode/home.md — the VS Code extension's help hub: quick start, parse trees, regression testing, compiling analyzers, and calling them from Python / Node.js.
    - {{helpDir}}/NLP_PP_Stuff/ — the language itself: Rule_syntax.md, Rule_Element_Modifiers.md, Special_rule_elements.md, Code_Zone.md, Grammar_Zone.md, Actions.md, Functions.md, About_NLP++_Variables.md, Special_Variables.md, Operators_and_Expressions.md, Variable_types.md, Tokens.md.
    - {{helpDir}}/VisualText_Basics/ — how an analyzer is put together: Structure_of_Analyzer_Projects.md, About_the_analyzer_sequence.md, About_the_Knowledge_Base.md, About_Parse_Trees.md, Standard_Rule_Format.md.
    - One page per builtin, named for it: {{helpDir}}/<name>.md — e.g. pnname.md, makeconcept.md, dictfindword.md, $text.md, _xWILD.md.

Learn NLP++ from these pages, and keep using them as you work — they are the authority on the language, not your priors. Before you call a function, read its page for the argument order, return value, and example. Before you write a rule, read the rule-syntax and element-modifier pages. When you meet a name you do not recognize, grep the help directory for it and read what comes back; that is faster and far more reliable than inferring the behavior from example analyzers.

An NLP++ analyzer is a folder containing: spec/ (the .nlp passes plus analyzer.seq, the ordered pass sequence), input/ (text files to analyze), and kb/user/ (the knowledge base sources). **The only knowledge base files you ever read or write are .dict dictionaries and .kbb knowledge base files.** The .kb files sitting in kb/user (attr.kb, hier.kb, phr.kb, word.kb) are the engine's runtime dump of the knowledge base — the engine writes them, rewrites them on every run, and they are not part of writing an analyzer. Do not read them to learn the KB, do not copy them as examples, and never hand-edit them. Before writing anything, read several of the example and template analyzers above to learn the analyzer.seq format, the pass regions (@CODE, @NODES/@PATH, @RULES, @PRE/@POST, @DECL), the rule and wildcard syntax, and the KB/library functions available in the languages and misc directories.

Build the analyzer by copying an appropriate template from the templates directory to the workspace and renaming it. When your analyzer needs to accumulate results and emit them, copy the **Knowledge Base** template and follow its intended design rather than bypassing it:

- Keep its scaffolding — spec/KBFuncs.nlp, spec/kbinit.nlp, and spec/output.nlp. Your grammar passes accumulate results into a knowledge base (a global root concept created in kbinit), and the output pass serializes that KB with the library's SaveKB and JsonKB functions. Do NOT hand-roll JSON with string writes.
- To make JsonKB emit a JSON array, store repeated items as numbered sibling concepts (item1, item2, ...) with their data in attributes; numbered concepts sharing a base name become a JSON array automatically. Name them directly with makeconcept rather than via MakeCountCon, so no "_count" bookkeeping attribute leaks into the JSON.
- The KB persists between runs, so in kbinit clear (rmconcept) any result concept left over from a previous run before rebuilding it.

Rules of thumb — build on the libraries, never on hand-typed word lists:

- **Look in the libraries before you write a vocabulary.** {{languagesDir}} already ships, per language, dictionaries and matching knowledge bases for countries, nationalities/demonyms, languages, months and days, first names and surnames, professions, US states and street suffixes, numbers, prepositions, determiners, pronouns, conjunctions and stop words — plus a full lexicon (en-full.dict / en-full.kbb) carrying part of speech, root, and verb/noun features. {{miscDir}} adds currencies, ISO country codes, telephone country codes, timezones, emojis, roman numerals and URL domains. A pass built on the twenty words you typed by hand is brittle: it handles the test file and nothing else. The library file handles the whole vocabulary.
- **Wire one in by copying the .dict and its matching .kbb into the analyzer's kb/user/.** The tokenizer auto-loads every .dict there and tags matching tokens. Keep the pair together — a .kbb with the same stem supplies the concept hierarchy and the ambiguity readings for its .dict. Files named `…full.dict` / `…full.kbb` lazy-load word by word, so even a large lexicon costs little at startup. For a heavy domain KB that only some inputs need, load it on demand with loaddict / loadkbb (a file name in kb/user, not a path), guarded by a global so it loads once.
- **Match on the attributes, not on the words.** Dictionary attributes ride on the node, so `@PRE <1,1> var("nationality");` selects every entry in the file, and `N("country",1)`, `N("iso3",1)` read the data straight off the node — no dictfindword call needed. Rules written this way keep working as the library file grows.
- **Match _phrase as well as _xALPHA.** Multi-word and hyphenated entries ("American Samoan", "Bissau-Guinean") arrive from the tokenizer as a single _phrase node carrying the same dictionary attributes. A rule that only matches _xALPHA silently misses every one of them.
- **Join on a stable attribute, never on $text.** Key KB lookups on country=, iso3=, root= and the like — the surface form varies with plural, synonym and hyphenation, and $text on a hyphenated phrase comes back mangled ("bissau - guine").
- **If the library is missing words, extend the library file rather than hard-coding them in a pass** — and keep the .dict and its .kbb on identical headword sets. Some library files are generated by a script (the header comment at the top of the file says so and names it); edit the generator's table and re-run it instead of hand-editing the output.

Useful engine facts:

- Tokenization (dicttok) splits alphabetic vs numeric vs punctuation and keeps whitespace as separate tokens, but does NOT split on internal case — so a mixed-case word like "NaCl" arrives as a single alpha token. $text preserves original case; adjacent tokens with no whitespace between them are contiguous, and a _xWILD [plus match=(_xALPHA _xNUM)] run stops at whitespace or punctuation.
- Dictionaries and knowledge bases: a .dict file placed in kb/user (flat "word attr=val ..." format, one word per line) is auto-loaded by the tokenizer, tagging matching tokens with its attributes. dictfindword("Word") looks a word up from code and is case-sensitive. A .kbb file is the hand-written source for a knowledge base — an indented concept hierarchy with attributes — and pairs with the .dict of the same stem. Again: .dict and .kbb are the authored files; .kb files are engine output, never a source you touch.

Run an analyzer with:

    nlp.exe -ANA <analyzer dir> -IN <input file> -WORK <ENGINE DIR> -DEV

-WORK must point at the engine directory (the folder containing nlp.exe), NOT the analyzer folder — otherwise the engine prints "ERROR IN ANALYZER INIT", silently runs only the tokenizer, and no passes execute. Per-input output (and .tree debug files under -DEV) appears in input/<file>.txt_log/.

Study a couple of the example and template analyzers now to learn the conventions, then tell me you are ready and I will describe the task. When we work, build the passes, run the analyzer over the input files, and show me the output so we can check it together.
