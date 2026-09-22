# DESC: Add words to en-feat-full.dict, generating the full set of inflected
#       readings with the features the file already uses.
#
# WHY
#   The English lexicon descends from an older open word list, and it shows in
#   what it has against what it lacks: it knows "aalii", "aardwolf", "qoph" and
#   "syzygy", and does not know "email", "internet", "website", "blog",
#   "online" or "app".  The gap is not random, it is a generation of
#   vocabulary, and it is the gap an analyzer meets first in ordinary modern
#   text.  A missing word costs more than the word: it arrives with no part of
#   speech at all, and every rule downstream has to guess.
#
#   Adding one by hand means writing five or six lines with the right vform,
#   tense, person and number on each, keeping root= pointing at a base entry
#   that exists, and keeping the file sorted.  That is a lot of ways to be
#   slightly wrong, so it is a script.
#
# WHAT IT DOES
#   Takes a table of (lemma, parts of speech), and for each one emits the
#   readings the file's own schema calls for:
#
#     noun   singular, plural
#     verb   base, pres3sg, past, pastpart, ger
#     adj    one reading
#     adv    one reading
#
#   English spelling rules are applied for the inflections -- doubling a final
#   consonant after a short vowel (blog -> blogged, blogging), -y -> -ies,
#   -e dropped before -ing, -es after a sibilant.  An irregular form can be
#   given explicitly in the table and is used as written.
#
#   A reading already in the file is left alone, so the script is idempotent
#   and safe to re-run as the table grows.  Nothing is removed, ever.
#
# WHAT IT DOES NOT DO
#   It does not add freq_<pos>=.  Those counts come from WordNet via
#   dict_freq.py, and a word WordNet has never seen should have no count
#   rather than a made-up one -- a missing count means no evidence.
#
# USAGE
#   python en_add_words.py <en-feat-full.dict>
#     --dry-run    report what would be added, write nothing
#
#   Then regenerate everything derived from it:
#     python kbb_rootfix.py kbb en-feat-full.dict en-full.kbb
#     python kbb_lemmas.py en-full.kbb en-lemmas-full.kbb
#     python kbb_roots.py  en-full.kbb en-roots.kbb
#     python dict_project.py en-feat-full.dict en-full.dict

import sys

VOWELS = "aeiou"
SIBILANT = ("s", "x", "z", "ch", "sh", "o")

# lemma -> parts of speech.  An irregular form goes in OVERRIDE below.
WORDS = {
    # the network and the things on it
    "email":         ["noun", "verb"],
    "internet":      ["noun"],
    "intranet":      ["noun"],
    "website":       ["noun"],
    "webpage":       ["noun"],
    "webcam":        ["noun"],
    "blog":          ["noun", "verb"],
    "blogger":       ["noun"],
    "podcast":       ["noun", "verb"],
    "hashtag":       ["noun"],
    "username":      ["noun"],
    "login":         ["noun"],
    "logout":        ["noun"],
    "online":        ["adj", "adv"],
    "offline":       ["adj", "adv"],
    "broadband":     ["noun"],
    "wifi":          ["noun"],
    "url":           ["noun"],
    "app":           ["noun"],
    "chatbot":       ["noun"],
    "spam":          ["noun", "verb"],
    "spyware":       ["noun"],
    "malware":       ["noun"],
    "cybersecurity": ["noun"],
    "cyberattack":   ["noun"],
    "paywall":       ["noun"],
    "streaming":     ["noun"],
    "livestream":    ["noun", "verb"],
    "download":      ["noun"],
    "upload":        ["noun"],
    # devices and everyday modern nouns
    "smartphone":    ["noun"],
    "laptop":        ["noun"],
    "tablet":        ["noun"],
    "touchscreen":   ["noun"],
    "smartwatch":    ["noun"],
    "earbud":        ["noun"],
    "selfie":        ["noun"],
    "emoji":         ["noun"],
    "avatar":        ["noun"],
    "voicemail":     ["noun"],
    "healthcare":    ["noun"],
    "childcare":     ["noun"],
    "workflow":      ["noun"],
    "workplace":     ["noun"],
    "lifestyle":     ["noun"],
    "teenager":      ["noun"],
    "carpool":       ["noun", "verb"],
    "takeout":       ["noun"],
    "smoothie":      ["noun"],
    "recycling":     ["noun"],
}

# forms that do not follow the spelling rules, or that should not be generated
OVERRIDE = {
    ("emoji", "plural"): "emojis",
    ("url", "plural"): "urls",
    ("wifi", "plural"): None,          # no plural
    ("broadband", "plural"): None,
    ("healthcare", "plural"): None,
    ("childcare", "plural"): None,
    ("cybersecurity", "plural"): None,
    ("streaming", "plural"): None,
    ("recycling", "plural"): None,
    ("spyware", "plural"): None,
    ("malware", "plural"): None,
    ("internet", "plural"): None,
    ("podcast", "past"): "podcast",     # like "broadcast"
    ("podcast", "pastpart"): "podcast",
}


def plural(base):
    if base.endswith("y") and len(base) > 1 and base[-2] not in VOWELS:
        return base[:-1] + "ies"
    if base.endswith(SIBILANT):
        return base + "es"
    return base + "s"


def doubles(base):
    """A final consonant doubles after a single short vowel: blog -> blogged."""
    if len(base) < 3 or base[-1] in VOWELS or base[-1] in "wxy":
        return False
    return base[-2] in VOWELS and base[-3] not in VOWELS


def verb_forms(base):
    third = plural(base)
    if base.endswith("e"):
        past, ger = base + "d", base[:-1] + "ing"
    elif doubles(base):
        past, ger = base + base[-1] + "ed", base + base[-1] + "ing"
    elif base.endswith("y") and len(base) > 1 and base[-2] not in VOWELS:
        past, ger = base[:-1] + "ied", base + "ing"
    else:
        past, ger = base + "ed", base + "ing"
    return third, past, ger


def readings(lemma, poses):
    """Every (surface, attribute string) this lemma should contribute."""
    out = []
    for pos in poses:
        if pos == "noun":
            out.append((lemma, "pos=noun number=singular"))
            pl = OVERRIDE.get((lemma, "plural"), plural(lemma))
            if pl:
                out.append((pl, f"pos=noun root={lemma} number=plural"))
        elif pos == "verb":
            third, past, ger = verb_forms(lemma)
            past = OVERRIDE.get((lemma, "past"), past)
            pastpart = OVERRIDE.get((lemma, "pastpart"), past)
            out.append((lemma, "pos=verb vform=base tense=present"))
            out.append((third, f"pos=verb root={lemma} vform=pres3sg "
                               f"tense=present person=3 number=singular"))
            out.append((past, f"pos=verb root={lemma} vform=past tense=past"))
            out.append((pastpart, f"pos=verb root={lemma} vform=pastpart"))
            out.append((ger, f"pos=verb root={lemma} vform=ger"))
        elif pos in ("adj", "adv"):
            out.append((lemma, f"pos={pos}"))
    return out


def key_of(reading):
    """What identifies a reading, for the already-present test.

    The whole line, minus any freq_<pos>= -- a regular verb has two lines that
    share a surface form and a part of speech, differing only in vform, so
    (surface, pos) is too coarse and would drop the participle.  But the counts
    are put there separately by dict_freq.py and are not part of what
    identifies a reading, so comparing them would make an existing entry that
    has one look different from the generated line that cannot.
    """
    parts = [t for t in reading.split() if not t.startswith("freq_")]
    return " ".join(parts).lower()


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    dry = "--dry-run" in sys.argv
    if not args:
        sys.stderr.write("usage: en_add_words.py <en-feat-full.dict> [--dry-run]\n")
        return 1
    path = args[0]

    lines = open(path, encoding="utf-8", errors="replace").read().splitlines()
    have = set()
    for line in lines:
        if not line.strip() or line.startswith("#"):
            continue
        have.add(key_of(line))

    added, skipped = [], 0
    for lemma in sorted(WORDS):
        for surface, attrs in readings(lemma, WORDS[lemma]):
            reading = f"{surface} {attrs}"
            key = key_of(reading)
            if key in have:
                skipped += 1
                continue
            have.add(key)
            added.append(reading)

    print(f"  lemmas in table: {len(WORDS)}")
    print(f"  readings already present: {skipped}")
    print(f"  readings to add: {len(added)}")
    for a in added[:8]:
        print(f"      {a}")
    if len(added) > 8:
        print(f"      ... and {len(added) - 8} more")

    if dry or not added:
        if dry:
            print("  (dry run -- nothing written)")
        return 0

    header = [l for l in lines if l.startswith("#")]
    body = [l for l in lines if l.strip() and not l.startswith("#")]
    body.extend(added)
    body.sort(key=lambda l: (l.split()[0].lower(), l))
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write("\n".join(header + body) + "\n")
    print(f"  wrote {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
