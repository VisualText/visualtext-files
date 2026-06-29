Build dictionaries and knowledge bases
Help me build dictionaries (.dict) and knowledge bases (.kbb) for an NLP++ analyzer.

- Current analyzer (its kb/user/ folder holds the KB sources): {{currentAnalyzer}}
- Shared language dictionaries / KBs to learn the format from: {{languagesDir}}
- Misc dictionaries / KBs (currencies, country codes, timezones, etc.): {{miscDir}}
- NLP engine executable: {{engineExe}}

NLP++ dictionaries are flat files of "word attr=val ..." (one word per line, .dict). Knowledge bases (.kbb) use an indented hierarchy to express concepts and their attributes. Study the examples in the directories above for the exact format, including how a .dict is paired with a .kbb of the same stem.

Build the following and place the files under the analyzer's kb/user/ directory:

(FILL IN: what the dictionary / KB should contain — the words or concepts, their attributes, and how they should be organized)
