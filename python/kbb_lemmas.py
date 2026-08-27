# DESC: Build en-lemmas.kbb (inflected form -> root) from en-full.kbb.
#
# WHAT IT DOES
#   This is the INVERSE of kbb_roots.py.  en-roots.kbb groups inflected forms
#   under their root, which is what a text GENERATOR wants: pick the lemma,
#   walk its children for the form matching the features you need.  An
#   ANALYZER wants the other direction -- it has "bears" in hand and needs
#   "bear" -- so this emits a flat table keyed on the inflected surface form:
#
#       lemmas
#         bears: root=bear
#         went: root=go
#
#   en-full.kbb already carries root= on every inflected reading, but it is a
#   10 MB table keyed by word with the answer buried one level down in m01/m02
#   reading sub-concepts.  This lifts just the lemma link out of it, so the
#   lookup is one findconcept and one strval:
#
#       L("c") = findconcept(G("lemmas"), strtolower(pnvar(N(1),"$text")));
#       if (L("c")) L("lemma") = strval(L("c"),"root");
#
#   WHY A KNOWLEDGE BASE AND NOT A DICTIONARY.  The same data loaded as a
#   .dict changes what every rule sees in every pass -- adding root= without
#   pos= sends words down lookup.nlp's unknown-word branch, and adding
#   pos=verb turns has/have/had into full verbs so vg regroups "has provided".
#   Both were measured to move real parses.  A knowledge base answers only
#   when asked and has no effect on the parse.
#
#   AMBIGUITY.  Of ~79k inflected forms only ~173 have more than one possible
#   root ("axes" <- ax / axe, "calves" <- calf / calve).  Those keep a default
#   root= on the parent so the flat one-hop lookup still answers everywhere,
#   and add m01/m02 children carrying pos= for a caller that can be exact.
#
#   THE DEFAULT IS THE FIRST READING'S ROOT, which in en-full.kbb is usually
#   the NOUN -- "calves: root=calf", not "calve".  A caller that knows it is
#   holding a verb must therefore scan the children for pos=verb before
#   falling back to the parent.  Measured over the 30,648 verb forms, that
#   walk reproduces a hand-built verbs-only table entry for entry; taking the
#   parent's root= blindly gets 172 of them wrong.
#
#   A word that is its own root gets no entry; the caller falls back to the
#   surface form, which is already correct.
#
# USAGE
#   python kbb_lemmas.py <en-full.kbb> <en-lemmas.kbb>

import sys
from collections import OrderedDict

HEADER = """\
# English inflected forms with their root (lemma).
# Built from en-full.kbb by python/kbb_lemmas.py -- the inverse of
# en-roots.kbb, for analysis rather than generation: the inflected
# surface form is the concept and root= is the lemma.
#
#   lemmas
#     bears: root=bear
#     calves: root=calf          <- the first reading, a noun
#       m01: pos=noun root=calf
#       m02: pos=verb root=calve <- a verb caller must read these
#
# Only ~173 of ~79k forms have more than one possible root. Those keep a
# root= on the parent, so a caller that does not know the part of speech
# still gets one answer in one hop, and add m01/m02 children so one that
# does can be exact -- scan them for the pos you are holding, and fall
# back to the parent's root= when none matches.
#
# Regenerate with:
#   python kbb_lemmas.py en-full.kbb en-lemmas.kbb
"""


def parse_reading(rest):
    # rest = "pos=verb root=go vform=past tense=past"  ->  (pos, root)
    pos = root = None
    for tok in rest.split():
        k, _, v = tok.partition("=")
        if k == "pos":
            pos = v
        elif k == "root":
            root = v
    return pos, root


def concept_line(indent, name, attrs):
    # A KBB concept line carries a trailing ':' only when attributes follow it.
    line = " " * indent + name
    if attrs:
        line += ": " + " ".join(k + "=" + v for k, v in attrs)
    return line + "\n"


def main(argv):
    if len(argv) < 2:
        sys.stderr.write("usage: kbb_lemmas.py <en-full.kbb> <en-lemmas.kbb>\n")
        return 1
    inpath, outpath = argv[0], argv[1]

    # surface form -> OrderedDict((pos, root) -> None), in reading order
    lemmas = OrderedDict()
    word = None
    n_readings = 0

    with open(inpath, "r", encoding="utf-8") as f:
        for raw in f:
            line = raw.rstrip("\n")
            if not line or line.lstrip().startswith("#"):
                continue
            indent = len(line) - len(line.lstrip(" "))
            content = line.strip()
            if indent == 2 and content.endswith(":"):
                word = content[:-1]
            elif indent == 4 and word is not None:
                # "m01: pos=verb root=go vform=past tense=past"
                _, _, rest = content.partition(":")
                pos, root = parse_reading(rest.strip())
                # an uninflected reading is its own root and needs no entry
                if not root or root == word:
                    continue
                n_readings += 1
                lemmas.setdefault(word, OrderedDict())[(pos, root)] = None

    n_ambiguous = 0
    with open(outpath, "w", encoding="utf-8", newline="\n") as out:
        out.write(HEADER)
        out.write("lemmas\n")
        for word in sorted(lemmas):
            readings = list(lemmas[word])
            roots = []
            for _, root in readings:
                if root not in roots:
                    roots.append(root)
            # the first reading's root is the default, so a caller that does
            # not care about part of speech still gets one answer, one hop
            out.write(concept_line(2, word, [("root", roots[0])]))
            if len(roots) > 1:
                n_ambiguous += 1
                for i, (pos, root) in enumerate(readings, start=1):
                    attrs = [("root", root)]
                    if pos:
                        attrs.insert(0, ("pos", pos))
                    out.write(concept_line(4, "m%02d" % i, attrs))

    sys.stderr.write("[kbb_lemmas: %d inflected forms, %d readings, "
                     "%d forms with more than one root -> %s]\n"
                     % (len(lemmas), n_readings, n_ambiguous, outpath))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
