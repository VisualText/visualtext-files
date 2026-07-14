General pointers: Claude + NLP++
<!-- desc: Start here — how Claude helps with NLP++ work (gathering development texts, mimicking the rule/code patterns of a logical language, and assisting on an existing analyzer), plus a guide to the five prompt files in this library and when to reach for each. -->
Claude pairs well with NLP++. This page is an overview; the other entries in this list are ready-to-use prompts you open, fill in, and paste into Claude.

**Start every new Claude session by pasting in [Prime Claude for NLP++](02-prime-claude.md).** It is everything Claude needs to know to work on your analyzers — the installed engine, example, and template paths, the KB and JSON conventions, and the engine facts that trip up newcomers. Paste it first, let Claude read the examples and templates, and only then ask for whatever you need. The other prompts below are task-specific and assume Claude has already been primed this way.

Why the pairing works:

- **Claude assists across the whole workflow of an existing analyzer.** Beyond building from scratch, it can add or refine grammar passes, write dictionaries and knowledge bases, generate more test inputs, debug why a rule does or doesn't fire, and explain unfamiliar passes or library functions.
- **It is good at gathering development texts.** Much of building an analyzer is assembling a realistic corpus to develop and test against. Claude can collect and clean excerpts from the internet, transcribe tricky formatting, and deliberately seed near-miss/edge cases that stress your rules.
- **NLP++ is a logical, rule-based programming language, so Claude's strength at mimicking code transfers directly.** Its passes, rules, wildcards, and KB operations are structured and pattern-like; Claude learns the conventions from the example and template analyzers and reproduces them faithfully.

The five prompt files in this library:

1. **[From scratch: chemical formulas](01-chemical-formulas.md)** — A complete worked example. It has Claude gather a Wikipedia chemistry corpus and build an analyzer that finds chemical formulas and breaks each into its elements and atom counts, emitting JSON. Use it to watch an analyzer built end to end, or as a model for your own from-scratch build.

2. **[Prime Claude for NLP++](02-prime-claude.md)** — Paste this into a fresh Claude session before anything else. It is everything Claude needs to know to work on your analyzers: the installed engine, example, and template paths, the conventions that keep it on the rails, and the engine facts newcomers stumble on. There is no blank to fill in — once Claude has read it and studied the examples, describe whatever task you have.

3. **[Harden analyzer](03-more-text-files.md)** — For an analyzer you already have. It generates additional, varied test inputs (including edge cases), runs them through the engine, and reports where the extraction looks wrong so you can tighten rules and re-bless your regression goldens.

4. **[Create Dictionaries & KBs](04-dictionaries-kbs.md)** — Also for an existing analyzer. It builds NLP++ dictionaries (.dict) and knowledge bases (.kbb), learning the exact format from the shared language and misc libraries, and places them under the analyzer's kb/user/ directory.

5. **[Add missing words to the English dictionary](05-missing-words.md)** — For an existing analyzer that reports unrecognized words. It reads missing_words.txt from the analyzer's output log and, for each genuine word, adds a properly featured entry (part of speech, root, verb/noun features) to en-full.dict and en-full.kbb — keeping both files alphabetized with identical headword sets, and quarantining noise (typos, fragments, proper nouns) for your review.

Tip: each prompt fills in machine-specific paths (engine, examples, templates) automatically when you open it, so it is ready to paste. Start from the closest-fitting prompt and edit rather than writing from a blank page.
