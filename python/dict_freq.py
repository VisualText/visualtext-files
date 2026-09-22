# DESC: Add freq= to the English dictionary: how often each word is used IN
#       THAT PART OF SPEECH, so an analyzer can prefer the likelier reading.
#
# WHY
#   9.5% of the lexicon's headwords have more than one part of speech, and
#   10,164 of them are both a noun and a verb -- run, walk, love, use, work,
#   change, help, call, need, order, hand.  Nothing in the dictionary says
#   which reading is the likely one, so an analyzer that cannot settle a word
#   from context has to fall back on a single global ordering, typically
#   "noun beats verb beats adjective".  That ordering is a guess standing in
#   for ten thousand separate facts, and it is wrong about a third of the time:
#   "use" is a verb far more often than a noun, and so are run, walk, help,
#   call, need, break, build and answer.
#
#   A count per reading replaces the guess with the fact.  It is not a general
#   word-frequency list -- "the" does not need one -- it is the far smaller
#   question of how a word divides between its own parts of speech.
#
# AN INFLECTED READING TAKES ITS ROOT'S COUNT
#   WordNet's counts sit on lemmas.  Looked up directly, "lifted" is found
#   only as the participial ADJECTIVE -- a real WordNet lemma, count 1 --
#   while its far commoner verb reading gets nothing, because that count
#   belongs to "lift".  Left alone a count of one beats no count at all and
#   every -ed form in the language drifts toward adjective: "when the fog
#   finally lifted" loses its verb.  So a reading with no count of its own
#   falls back to its root's count for the same part of speech.
#
# WHERE THE NUMBERS COME FROM
#   WordNet's sense-tagged counts, which come from SemCor, a corpus hand
#   tagged word by word with WordNet senses.  Summing a lemma's sense counts
#   per part of speech gives exactly the split this needs:
#
#       use     noun 118   verb 623
#       hand    noun 232   verb  25
#
#   WordNet ships with a permissive licence that allows redistribution with
#   its notice, so the derived numbers can be shipped in the library.  The
#   counts are evidence, not truth: SemCor is about 230,000 tagged words, so
#   it speaks with authority about common words and says nothing at all about
#   rare ones.  A reading it does not cover gets no freq= and the analyzer
#   falls back to whatever it did before -- which is the right behaviour, since
#   a missing number should never be read as "never happens".
#
# WHAT IT WRITES
#   The count is written as freq_<pos>=, not as a bare freq=, because a
#   dictionary's attributes merge onto one node per word: "use" arrives with
#   noun=1 and verb=1 together, and a single freq= would leave no way to tell
#   which reading the number belonged to.
#
#       use   pos=verb vform=base tense=present freq_verb=623
#       use   pos=noun number=singular freq_noun=118
#
#   so a rule reads N("freq_noun") against N("freq_verb") directly.  Every
#   reading of the same (word, pos) gets that pos's total: the split being
#   recorded is between parts of speech, not between inflected forms.
#   Re-running replaces any freq= already there, so the script is idempotent
#   and can be re-run when WordNet is updated.
#
# REQUIRES
#   nltk with the WordNet corpus:
#     pip install nltk
#     python -m nltk.downloader wordnet
#
# USAGE
#   python dict_freq.py <en-full-feat.dict>            rewrites in place
#     --dry-run    report the counts, write nothing
#
#   Afterwards regenerate the files derived from it:
#     python kbb_rootfix.py kbb en-full-feat.dict en-full.kbb
#     python kbb_lemmas.py en-full.kbb en-lemmas.kbb
#     python kbb_roots.py  en-full.kbb en-roots.kbb
#   and project the pos-only dictionary with dict_project.py.

import sys
import collections

WNPOS = {'n': 'noun', 'v': 'verb', 'a': 'adj', 's': 'adj', 'r': 'adv'}


def wordnet_counts():
    """(word, pos) -> summed SemCor sense count."""
    from nltk.corpus import wordnet as wn
    counts = collections.defaultdict(int)
    for lemma_name in wn.all_lemma_names():
        if '_' in lemma_name:
            continue
        for lemma in wn.lemmas(lemma_name):
            c = lemma.count()
            if not c:
                continue
            pos = WNPOS.get(lemma.synset().pos())
            if pos:
                counts[(lemma_name.lower(), pos)] += c
    return counts


def main():
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    dry = '--dry-run' in sys.argv
    if not args:
        sys.stderr.write("usage: dict_freq.py <en-full-feat.dict> [--dry-run]\n")
        return 1
    path = args[0]

    counts = wordnet_counts()
    sys.stderr.write(f"WordNet readings with a count: {len(counts)}\n")

    out = []
    tagged = words = 0
    seen = set()
    with open(path, encoding='utf-8', errors='replace') as fh:
        for raw in fh:
            line = raw.rstrip('\n').rstrip('\r')
            if not line.strip() or line.startswith('#'):
                out.append(line)
                continue
            parts = [p for p in line.split() if not p.startswith('freq_')]
            word = parts[0]
            pos = None
            for a in parts[1:]:
                if a.startswith('pos='):
                    pos = a[4:]
                    break
            root = None
            for a in parts[1:]:
                if a.startswith('root='):
                    root = a[5:]
                    break
            n = counts.get((word.lower(), pos), 0) if pos else 0
            # WordNet counts sit on the lemma, so an inflected reading asks its
            # root for the count of the same part of speech.
            if not n and root and pos:
                n = counts.get((root.lower(), pos), 0)
            if n:
                out.append(" ".join(parts) + f" freq_{pos}={n}")
                tagged += 1
                if (word, pos) not in seen:
                    seen.add((word, pos))
                    words += 1
            else:
                out.append(" ".join(parts))

    sys.stderr.write(f"readings given a freq_<pos>=: {tagged}  "
                     f"distinct (word, pos): {words}\n")
    if not dry:
        with open(path, 'w', encoding='utf-8', newline='\n') as fh:
            fh.write("\n".join(out) + "\n")
        sys.stderr.write(f"wrote {path}\n")
    return 0


if __name__ == '__main__':
    sys.exit(main())
