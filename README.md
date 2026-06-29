# VisualText Files

Support files distributed with the [VisualText VSCode extension](http://vscode.visualtext.org) and the [NLP++ engine](https://github.com/VisualText/nlp-engine). These files are copied into the `visualtext` directory of an NLP++ installation and provide the starter analyzers, help content, dictionaries, code libraries, and language assets that the extension exposes to end users.

A GitHub release of this repository zips the contents into `visualtext.zip`, which the VSCode extension downloads and unpacks the first time a user installs NLP++. See [`.github/workflows/visualtextfiles.yml`](.github/workflows/visualtextfiles.yml) for the release pipeline.

## Repository Layout

| Folder | Purpose |
| ------ | ------- |
| [analyzers/](analyzers/) | Ready-to-use block analyzers a user can pick when creating a new analyzer |
| [Help/](Help/) | HTML help pages shown by VisualText's "Lookup Word" / context-help feature |
| [spec/](spec/) | Reusable NLP++ pass libraries that can be inserted into an analyzer sequence |
| [languages/](languages/) | Per-language dictionary and knowledge-base files (English, Spanish, Arabic, etc.) |
| [misc/](misc/) | General-purpose dictionaries and knowledge bases (currencies, country codes, timezones, emojis) |
| [ecl/](ecl/) | Example `.ecl` configuration files for the NLP++ engine |
| [python/](python/) | Python wrappers and examples for driving `nlp.exe` from scripts |
| [templates/](templates/) | Legacy analyzer templates (kept for backward compatibility) |

## analyzers/

Block analyzers that appear in the VSCode extension's "New Analyzer" picker. Each analyzer is a self-contained folder with the standard NLP++ structure (`spec/`, `input/`, `kb/`, `tmp/`).

Current analyzers:

- **[Address Parser](analyzers/Address%20Parser/)** &mdash; parses American postal addresses and emits structured JSON (house number, street, suffix, city, state, ZIP). Also handles Rural Route and Highway Contract formats.
- **[Bare English](analyzers/Bare%20English/)** &mdash; a minimal parser that uses the full English dictionary lookup (`dicttokz`).
- **[Bare Minimum](analyzers/Bare%20Minimum/)** &mdash; the absolute minimum analyzer: a single `tokenize` pass. Good starting point when building from scratch.
- **[Date and Times](analyzers/Date%20and%20Times/)** &mdash; recognizes date and time expressions.
- **[Email Addresses](analyzers/Email%20Addresses/)** &mdash; extracts email addresses and decomposes them into local-name, domain, and TLD.
- **[Paragraphs Sentences](analyzers/Paragraphs%20Sentences/)** &mdash; demonstrates paragraph and sentence segmentation with dictionary lookup.
- **[Telephone Numbers](analyzers/Telephone%20Numbers/)** &mdash; recognizes a wide range of US and international phone-number formats.
- **[URLs](analyzers/URLs/)** &mdash; extracts hyperlinks and decomposes them into scheme, domain, subdomain, and path.
- **[xout](analyzers/xout/)** &mdash; masks all alphanumeric text as `x`. Useful for redaction and structural inspection.
- **[parse-en-us](analyzers/parse-en-us/)** &mdash; a full English parser, included as a Git submodule from [VisualText/parse-en-us](https://github.com/VisualText/parse-en-us).

See [`analyzers/README.md`](analyzers/README.md) for the conventions a submitted block analyzer must follow (folder name, README header, description line).

## Help/

Source content for VisualText's offline help system, including a precompiled `Help.chm` and the underlying `helps/` directory of HTML pages. Each NLP++ function, pattern variable, and special symbol has a corresponding `.htm` file (e.g. `$start.htm`, `@@RULES.htm`, `RECURSE.htm`) that the extension opens when a user invokes "Lookup Word" on an NLP++ token.

The markdown help system lives under [`Help/markdown/`](Help/markdown/), and the VSCode-specific help pages are under [`Help/markdown/vscode/`](Help/markdown/vscode/) (see below).

## VS Code Help, Version Notes, Announcements & LLM Prompts (`Help/markdown/vscode/`)

The NLP++ VSCode extension shows a **Help** view (and a 📖 book button) backed by the markdown under [`Help/markdown/vscode/`](Help/markdown/vscode/). Pages render in VS Code's markdown preview, so **keep any image in the same folder as the page that references it** — parent-folder paths like `../logo.png` are blocked by the preview's security policy.

| File | Shown as |
| ---- | -------- |
| `home.md` | the Help hub (logo, links, featured content) |
| `quickstart.md`, `compiling.md`, `testing.md`, `lazyload.md` | the guide pages |
| `versions/<version>.md` | **version notes** (see below) |
| `announcements/<id>.md` | **announcements** (see below) |
| `prompts/<name>.md` | **LLM prompts** (see below) |

### Version notes — `versions/<version>.md`

A version note is a "what's new" page tied to the **extension version**. Create one **only for a release significant enough that users should see it**, named after the version — e.g. `versions/3.2.0.md`.

- On a **first install**, the extension opens `home.md`.
- On an **upgrade**, it opens the **newest version note the user hasn't seen yet** whose version is greater than the last-seen version and ≤ the installed version — once. The last-seen version is remembered per user.
- All version notes are also listed on `home.md` and in the Help view's **Version Notes** node.

Because they are keyed to the extension version, a version note only appears when users **update the extension** to (at least) that version.

### Announcements — `announcements/<id>.md`

An announcement is a broadcast that is **independent of the extension version**. Drop a new file in `announcements/` and it shows **once, on the user's next relogin** — even if the extension version hasn't changed (e.g. delivered through a normal VisualText-files content update).

- Keyed by **id** (the file name without `.md`), **not** version. Seen ids are remembered per user, so each announcement shows at most once.
- **Name files so they sort newest-first** — a date prefix works well, e.g. `announcements/2026-06-29-textbook-launch.md`. The extension shows the newest unseen one.
- Keep any image **inside the `announcements/` folder** and reference it by plain file name.
- On a given startup the extension shows **at most one** popup: a pending version note takes priority over an announcement.
- Announcements are listed in the Help view's **Announcements** node, and the **Show Latest Announcement** (📣) button opens the newest one on demand.

### LLM prompts — `prompts/<name>.md`

A prompt file is a reusable, ready-to-paste prompt for an LLM (e.g. Claude) to help build or extend an analyzer. They are listed under the Help view's **LLM Prompts** node, and the **Create Claude Prompt** button (Analyzers toolbar) opens the first one.

File format:

- **The first line is the title** shown in the Help tree (a leading `#` is stripped). The rest of the file is the prompt body.
- The body may contain **`{{variable}}`** placeholders, which the extension fills in with this machine's actual paths before opening the prompt in a new editor. Clicking a prompt opens the filled-in result (the title line is dropped).

Available variables:

| Placeholder | Filled with |
| ----------- | ----------- |
| `{{engineExe}}` | full path to the NLP engine executable (`nlp.exe` / `nlp`) |
| `{{engineDir}}` | the engine's working directory |
| `{{visualTextDir}}` | the `visualText` support-files directory |
| `{{analyzersDir}}` | the example analyzers directory |
| `{{templatesDir}}` | the analyzer-templates directory |
| `{{languagesDir}}` | the per-language dictionaries / KBs directory |
| `{{miscDir}}` | the misc dictionaries / KBs directory |
| `{{currentAnalyzer}}` | the loaded analyzer's folder (or `(no analyzer loaded)`) |

An unknown `{{...}}` placeholder is left as-is. Name files with a numeric prefix (e.g. `01-build-analyzer.md`) to control their order in the list.

> Version notes, announcements, and prompts reach users only after this repo is **released** (so the files ship inside `visualtext.zip`). See [Releases](#releases).

## spec/

Reusable libraries of NLP++ passes that an analyzer can pull into its sequence rather than re-implementing common patterns.

| Library | What it provides |
| ------- | ---------------- |
| [Database_pats/](spec/Database_pats/) | Patterns for parsing tabular / record-style data |
| [DatePlusNumerics_pats/](spec/DatePlusNumerics_pats/) | Numerics plus date and time patterns |
| [Formatting/](spec/Formatting/) | Line, paragraph, sentence, and whitespace handling |
| [HTML_pats/](spec/HTML_pats/) | HTML tag and character-pattern recognition |
| [Numerics_pats/](spec/Numerics_pats/) | Simple and compound numeric patterns, phone numbers, numeric lists |
| [Trends/](spec/Trends/) | Trend extraction over parsed text |
| [Xml_pats/](spec/Xml_pats/) and [XML_DTD_pats/](spec/XML_DTD_pats/) | XML and DTD recognition |

Top-level `.nlp` files (e.g. [`funs.nlp`](spec/funs.nlp), [`KBFuncs.nlp`](spec/KBFuncs.nlp), [`TreeFuncs.nlp`](spec/TreeFuncs.nlp), [`UtilFuncs.nlp`](spec/UtilFuncs.nlp)) are utility code libraries that supply commonly needed functions for parse-tree traversal, knowledge-base manipulation, XML emission, and tag handling.

## languages/

Per-language dictionaries and knowledge bases. Languages currently shipped:

Arabic, Chinese, Dutch, English, French, German, Hebrew, Hindi, Italian, Japanese, Nepali, Portuguese, Russian, Spanish, Tamil.

English is the most fully developed and includes parts-of-speech dictionaries for adjectives, adverbs, conjunctions, determiners, interjections, nouns, prepositions, pronouns, verbs, stop words, and named-entity lists (first names, surnames, countries, states, street suffixes, etc.) &mdash; see [`languages/English/`](languages/English/).

## misc/

General-purpose lexical resources used by many analyzers: currencies, emojis, ISO country and language codes, Roman numerals, telephone country codes, timezones, and URL-domain mappings. Each resource ships as a `.dict` file (and where useful a paired `.kbb` knowledge-base file).

## ecl/

Engine configuration files (`.ecl`) that select which passes the NLP engine runs. Includes [`englishparser.ecl`](ecl/englishparser.ecl), [`flatxml.ecl`](ecl/flatxml.ecl), and [`nestedxml.ecl`](ecl/nestedxml.ecl).

## python/

A small Python wrapper around `nlp.exe` so analyzers can be driven from Python.

- [`nlpengine.py`](python/nlpengine.py) &mdash; the `NLPEngine` class. Constructed with the path to the engine directory and the analyzers directory, it exposes `analyzeFile(...)`, `analyzeStr(...)`, and helpers for reading log output.
- [`nlpengine-example.py`](python/nlpengine-example.py) &mdash; minimal example that runs the Telephone Numbers analyzer over a file and a string and prints the resulting JSON.
- [`nlpplus.py`](python/nlpplus.py) &mdash; additional NLP++ helpers.
- [`DeAccent.py`](python/DeAccent.py) &mdash; accent-stripping utility.

Locate `nlp.exe` either via the VisualText extension ("Engine path to clipboard" in the VISUALTEXT &rarr; LOGGING panel) or by cloning the platform-specific engine repo:

- Windows: <https://github.com/VisualText/nlp-engine-windows>
- macOS: <https://github.com/VisualText/nlp-engine-mac>
- Linux: <https://github.com/VisualText/nlp-engine-linux>

## templates/

Older analyzer templates (Bare, Database, DatesPlusNumbers, EnglishLexicon, XML, XML DTD). Retained for backward compatibility; new work should use the block analyzers under [`analyzers/`](analyzers/).

## Cloning

This repository contains a submodule ([`analyzers/parse-en-us`](analyzers/parse-en-us)). Clone with submodules:

```bash
git clone --recurse-submodules https://github.com/VisualText/visualtext-files.git
```

Or initialize submodules in an existing clone:

```bash
git submodule update --init --recursive
```

## Releases

Tagging a release triggers [`.github/workflows/visualtextfiles.yml`](.github/workflows/visualtextfiles.yml), which initializes submodules, zips `analyzers/`, `Help/`, `spec/`, `languages/`, `misc/`, `ecl/`, and `python/` into `visualtext.zip`, and attaches the archive to the GitHub release. The VSCode extension fetches this archive on first install.

## Contributing a Block Analyzer

To add a new block analyzer to the picker, place it in [`analyzers/`](analyzers/) following the rules in [`analyzers/README.md`](analyzers/README.md):

1. Folder name: a two- to three-word descriptive name.
2. The README's first non-blank line must be the same title prefixed with `#`.
3. The next non-blank line is a short one-sentence description &mdash; this is what users see in the VSCode "New Analyzer" picker.
4. The rest of the README documents how to use and extend the analyzer.

## License

MIT &mdash; see [LICENSE](LICENSE). Copyright (c) 2021 VisualText and NLP++.

## Related Projects

- [VisualText VSCode Extension](http://vscode.visualtext.org)
- [nlp-engine](https://github.com/VisualText/nlp-engine) &mdash; the NLP++ engine source
- [parse-en-us](https://github.com/VisualText/parse-en-us) &mdash; full English parser (included here as a submodule)

## Cross-repo release automation

This repo participates in the VisualText cross-repo release "percolation"
system: submodule bumps flow downstream automatically via `repository_dispatch`.
See **[nlp-engine/docs/PERCOLATION.md](https://github.com/VisualText/nlp-engine/blob/master/docs/PERCOLATION.md)** for the full map.
