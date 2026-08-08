From scratch: chemical formulas
<!-- desc: Worked from-scratch example — gathers Wikipedia chemistry excerpts, then builds an NLP++ analyzer (from the Knowledge Base template) that finds chemical formulas and breaks each into its elements and atom counts, emitting JSON via JsonKB. A complete, self-contained prompt that reaches the solution without extra back-and-forth. -->
I want you to help me write a prototype NLP++ analyzer. NLP++ is a rule-based programming language for natural language processing, run by the NLP engine. Everything you need is already installed on this machine at the paths below:

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

--------------------------------------------------------------------------

Now the specific task. Name the analyzer **ChemFormulas**. It finds chemical formulas embedded in ordinary prose and breaks each into its constituent elements and atom counts. A formula is a run of one or more element symbols; each symbol is a single uppercase letter optionally followed by one or two lowercase letters (H, O, Na, Cl), each optionally followed by a count (H2O, CO2, C6H12O6). When no count is present the count is 1.

Input corpus: Create a folder of text files from the internet — short excerpts from Wikipedia chemistry articles (Water, Sodium chloride, Photosynthesis, Combustion, Carbon dioxide) that are dense with chemical formulas written inline in prose. Transcribe any Unicode subscripts to plain ASCII (H₂O -> H2O). Save them as plain .txt files under the analyzer's input/ directory, and keep a SOURCES.md listing each file's page title and URL. Seed the text with near-miss distractors (Roman numerals, capitalized words, model/catalog codes).

Element dictionary (required approach): Create kb/user/element.dict containing every element as TWO dictionary words — the symbol in proper case and the full name in lowercase — tagged so you can tell them apart:

    H name=Hydrogen number=1 element=1 kind=symbol
    hydrogen symbol=H number=1 element=1 kind=name

Placing it in kb/user auto-loads it. A formula is recognized only when every one of its symbols is a real element confirmed against this dictionary (use dictfindword, matching the kind=symbol entries).

Parsing approach: Group each maximal run of adjacent alpha/number tokens into a node, reconstruct the run's raw text (this handles NaCl, CaCO3 and other formulas that tokenize as a single alpha token), and parse it character by character: greedy longest match (a valid two-letter symbol beats a one-letter one); a trailing digit-count applies to the last symbol of the run; every symbol must be in the dictionary.

Knowledge base & output (required approach): Build results under a global root concept G("formulas") — one numbered concept per formula (formula1, formula2, ...) carrying a "formula" attribute, each holding one numbered child per element (elements1, elements2, ...) carrying "symbol" and "count". Leave output.nlp as the template's two calls:

    SaveKB("formulas.kbb", G("formulas"), 2);
    JsonKB("formulas.json", G("formulas"));

That makes JsonKB produce formulas.json automatically, of the form:

    {
      "formulas": {
        "formula": [
          { "id": "1", "formula": "C6H12O6",
            "elements": [
              {"id": "1", "symbol": "C", "count": "6"},
              {"id": "2", "symbol": "H", "count": "12"},
              {"id": "3", "symbol": "O", "count": "6"}
            ] }
        ]
      }
    }

Requirements & precision filters:

- Recognize formulas embedded in ordinary sentences, not just on their own line.
- Reject near-misses: capitalized words (Table, Salt), model/catalog codes (US2024, Room101), lone capital letters used as words (I, A), and Roman numerals (II, IV, VII). Implement: each symbol must start uppercase; reject a single symbol with no explicit count; reject a run of only single Roman-numeral letters with no digits; reject any subscript greater than 999.

Run the analyzer over every input file and show me the formulas.json output for each so we can check recall and precision together.
