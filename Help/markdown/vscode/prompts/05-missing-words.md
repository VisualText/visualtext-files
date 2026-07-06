Add missing words to the English dictionary
<!-- desc: Reads missing_words.txt from the analyzer's output log and, for each genuine word, adds a properly featured entry (part of speech, root, verb/noun features) to en-full.dict and en-full.kbb — keeping both alphabetized with identical headword sets. -->
I want you to extend the full English dictionary from the missing words an analyzer collected. Everything you need is on this machine at the paths below:

- Current analyzer (its output log holds the missing-words list): {{currentAnalyzer}}
- Shared language dictionaries / KBs (the English full dictionary lives here): {{languagesDir}}
- NLP engine executable (to re-run and verify): {{engineExe}}

The missing-words list: find **missing_words.txt** in the analyzer's output — check the analyzer's `output/` folder first, then the per-input logs under `input/<file>.txt_log/`. It is a plain list of words the analyzer did not find in the dictionary (one word per line; if a line carries a count or other columns, use only the word). De-duplicate and lowercase the words before processing.

The two files to edit (both under `{{languagesDir}}/English/`):

1. **en-full.dict** — part-of-speech only, one line per (word, pos) reading, alphabetically sorted. Header line `# Full English Dictionary POS`. Example:

        aardvark pos=noun
        aahed pos=verb
        aah pos=verb
        aah pos=int

2. **en-full.kbb** — the knowledge-base form, first line `dictionary`, then one node per word with a numbered reading (`m01`, `m02`, …) per part of speech, attributes copied in full. Example:

        dictionary
          aah:
            m01: pos=verb vform=base tense=present
            m02: pos=int
          aahed:
            m01: pos=verb root=aah vform=past tense=past
            m02: pos=verb root=aah vform=pastpart
          aardvark:
            m01: pos=noun number=singular

Both files MUST keep the same headword set and stay alphabetically sorted. Preserve the existing line endings (CRLF) and indentation (two spaces before the word node, four before each `m##`).

For each missing word, create an entry that follows the schema:

- **Part of speech** (`pos=`): noun, verb, adj, adv, det, pro, prep, conj, int, etc. A word may have several readings — give each its own `.dict` line and its own `m##` in the `.kbb` (e.g. a word that is both a verb and an interjection).
- **root=** — on an *inflected* form only, giving the lemma (`aahed pos=verb root=aah`). Base forms carry no root. Only use a root that is itself a real base entry of the same pos.
- **verb features** — one reading per grammatical form, `vform` always present:
    - `vform=base tense=present`
    - `vform=pres3sg tense=present person=3 number=singular`
    - `vform=past tense=past`
    - `vform=pastpart`
    - `vform=ger`
- **noun number** — every `pos=noun` gets `number=singular` or `number=plural`; a noun has a `root=` only when it is a plural form.

Note: in en-full.dict the verb readings collapse to one line per (word, pos) with `pos=` only — no root or features there; the full features live only in the .kbb `m##` lines. Match what you see in the surrounding entries.

Precision — this dictionary should stay clean:

- Skip words that are already present (check both files first).
- Add genuine words only. If the list contains obvious noise — typos, fragments, single letters, run-together tokens, or proper nouns — do NOT pollute the dictionary with them. Collect those in a separate `missing_words_skipped.txt` (with a one-line reason each) so I can review them.
- If a word is a plural/inflection whose base is not yet in the dictionary, add the base entry too so every `root=` resolves.

When done:

- Show me a summary: how many words added, broken down by part of speech, and the skipped list.
- Re-run the analyzer over its inputs with the engine executable and confirm the previously missing words are now recognized (the new missing_words.txt should be shorter).
- Note: these two files are generated from `en-full-feat.dict` (the featured source of truth in the same directory). If it is present, add the same featured entry there as well so the additions survive a future regeneration.
