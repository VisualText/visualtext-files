# -*- coding: utf-8 -*-
# DESC: Generate the Portuguese academic-degree dictionary and knowledge base.
#
# WHAT IT DOES
#   Emits languages/Portuguese/pt-graus-academicos.dict and .kbb from the single
#   master table T below, so the two files can never drift apart.  Edit T (or
#   NIVELWORDS / AMBIG) and re-run; do not hand-edit the generated files.
#   This is the Portuguese counterpart of gen_degrees.py (en-degrees).
#
#   It covers the Brazilian system (bacharelado, licenciatura, tecnologo,
#   especializacao / MBA lato sensu, mestrado and doutorado stricto sensu,
#   pos-doutorado, livre-docencia), the Portuguese Bologna system
#   (licenciatura, mestrado integrado, doutoramento, agregacao, CTeSP), and
#   the foreign degrees Brazilians commonly list on a CV (PhD, MSc, LLM, ...).
#
#   Unlike English, a Portuguese degree is normally cited by its name
#   ("mestrado em fisica") or by its holder's title ("mestre em fisica",
#   "Dr. Fulano"), not by an abbreviation.  So the join key grau= is the
#   degree's usual citation form: the Portuguese name for a lusophone degree
#   (bacharelado, mestrado, doutorado), the acronym for a degree cited by
#   acronym (mba, phd, msc, llm).
#
#   The .dict gets one line per surface form: the degree name, every variant
#   name, every holder title (mestre, doutora, bacharel), every student word
#   (mestrando, doutoranda) and every abbreviation (me, dr, dra, bel, phd).
#   The .kbb gets five branches under "graus":
#       grau    - forward lookup, grau -> nivel, area, titles, abbreviations
#       nome    - reverse lookup, spelled / variant name -> grau
#       titulo  - holder title or student word -> grau
#       abrev   - abbreviation -> grau and the word it abbreviates
#       nivel   - nivel -> its generic words and the degrees that sit there
#   Every degree .dict line carries "grau=<key>", so rules join into the
#   knowledge base on that attribute rather than on $text.
#
#   Master table row, built with D(grau, nivel, ...):
#     nome    spelled name, only for a degree keyed by acronym (phd)
#     area    field of study, a canonical name from pt-areas-de-estudo
#     latim   the Latin name, where the abbreviation is Latin
#     abrev   [(form, completo, gen)]  abbreviations and what they spell out
#     var     alternate names                 pl   plural names
#     tit     [(form, gen, num)]  holder titles
#     aluno   [(form, gen, num)]  student words
#     flags   "br" (Brazilian system), "pt" (Portuguese system),
#             "estrangeiro" (foreign degree), "profissional", "honorario"
#
#   A grau key naming more than one degree (licenciatura: a teaching degree in
#   Brazil, the Bologna first cycle in Portugal) is marked ambig=1 and its
#   further readings hang below it as <grau>1, <grau>2, ... (same convention as
#   en-degrees.kbb).  A form belonging to such a further reading carries
#   sentido=<n>.
#
#   Dotted forms (Ph.D., Dr., Me., M.Sc.) are listed without their periods:
#   the tokenizer splits the periods off into separate tokens.
#
# USAGE
#   python gen_degrees_pt.py [output_dir]
#     output_dir  defaults to ../languages/Portuguese relative to this script

import io, os, sys

T = []


def D(grau, nivel, area=None, nome=None, latim=None, abrev=(), var=(), pl=(),
      tit=(), aluno=(), flags=()):
    T.append(dict(grau=grau, nivel=nivel, area=area, nome=nome, latim=latim,
                  abrev=list(abrev), var=list(var), pl=list(pl), tit=list(tit),
                  aluno=list(aluno), flags=list(flags)))


# --- curta duracao -----------------------------------------------------------
D("ctesp", "curta duração", nome="curso técnico superior profissional",
  var=["técnico superior profissional"], flags=["pt"])
D("associate degree", "curta duração", var=["associate of arts", "associate of science"],
  flags=["estrangeiro"])

# --- graduacao ---------------------------------------------------------------
D("bacharelado", "graduação", var=["grau de bacharel"], pl=["bacharelados"],
  tit=[("bacharel", "m", "s"), ("bacharela", "f", "s"), ("bacharéis", "m", "p"),
       ("bacharelas", "f", "p")],
  abrev=[("bel", "bacharel", "m"), ("bela", "bacharela", "f")],
  aluno=[("bacharelando", "m", "s"), ("bacharelanda", "f", "s"),
         ("bacharelandos", "m", "p"), ("bacharelandas", "f", "p")],
  flags=["br"])
D("bacharelato", "graduação", pl=["bacharelatos"], flags=["pt"])
D("licenciatura", "graduação", area="educação", var=["licenciatura plena"],
  pl=["licenciaturas"],
  tit=[("licenciado", "m", "s"), ("licenciada", "f", "s"), ("licenciados", "m", "p"),
       ("licenciadas", "f", "p")],
  abrev=[("lic", "licenciado", None)],
  aluno=[("licenciando", "m", "s"), ("licencianda", "f", "s"),
         ("licenciandos", "m", "p"), ("licenciandas", "f", "p")],
  flags=["br"])
# The same word in Portugal: the Bologna first cycle in any field.
D("licenciatura", "graduação", var=["licenciatura pré-bolonha"], flags=["pt"])
D("tecnólogo", "graduação", var=["curso superior de tecnologia", "graduação tecnológica"],
  tit=[("tecnóloga", "f", "s"), ("tecnólogos", "m", "p"), ("tecnólogas", "f", "p")],
  abrev=[("cst", "curso superior de tecnologia", None)],
  flags=["br"])

# --- especializacao (pos-graduacao lato sensu) ---------------------------------
D("especialização", "especialização",
  var=["pós-graduação lato sensu", "especialização lato sensu", "curso de especialização"],
  pl=["especializações"],
  tit=[("especialista", None, "s"), ("especialistas", None, "p")],
  abrev=[("esp", "especialista", None)],
  aluno=[("especializando", "m", "s"), ("especializanda", "f", "s"),
         ("especializandos", "m", "p"), ("especializandas", "f", "p")],
  flags=["br", "pt"])
D("mba", "especialização", area="administração", nome="master of business administration",
  var=["master in business administration", "mba executivo"], pl=["mbas"],
  flags=["br", "estrangeiro"])
D("aperfeiçoamento", "especialização", var=["curso de aperfeiçoamento"], flags=["br"])
D("residência médica", "especialização", area="medicina",
  var=["programa de residência médica"],
  tit=[("médico residente", "m", "s"), ("médica residente", "f", "s"),
       ("médicos residentes", "m", "p")],
  flags=["br", "profissional"])
D("residência multiprofissional", "especialização", area="saúde coletiva",
  var=["residência em saúde"], flags=["br", "profissional"])

# --- mestrado ----------------------------------------------------------------
D("mestrado", "mestrado",
  var=["mestrado acadêmico", "mestrado académico", "mestrado stricto sensu"],
  pl=["mestrados"],
  tit=[("mestre", "m", "s"), ("mestra", "f", "s"), ("mestres", "m", "p"),
       ("mestras", "f", "p")],
  abrev=[("me", "mestre", "m"), ("mestr", "mestre", None)],
  aluno=[("mestrando", "m", "s"), ("mestranda", "f", "s"), ("mestrandos", "m", "p"),
         ("mestrandas", "f", "p")],
  flags=["br", "pt"])
D("mestrado profissional", "mestrado", var=["mestrado profissionalizante"],
  pl=["mestrados profissionais"], flags=["br", "profissional"])
D("mestrado integrado", "mestrado", pl=["mestrados integrados"], flags=["pt"])

# --- doutorado ---------------------------------------------------------------
D("doutorado", "doutorado", var=["doutoramento", "doutorado stricto sensu"],
  pl=["doutorados", "doutoramentos"],
  tit=[("doutor", "m", "s"), ("doutora", "f", "s"), ("doutores", "m", "p"),
       ("doutoras", "f", "p")],
  abrev=[("dr", "doutor", "m"), ("dra", "doutora", "f"), ("drs", "doutores", "m"),
         ("dras", "doutoras", "f")],
  aluno=[("doutorando", "m", "s"), ("doutoranda", "f", "s"), ("doutorandos", "m", "p"),
         ("doutorandas", "f", "p")],
  flags=["br", "pt"])
D("doutorado profissional", "doutorado", pl=["doutorados profissionais"],
  flags=["br", "profissional"])
D("doutorado honoris causa", "doutorado", latim="doctor honoris causa",
  var=["honoris causa", "doutoramento honoris causa", "título de doutor honoris causa"],
  tit=[("doutor honoris causa", "m", "s"), ("doutora honoris causa", "f", "s")],
  flags=["br", "pt", "honorario"])

# --- pos-doutorado -----------------------------------------------------------
D("pós-doutorado", "pós-doutorado",
  var=["pós-doutoramento", "estágio pós-doutoral", "estágio de pós-doutorado"],
  pl=["pós-doutorados"],
  tit=[("pós-doutor", "m", "s"), ("pós-doutora", "f", "s")],
  abrev=[("pós-doc", "pós-doutorado", None), ("pos-doc", "pós-doutorado", None),
         ("posdoc", "pós-doutorado", None), ("postdoc", "pós-doutorado", None)],
  aluno=[("pós-doutorando", "m", "s"), ("pós-doutoranda", "f", "s")],
  flags=["br", "pt"])

# --- livre-docencia / agregacao ------------------------------------------------
D("livre-docência", "livre-docência", var=["livre docência"],
  tit=[("livre-docente", None, "s"), ("livre docente", None, "s"),
       ("livres-docentes", None, "p")],
  flags=["br"])
D("agregação", "livre-docência", var=["título de agregado", "provas de agregação"],
  flags=["pt"])

# --- estrangeiros: graduacao ---------------------------------------------------
D("ba", "graduação", area="artes liberais", nome="bachelor of arts",
  latim="artium baccalaureus", abrev=[("ab", "bachelor of arts", None)],
  flags=["estrangeiro"])
D("bsc", "graduação", area="ciências", nome="bachelor of science",
  latim="scientiae baccalaureus", abrev=[("bs", "bachelor of science", None)],
  flags=["estrangeiro"])
D("bba", "graduação", area="administração", nome="bachelor of business administration",
  flags=["estrangeiro"])
D("beng", "graduação", area="engenharia", nome="bachelor of engineering",
  flags=["estrangeiro"])
D("llb", "graduação", area="direito", nome="bachelor of laws", latim="legum baccalaureus",
  flags=["estrangeiro"])

# --- estrangeiros: mestrado ----------------------------------------------------
D("ma", "mestrado", area="artes liberais", nome="master of arts", latim="artium magister",
  flags=["estrangeiro"])
D("msc", "mestrado", area="ciências", nome="master of science", latim="scientiae magister",
  abrev=[("ms", "master of science", None)], flags=["estrangeiro"])
D("meng", "mestrado", area="engenharia", nome="master of engineering", flags=["estrangeiro"])
D("llm", "mestrado", area="direito", nome="master of laws", latim="legum magister",
  flags=["estrangeiro"])
D("mphil", "mestrado", area="filosofia", nome="master of philosophy", flags=["estrangeiro"])
D("mpa", "mestrado", area="administração pública", nome="master of public administration",
  flags=["estrangeiro"])
D("mph", "mestrado", area="saúde coletiva", nome="master of public health",
  flags=["estrangeiro"])
D("mfa", "mestrado", area="belas-artes", nome="master of fine arts", flags=["estrangeiro"])

# --- estrangeiros: doutorado ---------------------------------------------------
D("phd", "doutorado", area="filosofia", nome="doctor of philosophy",
  latim="philosophiae doctor", abrev=[("dphil", "doctor of philosophy", None)],
  flags=["estrangeiro"])
D("dsc", "doutorado", area="ciências", nome="doctor of science", latim="scientiae doctor",
  abrev=[("scd", "doctor of science", None)], flags=["estrangeiro"])
D("edd", "doutorado", area="educação", nome="doctor of education", flags=["estrangeiro"])
D("dba", "doutorado", area="administração", nome="doctor of business administration",
  flags=["estrangeiro"])
D("md", "doutorado", area="medicina", nome="doctor of medicine", latim="medicinae doctor",
  flags=["estrangeiro", "profissional"])
D("jd", "doutorado", area="direito", nome="juris doctor", latim="juris doctor",
  flags=["estrangeiro", "profissional"])
D("sjd", "doutorado", area="direito", nome="doctor of juridical science",
  latim="scientiae juridicae doctor", abrev=[("jsd", "doctor of juridical science", None)],
  flags=["estrangeiro"])

NIVEL_ORDER = ["curta duração", "graduação", "especialização", "mestrado", "doutorado",
               "pós-doutorado", "livre-docência"]

# ciclo= and sensu= follow from the nivel for a lusophone degree.
CICLO = {"graduação": "graduação", "especialização": "pós-graduação",
         "mestrado": "pós-graduação", "doutorado": "pós-graduação"}
SENSU = {"especialização": "lato", "mestrado": "stricto", "doutorado": "stricto"}

# Generic words for a level or cycle of study.  These name a level, not one
# degree, so they carry palavranivel=1 and nivel= / ciclo= but no grau=.
# form, nivel, ciclo, extra attributes
NIVELWORDS = [
 ("graduação", "graduação", "graduação", {}),
 ("graduações", "graduação", "graduação", {"num": "p"}),
 ("graduado", "graduação", "graduação", {"gen": "m", "num": "s"}),
 ("graduada", "graduação", "graduação", {"gen": "f", "num": "s"}),
 ("graduados", "graduação", "graduação", {"gen": "m", "num": "p"}),
 ("graduadas", "graduação", "graduação", {"gen": "f", "num": "p"}),
 ("graduando", "graduação", "graduação", {"estudante": "1", "gen": "m", "num": "s"}),
 ("graduanda", "graduação", "graduação", {"estudante": "1", "gen": "f", "num": "s"}),
 ("graduandos", "graduação", "graduação", {"estudante": "1", "gen": "m", "num": "p"}),
 ("graduandas", "graduação", "graduação", {"estudante": "1", "gen": "f", "num": "p"}),
 ("ensino superior", "graduação", "graduação", {}),
 ("nível superior", "graduação", "graduação", {}),
 ("curso superior", "graduação", "graduação", {}),
 ("formação superior", "graduação", "graduação", {}),
 ("superior completo", "graduação", "graduação", {}),
 ("superior incompleto", "graduação", "graduação", {}),
 ("pós-graduação", None, "pós-graduação", {}),
 ("pós-graduações", None, "pós-graduação", {"num": "p"}),
 ("pós-graduado", None, "pós-graduação", {"gen": "m", "num": "s"}),
 ("pós-graduada", None, "pós-graduação", {"gen": "f", "num": "s"}),
 ("pós-graduados", None, "pós-graduação", {"gen": "m", "num": "p"}),
 ("pós-graduadas", None, "pós-graduação", {"gen": "f", "num": "p"}),
 ("pós-graduando", None, "pós-graduação", {"estudante": "1", "gen": "m", "num": "s"}),
 ("pós-graduanda", None, "pós-graduação", {"estudante": "1", "gen": "f", "num": "s"}),
 ("pós", None, "pós-graduação", {}),
 ("lato sensu", "especialização", "pós-graduação", {"sensu": "lato"}),
 ("stricto sensu", None, "pós-graduação", {"sensu": "stricto"}),
 ("doutoral", "doutorado", "pós-graduação", {}),
 ("doutorais", "doutorado", "pós-graduação", {"num": "p"}),
 ("bachelor", "graduação", "graduação", {"estrangeiro": "1"}),
 ("bachelors", "graduação", "graduação", {"estrangeiro": "1", "num": "p"}),
 ("undergraduate", "graduação", "graduação", {"estrangeiro": "1"}),
 ("master", "mestrado", "pós-graduação", {"estrangeiro": "1"}),
 ("masters", "mestrado", "pós-graduação", {"estrangeiro": "1", "num": "p"}),
 ("doctorate", "doutorado", "pós-graduação", {"estrangeiro": "1"}),
 ("postgraduate", None, "pós-graduação", {"estrangeiro": "1"}),
]

# Forms that are also an ordinary Portuguese word with another meaning
# (pt-full.dict), a state code (pt-estados.dict) or a form of address
# (pt-tratamentos.dict).
AMBIG = set("""ba ma ms me bel bela lic mestre mestra mestres mestras doutor doutora
doutores doutoras dr dra drs dras licenciado licenciada licenciados licenciadas
especialista especialistas aperfeiçoamento agregação meng""".split())

# Forms pt-tratamentos.dict also carries as a form of address before a name.
TRATAMENTO = set("dr dra drs dras doutor doutora me mestre bel phd msc mba".split())

# Ordinary words that the generic level words collide with.
NIVELWORD_AMBIG = set("""graduação graduações graduado graduada graduados graduadas
pós master masters""".split())

# Degree forms that pt-full.dict carries only as the degree word itself, so a
# hit there is not an ambiguity.  Listed so report() stays quiet about them.
UNAMBIG = set("""bacharelado bacharelados bacharelato bacharelatos bacharel bacharéis
bacharela bacharelas bacharelando bacharelanda bacharelandos bacharelandas licenciatura licenciaturas licenciando
licencianda licenciandos licenciandas tecnólogo tecnóloga tecnólogos tecnólogas
especialização especializações especializando especializanda especializandos
especializandas mestrado mestrados mestrando mestranda mestrandos mestrandas
doutorado doutorados doutoramento doutoramentos doutorando doutoranda doutorandos
doutorandas pós-doutorado pós-doutorados pós-doutoramento livre-docência
livre-docente livres-docentes""".split())

# European-Portuguese spellings or usage.
PT_FORMS = set("""doutoramento doutoramentos pós-doutoramento""".split()) | {
    "mestrado académico", "doutoramento honoris causa"}

HDR_DICT = """\
# Graus académicos em português: nomes, títulos, estudantes e abreviaturas.
# Abrange o sistema brasileiro (bacharelado, licenciatura, tecnólogo,
# especialização e MBA lato sensu, mestrado e doutorado stricto sensu,
# pós-doutorado, livre-docência), o sistema português de Bolonha (licenciatura,
# mestrado integrado, doutoramento, agregação, CTeSP) e os graus estrangeiros
# que se costumam citar em currículos (phd, msc, llm, mba...).
# Uma linha por forma.
#   grau=         a forma canónica do grau -- em toda entrada de grau, para que
#                 as regras façam a junção com pt-graus-academicos.kbb por este
#                 atributo e não por $text.  É o nome do grau (mestrado,
#                 doutorado) ou, para um grau citado pela sigla, a sigla (phd)
#   nome=1        a forma é o nome do grau          sin=1  um nome alternativo
#   titulo=1      o título de quem tem o grau (mestre, doutora, bacharel)
#   estudante=1   quem cursa o grau (mestrando, doutoranda)
#   completo=     numa abreviatura, a palavra que ela abrevia (dr -> doutor,
#                 bel -> bacharel, phd -> "doctor of philosophy")
#   gen=m|f       género do título         num=s|p  número
#   nivel=        curta duração | graduação | especialização | mestrado |
#                 doutorado | pós-doutorado | livre-docência
#   ciclo=        graduação | pós-graduação
#   sensu=        lato (especialização, MBA) | stricto (mestrado, doutorado)
#   area=         área de estudo, um nome canónico de pt-areas-de-estudo.dict
#   br=1          grau do sistema brasileiro      pt=1  do sistema português,
#                 ou forma de uso europeu (doutoramento)
#   estrangeiro=1 grau estrangeiro (no Brasil, o MBA é especialização lato
#                 sensu, por isso tem br=1 e estrangeiro=1)
#   profissional=1  grau profissional (mestrado profissional, residência)
#   honorario=1   conferido honoris causa
#   tratamento=1  também está em pt-tratamentos.dict como forma de tratamento
#   ambig=1       a forma é também uma palavra comum com outro sentido, uma
#                 sigla de estado ou uma forma de tratamento (ver pt-full.dict,
#                 pt-estados.dict, pt-tratamentos.dict).  Em Portugal "dr." e
#                 "dra." tratam qualquer licenciado, não só o doutor
#   sentido=n     a forma pertence à n-ésima leitura adicional de um grau
#                 ambíguo; o conceito na kbb é <grau><n> (licenciatura1)
#   palavranivel=1  palavra genérica de nível ou ciclo (graduação,
#                 pós-graduação, stricto sensu), que nomeia um nível e não um
#                 grau, e por isso não tem grau=
# As formas com pontos (Ph.D., Dr., Me., M.Sc.) estão sem os pontos: o
# tokenizador separa os pontos em tokens próprios.
"""

HDR_KBB = """\
# Graus académicos em português, ligados aos seus títulos, níveis e áreas.
# Consulta direta:   grau -> nível, área, títulos  (conceito "graus grau mestrado" -> titulo=[mestre,...])
# Consulta inversa:  nome -> grau    (conceito "graus nome doctor of philosophy" -> grau=phd)
# Títulos:           título ou estudante -> grau  ("graus titulo doutora" -> grau=doutorado, gen=f)
# Abreviaturas:      abreviatura -> grau  ("graus abrev dr" -> grau=doutorado, completo=doutor)
# Níveis:            nível -> as suas palavras genéricas e os seus graus
#   nome=         o nome por extenso de um grau citado pela sigla (phd)
#   nivel=        curta duração | graduação | especialização | mestrado |
#                 doutorado | pós-doutorado | livre-docência
#   ciclo=        graduação | pós-graduação
#   sensu=        lato | stricto
#   area=         área de estudo, um nome canónico de pt-areas-de-estudo.kbb
#   latim=        o nome latino que a sigla de facto abrevia
#   sinonimo=     nomes alternativos          plural=  nomes no plural
#   titulo=       títulos de quem tem o grau  estudante=  quem o cursa
#   abrev=        abreviaturas                completo=  o que a abreviatura abrevia
#   gen=m|f, num=s|p
#   br=1, pt=1, estrangeiro=1   sistema a que o grau pertence
#   profissional=1  grau profissional        honorario=1  honoris causa
#   tratamento=1  também é forma de tratamento (pt-tratamentos.dict)
# Um grau com mais de uma leitura tem ambig=1 e as leituras adicionais ficam
# por baixo dele como <grau>1, <grau>2, ... (mesma convenção de
# en-degrees.kbb).
# Toda forma aqui citada é etiquetada por pt-graus-academicos.dict.
"""


def q(s):
    """Quote a value for a .dict / .kbb attribute when it is not a bare token."""
    # The dictionary loader mangles an unquoted value whose first letter is
    # not ASCII (area=ética loads as a broken byte string), so quote those.
    if s and ord(s[0]) < 128 and all(c.isalnum() or c in "_-." for c in s):
        return s
    return '"' + s.replace('"', '\\"') + '"'


def lst(vals):
    vals = list(vals)
    if len(vals) == 1:
        return q(vals[0])
    return "[" + ",".join(q(v) for v in vals) + "]"


def senses():
    """grau -> its records in table order (index = sense)."""
    by = {}
    for r in T:
        by.setdefault(r["grau"], []).append(r)
    return by


def build():
    """form -> {recs, role, sense, gen, num, completo} over every surface form."""
    by = senses()
    forms = {}

    def add(form, rec, role, gen=None, num=None, completo=None):
        sense = by[rec["grau"]].index(rec)
        if form == rec["grau"]:
            sense = 0               # the key itself is always the base concept
        e = forms.get(form)
        if e is None:
            forms[form] = dict(recs=[rec], role=role, sense=sense, gen=gen,
                               num=num, completo=completo)
        elif rec not in e["recs"]:
            e["recs"].append(rec)

    for r in T:
        if r["nome"]:
            add(r["grau"], r, "abrev", completo=r["nome"])
            add(r["nome"], r, "nome")
        else:
            add(r["grau"], r, "nome", num="s")
        for v in r["var"]:
            add(v, r, "sin")
        for v in r["pl"]:
            add(v, r, "sin", num="p")
        for f, c, g in r["abrev"]:
            add(f, r, "abrev", gen=g, completo=c)
        for f, g, n in r["tit"]:
            add(f, r, "titulo", gen=g, num=n)
        for f, g, n in r["aluno"]:
            add(f, r, "estudante", gen=g, num=n)
    return forms


def common_attrs(r):
    a = []
    a.append("nivel=" + q(r["nivel"]))
    if r["nivel"] in CICLO:
        a.append("ciclo=" + q(CICLO[r["nivel"]]))
    if (r["nivel"] in SENSU and "br" in r["flags"] and "estrangeiro" not in r["flags"]
            and "honorario" not in r["flags"]):
        a.append("sensu=" + SENSU[r["nivel"]])
    elif r["grau"] == "mba":
        a.append("sensu=lato")
    if r["area"]:
        a.append("area=" + q(r["area"]))
    return a


def flag_attrs(r):
    return [f + "=1" for f in ("br", "pt", "estrangeiro", "profissional", "honorario")
            if f in r["flags"]]


def write_dict(forms, path):
    out = io.StringIO()
    out.write(HDR_DICT)
    lines = []
    for form, e in forms.items():
        r = e["recs"][0]
        attrs = []
        role = e["role"]
        if role in ("nome", "sin", "titulo", "estudante"):
            attrs.append(role + "=1")
        if e["completo"]:
            attrs.append("completo=" + q(e["completo"]))
        attrs.append("grau=" + q(r["grau"]))
        if e["sense"]:
            attrs.append("sentido=%d" % e["sense"])
        if e["gen"]:
            attrs.append("gen=" + e["gen"])
        if e["num"]:
            attrs.append("num=" + e["num"])
        attrs += common_attrs(r)
        fl = flag_attrs(r)
        if form in PT_FORMS and "pt=1" not in fl:
            fl.append("pt=1")
        attrs += fl
        if form in TRATAMENTO:
            attrs.append("tratamento=1")
        if form in AMBIG or len(e["recs"]) > 1:
            attrs.append("ambig=1")
        lines.append(form + " " + " ".join(attrs))

    for form, nivel, ciclo, extra in NIVELWORDS:
        attrs = ["palavranivel=1"]
        if nivel:
            attrs.append("nivel=" + q(nivel))
        attrs.append("ciclo=" + q(ciclo))
        for k in ("estudante", "gen", "num", "sensu", "estrangeiro"):
            if k in extra:
                attrs.append(k + "=" + extra[k])
        if form in NIVELWORD_AMBIG:
            attrs.append("ambig=1")
        lines.append(form + " " + " ".join(attrs))

    for line in sorted(lines):
        out.write(line + "\n")
    save(path, out.getvalue())


def write_kbb(path):
    out = io.StringIO()
    out.write(HDR_KBB)
    out.write("graus\n")
    by = senses()

    # --- forward branch: grau -> everything ------------------------------------
    out.write("  grau\n")
    for grau in sorted(by):
        recs = by[grau]
        for i, r in enumerate(recs):
            concept = grau if i == 0 else grau + str(i)
            indent = "    " if i == 0 else "      "
            attrs = []
            if i == 0 and len(recs) > 1:
                attrs.append("ambig=1")
            if r["nome"]:
                attrs.append("nome=" + q(r["nome"]))
            attrs += common_attrs(r)
            if r["latim"]:
                attrs.append("latim=" + q(r["latim"]))
            if r["var"]:
                attrs.append("sinonimo=" + lst(r["var"]))
            if r["pl"]:
                attrs.append("plural=" + lst(r["pl"]))
            if r["tit"]:
                attrs.append("titulo=" + lst(f for f, g, n in r["tit"]))
            if r["aluno"]:
                attrs.append("estudante=" + lst(f for f, g, n in r["aluno"]))
            if r["abrev"]:
                attrs.append("abrev=" + lst(f for f, c, g in r["abrev"]))
            attrs += flag_attrs(r)
            if grau in TRATAMENTO:
                attrs.append("tratamento=1")
            out.write(indent + concept + ": " + ", ".join(attrs) + "\n")

    # --- reverse branch: spelled / variant name -> grau ------------------------
    out.write("  nome\n")
    rows = {}
    for r in T:
        sense = by[r["grau"]].index(r)
        names = ([(r["nome"], 0, "s")] if r["nome"] else []) + \
                [(v, 1, None) for v in r["var"]] + [(v, 1, "p") for v in r["pl"]]
        for n, is_alt, num in names:
            if n not in rows:
                rows[n] = (r, sense, is_alt, num)
    for name in sorted(rows):
        r, sense, is_alt, num = rows[name]
        attrs = ["grau=" + q(r["grau"])]
        if sense:
            attrs.append("sentido=%d" % sense)
        attrs.append("nivel=" + q(r["nivel"]))
        if is_alt:
            attrs.append("sin=1")
        if num == "p":
            attrs.append("num=p")
        if name in PT_FORMS:
            attrs.append("pt=1")
        out.write("    " + name + ": " + ", ".join(attrs) + "\n")

    # --- title branch: holder title / student word -> grau -----------------------
    out.write("  titulo\n")
    rows = {}
    for r in T:
        for f, g, n in r["tit"]:
            rows.setdefault(f, (r, "titulo", g, n))
        for f, g, n in r["aluno"]:
            rows.setdefault(f, (r, "estudante", g, n))
    for f in sorted(rows):
        r, role, g, n = rows[f]
        attrs = ["grau=" + q(r["grau"]), "nivel=" + q(r["nivel"])]
        if role == "estudante":
            attrs.append("estudante=1")
        if g:
            attrs.append("gen=" + g)
        if n:
            attrs.append("num=" + n)
        if f in TRATAMENTO:
            attrs.append("tratamento=1")
        out.write("    " + f + ": " + ", ".join(attrs) + "\n")

    # --- abbreviation branch: abbreviation -> grau --------------------------------
    out.write("  abrev\n")
    rows = {}
    for r in T:
        if r["nome"]:
            rows.setdefault(r["grau"], (r, r["nome"], None))
        for f, c, g in r["abrev"]:
            rows.setdefault(f, (r, c, g))
    for f in sorted(rows):
        r, c, g = rows[f]
        attrs = ["grau=" + q(r["grau"]), "completo=" + q(c), "nivel=" + q(r["nivel"])]
        if g:
            attrs.append("gen=" + g)
        if f in TRATAMENTO:
            attrs.append("tratamento=1")
        out.write("    " + f + ": " + ", ".join(attrs) + "\n")

    # --- level branch: nivel -> its words and its degrees ------------------------
    out.write("  nivel\n")
    for nivel in NIVEL_ORDER:
        words = [w for w, nv, c, x in NIVELWORDS if nv == nivel]
        graus = sorted({r["grau"] for r in T if r["nivel"] == nivel})
        attrs = []
        if nivel in CICLO:
            attrs.append("ciclo=" + q(CICLO[nivel]))
        if words:
            attrs.append("palavra=" + lst(words))
        attrs.append("grau=" + lst(graus))
        out.write("    " + nivel + ": " + ", ".join(attrs) + "\n")

    save(path, out.getvalue())


def save(path, text):
    with open(path, "wb") as f:
        f.write(text.replace("\n", "\r\n").encode("utf-8"))
    print("wrote", path, len(text.splitlines()), "lines")


def dict_key(line):
    """The entry word of a .dict line: every token before the first attr=."""
    parts = []
    for tok in line.split(" "):
        if "=" in tok:
            break
        parts.append(tok)
    return " ".join(parts).lower()


def report(forms, d):
    """Sanity checks, plus an ambiguity cross-check against the sibling dicts."""
    by = senses()
    print("graus with more than one reading:",
          sorted(g for g in by if len(by[g]) > 1))
    print("surface forms shared by several degrees:",
          sorted(f for f in forms if len(forms[f]["recs"]) > 1))
    print("niveis used but not ordered:",
          sorted({r["nivel"] for r in T if r["nivel"] not in NIVEL_ORDER}))
    print("nivel words that are also degree forms:",
          sorted(w for w, *_ in NIVELWORDS if w in forms))

    siblings = ["pt-full.dict", "pt-estados.dict", "pt-tratamentos.dict",
                "pt-paises.dict", "pt-nacionalidades.dict", "pt-nomes.dict"]
    known = set()
    for fn in siblings:
        p = os.path.join(d, fn)
        if not os.path.exists(p):
            continue
        with open(p, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#"):
                    known.add(dict_key(line))
    if known:
        print("forms in a sibling dict but not marked ambig:",
              sorted(f for f in forms
                     if f in known and f not in AMBIG and f not in TRATAMENTO
                     and f not in UNAMBIG))
        print("AMBIG entries no sibling dict has:",
              sorted(a for a in AMBIG if a not in known))

    areas = os.path.join(d, "pt-areas-de-estudo.dict")
    if os.path.exists(areas):
        names = set()
        with open(areas, "r", encoding="utf-8") as f:
            for line in f:
                if "nome=1" in line:
                    names.add(dict_key(line.strip()))
        print("area= values that do not join pt-areas-de-estudo:",
              sorted({r["area"] for r in T if r["area"] and r["area"] not in names}))
    print("degrees:", len(T), " surface forms:", len(forms),
          " level words:", len(NIVELWORDS))


if __name__ == "__main__":
    if len(sys.argv) > 1:
        d = sys.argv[1]
    else:
        here = os.path.dirname(os.path.abspath(__file__))
        d = os.path.join(here, os.pardir, "languages", "Portuguese")
    d = os.path.normpath(d)
    forms = build()
    write_dict(forms, os.path.join(d, "pt-graus-academicos.dict"))
    write_kbb(os.path.join(d, "pt-graus-academicos.kbb"))
    report(forms, d)
