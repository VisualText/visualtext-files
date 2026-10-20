Harden analyzer
<!-- desc: Generates additional, varied test inputs (with edge cases) for the current analyzer, runs them through the engine, and reports where extraction looks wrong — grouped by cause, so fixes address the whole class of input rather than one file — so you can tighten rules and re-bless regression goldens. -->
I am hardening an NLP++ analyzer by adding more test inputs. The analyzer and engine are here:

- Current analyzer (add files under its input/ directory): {{currentAnalyzer}}
- NLP engine executable (run analyzers with this): {{engineExe}}
- Example analyzers (for reference on input layout): {{analyzersDir}}

Generate additional, varied text files and place them under the analyzer's input/ directory (create subfolders as needed). I want realistic variety and edge cases that will stress the analyzer's rules:

(FILL IN: the domain / kind of text, and which edge cases or variations to emphasize)

After creating them, run the analyzer over the new files with the engine executable and report any inputs where the extraction looks wrong, so I can tighten the rules and re-bless the regression goldens.

**Fix the class, not the case.** When you report or fix a failure, group it by its cause — the kind of text that broke and why the analyzer missed it (a missing dictionary entry, a rule matching words instead of attributes, a missing _phrase alternative, an unhandled shape such as an optional title, a hyphen, or a line break inside a name) — not by the individual file. Never make a failing input pass with a rule tied to its exact words or punctuation, or an `if ($text == "...")` special case; that overfits the test and leaves every similar input still broken. Fix the cause so the whole family passes, then add two or three more inputs of the same kind to prove it.
