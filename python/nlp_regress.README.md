# nlp_regress.py — regression tester for NLP++ analyzers

Cross-platform (Windows/macOS/Linux), pure-Python-3 (standard library only).
This is the script behind VisualText's **Run Regression Test (All Files)** and
**Bless Regression Goldens (All Files)** commands (right-click an analyzer in the
Analyzers panel, or the beaker button in the panel toolbar).

It replays every file under an analyzer's `input/` directory through the engine
and compares the structured extraction to a committed *golden* under
`<analyzer>/test/expected/`. The comparison is **semantic** — it compares the set
of extracted records with the volatile `id` field removed and order ignored — so
it is stable across cosmetic engine drift (renumbered ids, provenance comments)
yet still flags a real regression: an added, removed or changed extraction.

This complements VisualText's built-in per-file "Run Regression Test", which
compares individual output files line-by-line.

## Command line

```sh
python nlp_regress.py bless <analyzer>   # capture the goldens (current output)
python nlp_regress.py test  <analyzer>   # run + compare; exit !=0 on a regression
python nlp_regress.py list  <analyzer>   # list inputs + golden status
```

VisualText invokes it with the bundled engine, e.g.:

```sh
python nlp_regress.py test "<analyzer-dir>" --cli --engine "<nlp-engine-dir>"
```

Engine backend is auto-detected: the `NLPPlus` pip package if installed, else the
`nlp` / `nlp.exe` CLI (`--engine` / `$NLP_ENGINE`). See the full docs in the
extractors repo at `tools/regress/README.md`.
