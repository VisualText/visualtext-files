# DESC: Rank the words an analyzer could not find in its lexicon, as a worklist
#       for en_add_words.py.
#
# WHAT IT DOES
#   The engine writes one missing-words.log per input, listing every word the
#   tokenizer failed to find in any loaded dictionary.  Run an analyzer over a
#   corpus and those logs are a record of what the lexicon actually lacks, as
#   opposed to what someone guessed it might lack.  This aggregates them into
#   one ranked worklist.
#
#   A miss is only a lexicon gap if it is a word.  Three kinds of miss are not:
#     - proper names:     written capitalized everywhere they appear
#     - inflections of a gap:  "blogging" is the same gap as "blog"
#     - one-off noise:    OCR debris, fragments, foreign words
#   So each miss is checked back against the text it came from for how it was
#   capitalized, grouped under the base form where the lexicon-building script
#   would put it, and ranked by how many separate documents it appears in --
#   document frequency, not raw count, so one chatty file cannot dominate.
#
# USAGE
#   python harvest_gaps.py <log-dir> <corpus-dir> [--min-docs N]
#     <log-dir>     directory of *.missing files (one per input)
#     <corpus-dir>  the input texts themselves, same base names
#
# OUTPUT
#   TSV on stdout: docs, count, forms seen, capitalization, verdict

import sys
import os
import re
from collections import defaultdict

SUFFIXES = [
    ("iness", "y"), ("ingly", ""), ("ies", "y"), ("ied", "y"), ("ier", "y"),
    ("iest", "y"), ("ing", ""), ("ing", "e"), ("ted", "t"), ("ed", ""),
    ("ed", "e"), ("es", ""), ("s", ""), ("ly", ""), ("er", ""), ("est", ""),
]


def base_forms(word):
    """Candidate base forms of a surface word, longest suffix first."""
    out = [word]
    for suf, repl in SUFFIXES:
        if word.endswith(suf) and len(word) - len(suf) >= 3:
            stem = word[: -len(suf)] + repl
            out.append(stem)
            # undo consonant doubling: "blogging" -> "blogg" -> "blog"
            if len(stem) >= 4 and stem[-1] == stem[-2]:
                out.append(stem[:-1])
    return out


def main():
    if len(sys.argv) < 3:
        print(__doc__ or "usage: harvest_gaps.py <log-dir> <corpus-dir>", file=sys.stderr)
        return 1
    logdir, corpusdir = sys.argv[1], sys.argv[2]
    min_docs = 1
    if "--min-docs" in sys.argv:
        min_docs = int(sys.argv[sys.argv.index("--min-docs") + 1])

    # how each word is written in the corpus, over all documents
    written = defaultdict(lambda: {"lower": 0, "cap": 0, "upper": 0})
    for name in os.listdir(corpusdir):
        if not name.endswith(".txt"):
            continue
        text = open(os.path.join(corpusdir, name), encoding="utf-8", errors="replace").read()
        for tok in re.findall(r"[A-Za-z][A-Za-z'-]*", text):
            key = tok.lower()
            if tok.isupper() and len(tok) > 1:
                written[key]["upper"] += 1
            elif tok[0].isupper():
                written[key]["cap"] += 1
            else:
                written[key]["lower"] += 1

    docs = defaultdict(set)
    count = defaultdict(int)
    for name in os.listdir(logdir):
        if not name.endswith(".missing"):
            continue
        doc = name[: -len(".missing")]
        for line in open(os.path.join(logdir, name), encoding="utf-8", errors="replace"):
            w = line.strip().lower()
            if not w or not w.isalpha():
                continue
            docs[w].add(doc)
            count[w] += 1

    # group surface forms under the base form the lexicon would key on
    groups = defaultdict(set)
    for w in docs:
        base = w
        for cand in base_forms(w):
            if cand in docs and len(cand) < len(base):
                base = cand
        groups[base].add(w)

    rows = []
    for base, forms in groups.items():
        alldocs = set()
        total = 0
        low = cap = upp = 0
        for f in forms:
            alldocs |= docs[f]
            total += count[f]
            low += written[f]["lower"]
            cap += written[f]["cap"]
            upp += written[f]["upper"]
        if len(alldocs) < min_docs:
            continue
        if low == 0 and (cap or upp):
            verdict = "NAME/ACRONYM (never lower case)"
        elif low == 0:
            verdict = "unseen"
        elif cap > low * 3:
            verdict = "probably a name"
        else:
            verdict = "LEXICON GAP"
        rows.append((len(alldocs), total, base, sorted(forms), low, cap, upp, verdict))

    rows.sort(key=lambda r: (-r[0], -r[1], r[2]))
    print("docs\tcount\tbase\tforms\tlower\tcap\tupper\tverdict")
    for d, c, base, forms, low, cap, upp, verdict in rows:
        print(f"{d}\t{c}\t{base}\t{','.join(forms)}\t{low}\t{cap}\t{upp}\t{verdict}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
