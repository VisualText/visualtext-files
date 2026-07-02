General pointers: Claude + NLP++
<!-- desc: Start here — how Claude helps with NLP++ work (gathering development texts, mimicking the rule/code patterns of a logical language, and assisting on an existing analyzer), plus a guide to the four prompt files in this library and when to reach for each. -->
Claude pairs well with NLP++. This page is an overview; the other entries in this list are ready-to-use prompts you open, fill in, and paste into Claude.

Why the pairing works:

- **Claude assists across the whole workflow of an existing analyzer.** Beyond building from scratch, it can add or refine grammar passes, write dictionaries and knowledge bases, generate more test inputs, debug why a rule does or doesn't fire, and explain unfamiliar passes or library functions.
- **It is good at gathering development texts.** Much of building an analyzer is assembling a realistic corpus to develop and test against. Claude can collect and clean excerpts from the internet, transcribe tricky formatting, and deliberately seed near-miss/edge cases that stress your rules.
- **NLP++ is a logical, rule-based programming language, so Claude's strength at mimicking code transfers directly.** Its passes, rules, wildcards, and KB operations are structured and pattern-like; Claude learns the conventions from the example and template analyzers and reproduces them faithfully.

The four prompt files in this library:

1. **[From scratch: chemical formulas](01-chemical-formulas.md)** — A complete worked example. It has Claude gather a Wikipedia chemistry corpus and build an analyzer that finds chemical formulas and breaks each into its elements and atom counts, emitting JSON. Use it to watch an analyzer built end to end, or as a model for your own from-scratch build.

2. **[NLP++ local install — build an analyzer](02-build-analyzer.md)** — The generic starting point for a brand-new analyzer. It hands Claude the installed engine, example, and template paths plus the conventions that keep it on the rails, then leaves a blank for you to describe the corpus and the extraction task.

3. **[Harden analyzer](03-more-text-files.md)** — For an analyzer you already have. It generates additional, varied test inputs (including edge cases), runs them through the engine, and reports where the extraction looks wrong so you can tighten rules and re-bless your regression goldens.

4. **[Create Dictionaries & KBs](04-dictionaries-kbs.md)** — Also for an existing analyzer. It builds NLP++ dictionaries (.dict) and knowledge bases (.kbb), learning the exact format from the shared language and misc libraries, and places them under the analyzer's kb/user/ directory.

Tip: each prompt fills in machine-specific paths (engine, examples, templates) automatically when you open it, so it is ready to paste. Start from the closest-fitting prompt and edit rather than writing from a blank page.
