# -*- coding: utf-8 -*-
# DESC: Generate the English subject / field-of-study dictionary and knowledge base.
#
# WHAT IT DOES
#   Emits languages/English/en-subjects.dict and en-subjects.kbb from the single
#   master table T below, so the two files can never drift apart.  Edit T and
#   re-run; do not hand-edit the generated files.
#
#   The .dict gets one line per surface form: the subject name, every synonym
#   and every adjective form.  The .kbb gets two branches under "subjects":
#       subject - forward lookup, subject -> area, parent, children, synonyms
#       area    - area -> the subjects that sit in it
#   Every .dict line carries "subject=<canonical name>", so rules join into the
#   knowledge base on that attribute rather than on $text.
#
#   The canonical names are also the vocabulary of field= in en-degrees.dict:
#   report() checks every field= value there against this table and prints any
#   that would not join.
#
#   Master table row:
#     (name, area, parent, [synonyms], [adjectives], [flags])
#     parent  the broader subject this one sits under, or None
#     flags   may hold "school" (a common primary / secondary school subject)
#             and "lang" (the name is also a language, see en-languages.dict)
#
# USAGE
#   python gen_subjects.py [output_dir]
#     output_dir  defaults to ../languages/English relative to this script

import io, os, sys

# name, area, parent, synonyms, adjectives, flags
T = [
 # --- natural science ------------------------------------------------------
 ("science","natural science",None,["sciences"],["scientific"],["school"]),
 ("biology","natural science","science",["bio","life science","biological science"],["biological"],["school"]),
 ("botany","natural science","biology",["plant science","plant biology"],["botanical"],[]),
 ("zoology","natural science","biology",[],["zoological"],[]),
 ("microbiology","natural science","biology",[],["microbiological"],[]),
 ("molecular biology","natural science","biology",[],[],[]),
 ("cell biology","natural science","biology",["cytology"],[],[]),
 ("genetics","natural science","biology",[],["genetic"],[]),
 ("genomics","natural science","genetics",[],["genomic"],[]),
 ("biochemistry","natural science","biology",["biochem"],["biochemical"],[]),
 ("biophysics","natural science","biology",[],["biophysical"],[]),
 ("ecology","natural science","biology",[],["ecological"],[]),
 ("marine biology","natural science","biology",[],[],[]),
 ("neuroscience","natural science","biology",["neurobiology"],["neuroscientific"],[]),
 ("physiology","natural science","biology",[],["physiological"],[]),
 ("anatomy","natural science","biology",[],["anatomical"],[]),
 ("immunology","natural science","biology",[],["immunological"],[]),
 ("virology","natural science","biology",[],[],[]),
 ("bacteriology","natural science","biology",[],[],[]),
 ("mycology","natural science","biology",[],[],[]),
 ("entomology","natural science","biology",[],[],[]),
 ("ornithology","natural science","biology",[],[],[]),
 ("paleontology","natural science","biology",["palaeontology"],[],[]),
 ("evolutionary biology","natural science","biology",[],[],[]),
 ("biotechnology","natural science","biology",["biotech"],[],[]),
 ("chemistry","natural science","science",["chem"],["chemical"],["school"]),
 ("organic chemistry","natural science","chemistry",[],[],[]),
 ("inorganic chemistry","natural science","chemistry",[],[],[]),
 ("physical chemistry","natural science","chemistry",[],[],[]),
 ("analytical chemistry","natural science","chemistry",[],[],[]),
 ("physics","natural science","science",[],[],["school"]),
 ("astrophysics","natural science","physics",[],[],[]),
 ("nuclear physics","natural science","physics",[],[],[]),
 ("particle physics","natural science","physics",["high energy physics"],[],[]),
 ("quantum mechanics","natural science","physics",["quantum physics"],[],[]),
 ("thermodynamics","natural science","physics",[],[],[]),
 ("optics","natural science","physics",[],["optical"],[]),
 ("mechanics","natural science","physics",[],["mechanical"],[]),
 ("astronomy","natural science","science",[],["astronomical"],["school"]),
 ("cosmology","natural science","astronomy",[],["cosmological"],[]),
 ("planetary science","natural science","astronomy",[],[],[]),
 ("earth science","natural science","science",["earth sciences","geoscience","geosciences"],[],["school"]),
 ("geology","natural science","earth science",[],["geological"],[]),
 ("meteorology","natural science","earth science",[],["meteorological"],[]),
 ("oceanography","natural science","earth science",["marine science"],[],[]),
 ("climatology","natural science","earth science",["climate science"],[],[]),
 ("seismology","natural science","earth science",[],[],[]),
 ("hydrology","natural science","earth science",[],[],[]),
 ("soil science","natural science","earth science",[],[],[]),
 ("environmental science","natural science","earth science",["environmental sciences"],["environmental"],["school"]),

 # --- formal science -------------------------------------------------------
 ("mathematics","formal science",None,["math","maths"],["mathematical"],["school"]),
 ("arithmetic","formal science","mathematics",[],[],["school"]),
 ("algebra","formal science","mathematics",[],["algebraic"],["school"]),
 ("geometry","formal science","mathematics",[],["geometric"],["school"]),
 ("trigonometry","formal science","mathematics",["trig"],[],["school"]),
 ("calculus","formal science","mathematics",[],[],["school"]),
 ("statistics","formal science","mathematics",["stats"],["statistical"],["school"]),
 ("probability","formal science","mathematics",[],[],[]),
 ("number theory","formal science","mathematics",[],[],[]),
 ("topology","formal science","mathematics",[],[],[]),
 ("linear algebra","formal science","mathematics",[],[],[]),
 ("discrete mathematics","formal science","mathematics",["discrete math"],[],[]),
 ("applied mathematics","formal science","mathematics",["applied math"],[],[]),
 ("logic","formal science",None,[],["logical"],[]),
 ("computer science","formal science",None,["cs","computing","comp sci"],["computational"],["school"]),
 ("software engineering","formal science","computer science",[],[],[]),
 ("artificial intelligence","formal science","computer science",["ai"],[],[]),
 ("machine learning","formal science","artificial intelligence",[],[],[]),
 ("data science","formal science","computer science",[],[],[]),
 ("cybersecurity","formal science","computer science",["information security","cyber security"],[],[]),
 ("information technology","formal science","computer science",["it"],[],[]),
 ("information systems","formal science","computer science",[],[],[]),
 ("computer graphics","formal science","computer science",[],[],[]),
 ("human-computer interaction","formal science","computer science",[],[],[]),
 ("library science","formal science",None,["information science","library and information science"],[],[]),

 # --- social science -------------------------------------------------------
 ("social studies","social science",None,[],[],["school"]),
 ("history","social science","social studies",[],["historical"],["school"]),
 ("ancient history","social science","history",[],[],[]),
 ("world history","social science","history",[],[],["school"]),
 ("american history","social science","history",["us history"],[],["school"]),
 ("art history","social science","history",[],[],[]),
 ("geography","social science","social studies",[],["geographic","geographical"],["school"]),
 ("human geography","social science","geography",[],[],[]),
 ("physical geography","social science","geography",[],[],[]),
 ("economics","social science","social studies",["econ"],["economic"],["school"]),
 ("microeconomics","social science","economics",[],[],[]),
 ("macroeconomics","social science","economics",[],[],[]),
 ("econometrics","social science","economics",[],[],[]),
 ("political science","social science","social studies",["politics","poli sci","government"],["political"],["school"]),
 ("international relations","social science","political science",["international affairs","international studies"],[],[]),
 ("public policy","social science","political science",[],[],[]),
 ("public administration","social science","political science",["public affairs"],[],[]),
 ("civics","social science","social studies",[],["civic"],["school"]),
 ("sociology","social science",None,[],["sociological"],["school"]),
 ("criminology","social science","sociology",[],[],[]),
 ("demography","social science","sociology",[],["demographic"],[]),
 ("social work","social science","sociology",[],[],[]),
 ("psychology","social science",None,["psych"],["psychological"],["school"]),
 ("clinical psychology","social science","psychology",[],[],[]),
 ("developmental psychology","social science","psychology",[],[],[]),
 ("social psychology","social science","psychology",[],[],[]),
 ("educational psychology","social science","psychology",[],[],[]),
 ("cognitive science","social science","psychology",[],["cognitive"],[]),
 ("anthropology","social science",None,[],["anthropological"],[]),
 ("archaeology","social science","anthropology",["archeology"],["archaeological"],[]),
 ("linguistics","social science",None,[],["linguistic"],[]),
 ("communications","social science",None,["communication","communication studies"],[],[]),
 ("journalism","social science","communications",[],["journalistic"],[]),
 ("public relations","social science","communications",[],[],[]),
 ("media studies","social science","communications",[],[],[]),
 ("urban planning","social science",None,["city planning","urban studies"],[],[]),
 ("gender studies","social science",None,["womens studies"],[],[]),

 # --- humanities -----------------------------------------------------------
 ("humanities","humanities",None,[],[],[]),
 ("english","humanities","humanities",["english language arts","language arts"],[],["school","lang"]),
 ("literature","humanities","english",[],["literary"],["school"]),
 ("poetry","humanities","literature",[],["poetic"],[]),
 ("creative writing","humanities","english",[],[],["school"]),
 ("composition","humanities","english",[],[],["school"]),
 ("rhetoric","humanities","english",[],["rhetorical"],[]),
 ("grammar","humanities","english",[],["grammatical"],["school"]),
 ("spelling","humanities","english",[],[],["school"]),
 ("reading","humanities","english",[],[],["school"]),
 ("philosophy","humanities","humanities",[],["philosophical"],[]),
 ("ethics","humanities","philosophy",[],["ethical"],[]),
 ("metaphysics","humanities","philosophy",[],[],[]),
 ("epistemology","humanities","philosophy",[],[],[]),
 ("classics","humanities","humanities",["classical studies"],["classical"],[]),
 ("latin","humanities","classics",[],[],["school","lang"]),
 ("greek","humanities","classics",[],[],["lang"]),
 ("religious studies","humanities","humanities",["religion"],["religious"],[]),
 ("theology","humanities","religious studies",[],["theological"],[]),
 ("divinity","humanities","religious studies",[],[],[]),
 ("modern languages","humanities","humanities",["foreign languages","world languages"],[],["school"]),
 ("spanish","humanities","modern languages",[],[],["school","lang"]),
 ("french","humanities","modern languages",[],[],["school","lang"]),
 ("german","humanities","modern languages",[],[],["school","lang"]),
 ("italian","humanities","modern languages",[],[],["lang"]),
 ("portuguese","humanities","modern languages",[],[],["lang"]),
 ("russian","humanities","modern languages",[],[],["lang"]),
 ("chinese","humanities","modern languages",["mandarin"],[],["school","lang"]),
 ("japanese","humanities","modern languages",[],[],["school","lang"]),
 ("korean","humanities","modern languages",[],[],["lang"]),
 ("arabic","humanities","modern languages",[],[],["lang"]),
 ("hebrew","humanities","modern languages",[],[],["lang"]),
 ("letters","humanities","humanities",["humane letters"],[],[]),

 # --- arts -----------------------------------------------------------------
 ("art","arts",None,["visual arts","arts"],["artistic"],["school"]),
 ("fine arts","arts","art",[],[],[]),
 ("drawing","arts","art",[],[],["school"]),
 ("painting","arts","art",[],[],["school"]),
 ("sculpture","arts","art",[],[],[]),
 ("photography","arts","art",[],["photographic"],["school"]),
 ("ceramics","arts","art",["pottery"],[],["school"]),
 ("printmaking","arts","art",[],[],[]),
 ("design","arts",None,[],[],[]),
 ("graphic design","arts","design",[],[],[]),
 ("industrial design","arts","design",[],[],[]),
 ("fashion design","arts","design",[],[],[]),
 ("interior design","arts","design",[],[],[]),
 ("architecture","arts",None,[],["architectural"],[]),
 ("landscape architecture","arts","architecture",[],[],[]),
 ("music","arts",None,[],["musical"],["school"]),
 ("music theory","arts","music",[],[],["school"]),
 ("music composition","arts","music",[],[],[]),
 ("theater","arts",None,["theatre","drama","dramatic arts"],["dramatic"],["school"]),
 ("dance","arts",None,[],[],["school"]),
 ("film","arts",None,["film studies","cinema","cinema studies"],[],[]),
 ("performing arts","arts",None,[],[],["school"]),

 # --- engineering ----------------------------------------------------------
 ("engineering","engineering",None,[],[],[]),
 ("civil engineering","engineering","engineering",[],[],[]),
 ("mechanical engineering","engineering","engineering",[],[],[]),
 ("electrical engineering","engineering","engineering",[],[],[]),
 ("chemical engineering","engineering","engineering",[],[],[]),
 ("aerospace engineering","engineering","engineering",["aeronautical engineering"],[],[]),
 ("biomedical engineering","engineering","engineering",["bioengineering"],[],[]),
 ("industrial engineering","engineering","engineering",[],[],[]),
 ("environmental engineering","engineering","engineering",[],[],[]),
 ("nuclear engineering","engineering","engineering",[],[],[]),
 ("petroleum engineering","engineering","engineering",[],[],[]),
 ("structural engineering","engineering","civil engineering",[],[],[]),
 ("systems engineering","engineering","engineering",[],[],[]),
 ("computer engineering","engineering","engineering",[],[],[]),
 ("engineering management","engineering","engineering",[],[],[]),
 ("materials science","engineering","engineering",["materials engineering","material science"],[],[]),
 ("robotics","engineering","engineering",[],[],[]),
 ("technology","engineering",None,["tech"],["technological"],["school"]),
 ("industrial arts","engineering","technology",["shop","woodworking","metalworking"],[],["school"]),
 ("drafting","engineering","technology",["technical drawing"],[],["school"]),

 # --- health ---------------------------------------------------------------
 ("medicine","health",None,[],["medical"],[]),
 ("surgery","health","medicine",[],["surgical"],[]),
 ("pediatrics","health","medicine",["paediatrics"],["pediatric"],[]),
 ("psychiatry","health","medicine",[],["psychiatric"],[]),
 ("cardiology","health","medicine",[],[],[]),
 ("oncology","health","medicine",[],[],[]),
 ("radiology","health","medicine",[],[],[]),
 ("neurology","health","medicine",[],[],[]),
 ("pathology","health","medicine",[],["pathological"],[]),
 ("anesthesiology","health","medicine",["anaesthesiology"],[],[]),
 ("dermatology","health","medicine",[],[],[]),
 ("obstetrics","health","medicine",[],[],[]),
 ("gynecology","health","medicine",["gynaecology"],[],[]),
 ("orthopedics","health","medicine",["orthopaedics"],[],[]),
 ("geriatrics","health","medicine",[],[],[]),
 ("osteopathic medicine","health","medicine",["osteopathy"],[],[]),
 ("nursing","health",None,[],[],[]),
 ("pharmacy","health",None,[],["pharmaceutical"],[]),
 ("dentistry","health",None,[],["dental"],[]),
 ("veterinary medicine","health",None,["veterinary science"],["veterinary"],[]),
 ("optometry","health",None,[],[],[]),
 ("audiology","health",None,[],[],[]),
 ("podiatry","health",None,["podiatric medicine"],["podiatric"],[]),
 ("chiropractic","health",None,[],[],[]),
 ("physical therapy","health",None,["physiotherapy"],[],[]),
 ("occupational therapy","health",None,[],[],[]),
 ("speech pathology","health",None,["speech-language pathology","speech therapy"],[],[]),
 ("public health","health",None,[],[],[]),
 ("epidemiology","health","public health",[],["epidemiological"],[]),
 ("health administration","health","public health",["healthcare administration"],[],[]),
 ("nutrition","health",None,["dietetics"],["nutritional"],["school"]),
 ("kinesiology","health",None,["exercise science"],[],[]),
 ("physical education","health",None,["pe","gym","phys ed"],[],["school"]),
 ("health","health",None,["health education"],[],["school"]),
 ("physician assistant studies","health","medicine",[],[],[]),

 # --- business -------------------------------------------------------------
 ("business","business",None,["business administration","business studies"],[],["school"]),
 ("accounting","business","business",["accountancy"],[],["school"]),
 ("finance","business","business",[],["financial"],[]),
 ("marketing","business","business",[],[],[]),
 ("management","business","business",[],["managerial"],[]),
 ("entrepreneurship","business","business",[],[],[]),
 ("human resources","business","management",["human resource management"],[],[]),
 ("international business","business","business",[],[],[]),
 ("supply chain management","business","management",["logistics"],[],[]),
 ("real estate","business","business",[],[],[]),
 ("hospitality management","business","management",["hotel management"],[],[]),
 ("actuarial science","business","business",[],["actuarial"],[]),
 ("taxation","business","accounting",[],[],[]),

 # --- education ------------------------------------------------------------
 ("education","education",None,[],["educational"],[]),
 ("early childhood education","education","education",[],[],[]),
 ("elementary education","education","education",["primary education"],[],[]),
 ("secondary education","education","education",[],[],[]),
 ("special education","education","education",["sped"],[],[]),
 ("curriculum and instruction","education","education",[],[],[]),
 ("pedagogy","education","education",["teaching"],["pedagogical"],[]),

 # --- law ------------------------------------------------------------------
 ("law","law",None,["legal studies","jurisprudence"],["legal"],[]),
 ("criminal justice","law","law",[],[],["school"]),
 ("international law","law","law",[],[],[]),
 ("constitutional law","law","law",[],[],[]),

 # --- agriculture ----------------------------------------------------------
 ("agriculture","agriculture",None,["agricultural science","ag"],["agricultural"],["school"]),
 ("agronomy","agriculture","agriculture",[],[],[]),
 ("horticulture","agriculture","agriculture",[],["horticultural"],[]),
 ("animal science","agriculture","agriculture",["animal husbandry"],[],[]),
 ("forestry","agriculture","agriculture",[],[],[]),
 ("food science","agriculture","agriculture",[],[],[]),
 ("fisheries","agriculture","agriculture",["fishery science"],[],[]),

 # --- interdisciplinary ----------------------------------------------------
 ("liberal arts","interdisciplinary",None,["liberal studies"],[],[]),
 ("general studies","interdisciplinary",None,[],[],[]),
 ("professional studies","interdisciplinary",None,[],[],[]),
 ("occupational studies","interdisciplinary",None,[],[],[]),
 ("applied science","interdisciplinary",None,["applied sciences"],[],[]),
 ("applied arts","interdisciplinary",None,[],[],[]),
 ("interdisciplinary studies","interdisciplinary",None,["multidisciplinary studies"],[],[]),
 ("environmental studies","interdisciplinary",None,[],[],[]),
 ("sustainability","interdisciplinary","environmental studies",[],[],[]),
 ("research","interdisciplinary",None,[],[],[]),
 ("home economics","interdisciplinary",None,["family and consumer science","family and consumer sciences"],[],["school"]),
 ("driver education","interdisciplinary",None,["drivers education","driver training"],[],["school"]),
 ("keyboarding","interdisciplinary",None,["typing"],[],["school"]),
]

AREA_ORDER = ["natural science","formal science","social science","humanities",
              "arts","engineering","health","business","education","law",
              "agriculture","interdisciplinary"]

HDR_DICT = """\
# Subjects and fields of study in English: school subjects and academic
# disciplines.  One line per surface form.
#   subject=      the canonical subject name -- on every entry, so rules join
#                 into en-subjects.kbb on this, not on $text
#   area=         the broad division the subject sits in (natural science,
#                 formal science, social science, humanities, arts,
#                 engineering, health, business, education, law, agriculture,
#                 interdisciplinary)
#   parent=       the broader subject this one sits under, where there is one
#   name=1        the form is the canonical name    syn=1  a synonym
#   adj=1         an adjective form (biological, mathematical)
#   school=1      a common primary or secondary school subject
#   lang=1        the name is also a language and a nationality (english,
#                 french, latin) -- see en-languages.dict, en-nationalities.dict
#   ambig=1       the form is also an entry in another library dictionary
# Nearly every subject name is also an ordinary English word (art, history,
# reading, design, law), so a subject reading always needs context: a "degree
# in", "majored in", "class" or "department" frame, or a course listing.  The
# dictionary does not flag that; only cross-library collisions are flagged.
# The canonical names here are the vocabulary of field= in en-degrees.dict, so
# a degree joins to its subject on that attribute.
"""

HDR_KBB = """\
# Subjects and fields of study in English, related to their broader areas.
# Forward lookup:  subject -> area   (concept "subjects subject biology" -> area="natural science")
# Area lookup:     area -> its subjects
# The tree walks both ways: parent= points up, child= points down.
#   area=         natural science | formal science | social science |
#                 humanities | arts | engineering | health | business |
#                 education | law | agriculture | interdisciplinary
#   parent=       the broader subject this one sits under
#   child=        the immediate children of this subject
#   synonym=      alternate names        adjective=  adjective forms
#   school=1      a common primary or secondary school subject
#   lang=1        the name is also a language and a nationality
# The subject names here are the vocabulary of field= in en-degrees.dict, so a
# degree joins to its subject on that attribute.
# Every form named here is tagged by en-subjects.dict.
"""


def q(s):
    """Quote a value for a .dict / .kbb attribute when it is not a bare token."""
    if s and all(c.isalnum() or c in "_-." for c in s):
        return s
    return '"' + s.replace('"', '\\"') + '"'


def build():
    """form -> (rec, role) over every surface form in T; first reading wins."""
    forms = {}
    for rec in T:
        name, area, parent, syns, adjs, flags = rec
        for form, role in ([(name, "name")] + [(s, "syn") for s in syns]
                           + [(a, "adj") for a in adjs]):
            if form not in forms:
                forms[form] = (rec, role)
    return forms


def dict_key(line):
    """The entry word of a .dict line: every token before the first attr=."""
    parts = []
    for tok in line.split(" "):
        if "=" in tok:
            break
        parts.append(tok)
    return " ".join(parts).lower()


def ambiguous(d):
    """Forms that another library dictionary also carries."""
    known = set()
    for fn in ("en-languages.dict", "en-nationalities.dict", "en-countries.dict",
               "en-usa-states.dict", "en-name-pre-suffix.dict", "en-degrees.dict",
               "en-professions.dict"):
        p = os.path.join(d, fn)
        if not os.path.exists(p):
            continue
        with open(p, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#"):
                    known.add(dict_key(line))
    return known


def write_dict(forms, path, known):
    out = io.StringIO()
    out.write(HDR_DICT)
    for form in sorted(forms):
        rec, role = forms[form]
        name, area, parent, syns, adjs, flags = rec
        attrs = [role + "=1", "subject=" + q(name), "area=" + q(area)]
        if parent:
            attrs.append("parent=" + q(parent))
        if "school" in flags:
            attrs.append("school=1")
        if "lang" in flags:
            attrs.append("lang=1")
        if form in known:
            attrs.append("ambig=1")
        out.write(form + " " + " ".join(attrs) + "\n")
    save(path, out.getvalue())


def write_kbb(path):
    out = io.StringIO()
    out.write(HDR_KBB)
    out.write("subjects\n")

    children = {}
    for rec in T:
        if rec[2]:
            children.setdefault(rec[2], []).append(rec[0])

    # --- forward branch: subject -> area, parent, children --------------------
    out.write("  subject\n")
    for rec in sorted(T):
        name, area, parent, syns, adjs, flags = rec
        attrs = ["area=" + q(area)]
        if parent:
            attrs.append("parent=" + q(parent))
        if len(syns) == 1:
            attrs.append("synonym=" + q(syns[0]))
        elif syns:
            attrs.append("synonym=[" + ",".join(q(s) for s in syns) + "]")
        if len(adjs) == 1:
            attrs.append("adjective=" + q(adjs[0]))
        elif adjs:
            attrs.append("adjective=[" + ",".join(q(a) for a in adjs) + "]")
        kids = children.get(name, [])
        if len(kids) == 1:
            attrs.append("child=" + q(kids[0]))
        elif kids:
            attrs.append("child=[" + ",".join(q(k) for k in kids) + "]")
        if "school" in flags:
            attrs.append("school=1")
        if "lang" in flags:
            attrs.append("lang=1")
        out.write("    " + name + ": " + ", ".join(attrs) + "\n")

    # --- area branch: area -> its subjects -------------------------------------
    out.write("  area\n")
    for area in AREA_ORDER:
        names = sorted(r[0] for r in T if r[1] == area)
        tops = sorted(r[0] for r in T if r[1] == area and not r[2])
        attrs = ["count=%d" % len(names)]
        if tops:
            attrs.append("top=[" + ",".join(q(t) for t in tops) + "]")
        attrs.append("subject=[" + ",".join(q(n) for n in names) + "]")
        out.write("    " + area + ": " + ", ".join(attrs) + "\n")

    save(path, out.getvalue())


def save(path, text):
    with open(path, "wb") as f:
        f.write(text.replace("\n", "\r\n").encode("utf-8"))
    print("wrote", path, len(text.splitlines()), "lines")


def degree_fields(d):
    """Every field= value in en-degrees.dict, so the join can be checked."""
    p = os.path.join(d, "en-degrees.dict")
    if not os.path.exists(p):
        return []
    vals = set()
    with open(p, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#") or "field=" not in line:
                continue
            rest = line.split("field=", 1)[1]
            if rest.startswith('"'):
                vals.add(rest[1:].split('"', 1)[0])
            else:
                vals.add(rest.split(" ", 1)[0])
    return sorted(vals)


def report(forms, d):
    names = [r[0] for r in T]
    print("duplicate subject names:",
          sorted({n for n in names if names.count(n) > 1}))

    known_names = set(names)
    print("parents with no subject of their own:",
          sorted({r[2] for r in T if r[2] and r[2] not in known_names}))

    print("areas used but not ordered:",
          sorted({r[1] for r in T if r[1] not in AREA_ORDER}))

    fields = degree_fields(d)
    if fields:
        print("en-degrees field= values that do not join:",
              [f for f in fields if f not in known_names])

    print("subjects:", len(T), " surface forms:", len(forms))


if __name__ == "__main__":
    if len(sys.argv) > 1:
        d = sys.argv[1]
    else:
        here = os.path.dirname(os.path.abspath(__file__))
        d = os.path.join(here, os.pardir, "languages", "English")
    d = os.path.normpath(d)
    forms = build()
    known = ambiguous(d)
    write_dict(forms, os.path.join(d, "en-subjects.dict"), known)
    write_kbb(os.path.join(d, "en-subjects.kbb"))
    report(forms, d)
