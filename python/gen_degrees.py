# -*- coding: utf-8 -*-
# DESC: Generate the English academic-degree dictionary and knowledge base.
#
# WHAT IT DOES
#   Emits languages/English/en-degrees.dict and en-degrees.kbb from the single
#   master table T below, so the two files can never drift apart.  Edit T (or
#   LEVELWORDS / AMBIG) and re-run; do not hand-edit the generated files.
#
#   The .dict gets one line per surface form: the abbreviation, every variant
#   abbreviation, the spelled-out name and every variant name.  The .kbb gets
#   three branches under "degrees":
#       degree  - forward lookup, abbreviation -> name, level, field, latin
#       name    - reverse lookup, spelled-out name -> abbreviation
#       level   - level -> its generic words and the degrees that sit there
#   Every .dict line carries "degree=<abbreviation>", so rules join into the
#   knowledge base on that attribute rather than on $text.
#
#   Master table row:
#     (abbrev, name, level, field, latin, [syn abbrevs], [syn names], [flags])
#     level  is associate | bachelor | master | specialist | doctorate
#     flags  may hold "professional" (a practice / first-professional degree),
#            "honorary" (normally conferred honoris causa) and "uk" (chiefly
#            British or Commonwealth usage)
#
#   An abbreviation naming more than one degree (mla, mst) is marked ambig=1
#   and its further readings hang below it as <abbrev>1, <abbrev>2, ... (the
#   same convention en-nationalities.kbb and timezones.kbb use).  A surface
#   form belonging to such a further reading carries sense=<n>, so the concept
#   to look up is <degree><sense>.
#
#   Dotted forms (Ph.D., B.A., M.Sc.) are not listed: the tokenizer splits
#   them into separate tokens.
#
# USAGE
#   python gen_degrees.py [output_dir]
#     output_dir  defaults to ../languages/English relative to this script

import io, os, sys

# abbrev, name, level, field, latin, syn abbrevs, syn names, flags
T = [
 # --- associate ------------------------------------------------------------
 ("aa","associate of arts","associate","arts",None,[],[],[]),
 ("as","associate of science","associate","science",None,[],[],[]),
 ("aas","associate of applied science","associate","applied science",None,[],[],[]),
 ("aaa","associate of applied arts","associate","applied arts",None,[],[],[]),
 ("afa","associate of fine arts","associate","fine arts",None,[],[],[]),
 ("ags","associate of general studies","associate","general studies",None,[],[],[]),
 ("aat","associate of arts in teaching","associate","education",None,[],[],[]),
 ("aba","associate of business administration","associate","business",None,[],[],[]),
 ("adn","associate degree in nursing","associate","nursing",None,[],["associate of nursing"],[]),
 ("asn","associate of science in nursing","associate","nursing",None,[],[],[]),
 ("aos","associate of occupational studies","associate","occupational studies",None,[],[],[]),

 # --- bachelor -------------------------------------------------------------
 ("ba","bachelor of arts","bachelor","arts","artium baccalaureus",["ab"],[],[]),
 ("bs","bachelor of science","bachelor","science","scientiae baccalaureus",["bsc","sb","scb"],[],[]),
 ("bfa","bachelor of fine arts","bachelor","fine arts",None,[],[],[]),
 ("bba","bachelor of business administration","bachelor","business",None,[],[],[]),
 ("bsba","bachelor of science in business administration","bachelor","business",None,[],[],[]),
 ("bas","bachelor of applied science","bachelor","applied science",None,["basc"],[],[]),
 ("barch","bachelor of architecture","bachelor","architecture",None,[],[],[]),
 ("beng","bachelor of engineering","bachelor","engineering",None,["be"],[],[]),
 ("bse","bachelor of science in engineering","bachelor","engineering",None,[],[],[]),
 ("bsee","bachelor of science in electrical engineering","bachelor","engineering",None,[],[],[]),
 ("bsme","bachelor of science in mechanical engineering","bachelor","engineering",None,[],[],[]),
 ("bsce","bachelor of science in civil engineering","bachelor","engineering",None,[],[],[]),
 ("bscs","bachelor of science in computer science","bachelor","computer science",None,[],[],[]),
 ("bcs","bachelor of computer science","bachelor","computer science",None,[],[],[]),
 ("bsit","bachelor of science in information technology","bachelor","information technology",None,[],[],[]),
 ("bsn","bachelor of science in nursing","bachelor","nursing",None,[],[],[]),
 ("bed","bachelor of education","bachelor","education",None,[],[],[]),
 ("bsed","bachelor of science in education","bachelor","education",None,[],[],[]),
 ("bm","bachelor of music","bachelor","music",None,["bmus"],[],[]),
 ("bsw","bachelor of social work","bachelor","social work",None,[],[],[]),
 ("bphil","bachelor of philosophy","bachelor","philosophy",None,[],[],[]),
 ("bla","bachelor of landscape architecture","bachelor","architecture",None,[],[],[]),
 ("bls","bachelor of liberal studies","bachelor","liberal studies",None,[],[],[]),
 ("bgs","bachelor of general studies","bachelor","general studies",None,[],[],[]),
 ("bsa","bachelor of science in agriculture","bachelor","agriculture",None,[],[],[]),
 ("bsj","bachelor of science in journalism","bachelor","journalism",None,[],[],[]),
 ("bj","bachelor of journalism","bachelor","journalism",None,[],[],[]),
 ("bsph","bachelor of science in public health","bachelor","public health",None,[],[],[]),
 ("bd","bachelor of divinity","bachelor","theology",None,[],[],[]),
 ("bth","bachelor of theology","bachelor","theology",None,[],[],[]),
 ("bpharm","bachelor of pharmacy","bachelor","pharmacy",None,[],[],["uk"]),
 ("btech","bachelor of technology","bachelor","technology",None,[],[],["uk"]),
 ("bcom","bachelor of commerce","bachelor","business",None,["bcomm"],[],["uk"]),
 ("llb","bachelor of laws","bachelor","law","legum baccalaureus",[],[],["uk"]),
 ("mbbs","bachelor of medicine and bachelor of surgery","bachelor","medicine",None,["bmbs","mbchb"],["bachelor of medicine and surgery"],["uk","professional"]),
 ("bvsc","bachelor of veterinary science","bachelor","veterinary medicine",None,["bvms"],[],["uk","professional"]),

 # --- master ---------------------------------------------------------------
 ("ma","master of arts","master","arts","artium magister",["am"],[],[]),
 ("ms","master of science","master","science","scientiae magister",["msc","sm","scm"],[],[]),
 ("mba","master of business administration","master","business",None,[],[],[]),
 ("mfa","master of fine arts","master","fine arts",None,[],[],[]),
 ("med","master of education","master","education",None,[],[],[]),
 ("msed","master of science in education","master","education",None,[],[],[]),
 ("mat","master of arts in teaching","master","education",None,[],[],[]),
 ("mst","master of science in teaching","master","education",None,[],[],[]),
 ("mst","master of studies","master","general studies",None,[],[],["uk"]),
 ("meng","master of engineering","master","engineering",None,["me"],[],[]),
 ("march","master of architecture","master","architecture",None,[],[],[]),
 ("mla","master of landscape architecture","master","architecture",None,[],[],[]),
 ("mla","master of liberal arts","master","liberal studies",None,[],[],[]),
 ("mpa","master of public administration","master","public affairs",None,[],[],[]),
 ("mpp","master of public policy","master","public affairs",None,[],[],[]),
 ("mph","master of public health","master","public health",None,[],[],[]),
 ("msph","master of science in public health","master","public health",None,[],[],[]),
 ("msw","master of social work","master","social work",None,[],[],[]),
 ("msn","master of science in nursing","master","nursing",None,[],[],[]),
 ("mls","master of library science","master","library science",None,[],[],[]),
 ("mlis","master of library and information science","master","library science",None,[],[],[]),
 ("mm","master of music","master","music",None,["mmus"],[],[]),
 ("mdiv","master of divinity","master","theology",None,[],[],["professional"]),
 ("mth","master of theology","master","theology",None,["thm"],[],[]),
 ("llm","master of laws","master","law","legum magister",[],[],[]),
 ("macc","master of accountancy","master","accounting",None,["macct"],["master of accounting"],[]),
 ("msa","master of science in accounting","master","accounting",None,[],[],[]),
 ("msf","master of science in finance","master","finance",None,[],[],[]),
 ("mtax","master of taxation","master","accounting",None,[],[],[]),
 ("mha","master of health administration","master","health administration",None,[],[],[]),
 ("mphil","master of philosophy","master","philosophy",None,[],[],[]),
 ("mres","master of research","master","research",None,[],[],["uk"]),
 ("mcs","master of computer science","master","computer science",None,[],[],[]),
 ("mscs","master of science in computer science","master","computer science",None,[],[],[]),
 ("msee","master of science in electrical engineering","master","engineering",None,[],[],[]),
 ("msme","master of science in mechanical engineering","master","engineering",None,[],[],[]),
 ("msce","master of science in civil engineering","master","engineering",None,[],[],[]),
 ("msis","master of science in information systems","master","information systems",None,[],[],[]),
 ("mup","master of urban planning","master","urban planning",None,[],[],[]),
 ("mcp","master of city planning","master","urban planning",None,[],[],[]),
 ("mps","master of professional studies","master","professional studies",None,[],[],[]),
 ("mia","master of international affairs","master","international affairs",None,[],[],[]),
 ("msm","master of science in management","master","management",None,[],[],[]),
 ("mem","master of engineering management","master","engineering management",None,[],[],[]),
 ("mpt","master of physical therapy","master","physical therapy",None,[],[],["professional"]),
 ("mot","master of occupational therapy","master","occupational therapy",None,[],[],["professional"]),
 ("mpas","master of physician assistant studies","master","physician assistant studies",None,[],[],["professional"]),

 # --- specialist -----------------------------------------------------------
 ("eds","education specialist","specialist","education",None,[],["specialist in education"],[]),

 # --- doctorate ------------------------------------------------------------
 ("phd","doctor of philosophy","doctorate","philosophy","philosophiae doctor",["dphil"],[],[]),
 ("edd","doctor of education","doctorate","education",None,[],[],[]),
 ("dba","doctor of business administration","doctorate","business",None,[],[],[]),
 ("scd","doctor of science","doctorate","science","scientiae doctor",["dsc"],[],[]),
 ("da","doctor of arts","doctorate","arts",None,[],[],[]),
 ("dma","doctor of musical arts","doctorate","music",None,[],[],[]),
 ("thd","doctor of theology","doctorate","theology","theologiae doctor",["dth"],[],[]),
 ("dmin","doctor of ministry","doctorate","theology",None,[],[],["professional"]),
 ("dpa","doctor of public administration","doctorate","public affairs",None,[],[],[]),
 ("drph","doctor of public health","doctorate","public health",None,["dph"],[],[]),
 ("deng","doctor of engineering","doctorate","engineering",None,["engd"],[],[]),
 ("dsw","doctor of social work","doctorate","social work",None,[],[],[]),
 ("littd","doctor of letters","doctorate","letters","litterarum doctor",["dlitt"],[],[]),
 ("sjd","doctor of juridical science","doctorate","law","scientiae juridicae doctor",["jsd"],[],[]),

 # --- doctorate, professional practice -------------------------------------
 ("md","doctor of medicine","doctorate","medicine","medicinae doctor",[],[],["professional"]),
 ("do","doctor of osteopathic medicine","doctorate","medicine",None,[],["doctor of osteopathy"],["professional"]),
 ("jd","juris doctor","doctorate","law","juris doctor",[],["doctor of jurisprudence"],["professional"]),
 ("dds","doctor of dental surgery","doctorate","dentistry",None,[],[],["professional"]),
 ("dmd","doctor of dental medicine","doctorate","dentistry","dentariae medicinae doctor",[],[],["professional"]),
 ("dvm","doctor of veterinary medicine","doctorate","veterinary medicine",None,["vmd"],[],["professional"]),
 ("od","doctor of optometry","doctorate","optometry",None,[],[],["professional"]),
 ("dpm","doctor of podiatric medicine","doctorate","podiatry",None,[],[],["professional"]),
 ("pharmd","doctor of pharmacy","doctorate","pharmacy",None,[],[],["professional"]),
 ("dc","doctor of chiropractic","doctorate","chiropractic",None,[],[],["professional"]),
 ("dpt","doctor of physical therapy","doctorate","physical therapy",None,[],[],["professional"]),
 ("otd","doctor of occupational therapy","doctorate","occupational therapy",None,[],[],["professional"]),
 ("aud","doctor of audiology","doctorate","audiology",None,[],[],["professional"]),
 ("dnp","doctor of nursing practice","doctorate","nursing",None,[],[],["professional"]),
 ("psyd","doctor of psychology","doctorate","psychology",None,[],[],["professional"]),

 # --- doctorate, normally honorary -----------------------------------------
 ("lld","doctor of laws","doctorate","law","legum doctor",[],[],["honorary"]),
 ("dd","doctor of divinity","doctorate","theology","divinitatis doctor",[],[],["honorary"]),
 ("dhl","doctor of humane letters","doctorate","letters","doctor humanitatum",["lhd"],[],["honorary"]),
 ("dfa","doctor of fine arts","doctorate","fine arts",None,[],[],["honorary"]),
]

# Generic words for a level of study.  These name a level, not one degree, so
# they carry level= and levelword=1 but no degree=.
# form, level, plural
LEVELWORDS = [
 ("associate","associate",0),
 ("associates","associate",1),
 ("bachelor","bachelor",0),
 ("bachelors","bachelor",1),
 ("baccalaureate","bachelor",0),
 ("master","master",0),
 ("masters","master",1),
 ("doctorate","doctorate",0),
 ("doctorates","doctorate",1),
 ("doctoral","doctorate",0),
]

LEVEL_ORDER = ["associate","bachelor","master","specialist","doctorate"]

# Forms that are also an ordinary English word (en-full.dict), a USPS state
# code (en-usa-states.dict) or a courtesy title (en-name-pre-suffix.dict).
AMBIG = set("aa aas ab aba as ma am me ms md mm mph mat march mem mot med bed be bas do dc".split())

# Forms en-name-pre-suffix.dict also carries as a post-nominal name suffix.
SUFFIX = set("phd md do jd dds dmd dvm edd psyd mba".split())

# Ordinary words that the generic level words collide with.
LEVELWORD_AMBIG = set("associate associates bachelor bachelors master masters doctoral".split())

HDR_DICT = """\
# Academic degrees in English: abbreviations and spelled-out names.
# One line per surface form.
#   degree=       the canonical abbreviation -- on every degree entry, so
#                 rules join into en-degrees.kbb on this, not on $text
#   abbrev=1      the form is an abbreviation      spelled=1  the spelled name
#   syn=1         a variant abbreviation or an alternate name of the degree
#   level=        associate | bachelor | master | specialist | doctorate
#   field=        broad subject area
#   professional=1  a practice (first-professional) degree
#   honorary=1    normally conferred honoris causa
#   uk=1          chiefly British or Commonwealth usage
#   suffix=1      also listed in en-name-pre-suffix.dict as a name suffix
#   ambig=1       the form is also an ordinary English word, a USPS state code
#                 or a courtesy title (see en-full.dict, en-usa-states.dict,
#                 en-name-pre-suffix.dict)
#   sense=n       the form belongs to the nth further reading of an ambiguous
#                 abbreviation; the kbb concept is <degree><n> (mla1, mst1)
#   levelword=1   a generic word for a level of study (bachelor, masters,
#                 doctorate), which names a level and not a single degree and
#                 so carries no degree=
# Dotted forms (Ph.D., B.A., M.Sc.) are not listed: the tokenizer splits them
# into separate tokens.
"""

HDR_KBB = """\
# Academic degrees in English, related to their names, levels and fields.
# Forward lookup:  abbreviation -> name  (concept "degrees degree phd" -> name="doctor of philosophy")
# Reverse lookup:  name -> abbreviation  (concept "degrees name doctor of philosophy" -> abbrev=phd)
# Level lookup:    level -> its generic words and its degrees
#   level=        associate | bachelor | master | specialist | doctorate
#   field=        broad subject area
#   latin=        the Latin name the abbreviation actually spells, where the
#                 abbreviation is Latin rather than English
#   synonym=      variant abbreviations       altname=  alternate spelled names
#   professional=1  a practice (first-professional) degree
#   honorary=1    normally conferred honoris causa
#   uk=1          chiefly British or Commonwealth usage
#   suffix=1      also listed in en-name-pre-suffix.dict as a name suffix
# An abbreviation naming more than one degree is marked ambig=1 and its
# further readings hang below it as <abbrev>1, <abbrev>2, ... (same convention
# as en-nationalities.kbb).
# Every form named here is tagged by en-degrees.dict.
"""


def q(s):
    """Quote a value for a .dict / .kbb attribute when it is not a bare token."""
    if s and all(c.isalnum() or c in "_-." for c in s):
        return s
    return '"' + s.replace('"', '\\"') + '"'


def build():
    """form -> {recs, flags, sense} over every surface form in T."""
    forms = {}

    def add(form, flags, rec, sense):
        e = forms.setdefault(form, {"recs": [], "flags": set(), "sense": sense})
        if rec not in e["recs"]:
            e["recs"].append(rec)
        e["flags"].update(flags)

    order = {}
    for rec in T:
        order.setdefault(rec[0], []).append(rec)

    for rec in T:
        abbrev, name, level, field, latin, syns, altnames, flags = rec
        sense = order[abbrev].index(rec)
        add(abbrev, ["abbrev"], rec, 0)     # the abbreviation itself is always
        for s in syns:                       # the base concept
            add(s, ["abbrev", "syn"], rec, sense)
        add(name, ["spelled"], rec, sense)
        for n in altnames:
            add(n, ["spelled", "syn"], rec, sense)

    return forms


def write_dict(forms, path):
    out = io.StringIO()
    out.write(HDR_DICT)
    lines = []
    for form in forms:
        e = forms[form]
        rec = e["recs"][0]
        abbrev, name, level, field, latin, syns, altnames, flags = rec
        attrs = []
        for f in ("abbrev", "spelled", "syn"):
            if f in e["flags"]:
                attrs.append(f + "=1")
        attrs.append("degree=" + abbrev)
        if e["sense"]:
            attrs.append("sense=%d" % e["sense"])
        attrs.append("level=" + level)
        attrs.append("field=" + q(field))
        for f in ("professional", "honorary", "uk"):
            if f in flags:
                attrs.append(f + "=1")
        if form in SUFFIX:
            attrs.append("suffix=1")
        if form in AMBIG or len(e["recs"]) > 1:
            attrs.append("ambig=1")
        lines.append(form + " " + " ".join(attrs))

    for form, level, plural in LEVELWORDS:
        attrs = ["levelword=1", "level=" + level]
        if plural:
            attrs.append("plural=1")
        if form in LEVELWORD_AMBIG:
            attrs.append("ambig=1")
        lines.append(form + " " + " ".join(attrs))

    for line in sorted(lines):
        out.write(line + "\n")
    save(path, out.getvalue())


def write_kbb(path):
    out = io.StringIO()
    out.write(HDR_KBB)
    out.write("degrees\n")

    by_abbrev = {}
    for rec in T:
        by_abbrev.setdefault(rec[0], []).append(rec)

    # --- forward branch: abbreviation -> degree ------------------------------
    out.write("  degree\n")
    for abbrev in sorted(by_abbrev):
        recs = by_abbrev[abbrev]
        for i, rec in enumerate(recs):
            _, name, level, field, latin, syns, altnames, flags = rec
            concept = abbrev if i == 0 else abbrev + str(i)
            indent = "    " if i == 0 else "      "
            attrs = []
            if i == 0 and len(recs) > 1:
                attrs.append("ambig=1")
            attrs.append("name=" + q(name))
            attrs.append("level=" + level)
            attrs.append("field=" + q(field))
            if latin:
                attrs.append("latin=" + q(latin))
            if len(syns) == 1:
                attrs.append("synonym=" + q(syns[0]))
            elif syns:
                attrs.append("synonym=[" + ",".join(q(s) for s in syns) + "]")
            if len(altnames) == 1:
                attrs.append("altname=" + q(altnames[0]))
            elif altnames:
                attrs.append("altname=[" + ",".join(q(n) for n in altnames) + "]")
            for f in ("professional", "honorary", "uk"):
                if f in flags:
                    attrs.append(f + "=1")
            if abbrev in SUFFIX:
                attrs.append("suffix=1")
            out.write(indent + concept + ": " + ", ".join(attrs) + "\n")

    # --- reverse branch: spelled name -> abbreviation -------------------------
    out.write("  name\n")
    rows = {}
    for rec in T:
        abbrev, name, level, field, latin, syns, altnames, flags = rec
        sense = by_abbrev[abbrev].index(rec)
        for n in [name] + list(altnames):
            if n not in rows:
                rows[n] = (abbrev, sense, level, field, n != name)
    for name in sorted(rows):
        abbrev, sense, level, field, is_alt = rows[name]
        attrs = ["abbrev=" + abbrev]
        if sense:
            attrs.append("sense=%d" % sense)
        attrs.append("level=" + level)
        attrs.append("field=" + q(field))
        if is_alt:
            attrs.append("syn=1")
        out.write("    " + name + ": " + ", ".join(attrs) + "\n")

    # --- level branch: level -> its words and its degrees ---------------------
    out.write("  level\n")
    for level in LEVEL_ORDER:
        words = [w for w, lv, _ in LEVELWORDS if lv == level]
        degs = sorted({r[0] for r in T if r[2] == level})
        attrs = []
        if words:
            attrs.append("word=[" + ",".join(words) + "]")
        attrs.append("degree=[" + ",".join(degs) + "]")
        out.write("    " + level + ": " + ", ".join(attrs) + "\n")

    save(path, out.getvalue())


def save(path, text):
    with open(path, "wb") as f:
        f.write(text.replace("\n", "\r\n").encode("utf-8"))
    print("wrote", path, len(text.splitlines()), "lines")


def report(forms, d):
    """Sanity checks, plus an ambiguity cross-check against the sibling dicts."""
    abbrevs = [r[0] for r in T]
    print("abbreviations with more than one reading:",
          sorted({a for a in abbrevs if abbrevs.count(a) > 1}))
    names = [r[1] for r in T]
    print("duplicate spelled names:",
          sorted({n for n in names if names.count(n) > 1}))
    print("surface forms shared by several degrees:",
          sorted(f for f in forms if len(forms[f]["recs"]) > 1))

    siblings = ["en-full.dict", "en-usa-states.dict", "en-name-pre-suffix.dict",
                "en-countries.dict", "en-nationalities.dict", "en-firstnames.dict"]
    known = set()
    for fn in siblings:
        p = os.path.join(d, fn)
        if not os.path.exists(p):
            continue
        with open(p, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#"):
                    known.add(line.split(" ")[0].lower())
    if known:
        print("forms in a sibling dict but not marked ambig:",
              sorted(f for f in forms
                     if f in known and f not in AMBIG and f not in SUFFIX))
        print("AMBIG entries no sibling dict has:",
              sorted(a for a in AMBIG if a not in known))
    print("degrees:", len(T), " surface forms:", len(forms))


if __name__ == "__main__":
    if len(sys.argv) > 1:
        d = sys.argv[1]
    else:
        here = os.path.dirname(os.path.abspath(__file__))
        d = os.path.join(here, os.pardir, "languages", "English")
    d = os.path.normpath(d)
    forms = build()
    write_dict(forms, os.path.join(d, "en-degrees.dict"))
    write_kbb(os.path.join(d, "en-degrees.kbb"))
    report(forms, d)
