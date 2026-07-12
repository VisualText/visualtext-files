# DESC: Build a flat KBB knowledge-base file from a value-bearing .dict file.
#
# WHAT IT DOES
#   Reads a VisualText .dict file whose lines have the shape
#       <word> attr=value attr=value ...
#   (the <word> may be several tokens, e.g. "american samoa") and emits a KBB
#   file with one concept per word, keyed by the word, carrying the same
#   attr=value pairs.  This is the forward "word -> attributes" lookup table
#   that analyzers load into the KB (same shape as en-languages.kbb).
#
#   Comment (#) and blank lines are skipped.  Duplicate word keys are emitted
#   once (first reading wins) and reported to stderr.
#
# USAGE
#   python dict2kbb.py <input.dict> <output.kbb> <tablename> [--drop attr[,attr]]
#     <tablename>   root concept name that holds the entries
#     --drop        comma-separated attrs to omit (e.g. a bare membership flag
#                   like country=1 that carries no lookup value)
#
#   Example:
#     python dict2kbb.py en-countries.dict en-countries.kbb countries --drop country

import sys


def split_tokens(line):
    # whitespace split but keep double-quoted values together
    toks, buf, inq = [], [], False
    for ch in line:
        if ch == '"':
            inq = not inq
            buf.append(ch)
        elif ch.isspace() and not inq:
            if buf:
                toks.append("".join(buf))
                buf = []
        else:
            buf.append(ch)
    if buf:
        toks.append("".join(buf))
    return toks


def is_simple_token(s):
    return len(s) > 0 and all(c.isalnum() or c in "_-." for c in s)


def format_value(v):
    v = v.strip()
    if len(v) >= 2 and v[0] == '"' and v[-1] == '"':
        v = v[1:-1]  # already quoted in the dict; re-quote consistently below
    if is_simple_token(v):
        return v
    return '"' + v.replace("\\", "\\\\").replace('"', '\\"') + '"'


def parse_line(line):
    toks = split_tokens(line)
    key_parts, attrs, i = [], [], 0
    # word = leading tokens up to the first "attr=value" token
    while i < len(toks) and "=" not in toks[i]:
        key_parts.append(toks[i])
        i += 1
    for tok in toks[i:]:
        if "=" not in tok:
            continue
        k, _, val = tok.partition("=")
        attrs.append((k, val))
    return " ".join(key_parts), attrs


def main(argv):
    if len(argv) < 3:
        sys.stderr.write("usage: dict2kbb.py <in.dict> <out.kbb> <tablename> "
                         "[--drop attr,attr]\n")
        return 1
    inpath, outpath, table = argv[0], argv[1], argv[2]
    drop = set()
    if "--drop" in argv:
        drop = set(argv[argv.index("--drop") + 1].split(","))

    header = None
    rows, seen = [], set()
    with open(inpath, "r", encoding="utf-8") as f:
        for raw in f:
            line = raw.rstrip("\n")
            stripped = line.strip()
            if not stripped:
                continue
            if stripped.startswith("#"):
                if header is None:
                    header = stripped
                continue
            key, attrs = parse_line(stripped)
            if not key:
                continue
            if key in seen:
                sys.stderr.write("[dict2kbb: duplicate key '%s' skipped]\n" % key)
                continue
            seen.add(key)
            attrs = [(k, v) for k, v in attrs if k not in drop]
            rows.append((key, attrs))

    with open(outpath, "w", encoding="utf-8") as out:
        if header:
            out.write(header + "\n")
        out.write(table + "\n")
        for key, attrs in rows:
            line = "  " + key + ":"
            if attrs:
                line += " " + ", ".join(k + "=" + format_value(v) for k, v in attrs)
            out.write(line + "\n")

    sys.stderr.write("[dict2kbb: wrote %d concepts to %s]\n" % (len(rows), outpath))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
