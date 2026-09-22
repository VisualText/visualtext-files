# DESC: Give a domain dictionary's entries their part of speech, so that
#       stacking it on the full lexicon adds meaning instead of removing grammar.
#
# WHY
#   Dictionaries in kb/user are meant to stack: an analyzer loads the general
#   lexicon plus whichever domain files it needs.  But when two dictionaries
#   define the same word, the one that defines it wins outright -- a word
#   another dictionary defines is never looked up in the lazily loaded en-full
#   lexicon.  So a domain file that carries only domain attributes silently
#   takes the grammar away:
#
#       en-full.dict        may  pos=noun / pos=verb
#       en-monthsdays.dict  may  month=5
#       stacked             may  month=5                 <- noun and verb gone
#
#   The parse falls apart in ways that look nothing like a dictionary problem:
#   "I may go" loses its auxiliary, "the cat sat" reads "sat" as a date, and
#   "the quick brown fox" loses its adjectives if en-adj is shadowed.  Measured
#   over the English library, the domain dictionaries between them would strip
#   the part of speech from about 4,000 words that en-full.dict knows --
#   1,168 of them from en-surnames.dict alone (Baker, Brown, Fisher, Mason).
#
#   The fix is for each entry to carry its own part of speech.  Then the
#   override is harmless, because the winning entry says everything the losing
#   one did.
#
# WHAT IT DOES
#   For every entry, appends pos= taken from en-full.dict.  A word with more
#   than one part of speech gets one extra line per reading, which is how
#   en-full.dict itself writes them:
#
#       may month=5 pos=noun
#       may pos=verb
#
#   An entry the general lexicon does not know is a proper name, a place or a
#   coined term, so it is given pos=noun -- except where the file already says
#   what role the entry plays (en-nationalities.dict marks adj=/noun=/plural=),
#   in which case that is used.  Comments, blank lines and attribute order are
#   preserved, and the script is idempotent: an entry that already has a pos=
#   is left exactly as it is.
#
# USAGE
#   python dict_addpos.py <en-full.dict> <domain.dict> [more.dict ...]
#     --dry-run    report what would change, write nothing
#
#   Rewrites each domain dictionary in place.

import sys
import collections


def load_full(path):
    """word -> set of parts of speech, from the general lexicon."""
    pos = collections.defaultdict(set)
    with open(path, encoding='utf-8', errors='replace') as fh:
        for line in fh:
            if not line.strip() or line.startswith('#'):
                continue
            parts = line.split()
            for a in parts[1:]:
                if a.startswith('pos='):
                    pos[parts[0].lower()].add(a[4:])
    return pos


def entry_word(parts):
    """The headword, which may be several tokens ("american samoa")."""
    head = []
    for tok in parts:
        if '=' in tok:
            break
        head.append(tok)
    return ' '.join(head) if head else parts[0]


def roles_from_attrs(attrs):
    """What the file itself says the entry is, where it says so."""
    out = []
    if attrs.get('adj') == '1':
        out.append('adj')
    if attrs.get('noun') == '1' or attrs.get('plural') == '1':
        out.append('noun')
    return out


def process(full, path, dry_run=False):
    added = lines_added = already = 0
    out = []
    with open(path, encoding='utf-8', errors='replace') as fh:
        for raw in fh:
            line = raw.rstrip('\n').rstrip('\r')
            if not line.strip() or line.startswith('#'):
                out.append(line)
                continue
            parts = line.split()
            attrs = dict(a.split('=', 1) for a in parts if '=' in a)
            if 'pos' in attrs:
                already += 1
                out.append(line)
                continue
            word = entry_word(parts)
            ps = sorted(full.get(word.lower(), ()))
            if not ps:
                ps = roles_from_attrs(attrs) or ['noun']
            out.append(f"{line} pos={ps[0]}")
            for extra in ps[1:]:
                out.append(f"{word} pos={extra}")
                lines_added += 1
            added += 1
    name = path.rsplit('/', 1)[-1].rsplit('\\', 1)[-1]
    print(f"{name:<38} entries given a pos: {added:>5}   "
          f"extra reading lines: {lines_added:>4}   already had one: {already}")
    if not dry_run and added:
        with open(path, 'w', encoding='utf-8', newline='\n') as fh:
            fh.write("\n".join(out) + "\n")
    return added


def main():
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    dry = '--dry-run' in sys.argv
    if len(args) < 2:
        sys.stderr.write("usage: dict_addpos.py <en-full.dict> <domain.dict> [...]\n")
        return 1
    full = load_full(args[0])
    for path in args[1:]:
        process(full, path, dry)
    return 0


if __name__ == '__main__':
    sys.exit(main())
