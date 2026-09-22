# DESC: Build en-full.dict, the part-of-speech dictionary, from the featured
#       dictionary it is a projection of.
#
# WHY
#   en-full-feat.dict is the source of truth: one line per grammatical reading,
#   carrying the root and the verb/noun features.  en-full.dict is what an
#   analyzer actually loads, and it wants one line per (word, part of speech) --
#   the morphology would only slow the lookup down and change what every rule
#   sees.  The relationship between them was true but unenforced: nothing
#   regenerated the smaller file, so an entry added to one could go missing
#   from the other.  This makes the projection a command.
#
#       en-full-feat.dict   aahed pos=verb root=aah vform=past tense=past
#                           aahed pos=verb root=aah vform=pastpart
#       en-full.dict        aahed pos=verb
#
#   Readings that differ only in morphology collapse to one line, in the order
#   the featured file first mentions them, which is how the shipped file is
#   ordered.  Run against an unmodified featured dictionary this reproduces
#   the shipped en-full.dict byte for byte, so a diff of the rebuilt file shows
#   only what actually changed -- the same guarantee kbb_rootfix.py gives for
#   en-full.kbb.
#
# CARRIED ATTRIBUTES
#   pos= always, and freq_<pos>= where dict_freq.py has put one there, because
#   an analyzer choosing between a word's readings needs the counts on the node.
#   Everything else -- root, vform, tense, person, number -- stays behind in
#   the featured file and in en-full.kbb.
#
# USAGE
#   python dict_project.py <en-full-feat.dict> <en-full.dict>
#     --check   rebuild and compare against the existing file, write nothing

import sys


HEADER = "# Full English Dictionary POS"


def project(src):
    lines = [HEADER]
    seen = set()
    with open(src, encoding='utf-8', errors='replace') as fh:
        for raw in fh:
            line = raw.rstrip('\n').rstrip('\r')
            if not line.strip() or line.startswith('#'):
                continue
            parts = line.split()
            word = parts[0]
            pos = freq = None
            for a in parts[1:]:
                if a.startswith('pos='):
                    pos = a[4:]
                elif a.startswith('freq_'):
                    freq = a
            if not pos:
                continue
            key = (word, pos)
            if key in seen:
                continue
            seen.add(key)
            out = f"{word} pos={pos}"
            if freq:
                out += f" {freq}"
            lines.append(out)
    return lines


def main():
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    check = '--check' in sys.argv
    if len(args) < 2:
        sys.stderr.write("usage: dict_project.py <en-full-feat.dict> <en-full.dict>\n")
        return 1
    src, dst = args

    lines = project(src)
    sys.stderr.write(f"projected readings: {len(lines) - 1}\n")

    if check:
        try:
            old = open(dst, encoding='utf-8', errors='replace').read().splitlines()
        except FileNotFoundError:
            sys.stderr.write(f"{dst} does not exist\n")
            return 1
        if old == lines:
            sys.stderr.write("identical to the existing file\n")
            return 0
        sys.stderr.write(f"DIFFERS: {len(old)} existing lines, {len(lines)} rebuilt\n")
        shown = 0
        for i, (a, b) in enumerate(zip(old, lines)):
            if a != b and shown < 10:
                sys.stderr.write(f"  line {i + 1}:\n    old: {a}\n    new: {b}\n")
                shown += 1
        return 1

    with open(dst, 'w', encoding='utf-8', newline='\n') as fh:
        fh.write("\n".join(lines) + "\n")
    sys.stderr.write(f"wrote {dst}\n")
    return 0


if __name__ == '__main__':
    sys.exit(main())
