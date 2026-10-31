# -*- coding: utf-8 -*-
# DESC: Generate the Spanish academic-degree dictionary and knowledge base.
#
# WHAT IT DOES
#   Emits languages/Spanish/es-grados-academicos.dict and
#   es-grados-academicos.kbb from the single master table T below, so the two
#   files can never drift apart.  Edit T (or PLURALS / LEVELWORDS / AMBIG) and
#   re-run; do not hand-edit the generated files.  Spanish counterpart of
#   gen_degrees.py (en-degrees.dict / .kbb).
#
#   It covers the systems of Spain (grado, máster, doctorado and the extinct
#   pre-Bologna diplomatura / licenciatura / ingeniería técnica) and Latin
#   America (técnico superior universitario, tecnólogo, licenciatura,
#   ingeniería, especialización, maestría / magíster, doctorado), plus the
#   foreign (English-language) degrees most often written in Spanish text.
#
#   Spanish degrees are named, not abbreviated, so unlike the English file the
#   key is the canonical spelled-out name (licenciatura, maestría en
#   administración de empresas), not an abbreviation.  The .dict gets one line
#   per surface form: the name, every variant name, every abbreviation, every
#   holder noun (licenciado, ingeniera civil, mtra) and plural.  The .kbb gets
#   three branches under "grados":
#       titulo  - forward lookup, name -> nivel, area, abbreviations, holders
#       abrev   - reverse lookup, abbreviation -> name
#       nivel   - level -> its generic words and the degrees that sit there
#   Every .dict line of a degree carries "titulo=<canonical name>", so rules
#   join into the knowledge base on that attribute rather than on $text.
#
#   Master table row:
#     (name, nivel, area, [abbrevs], [variant names], [holders], [flags])
#     nivel    técnico | grado | especialización | maestría | doctorado
#     area     a canonical subject of es-areas-de-estudio (gen_subjects_es.py),
#              or None for a degree that names no field
#     abbrevs  the first is the canonical abbreviation (abrev= on the name)
#     holders  (form, gen, completo): the noun for a holder of the degree;
#              gen is m | f | None (common gender); completo is the spelled
#              holder noun when the form is itself an abbreviation (mtra ->
#              maestra), else None
#     flags    may hold "es" (Spain), "latam" (Latin America), "extranjero"
#              (a foreign, English-language degree), "antiguo" (a qualification
#              of an extinct plan of study), "profesional" (qualifies for a
#              regulated profession) and "honorifico" (conferred honoris causa)
#
#   An abbreviation that names more than one degree keeps the first as its
#   titulo= and is marked ambig=1; the abrev branch lists every reading.
#
#   Dotted forms (Lic., Ph.D., M.Sc., Dr.ª) are not listed: the tokenizer
#   splits them into separate tokens.  Abbreviations are given without
#   periods, like the English files (phd, jr).
#
# USAGE
#   python gen_degrees_es.py [output_dir]
#     output_dir  defaults to ../languages/Spanish relative to this script

import io, os, sys, unicodedata

LIC = lambda f: [("licenciado en " + f, "m", None), ("licenciada en " + f, "f", None)]
ING = lambda f, fm=None: [("ingeniero " + f, "m", None), ("ingeniera " + (fm or f), "f", None)]

# name, nivel, area, abbrevs, variant names, holders, flags
T = [
 # --- técnico --------------------------------------------------------------
 ("técnico superior","técnico",None,[],["ciclo formativo de grado superior","formación profesional de grado superior","fp de grado superior"],[("técnica superior","f",None)],["es"]),
 ("técnico superior universitario","técnico",None,["tsu"],[],[("técnica superior universitaria","f",None)],["latam"]),
 ("técnico universitario","técnico",None,[],["título técnico universitario"],[("técnica universitaria","f",None)],["latam"]),
 ("tecnólogo","técnico",None,[],["título de tecnólogo"],[("tecnóloga","f",None)],["latam"]),
 ("profesorado","técnico","educación",[],["título de profesor"],[],["latam"]),

 # --- grado ----------------------------------------------------------------
 ("grado","grado",None,[],["título de grado","grado universitario"],[("graduado","m",None),("graduada","f",None),("graduado universitario","m",None),("graduada universitaria","f",None)],["es"]),
 ("licenciatura","grado",None,["lic"],["título de licenciado"],[("licenciado","m",None),("licenciada","f",None),("lcdo","m","licenciado"),("lcda","f","licenciada"),("licdo","m","licenciado"),("licda","f","licenciada"),("ldo","m","licenciado"),("lda","f","licenciada")],[]),
 ("diplomatura","grado",None,[],[],[("diplomado","m",None),("diplomada","f",None)],["es","antiguo"]),
 ("bachillerato universitario","grado",None,["bach"],["grado de bachiller","grado académico de bachiller"],[("bachiller",None,None)],["latam"]),
 ("ingeniería","grado","ingeniería",["ing"],["título de ingeniero"],[("ingeniero","m",None),("ingeniera","f",None)],["profesional"]),
 ("ingeniería técnica","grado","ingeniería",[],[],[("ingeniero técnico","m",None),("ingeniera técnica","f",None)],["es","antiguo","profesional"]),
 ("arquitectura","grado","arquitectura",["arq"],["título de arquitecto"],[("arquitecto","m",None),("arquitecta","f",None)],["profesional"]),
 ("arquitectura técnica","grado","arquitectura",[],[],[("arquitecto técnico","m",None),("arquitecta técnica","f",None),("aparejador","m",None),("aparejadora","f",None)],["es","antiguo","profesional"]),

 # licenciaturas / grados por área (LatAm "licenciatura en", Spain "grado en")
 ("licenciatura en derecho","grado","derecho",[],["grado en derecho","título de abogado"],LIC("derecho")+[("abogado","m",None),("abogada","f",None),("abg",None,"abogado"),("abog",None,"abogado")],["profesional"]),
 ("licenciatura en administración de empresas","grado","administración de empresas",[],["grado en administración y dirección de empresas","grado en administración de empresas","licenciatura en administración"],LIC("administración de empresas"),[]),
 ("licenciatura en contaduría pública","grado","contabilidad",[],["licenciatura en contaduría","licenciatura en contabilidad","grado en contabilidad"],[("contador público","m",None),("contadora pública","f",None),("cp",None,"contador público"),("cpc",None,"contador público colegiado")],["latam","profesional"]),
 ("licenciatura en economía","grado","economía",[],["grado en economía"],LIC("economía"),[]),
 ("licenciatura en psicología","grado","psicología",[],["grado en psicología"],LIC("psicología"),[]),
 ("licenciatura en enfermería","grado","enfermería",[],["grado en enfermería"],LIC("enfermería"),["profesional"]),
 ("licenciatura en educación","grado","educación",[],["grado en educación","grado en magisterio"],LIC("educación"),["profesional"]),
 ("licenciatura en pedagogía","grado","pedagogía",[],["grado en pedagogía"],LIC("pedagogía"),[]),
 ("licenciatura en comunicación","grado","comunicación",[],["licenciatura en ciencias de la comunicación","grado en comunicación"],LIC("comunicación"),[]),
 ("licenciatura en periodismo","grado","periodismo",[],["grado en periodismo"],LIC("periodismo"),[]),
 ("licenciatura en filosofía","grado","filosofía",[],["grado en filosofía"],LIC("filosofía"),[]),
 ("licenciatura en historia","grado","historia",[],["grado en historia"],LIC("historia"),[]),
 ("licenciatura en letras","grado","letras",[],["licenciatura en letras hispánicas","grado en filología hispánica","licenciatura en filología hispánica"],LIC("letras"),[]),
 ("licenciatura en matemáticas","grado","matemáticas",[],["grado en matemáticas"],LIC("matemáticas"),[]),
 ("licenciatura en física","grado","física",[],["grado en física"],LIC("física"),[]),
 ("licenciatura en química","grado","química",[],["grado en química"],LIC("química"),[]),
 ("licenciatura en biología","grado","biología",[],["grado en biología"],LIC("biología"),[]),
 ("licenciatura en sociología","grado","sociología",[],["grado en sociología"],LIC("sociología"),[]),
 ("licenciatura en ciencia política","grado","ciencia política",[],["licenciatura en ciencias políticas","grado en ciencia política","grado en ciencias políticas"],LIC("ciencia política"),[]),
 ("licenciatura en relaciones internacionales","grado","relaciones internacionales",[],["grado en relaciones internacionales"],LIC("relaciones internacionales"),[]),
 ("licenciatura en trabajo social","grado","trabajo social",[],["grado en trabajo social"],LIC("trabajo social"),[]),
 ("licenciatura en antropología","grado","antropología",[],["grado en antropología"],LIC("antropología"),[]),
 ("licenciatura en geografía","grado","geografía",[],["grado en geografía"],LIC("geografía"),[]),
 ("licenciatura en informática","grado","informática",[],["licenciatura en ciencias de la computación","grado en informática"],LIC("informática"),[]),
 ("licenciatura en mercadotecnia","grado","mercadotecnia",[],["grado en marketing","licenciatura en marketing"],LIC("mercadotecnia"),[]),
 ("licenciatura en turismo","grado","turismo",[],["grado en turismo"],LIC("turismo"),[]),
 ("licenciatura en nutrición","grado","nutrición",[],["grado en nutrición humana y dietética"],LIC("nutrición"),[]),
 ("licenciatura en diseño gráfico","grado","diseño gráfico",[],["grado en diseño"],LIC("diseño gráfico"),[]),
 ("licenciatura en música","grado","música",[],["grado en música"],LIC("música"),[]),
 ("licenciatura en bellas artes","grado","arte",[],["grado en bellas artes","licenciatura en artes visuales"],LIC("bellas artes"),[]),
 ("licenciatura en medicina","grado","medicina",[],["grado en medicina","licenciatura en medicina y cirugía","título de médico cirujano"],[("médico cirujano","m",None),("médica cirujana","f",None),("médico","m",None),("médica","f",None)],["profesional"]),
 ("licenciatura en odontología","grado","odontología",[],["grado en odontología","título de cirujano dentista"],[("cirujano dentista","m",None),("cirujana dentista","f",None),("odontólogo","m",None),("odontóloga","f",None)],["profesional"]),
 ("licenciatura en veterinaria","grado","veterinaria",[],["grado en veterinaria","título de médico veterinario"],[("médico veterinario","m",None),("médica veterinaria","f",None),("médico veterinario zootecnista","m",None),("mvz",None,"médico veterinario zootecnista")],["profesional"]),
 ("licenciatura en farmacia","grado","farmacia",[],["grado en farmacia","licenciatura en química farmacéutica"],[("químico farmacéutico","m",None),("química farmacéutica","f",None),("químico farmacéutico biólogo","m",None),("qfb",None,"químico farmacéutico biólogo")],["profesional"]),

 # ingenierías
 ("ingeniería civil","grado","ingeniería civil",[],["ingeniería de caminos"],ING("civil")+[("ingeniero de caminos","m",None),("ingeniera de caminos","f",None)],["profesional"]),
 ("ingeniería industrial","grado","ingeniería industrial",[],[],ING("industrial"),["profesional"]),
 ("ingeniería mecánica","grado","ingeniería mecánica",[],[],ING("mecánico","mecánica"),["profesional"]),
 ("ingeniería eléctrica","grado","ingeniería eléctrica",[],[],ING("electricista"),["profesional"]),
 ("ingeniería electrónica","grado","ingeniería electrónica",[],[],ING("electrónico","electrónica"),["profesional"]),
 ("ingeniería química","grado","ingeniería química",[],[],ING("químico","química"),["profesional"]),
 ("ingeniería de sistemas","grado","ingeniería de sistemas",[],[],ING("de sistemas")+[("ingeniero en sistemas","m",None),("ingeniera en sistemas","f",None)],[]),
 ("ingeniería informática","grado","ingeniería informática",[],["ingeniería en computación"],ING("informático","informática")+[("ingeniero en computación","m",None),("ingeniera en computación","f",None)],[]),
 ("ingeniería de software","grado","ingeniería de software",[],[],ING("de software"),[]),
 ("ingeniería de telecomunicaciones","grado","ingeniería de telecomunicaciones",[],[],ING("de telecomunicaciones")+[("ingeniero en telecomunicaciones","m",None),("ingeniera en telecomunicaciones","f",None)],["profesional"]),
 ("ingeniería ambiental","grado","ingeniería ambiental",[],[],ING("ambiental"),[]),
 ("ingeniería agronómica","grado","agronomía",[],["ingeniería agrícola"],ING("agrónomo","agrónoma"),["profesional"]),
 ("ingeniería forestal","grado","ingeniería forestal",[],["ingeniería de montes"],ING("forestal")+[("ingeniero de montes","m",None),("ingeniera de montes","f",None)],["profesional"]),
 ("ingeniería de minas","grado","ingeniería de minas",[],[],ING("de minas"),["profesional"]),
 ("ingeniería petrolera","grado","ingeniería petrolera",[],["ingeniería de petróleos"],ING("petrolero","petrolera"),[]),
 ("ingeniería biomédica","grado","ingeniería biomédica",[],[],ING("biomédico","biomédica"),[]),
 ("ingeniería aeroespacial","grado","ingeniería aeroespacial",[],["ingeniería aeronáutica"],ING("aeronáutico","aeronáutica")+ING("aeroespacial"),["profesional"]),
 ("ingeniería de alimentos","grado","ciencia de los alimentos",[],[],ING("en alimentos"),[]),

 # --- especialización ------------------------------------------------------
 ("especialización","especialización",None,["esp"],["especialidad","título de especialista","diploma de especialización"],[("especialista",None,None)],[]),
 ("especialidad médica","especialización","medicina",[],["residencia médica"],[("médico especialista","m",None),("médica especialista","f",None)],["profesional"]),

 # --- maestría -------------------------------------------------------------
 ("maestría","maestría",None,[],["título de maestría","grado de maestro","grado de maestría"],[("maestro","m",None),("maestra","f",None),("mtro","m","maestro"),("mtra","f","maestra")],["latam"]),
 ("máster","maestría",None,[],["master","máster universitario","máster oficial","título de máster"],[],["es"]),
 ("magíster","maestría",None,["mg","mag"],["magister","grado de magíster"],[],["latam"]),
 ("maestría en ciencias","maestría","ciencias naturales",[],["máster en ciencias"],[("maestro en ciencias","m",None),("maestra en ciencias","f",None)],["latam"]),
 ("maestría en administración de empresas","maestría","administración de empresas",["mba"],["máster en administración de empresas","máster en administración y dirección de empresas","maestría en administración de negocios","master of business administration"],[],[]),
 ("maestría en educación","maestría","educación",[],["máster en educación"],[("maestro en educación","m",None),("maestra en educación","f",None)],[]),
 ("maestría en derecho","maestría","derecho",[],["máster en derecho"],[("maestro en derecho","m",None),("maestra en derecho","f",None)],[]),
 ("maestría en finanzas","maestría","finanzas",[],["máster en finanzas"],[],[]),
 ("maestría en salud pública","maestría","salud pública",[],["máster en salud pública"],[],[]),
 ("máster en formación del profesorado","maestría","educación",[],["máster de profesorado","máster del profesorado","máster en profesorado"],[],["es","profesional"]),
 ("máster de acceso a la abogacía","maestría","derecho",[],["máster de abogacía","máster en abogacía"],[],["es","profesional"]),
 ("diploma de estudios avanzados","maestría",None,["dea"],["suficiencia investigadora"],[],["es","antiguo"]),

 # --- doctorado ------------------------------------------------------------
 ("doctorado","doctorado",None,[],["título de doctor","grado de doctor"],[("doctor","m",None),("doctora","f",None),("dr","m","doctor"),("dra","f","doctora")],[]),
 ("doctorado en ciencias","doctorado","ciencias naturales",[],[],[("doctor en ciencias","m",None),("doctora en ciencias","f",None)],[]),
 ("doctorado en derecho","doctorado","derecho",[],[],[("doctor en derecho","m",None),("doctora en derecho","f",None)],[]),
 ("doctorado en filosofía","doctorado","filosofía",[],[],[("doctor en filosofía","m",None),("doctora en filosofía","f",None)],[]),
 ("doctorado en educación","doctorado","educación",[],[],[("doctor en educación","m",None),("doctora en educación","f",None)],[]),
 ("doctorado honoris causa","doctorado",None,[],["doctor honoris causa","doctora honoris causa","honoris causa"],[],["honorifico"]),

 # --- títulos extranjeros ----------------------------------------------------
 ("bachelor of arts","grado","humanidades",["ba"],[],[],["extranjero"]),
 ("bachelor of science","grado","ciencias naturales",["bsc"],[],[],["extranjero"]),
 ("bachelor of business administration","grado","administración de empresas",["bba"],[],[],["extranjero"]),
 ("master of arts","maestría","humanidades",["ma"],[],[],["extranjero"]),
 ("master of science","maestría","ciencias naturales",["msc"],[],[],["extranjero"]),
 ("master of philosophy","maestría",None,["mphil"],[],[],["extranjero"]),
 ("master of laws","maestría","derecho",["llm"],[],[],["extranjero"]),
 ("doctor of philosophy","doctorado",None,["phd","dphil"],["philosophiae doctor"],[],["extranjero"]),
 ("doctor of medicine","doctorado","medicina",["md"],[],[],["extranjero","profesional"]),
 ("juris doctor","doctorado","derecho",["jd"],[],[],["extranjero","profesional"]),
]

# Plural forms of the generic degrees: form, titulo.
PLURALS = [
 ("grados","grado"),
 ("licenciaturas","licenciatura"),
 ("diplomaturas","diplomatura"),
 ("ingenierías","ingeniería"),
 ("especializaciones","especialización"),
 ("especialidades","especialización"),
 ("maestrías","maestría"),
 ("másteres","máster"),
 ("masters","máster"),
 ("doctorados","doctorado"),
]

# Generic words for a level of study.  These name a level, not one degree, so
# they carry nivel= and generico=1 but no titulo=.
# form, nivel, plural
LEVELWORDS = [
 ("pregrado","grado",0),
 ("posgrado","posgrado",0),
 ("postgrado","posgrado",0),
 ("posgrados","posgrado",1),
 ("postgrados","posgrado",1),
 ("posdoctorado","posdoctorado",0),
 ("postdoctorado","posdoctorado",0),
 ("posdoc","posdoctorado",0),
 ("postdoc","posdoctorado",0),
 ("posdoctoral","posdoctorado",0),
 ("postdoctoral","posdoctorado",0),
]

LEVEL_ORDER = ["técnico","grado","especialización","maestría","doctorado","posdoctorado"]

# posgrado is a cover term for the levels after the first degree.
COVER = {"posgrado": ["especialización","maestría","doctorado"]}

# Forms that are also an ordinary Spanish word (a teacher, a physician, a
# temperature degree), an English word, or another common abbreviation
# (cp = código postal, mg = miligramo, esp = España / español).
AMBIG = set("""grado grados graduado graduada doctor doctora maestro maestra
médico médica bachiller diplomado diplomada especialista especialidad
especialidades master masters magister ma mg cp esp profesorado aparejador
ba dea""".split()) | {"honoris causa"}

# Forms es-tratamientos.dict also carries as a title before or after a name.
TRATAMIENTO = set("""lic lcdo lcda licdo licda ldo lda licenciado licenciada
ing ingeniero ingeniera arq arquitecto arquitecta mtro mtra maestro maestra
dr dra doctor doctora abg abog abogado abogada cp mvz phd mba msc
md""".split())

HDR_DICT = """\
# Títulos y grados académicos en español: nombres, abreviaturas y
# denominaciones de quien los posee.  Una línea por forma de superficie.
# Cubre el sistema español (grado, máster, doctorado y los planes extinguidos:
# diplomatura, licenciatura, ingeniería técnica), el latinoamericano (técnico
# superior universitario, tecnólogo, licenciatura, ingeniería, especialización,
# maestría / magíster, doctorado) y los títulos extranjeros más citados.
#   titulo=       el nombre canónico del título -- en todas las entradas de un
#                 título, de modo que las reglas se unen a
#                 es-grados-academicos.kbb por este atributo y no por $text
#   canonico=1    la forma es el nombre canónico    sin=1  un nombre o una
#                 abreviatura variante
#   abrev=        la abreviatura canónica, en la forma desarrollada
#   completo=     la forma desarrollada, en una abreviatura (el nombre del
#                 título, o el sustantivo de poseedor: mtra -> maestra)
#   poseedor=1    la forma designa a quien posee el título (licenciado,
#                 ingeniera civil, mtro)
#   gen=m|f       género de una forma de poseedor (sin gen= si es común:
#                 especialista, bachiller)
#   num=p         forma plural (licenciaturas, másteres)
#   nivel=        técnico | grado | especialización | maestría | doctorado
#                 (los genéricos añaden posgrado y posdoctorado)
#   area=         la materia; es un nombre canónico de es-areas-de-estudio.dict
#   es=1          propio de España              latam=1  propio de Latinoamérica
#   extranjero=1  título extranjero (en inglés) citado en textos en español
#   antiguo=1     título de un plan de estudios extinguido
#   profesional=1 habilita para una profesión regulada
#   honorifico=1  se concede honoris causa
#   tratamiento=1 también figura en es-tratamientos.dict como tratamiento
#   materia=1     la forma es también una entrada de es-areas-de-estudio.dict
#                 (ingeniería civil, arquitectura): el título y su materia
#   ambig=1       la forma es también una palabra corriente (maestro, doctor,
#                 grado), otra abreviatura frecuente (cp, mg) o nombra más de
#                 un título
#   generico=1    una palabra genérica de nivel (posgrado, pregrado,
#                 posdoctorado), que nombra un nivel y no un título concreto y
#                 por eso no lleva titulo=
# Las formas con puntos (Lic., Ph.D., Dr.ª) no se listan: el tokenizador las
# separa en varios tokens.  Las abreviaturas van sin puntos (phd, mtra).
# Generado por python/gen_degrees_es.py; no editar a mano.
"""

HDR_KBB = """\
# Títulos y grados académicos en español, con sus niveles, áreas y abreviaturas.
# Búsqueda directa:  nombre -> nivel, área  (concepto "grados titulo licenciatura" -> nivel=grado)
# Búsqueda inversa:  abreviatura -> nombre  (concepto "grados abrev mba" -> titulo="maestría en administración de empresas")
# Búsqueda por nivel: nivel -> sus palabras genéricas y sus títulos
# A diferencia de en-degrees.kbb, la clave es el nombre desarrollado: los
# títulos en español se nombran, casi nunca se abrevian.
#   nivel=        técnico | grado | especialización | maestría | doctorado
#   area=         la materia (nombre canónico de es-areas-de-estudio.kbb)
#   abrev=        la abreviatura canónica    sinonimo=  abreviaturas variantes
#   variante=     nombres alternativos del título
#   poseedor=     los sustantivos de quien lo posee (masculino, femenino...)
#   es=1  latam=1  extranjero=1  antiguo=1  profesional=1  honorifico=1
#                 como en es-grados-academicos.dict
#   tratamiento=1 la abreviatura figura también en es-tratamientos.dict
# En la rama abrev, una abreviatura de varios títulos lleva ambig=1 y
# titulo=[...] con todos ellos.
# En la rama nivel, palabra= son las palabras genéricas, titulo= los títulos
# de ese nivel e incluye= los niveles que abarca un término genérico (posgrado).
# Todas las formas nombradas aquí están etiquetadas en es-grados-academicos.dict.
# Generado por python/gen_degrees_es.py; no editar a mano.
"""


def q(s):
    """Quote a value for a .dict / .kbb attribute when it is not a bare token."""
    # The dictionary loader mangles an unquoted value whose first letter is
    # not ASCII (area=ética loads as a broken byte string), so quote those.
    if s and ord(s[0]) < 128 and all(c.isalnum() or c in "_-." for c in s):
        return s
    return '"' + s.replace('"', '\\"') + '"'


def skey(s):
    """Sort key that ignores accents, so cálculo sorts next to calculo."""
    base = "".join(c for c in unicodedata.normalize("NFD", s)
                   if unicodedata.category(c) != "Mn")
    return (base, s)


def qlist(vals):
    if len(vals) == 1:
        return q(vals[0])
    return "[" + ",".join(q(v) for v in vals) + "]"


def subject_forms():
    """Every surface form of es-areas-de-estudio, from gen_subjects_es.T."""
    sys.dont_write_bytecode = True
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import gen_subjects_es as gs
    return set(gs.build().keys()), {r[0] for r in gs.T}


def build():
    """form -> {recs, role, gen, completo, num} over every degree surface form."""
    forms = {}

    def add(form, rec, role, gen=None, completo=None, num=None):
        e = forms.get(form)
        if e is None:
            forms[form] = {"recs": [rec], "role": role, "gen": gen,
                           "completo": completo, "num": num}
        elif rec not in e["recs"]:
            e["recs"].append(rec)

    by_name = {r[0]: r for r in T}
    for rec in T:
        name, nivel, area, abbrevs, variants, holders, flags = rec
        add(name, rec, "nombre")
        for v in variants:
            add(v, rec, "sin")
        for i, a in enumerate(abbrevs):
            add(a, rec, "abrev" if i == 0 else "abrevsin", completo=name)
        for form, gen, completo in holders:
            add(form, rec, "poseedor", gen=gen, completo=completo)
    for form, name in PLURALS:
        add(form, by_name[name], "plural", num="p")
    return forms


def write_dict(forms, path, materia):
    out = io.StringIO()
    out.write(HDR_DICT)
    lines = []
    for form, e in forms.items():
        rec = e["recs"][0]
        name, nivel, area, abbrevs, variants, holders, flags = rec
        role = e["role"]
        attrs = []
        if role == "nombre":
            attrs.append("canonico=1")
        elif role in ("sin", "abrevsin"):
            attrs.append("sin=1")
        elif role == "poseedor":
            attrs.append("poseedor=1")
        attrs.append("titulo=" + q(name))
        if role == "nombre" and abbrevs:
            attrs.append("abrev=" + q(abbrevs[0]))
        if role in ("abrev", "abrevsin"):
            attrs.append("completo=" + q(name))
        if role == "poseedor" and e["completo"]:
            attrs.append("completo=" + q(e["completo"]))
        if e["gen"]:
            attrs.append("gen=" + e["gen"])
        if e["num"]:
            attrs.append("num=" + e["num"])
        attrs.append("nivel=" + q(nivel))
        if area:
            attrs.append("area=" + q(area))
        for f in ("es", "latam", "extranjero", "antiguo", "profesional", "honorifico"):
            if f in flags:
                attrs.append(f + "=1")
        if form in TRATAMIENTO:
            attrs.append("tratamiento=1")
        if form in materia:
            attrs.append("materia=1")
        if form in AMBIG or len(e["recs"]) > 1:
            attrs.append("ambig=1")
        lines.append((form, form + " " + " ".join(attrs)))

    for form, nivel, plural in LEVELWORDS:
        attrs = ["generico=1", "nivel=" + q(nivel)]
        if plural:
            attrs.append("num=p")
        if form in AMBIG:
            attrs.append("ambig=1")
        lines.append((form, form + " " + " ".join(attrs)))

    for _, line in sorted(lines, key=lambda x: skey(x[0])):
        out.write(line + "\n")
    save(path, out.getvalue())


def write_kbb(path):
    out = io.StringIO()
    out.write(HDR_KBB)
    out.write("grados\n")

    # --- forward branch: name -> degree --------------------------------------
    out.write("  titulo\n")
    for rec in sorted(T, key=lambda r: skey(r[0])):
        name, nivel, area, abbrevs, variants, holders, flags = rec
        attrs = ["nivel=" + q(nivel)]
        if area:
            attrs.append("area=" + q(area))
        if abbrevs:
            attrs.append("abrev=" + q(abbrevs[0]))
        if len(abbrevs) > 1:
            attrs.append("sinonimo=" + qlist(abbrevs[1:]))
        if variants:
            attrs.append("variante=" + qlist(variants))
        spelled = [h[0] for h in holders if not h[2]]
        if spelled:
            attrs.append("poseedor=" + qlist(spelled))
        for f in ("es", "latam", "extranjero", "antiguo", "profesional", "honorifico"):
            if f in flags:
                attrs.append(f + "=1")
        out.write("    " + name + ": " + ", ".join(attrs) + "\n")

    # --- reverse branch: abbreviation -> name --------------------------------
    out.write("  abrev\n")
    rows = {}
    for rec in T:
        name, nivel, area, abbrevs, variants, holders, flags = rec
        for a in abbrevs:
            rows.setdefault(a, {"titulos": [], "completo": None, "gen": None, "nivel": nivel})
            if name not in rows[a]["titulos"]:
                rows[a]["titulos"].append(name)
        for form, gen, completo in holders:
            if completo:
                rows.setdefault(form, {"titulos": [], "completo": completo, "gen": gen, "nivel": nivel})
                if name not in rows[form]["titulos"]:
                    rows[form]["titulos"].append(name)
    for a in sorted(rows, key=skey):
        r = rows[a]
        attrs = []
        if len(r["titulos"]) > 1:
            attrs.append("ambig=1")
        attrs.append("titulo=" + qlist(r["titulos"]))
        if r["completo"]:
            attrs.append("completo=" + q(r["completo"]))
            attrs.append("poseedor=1")
        if r["gen"]:
            attrs.append("gen=" + r["gen"])
        attrs.append("nivel=" + q(r["nivel"]))
        if a in TRATAMIENTO:
            attrs.append("tratamiento=1")
        out.write("    " + a + ": " + ", ".join(attrs) + "\n")

    # --- level branch: level -> its words and its degrees ---------------------
    out.write("  nivel\n")
    for level in LEVEL_ORDER + sorted(COVER):
        words = [w for w, lv, _ in LEVELWORDS if lv == level]
        degs = sorted({r[0] for r in T if r[1] == level}, key=skey)
        attrs = []
        if words:
            attrs.append("palabra=[" + ",".join(q(w) for w in words) + "]")
        if level in COVER:
            attrs.append("incluye=[" + ",".join(q(c) for c in COVER[level]) + "]")
        if degs:
            attrs.append("titulo=[" + ",".join(q(d) for d in degs) + "]")
        out.write("    " + level + ": " + ", ".join(attrs) + "\n")

    save(path, out.getvalue())


def save(path, text):
    with open(path, "wb") as f:
        f.write(text.replace("\n", "\r\n").encode("utf-8"))
    print("wrote", path, len(text.splitlines()), "lines")


def dict_key(line):
    parts = []
    for tok in line.split(" "):
        if "=" in tok:
            break
        parts.append(tok)
    return " ".join(parts).lower()


def report(forms, d, subj_names):
    names = [r[0] for r in T]
    print("duplicate degree names:",
          sorted({n for n in names if names.count(n) > 1}))
    print("surface forms shared by several degrees:",
          sorted(f for f in forms if len(forms[f]["recs"]) > 1))
    print("area= values that are not a subject in gen_subjects_es:",
          sorted({r[2] for r in T if r[2] and r[2] not in subj_names}))
    print("levels used but not ordered:",
          sorted({r[1] for r in T if r[1] not in LEVEL_ORDER}))

    all_forms = set(forms) | {w for w, _, _ in LEVELWORDS}
    print("multi-word forms the .dict loader rejects (accented later word):",
          sorted(f for f in all_forms
                 if any(ord(w[0]) > 127 for w in f.split(" ")[1:])))
    print("AMBIG entries that are not a form here:",
          sorted(a for a in AMBIG if a not in all_forms))
    print("TRATAMIENTO entries that are not a form here:",
          sorted(a for a in TRATAMIENTO if a not in all_forms))

    p = os.path.join(d, "es-tratamientos.dict")
    if os.path.exists(p):
        with open(p, "r", encoding="utf-8") as f:
            trat = {dict_key(l.strip()) for l in f if l.strip() and not l.startswith("#")}
        print("forms in es-tratamientos.dict but not marked tratamiento:",
              sorted(f for f in all_forms if f in trat and f not in TRATAMIENTO))
        print("TRATAMIENTO entries es-tratamientos.dict does not have:",
              sorted(a for a in TRATAMIENTO if a not in trat))

    siblings = ["es-function-words.dict", "sp-names.dict", "es-mesesdias.dict",
                "es-direcciones.dict", "es-numeros.dict", "es-complementos.dict",
                "es-paises.dict", "es-nacionalidades.dict", "es-idiomas.dict",
                "es-apellidos.dict"]
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
              sorted(f for f in all_forms
                     if f in known and f not in AMBIG and f not in TRATAMIENTO))

    # Single-token abbreviations that es-full.dict also knows as a word.
    p = os.path.join(d, "es-full.dict")
    if os.path.exists(p):
        abbr = {f for f, e in forms.items()
                if e["role"] in ("abrev", "abrevsin") or (e["role"] == "poseedor" and e["completo"])}
        words = set()
        with open(p, "r", encoding="utf-8") as f:
            for line in f:
                if line and not line.startswith("#"):
                    w = line.split(" ", 1)[0]
                    if w in abbr:
                        words.add(w)
        print("abbreviations es-full.dict also has as a word, not marked ambig:",
              sorted(w for w in words if w not in AMBIG))
    print("degrees:", len(T), " surface forms:", len(all_forms))


if __name__ == "__main__":
    if len(sys.argv) > 1:
        d = sys.argv[1]
    else:
        here = os.path.dirname(os.path.abspath(__file__))
        d = os.path.join(here, os.pardir, "languages", "Spanish")
    d = os.path.normpath(d)
    forms = build()
    materia, subj_names = subject_forms()
    write_dict(forms, os.path.join(d, "es-grados-academicos.dict"), materia)
    write_kbb(os.path.join(d, "es-grados-academicos.kbb"))
    report(forms, d, subj_names)
