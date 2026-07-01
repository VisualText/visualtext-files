Harden analyzer
<!-- desc: Generates additional, varied test inputs (with edge cases) for the current analyzer, runs them through the engine, and reports where extraction looks wrong so you can tighten rules and re-bless regression goldens. -->
I am hardening an NLP++ analyzer by adding more test inputs. The analyzer and engine are here:

- Current analyzer (add files under its input/ directory): {{currentAnalyzer}}
- NLP engine executable (run analyzers with this): {{engineExe}}
- Example analyzers (for reference on input layout): {{analyzersDir}}

Generate additional, varied text files and place them under the analyzer's input/ directory (create subfolders as needed). I want realistic variety and edge cases that will stress the analyzer's rules:

(FILL IN: the domain / kind of text, and which edge cases or variations to emphasize)

After creating them, run the analyzer over the new files with the engine executable and report any inputs where the extraction looks wrong, so I can tighten the rules and re-bless the regression goldens.
