# DESC: Build en-roots.kbb (root -> inflected forms) from en-full.kbb.
#
# WHAT IT DOES
#   en-full.kbb is keyed by surface word; each inflected reading carries a
#   "root=<lemma>" pointer back to its base form.  This script inverts that:
#   it groups every inflected surface form UNDER its root, producing a
#   generation-oriented table
#
#       roots
#         go:
#           goes: pos=verb vform=pres3sg tense=present person=3 number=singular
#           going: pos=verb vform=ger
#           gone: pos=verb vform=pastpart
#           went: pos=verb vform=past tense=past
#
#   so a text generator can look up a lemma and walk its children to pick the
#   surface form matching the desired features.  The root (base/lemma) form is
#   the PARENT concept name; only its conjugations/plurals are children.  The
#   redundant "root=" attribute is dropped from each child.
#
#   When one surface form has several readings that share the same root
#   (e.g. "goes" = noun-plural AND verb-3sg), the form gets m01/m02 reading
#   sub-concepts, exactly like en-full.kbb; a single-reading form is inlined.
#
#   Only roots that actually have inflected forms are emitted (invariant words
#   such as adverbs / interjections have nothing to generate and are skipped).
#
# USAGE
#   python kbb_roots.py <en-full.kbb> <en-roots.kbb>

import sys
from collections import OrderedDict


def parse_reading(rest):
    # rest = "pos=verb root=go vform=past tense=past"  ->  (root, [(k,v),...])
    root = None
    attrs = []
    for tok in rest.split():
        k, _, v = tok.partition("=")
        if not k:
            continue
        if k == "root":
            root = v
        else:
            attrs.append((k, v))
    return root, attrs


VOWELS = set("aeiou")

# Suppletive / irregular adjective degrees that no spelling rule produces.
IRREGULAR_ADJ = {
    "good": (["better"], ["best"]),
    "bad": (["worse"], ["worst"]),
    "far": (["farther", "further"], ["farthest", "furthest"]),
    "little": (["less", "lesser"], ["least"]),
}


def degree_candidates(base):
    # Return (comparative_forms, superlative_forms) spelling candidates for an
    # adjective base. Multiple rules may apply (we can't know stress/geminate
    # from spelling alone) so we generate all plausible forms and let the
    # caller keep only those attested as adjectives.
    comps, supers = set(), set()

    def add(suffix_c, suffix_s, stem=base):
        comps.add(stem + suffix_c)
        supers.add(stem + suffix_s)

    add("er", "est")                                   # small -> smaller/smallest
    if base.endswith("e"):
        add("r", "st")                                 # large -> larger/largest
    if len(base) >= 2 and base[-1] == "y" and base[-2] not in VOWELS:
        add("ier", "iest", base[:-1])                  # happy -> happier/happiest
    if (len(base) >= 3 and base[-1] not in VOWELS and base[-1] not in "wxy"
            and base[-2] in VOWELS and base[-3] not in VOWELS):
        add(base[-1] + "er", base[-1] + "est")         # big -> bigger/biggest
    return comps, supers


def add_degree(paradigms, base, form, degree):
    reading = [("pos", "adj"), ("degree", degree)]
    forms = paradigms.setdefault(base, OrderedDict())
    lst = forms.setdefault(form, [])
    if reading not in lst:
        lst.append(reading)
        return 1
    return 0


def derive_adjective_degrees(paradigms, adj_words, all_words):
    n = 0
    for base in adj_words:
        comps, supers = degree_candidates(base)
        for form in comps:
            if form != base and form in adj_words:
                n += add_degree(paradigms, base, form, "comparative")
        for form in supers:
            if form != base and form in adj_words:
                n += add_degree(paradigms, base, form, "superlative")
    for base, (comps, supers) in IRREGULAR_ADJ.items():
        if base not in all_words:
            continue
        for form in comps:
            if form in all_words:
                n += add_degree(paradigms, base, form, "comparative")
        for form in supers:
            if form in all_words:
                n += add_degree(paradigms, base, form, "superlative")
    return n


def concept_line(indent, name, attrs):
    # A KBB concept line carries a trailing ':' only when attributes follow it;
    # a bare concept (children only, or a leaf marker) needs no colon.
    line = " " * indent + name
    if attrs:
        line += ": " + " ".join(k + "=" + v for k, v in attrs)
    return line + "\n"


def main(argv):
    if len(argv) < 2:
        sys.stderr.write("usage: kbb_roots.py <en-full.kbb> <en-roots.kbb>\n")
        return 1
    inpath, outpath = argv[0], argv[1]

    # root -> OrderedDict(surface_word -> list of attr-lists)
    paradigms = {}
    all_words = set()     # every surface form in the dictionary
    adj_words = set()     # surface forms that have a pos=adj reading
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
                all_words.add(word)
            elif indent == 4 and word is not None:
                # "m01: pos=verb root=go ..."
                _, _, rest = content.partition(":")
                root, attrs = parse_reading(rest.strip())
                if ("pos", "adj") in attrs:
                    adj_words.add(word)
                if root is None:
                    continue  # base/uninflected reading — not a child of anything
                n_readings += 1
                forms = paradigms.setdefault(root, OrderedDict())
                forms.setdefault(word, []).append(attrs)

    # en-full.kbb encodes no adjective degree, so derive comparative/superlative
    # links morphologically and keep only forms that actually exist as adjectives
    # in the dictionary (never invent a surface form).
    n_degree = derive_adjective_degrees(paradigms, adj_words, all_words)

    with open(outpath, "w", encoding="utf-8") as out:
        out.write("# English word roots with their inflected forms "
                  "(conjugations / plurals).\n")
        out.write("# Built from en-full.kbb by python/kbb_roots.py — for text "
                  "generation:\n")
        out.write("# parent concept = root/lemma (base surface form); children "
                  "= inflected\n")
        out.write("# forms carrying their morphological features. Regenerate "
                  "with:\n")
        out.write("#   python kbb_roots.py en-full.kbb en-roots.kbb\n")
        out.write("roots\n")
        for root in sorted(paradigms):
            out.write(concept_line(2, root, None))       # bare root, no attrs
            forms = paradigms[root]
            for surface in sorted(forms):
                readings = forms[surface]
                if len(readings) == 1:
                    out.write(concept_line(4, surface, readings[0]))
                else:
                    out.write(concept_line(4, surface, None))  # parent of m01..
                    for i, attrs in enumerate(readings, start=1):
                        out.write(concept_line(6, "m%02d" % i, attrs))

    sys.stderr.write("[kbb_roots: %d roots, %d inflected readings, "
                     "%d derived adj-degree links -> %s]\n"
                     % (len(paradigms), n_readings, n_degree, outpath))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
