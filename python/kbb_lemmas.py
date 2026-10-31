# DESC: Build en-lemmas-full.kbb (inflected form -> root) from en-full.kbb.
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
#   AMBIGUITY.  Of ~79k inflected forms only ~90 have more than one possible
#   root ("axes" <- ax / axe, "calves" <- calf / calve).  Those keep a default
#   root= on the parent so the flat one-hop lookup still answers everywhere,
#   and add m01/m02 children carrying pos= for a caller that can be exact.
#
#   THE DEFAULT IS THE FIRST READING'S ROOT, which in en-full.kbb is usually
#   the NOUN -- "calves: root=calf", not "calve".  A caller that knows it is
#   holding a verb must therefore scan the children for pos=verb before
#   falling back to the parent.  Measured over the 30,648 verb forms, taking
#   the parent's root= blindly gets 88 of them wrong ("attaches" -> attache).
#   It was 172 before kbb_rootfix.py corrected roots that belonged to a
#   different word ("cares" -> car); most multi-root forms were that error.
#
#   A word that is its own root gets no entry; the caller falls back to the
#   surface form, which is already correct.
#
#   OTHER LANGUAGES.  The language is taken from the output file's prefix.
#   pt-full.kbb (and es-full.kbb) carry the lemma as raiz= rather than root=
#   and separate attributes with ", ", so the key and the top concept
#   (lemas) come from LANGS below; the table shape is the same.
#
# USAGE
#   python kbb_lemmas.py <en-full.kbb> <en-lemmas-full.kbb>
#   python kbb_lemmas.py <pt-full.kbb> <pt-lemmas-full.kbb>
#   python kbb_lemmas.py <es-full.kbb> <es-lemmas-full.kbb>

import os
import sys
from collections import OrderedDict

HEADER_EN = """\
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
# Only ~90 of ~79k forms have more than one possible root. Those keep a
# root= on the parent, so a caller that does not know the part of speech
# still gets one answer in one hop, and add m01/m02 children so one that
# does can be exact -- scan them for the pos you are holding, and fall
# back to the parent's root= when none matches.
#
# Regenerate with:
#   python kbb_lemmas.py en-full.kbb en-lemmas-full.kbb
"""

HEADER_PT = """# Formas flexionadas do português com a sua raiz (lema).
# Gerado a partir de pt-full.kbb por python/kbb_lemmas.py: a forma
# flexionada é o conceito e raiz= é o lema -- para análise, não geração.
#
#   lemas
#     gatos: raiz=gato
#     pelo: raiz=pelo             <- a primeira leitura (prep: por+o)
#       m01: pos=prep raiz=pelo
#       m02: pos=v raiz=pelar
#
# Uma forma com mais de uma raiz possível guarda a raiz= da primeira
# leitura no pai, para quem não sabe a classe gramatical ter uma resposta
# num só passo, e acrescenta filhos m01/m02 com pos= para quem sabe ser
# exato: procure o pos= que tem em mãos e, se nenhum servir, use a raiz=
# do pai.  pos= usa as abreviações de pt-full.kbb
# (s adj v adv art pron prep conj int num).
#
# Ao contrário de en-lemmas-full.kbb, uma leitura que é a sua própria raiz
# (raiz=pelo para a contração por+o) aparece entre os filhos quando a
# forma tem também outra raiz -- senão "pelo" e "pelas" responderiam pelar.
# Uma forma que só é a sua própria raiz não tem entrada: use a forma.
#
# Regenerar com:
#   python kbb_lemmas.py pt-full.kbb pt-lemmas-full.kbb
"""

HEADER_ES = """# Formas flexionadas del español con su raíz (lema).
# Generado a partir de es-full.kbb por python/kbb_lemmas.py: la forma
# flexionada es el concepto y raiz= es el lema -- para análisis, no
# generación.
#
#   lemas
#     gatos: raiz=gato
#     fue: raiz=ir                <- la primera lectura
#       m01: pos=v raiz=ir
#       m02: pos=v raiz=ser
#
# Una forma con más de una raíz posible guarda la raiz= de la primera
# lectura en el padre, para que quien no sabe la categoría gramatical
# obtenga una respuesta en un solo paso, y añade hijos m01/m02 con pos=
# para que quien la sabe sea exacto: busque el pos= que tiene y, si
# ninguno sirve, use la raiz= del padre.  pos= usa las abreviaturas de
# es-full.kbb (s adj v adv art pron prep conj int num).
#
# A diferencia de en-lemmas-full.kbb, una lectura que es su propia raíz aparece
# entre los hijos cuando la forma tiene también otra raíz.  Una forma que
# solo es su propia raíz no tiene entrada: use la forma.
#
# Regenerar con:
#   python kbb_lemmas.py es-full.kbb es-lemmas-full.kbb
"""

# output prefix -> (header, top concept, lemma attribute, keep self readings)
LANGS = {
    "en": (HEADER_EN, "lemmas", "root", False),
    "pt": (HEADER_PT, "lemas", "raiz", True),
    "es": (HEADER_ES, "lemas", "raiz", True),
}


def parse_reading(rest, root_key):
    # rest = "pos=verb root=go vform=past tense=past"  ->  (pos, root)
    # or     "pos=v, raiz=ir, pes=3, num=s, tem=pps"
    pos = root = None
    for tok in rest.split():
        k, _, v = tok.rstrip(",").partition("=")
        if k == "pos":
            pos = v
        elif k == root_key:
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
        sys.stderr.write("usage: kbb_lemmas.py <en-full.kbb> <en-lemmas-full.kbb>\n")
        return 1
    inpath, outpath = argv[0], argv[1]
    prefix = os.path.basename(outpath).split("-")[0]
    header, top, root_key, keep_self = LANGS.get(prefix, LANGS["en"])

    # surface form -> OrderedDict((pos, root) -> None), in reading order
    lemmas = OrderedDict()
    selfread = {}
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
                pos, root = parse_reading(rest.strip(), root_key)
                # an uninflected reading is its own root and needs no entry,
                # unless keep_self holds it until the form proves to have
                # another root too (dropped again below if it does not)
                if not root or root == word:
                    if keep_self:
                        selfread.setdefault(word, OrderedDict())[(pos, word)] = None
                    continue
                n_readings += 1
                lemmas.setdefault(word, OrderedDict())[(pos, root)] = None

    # pt/es: put the self readings back, in reading (pos) order
    for word in lemmas:
        if word in selfread:
            merged = list(selfread[word]) + list(lemmas[word])
            merged.sort(key=lambda r: r[0] or "")
            lemmas[word] = OrderedDict((r, None) for r in merged)

    n_ambiguous = 0
    with open(outpath, "w", encoding="utf-8", newline="\n") as out:
        out.write(header)
        out.write(top + "\n")
        for word in sorted(lemmas):
            readings = list(lemmas[word])
            roots = []
            for _, root in readings:
                if root not in roots:
                    roots.append(root)
            # the first reading's root is the default, so a caller that does
            # not care about part of speech still gets one answer, one hop
            out.write(concept_line(2, word, [(root_key, roots[0])]))
            if len(roots) > 1:
                n_ambiguous += 1
                for i, (pos, root) in enumerate(readings, start=1):
                    attrs = [(root_key, root)]
                    if pos:
                        attrs.insert(0, ("pos", pos))
                    out.write(concept_line(4, "m%02d" % i, attrs))

    sys.stderr.write("[kbb_lemmas: %d inflected forms, %d readings, "
                     "%d forms with more than one root -> %s]\n"
                     % (len(lemmas), n_readings, n_ambiguous, outpath))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
