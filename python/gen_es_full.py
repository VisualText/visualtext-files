# DESC: Build es-full.dict and es-full.kbb from FreeLing's Spanish dictionary.
#
# WHAT IT DOES
#   Reads FreeLing's data/es/dictionary/entries/MM.* files (one line per
#   reading: "form lemma EAGLES-tag") and writes the two lazy-loaded Spanish
#   full dictionaries, in the same shape as pt-full.dict / pt-full.kbb so a
#   pass written for one Romance language reads the other:
#
#     es-full.dict   one line per distinct (form, pos):    casa pos=s
#     es-full.kbb    one 2-space concept per form, one m## reading per
#                    distinct analysis:
#
#       dictionary
#         casa:
#           m01: pos=s, gen=f, num=s
#           m02: pos=v, raiz=casar, pes=2, num=s, tem=ia
#           m03: pos=v, raiz=casar, pes=3, num=s, tem=p
#
#   pos=   s adj v adv art pron prep conj int   (pt-full.kbb abbreviations)
#   raiz=  the lemma, only when it differs from the form
#   inf=1  the infinitive (its own lemma, so no raiz=)
#   gen=   m f c (comun)        num=  s p      pes=  1 2 3
#   tem=   p   presente de indicativo        pi  preterito imperfecto
#          pp  preterito perfecto simple     fps futuro simple
#          fpt condicional                    ps  presente de subjuntivo
#          pis preterito imperfecto de subj.  fs  futuro de subjuntivo
#          ia  imperativo   ger gerundio   part participio
#   The tem= codes are pt-full.kbb's (fpt = futuro do preterito = condicional).
#
#   Contractions al / del (SP+DA) are pos=prep carrying the article's gen= and
#   num=, as das / pela are in pt-full.  Punctuation (F*) is skipped.
#   FreeLing's Spanish dictionary has no numerals -- its number module handles
#   them -- so es-full has no pos=num; see es-numeros.dict.
#
# SORT ORDER IS CRITICAL.  The engine lazy-loads *full.dict / *full.kbb by
#   binary search and checks the order with strcmp, so both files are sorted in
#   byte (code point) order: Python's default sorted(), never lower() or an
#   accent-folding key.  Accented initials (a with acute, n with tilde ...)
#   therefore sort after z, and uppercase before lowercase.  That is correct.
#
# LICENSE.  FreeLing's data is AGPL (Universitat Politecnica de Catalunya);
#   the generated files are derived from it.
#
# USAGE
#   git clone --depth 1 --filter=blob:none --sparse \
#       https://github.com/TALP-UPC/FreeLing.git fl
#   git -C fl sparse-checkout set data/es/dictionary
#   python gen_es_full.py fl/data/es/dictionary/entries ../languages/Spanish

import os
import sys

FILES = ["MM.nom", "MM.adj", "MM.adv", "MM.verb", "MM.vaux", "MM.int", "MM.tanc"]

MOOD_TENSE = {
    "IP": "p", "II": "pi", "IS": "pp", "IF": "fps", "IC": "fpt",
    "SP": "ps", "SI": "pis", "SF": "fs",
}
GEN = {"M": "m", "F": "f", "C": "c"}
NUM = {"S": "s", "P": "p"}
ARTICLE = {"el": ("M", "S"), "la": ("F", "S"), "los": ("M", "P"), "las": ("F", "P")}


def gn(attrs, g, n):
    if g in GEN:
        attrs.append(("gen", GEN[g]))
    if n in NUM:
        attrs.append(("num", NUM[n]))


def analyse(form, lemma, tag):
    # -> (pos, [(attr, value), ...]) or None to skip the reading
    raiz = [("raiz", lemma)] if lemma != form else []
    t = tag + "0000000"
    c = tag[0]
    if "+" in tag:
        first, second = tag.split("+", 1)
        if first != "SP":
            return None
        # FreeLing tags al / del as a bare "SP+DA"; the article is the
        # lemma's second half ("a+el"), so take gen/num from that
        attrs = []
        if second == "DA" and lemma.split("+")[-1] in ARTICLE:
            gn(attrs, *ARTICLE[lemma.split("+")[-1]])
        return "prep", attrs
    if c == "N":
        attrs = list(raiz)
        gn(attrs, t[2], t[3])
        return "s", attrs
    if c == "A":
        attrs = list(raiz)
        gn(attrs, t[3], t[4])
        return "adj", attrs
    if c == "R":
        return "adv", list(raiz)
    if c == "C":
        return "conj", []
    if c == "I":
        return "int", list(raiz)
    if c == "S":
        return "prep", []
    if c == "D":
        attrs = list(raiz)
        gn(attrs, t[3], t[4])
        return ("art" if tag.startswith("DA") else "pron"), attrs
    if c == "P":
        attrs = list(raiz)
        gn(attrs, t[3], t[4])
        return "pron", attrs
    if c == "V":
        mood, tense = t[2], t[3]
        if mood == "N":
            return "v", ([("inf", "1")] if lemma == form else raiz)
        if mood == "G":
            return "v", raiz + [("tem", "ger")]
        if mood == "P":
            attrs = list(raiz)
            if t[5] in NUM:
                attrs.append(("num", NUM[t[5]]))
            if t[6] in GEN:
                attrs.append(("gen", GEN[t[6]]))
            return "v", attrs + [("tem", "part")]
        if mood == "M":
            tem = "ia"
        else:
            tem = MOOD_TENSE.get(mood + tense)
            if not tem:
                return None
        attrs = list(raiz)
        if t[4] in "123":
            attrs.append(("pes", t[4]))
        if t[5] in NUM:
            attrs.append(("num", NUM[t[5]]))
        return "v", attrs + [("tem", tem)]
    return None                       # F* punctuation, anything unexpected


def main(argv):
    if len(argv) != 2:
        sys.stderr.write("usage: gen_es_full.py <FreeLing es entries dir> <out dir>\n")
        return 1
    src, outdir = argv
    readings = {}                     # form -> set of reading strings
    dict_pos = {}                     # form -> [pos, ...] in first-seen order
    skipped = 0
    for name in FILES:
        with open(os.path.join(src, name), encoding="utf-8") as f:
            for line in f:
                parts = line.split()
                if len(parts) != 3:
                    continue
                form, lemma, tag = parts
                if "_" in form:
                    skipped += 1
                    continue
                res = analyse(form, lemma, tag)
                if res is None:
                    skipped += 1
                    continue
                pos, attrs = res
                text = ", ".join(["pos=" + pos] + [k + "=" + v for k, v in attrs])
                readings.setdefault(form, set()).add(text)
                plist = dict_pos.setdefault(form, [])
                if pos not in plist:
                    plist.append(pos)

    forms = sorted(readings)          # byte / code point order -- see header
    with open(os.path.join(outdir, "es-full.dict"), "w", encoding="utf-8", newline="\r\n") as out:
        out.write("# Diccionario español completo\n")
        for form in forms:
            for pos in dict_pos[form]:
                out.write("%s pos=%s\n" % (form, pos))

    n_read = 0
    with open(os.path.join(outdir, "es-full.kbb"), "w", encoding="utf-8", newline="\r\n") as out:
        out.write("# Diccionario español completo -- generado por python/gen_es_full.py\n")
        out.write("# a partir del diccionario de FreeLing (AGPL).  Atributos y códigos tem=\n")
        out.write("# como en pt-full.kbb; véase la cabecera de gen_es_full.py.\n")
        out.write("dictionary\n")
        for form in forms:
            out.write("  %s:\n" % form)
            for i, r in enumerate(sorted(readings[form]), start=1):
                out.write("    m%02d: %s\n" % (i, r))
                n_read += 1

    sys.stderr.write("[gen_es_full: %d forms, %d readings, %d dict lines, %d source lines skipped]\n"
                     % (len(forms), n_read, sum(len(p) for p in dict_pos.values()), skipped))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
