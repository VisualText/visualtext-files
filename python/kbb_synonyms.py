# DESC: Build en-synonyms-full.kbb (word -> synonyms) from en-full.kbb + WordNet.
#
# WHAT IT DOES
#   For every headword in en-full.kbb, collects its WordNet synonyms (the other
#   lemmas that share any of the word's synsets, across all senses and parts of
#   speech) and writes a flat KBB table where each word is a concept and its
#   synonyms are child concepts:
#
#       synonyms
#         car:
#           auto:
#           automobile:
#           cable car:
#           gondola:
#           machine:
#           motorcar:
#
#   Headwords are taken from en-full.kbb so the table stays aligned with the
#   English dictionary / en-roots.kbb.  A word with no synonyms is omitted.
#   Multi-word WordNet lemmas keep their words but the underscore becomes a
#   space (cable_car -> "cable car"); synonyms are lower-cased and de-duped.
#   The word itself is never listed as its own synonym.
#
# USAGE
#   python kbb_synonyms.py <en-full.kbb> <en-synonyms-full.kbb> [nltk_data_dir]
#
#   Needs nltk + the WordNet corpus.  If nltk_data lives outside the default
#   search path, pass its directory as the 3rd arg (or set NLTK_DATA); this
#   pipeline keeps it at c:/tmp/nltk_data.

import os
import sys


def load_wordnet(extra_dir):
    import nltk
    for d in [extra_dir, os.environ.get("NLTK_DATA"), r"c:/tmp/nltk_data"]:
        if d and os.path.isdir(d):
            nltk.data.path.insert(0, d)
    from nltk.corpus import wordnet as wn
    wn.ensure_loaded()
    return wn


def read_headwords(path):
    # concept lines are indented exactly 2 spaces and end with ':'
    heads = []
    with open(path, "r", encoding="utf-8") as f:
        for raw in f:
            line = raw.rstrip("\n")
            if (line.startswith("  ") and not line.startswith("   ")
                    and line.rstrip().endswith(":")):
                heads.append(line.strip()[:-1])
    return heads


def synonyms_for(wn, word):
    # Only trust synsets in which the word is itself a lemma. wn.synsets()
    # applies morphy, so "aahed" would otherwise pull in "aah"'s synset and
    # report the lemma as a bogus synonym of its own inflection. Requiring exact
    # lemma membership keeps synonymy a lemma-level relation (surface forms get
    # no entry — lemmatize via en-roots.kbb first).
    key = word.replace(" ", "_").lower()
    out = set()
    for ss in wn.synsets(word):
        names = [n.lower() for n in ss.lemma_names()]
        if key not in names:
            continue
        for name in ss.lemma_names():
            norm = name.replace("_", " ").lower()
            if norm != word:
                out.add(norm)
    return sorted(out)


def main(argv):
    if len(argv) < 2:
        sys.stderr.write("usage: kbb_synonyms.py <en-full.kbb> "
                         "<en-synonyms-full.kbb> [nltk_data_dir]\n")
        return 1
    inpath, outpath = argv[0], argv[1]
    extra_dir = argv[2] if len(argv) > 2 else None

    wn = load_wordnet(extra_dir)
    heads = read_headwords(inpath)

    n_words = 0
    n_links = 0
    with open(outpath, "w", encoding="utf-8") as out:
        out.write("# English word synonyms from WordNet, keyed by en-full.kbb "
                  "headword.\n")
        out.write("# Built by python/kbb_synonyms.py — each word concept lists "
                  "its synonyms\n")
        out.write("# (union of all WordNet senses / parts of speech) as child "
                  "concepts.\n")
        out.write("# Regenerate with:\n")
        out.write("#   python kbb_synonyms.py en-full.kbb en-synonyms-full.kbb\n")
        out.write("synonyms\n")
        seen = set()
        for word in heads:
            if word in seen:
                continue
            seen.add(word)
            syns = synonyms_for(wn, word)
            if not syns:
                continue
            # A concept line carries a trailing ':' only when attributes follow;
            # these are all bare names, so no colons.
            out.write("  " + word + "\n")
            for s in syns:
                out.write("    " + s + "\n")
            n_words += 1
            n_links += len(syns)

    sys.stderr.write("[kbb_synonyms: %d words, %d synonym links -> %s]\n"
                     % (n_words, n_links, outpath))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
