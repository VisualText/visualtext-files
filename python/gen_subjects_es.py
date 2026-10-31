# -*- coding: utf-8 -*-
# DESC: Generate the Spanish subject / field-of-study dictionary and knowledge base.
#
# WHAT IT DOES
#   Emits languages/Spanish/es-areas-de-estudio.dict and es-areas-de-estudio.kbb
#   from the single master table T below, so the two files can never drift
#   apart.  Edit T and re-run; do not hand-edit the generated files.
#   Spanish counterpart of gen_subjects.py (en-subjects.dict / .kbb).
#
#   The .dict gets one line per surface form: the subject name, every synonym
#   and every adjective form (masculine and, where it differs, feminine).  The
#   .kbb gets two branches under "areas":
#       area  - forward lookup, subject -> rama, padre, hijos, synonyms
#       rama  - broad division -> the subjects that sit in it
#   Every .dict line carries "area=<canonical name>", so rules join into the
#   knowledge base on that attribute rather than on $text.
#
#   The canonical names are also the vocabulary of area= in
#   es-grados-academicos.dict: report() checks every area= value there against
#   this table and prints any that would not join.
#
#   Master table row:
#     (name, rama, padre, [synonyms], [adjectives], [flags])
#     padre   the broader subject this one sits under, or None
#     adjectives are given in the masculine singular; a feminine form is
#             derived for every adjective ending in -o (biológico -> biológica)
#     A multi-word form whose second or later word starts with an accented
#     letter (valores éticos, formación cívica y ética) is rejected by the
#     .dict loader ("Unhandled" at load time) in the current engine, so such
#     forms are left out of T until that is fixed; report() lists any that
#     slip in.
#     flags   may hold "escolar" (a common primary / secondary school subject in
#             Spain or Latin America) and "idioma" (the name is also a language
#             and a nationality adjective, see es-idiomas.dict)
#
# USAGE
#   python gen_subjects_es.py [output_dir]
#     output_dir  defaults to ../languages/Spanish relative to this script

import io, os, sys, unicodedata

CN = "ciencias naturales"
CF = "ciencias formales"
CS = "ciencias sociales"
HU = "humanidades"
AR = "artes"
IN = "ingeniería"
SA = "salud"
NE = "negocios"
ED = "educación"
DE = "derecho"
AG = "agricultura"
IT = "interdisciplinario"

# name, rama, padre, synonyms, adjectives, flags
T = [
 # --- ciencias naturales ---------------------------------------------------
 ("ciencias naturales",CN,None,["ciencias","ciencia","ciencias de la naturaleza"],["científico"],["escolar"]),
 ("conocimiento del medio",CN,"ciencias naturales",["conocimiento del medio natural","ciencias del entorno"],[],["escolar"]),
 ("biología",CN,"ciencias naturales",["ciencias biológicas","ciencias de la vida"],["biológico"],["escolar"]),
 ("biología y geología",CN,"ciencias naturales",[],[],["escolar"]),
 ("botánica",CN,"biología",["biología vegetal"],["botánico"],[]),
 ("zoología",CN,"biología",["biología animal"],["zoológico"],[]),
 ("microbiología",CN,"biología",[],["microbiológico"],[]),
 ("biología molecular",CN,"biología",[],[],[]),
 ("biología celular",CN,"biología",["citología"],[],[]),
 ("genética",CN,"biología",[],["genético"],[]),
 ("genómica",CN,"genética",[],["genómico"],[]),
 ("bioquímica",CN,"biología",[],["bioquímico"],[]),
 ("biofísica",CN,"biología",[],["biofísico"],[]),
 ("ecología",CN,"biología",[],["ecológico"],[]),
 ("biología marina",CN,"biología",[],[],[]),
 ("neurociencia",CN,"biología",["neurociencias","neurobiología"],[],[]),
 ("fisiología",CN,"biología",[],["fisiológico"],[]),
 ("anatomía",CN,"biología",[],["anatómico"],[]),
 ("inmunología",CN,"biología",[],["inmunológico"],[]),
 ("virología",CN,"biología",[],[],[]),
 ("bacteriología",CN,"biología",[],[],[]),
 ("micología",CN,"biología",[],[],[]),
 ("entomología",CN,"biología",[],[],[]),
 ("ornitología",CN,"biología",[],[],[]),
 ("paleontología",CN,"biología",[],["paleontológico"],[]),
 ("biología evolutiva",CN,"biología",[],[],[]),
 ("biotecnología",CN,"biología",[],["biotecnológico"],[]),
 ("química",CN,"ciencias naturales",["ciencias químicas"],["químico"],["escolar"]),
 ("física y química",CN,"ciencias naturales",[],[],["escolar"]),
 ("química orgánica",CN,"química",[],[],[]),
 ("química inorgánica",CN,"química",[],[],[]),
 ("fisicoquímica",CN,"química",["química física"],[],[]),
 ("química analítica",CN,"química",[],[],[]),
 ("física",CN,"ciencias naturales",["ciencias físicas"],["físico"],["escolar"]),
 ("astrofísica",CN,"física",[],[],[]),
 ("física nuclear",CN,"física",[],[],[]),
 ("física de partículas",CN,"física",["física de altas energías"],[],[]),
 ("mecánica cuántica",CN,"física",["física cuántica"],[],[]),
 ("termodinámica",CN,"física",[],[],[]),
 ("óptica",CN,"física",[],["óptico"],[]),
 ("mecánica",CN,"física",[],["mecánico"],[]),
 ("astronomía",CN,"ciencias naturales",[],["astronómico"],[]),
 ("cosmología",CN,"astronomía",[],["cosmológico"],[]),
 ("ciencias planetarias",CN,"astronomía",[],[],[]),
 ("ciencias de la tierra",CN,"ciencias naturales",["geociencias"],[],["escolar"]),
 ("geología",CN,"ciencias de la tierra",["ciencias geológicas"],["geológico"],[]),
 ("meteorología",CN,"ciencias de la tierra",[],["meteorológico"],[]),
 ("oceanografía",CN,"ciencias de la tierra",["ciencias del mar"],["oceanográfico"],[]),
 ("climatología",CN,"ciencias de la tierra",[],["climatológico"],[]),
 ("sismología",CN,"ciencias de la tierra",[],[],[]),
 ("hidrología",CN,"ciencias de la tierra",[],[],[]),
 ("edafología",CN,"ciencias de la tierra",["ciencia del suelo"],[],[]),
 ("ciencias ambientales",CN,"ciencias de la tierra",["ciencias del medio ambiente"],["ambiental"],["escolar"]),

 # --- ciencias formales ----------------------------------------------------
 ("matemáticas",CF,None,["matemática","mates"],["matemático"],["escolar"]),
 ("aritmética",CF,"matemáticas",[],["aritmético"],["escolar"]),
 ("álgebra",CF,"matemáticas",[],["algebraico"],["escolar"]),
 ("geometría",CF,"matemáticas",[],["geométrico"],["escolar"]),
 ("trigonometría",CF,"matemáticas",[],["trigonométrico"],["escolar"]),
 ("cálculo",CF,"matemáticas",[],[],["escolar"]),
 ("estadística",CF,"matemáticas",[],["estadístico"],["escolar"]),
 ("probabilidad",CF,"matemáticas",[],[],[]),
 ("teoría de números",CF,"matemáticas",[],[],[]),
 ("topología",CF,"matemáticas",[],["topológico"],[]),
 ("álgebra lineal",CF,"matemáticas",[],[],[]),
 ("matemática discreta",CF,"matemáticas",["matemáticas discretas"],[],[]),
 ("matemática aplicada",CF,"matemáticas",["matemáticas aplicadas"],[],[]),
 ("lógica",CF,None,[],["lógico"],[]),
 ("informática",CF,None,["ciencias de la computación","ciencias de la informática","computación","ciencia de la computación"],["informático","computacional"],["escolar"]),
 ("ingeniería de software",CF,"informática",["ingeniería del software"],[],[]),
 ("inteligencia artificial",CF,"informática",["ia"],[],[]),
 ("aprendizaje automático",CF,"inteligencia artificial",["aprendizaje de máquina"],[],[]),
 ("ciencia de datos",CF,"informática",[],[],[]),
 ("ciberseguridad",CF,"informática",["seguridad informática","seguridad de la información"],[],[]),
 ("tecnologías de la información",CF,"informática",["ti","tic","tecnologías de la información y la comunicación"],[],["escolar"]),
 ("sistemas de información",CF,"informática",["sistemas"],[],[]),
 ("gráficos por computadora",CF,"informática",["computación gráfica","informática gráfica"],[],[]),
 ("interacción persona-computadora",CF,"informática",["interacción persona-ordenador","interacción humano-computadora"],[],[]),
 ("biblioteconomía",CF,None,["bibliotecología","ciencias de la información","biblioteconomía y documentación"],[],[]),

 # --- ciencias sociales ----------------------------------------------------
 ("ciencias sociales",CS,None,["estudios sociales"],[],["escolar"]),
 ("historia",CS,"ciencias sociales",[],["histórico"],["escolar"]),
 ("historia antigua",CS,"historia",[],[],[]),
 ("historia universal",CS,"historia",["historia del mundo contemporáneo","historia mundial"],[],["escolar"]),
 ("historia de españa",CS,"historia",[],[],["escolar"]),
 ("historia de méxico",CS,"historia",[],[],["escolar"]),
 ("historia de américa",CS,"historia",["historia de américa latina","historia latinoamericana"],[],[]),
 ("historia del arte",CS,"historia",[],[],["escolar"]),
 ("geografía",CS,"ciencias sociales",[],["geográfico"],["escolar"]),
 ("geografía e historia",CS,"ciencias sociales",[],[],["escolar"]),
 ("geografía humana",CS,"geografía",[],[],[]),
 ("geografía física",CS,"geografía",[],[],[]),
 ("economía",CS,"ciencias sociales",["ciencias económicas"],["económico"],["escolar"]),
 ("microeconomía",CS,"economía",[],[],[]),
 ("macroeconomía",CS,"economía",[],[],[]),
 ("econometría",CS,"economía",[],[],[]),
 ("ciencia política",CS,"ciencias sociales",["ciencias políticas","politología","política"],["político"],[]),
 ("relaciones internacionales",CS,"ciencia política",["estudios internacionales","asuntos internacionales"],[],[]),
 ("políticas públicas",CS,"ciencia política",[],[],[]),
 ("administración pública",CS,"ciencia política",["gestión pública"],[],[]),
 ("educación cívica",CS,"ciencias sociales",["civismo","educación para la ciudadanía","formación ciudadana"],["cívico"],["escolar"]),
 ("sociología",CS,None,[],["sociológico"],["escolar"]),
 ("criminología",CS,"sociología",[],["criminológico"],[]),
 ("demografía",CS,"sociología",[],["demográfico"],[]),
 ("trabajo social",CS,"sociología",[],[],[]),
 ("psicología",CS,None,[],["psicológico"],["escolar"]),
 ("psicología clínica",CS,"psicología",[],[],[]),
 ("psicología del desarrollo",CS,"psicología",["psicología evolutiva"],[],[]),
 ("psicología social",CS,"psicología",[],[],[]),
 ("psicología educativa",CS,"psicología",["psicología de la educación","psicopedagogía"],[],[]),
 ("ciencias cognitivas",CS,"psicología",["ciencia cognitiva"],["cognitivo"],[]),
 ("antropología",CS,None,[],["antropológico"],[]),
 ("arqueología",CS,"antropología",[],["arqueológico"],[]),
 ("lingüística",CS,None,[],["lingüístico"],[]),
 ("comunicación",CS,None,["ciencias de la comunicación","comunicación social"],[],[]),
 ("periodismo",CS,"comunicación",[],["periodístico"],[]),
 ("relaciones públicas",CS,"comunicación",[],[],[]),
 ("comunicación audiovisual",CS,"comunicación",["estudios de medios"],[],[]),
 ("publicidad",CS,"comunicación",["publicidad y relaciones públicas"],["publicitario"],[]),
 ("urbanismo",CS,None,["planificación urbana","planeación urbana","estudios urbanos"],["urbanístico"],[]),
 ("estudios de género",CS,None,["estudios de la mujer"],[],[]),

 # --- humanidades ----------------------------------------------------------
 ("humanidades",HU,None,[],["humanístico"],[]),
 ("lengua castellana",HU,"humanidades",["lengua castellana y literatura","lengua y literatura","lengua","castellano","lenguaje","lenguaje y comunicación","lengua española","español"],[],["escolar","idioma"]),
 ("literatura",HU,"lengua castellana",[],["literario"],["escolar"]),
 ("poesía",HU,"literatura",[],["poético"],[]),
 ("escritura creativa",HU,"lengua castellana",["creación literaria"],[],[]),
 ("redacción",HU,"lengua castellana",["composición","expresión escrita"],[],["escolar"]),
 ("retórica",HU,"lengua castellana",[],["retórico"],[]),
 ("gramática",HU,"lengua castellana",[],["gramatical"],["escolar"]),
 ("ortografía",HU,"lengua castellana",[],["ortográfico"],["escolar"]),
 ("lectura",HU,"lengua castellana",["comprensión lectora","lectoescritura"],[],["escolar"]),
 ("filología",HU,"humanidades",["filología hispánica"],["filológico"],[]),
 ("filosofía",HU,"humanidades",[],["filosófico"],["escolar"]),
 ("ética",HU,"filosofía",["moral"],["ético"],["escolar"]),
 ("metafísica",HU,"filosofía",[],["metafísico"],[]),
 ("epistemología",HU,"filosofía",[],["epistemológico"],[]),
 ("estudios clásicos",HU,"humanidades",["filología clásica","cultura clásica"],["clásico"],["escolar"]),
 ("latín",HU,"estudios clásicos",[],[],["escolar","idioma"]),
 ("griego",HU,"estudios clásicos",["griego antiguo"],[],["escolar","idioma"]),
 ("ciencias de las religiones",HU,"humanidades",["estudios religiosos"],[],[]),
 ("religión",HU,"ciencias de las religiones",["educación religiosa","religión católica"],["religioso"],["escolar"]),
 ("teología",HU,"ciencias de las religiones",["ciencias religiosas"],["teológico"],[]),
 ("lenguas extranjeras",HU,"humanidades",["lenguas modernas","idiomas","idioma extranjero"],[],["escolar"]),
 ("inglés",HU,"lenguas extranjeras",["lengua inglesa"],[],["escolar","idioma"]),
 ("francés",HU,"lenguas extranjeras",["lengua francesa"],[],["escolar","idioma"]),
 ("alemán",HU,"lenguas extranjeras",["lengua alemana"],[],["escolar","idioma"]),
 ("italiano",HU,"lenguas extranjeras",[],[],["idioma"]),
 ("portugués",HU,"lenguas extranjeras",[],[],["escolar","idioma"]),
 ("ruso",HU,"lenguas extranjeras",[],[],["idioma"]),
 ("chino",HU,"lenguas extranjeras",["mandarín","chino mandarín"],[],["idioma"]),
 ("japonés",HU,"lenguas extranjeras",[],[],["idioma"]),
 ("coreano",HU,"lenguas extranjeras",[],[],["idioma"]),
 ("árabe",HU,"lenguas extranjeras",[],[],["idioma"]),
 ("hebreo",HU,"lenguas extranjeras",[],[],["idioma"]),
 ("lenguas cooficiales",HU,"humanidades",["lengua cooficial","lengua propia"],[],["escolar"]),
 ("catalán",HU,"lenguas cooficiales",["valenciano","lengua catalana"],[],["escolar","idioma"]),
 ("gallego",HU,"lenguas cooficiales",["lengua gallega"],[],["escolar","idioma"]),
 ("euskera",HU,"lenguas cooficiales",["vasco","euskara","lengua vasca"],[],["escolar","idioma"]),
 ("letras",HU,"humanidades",["filosofía y letras"],[],[]),

 # --- artes ----------------------------------------------------------------
 ("arte",AR,None,["artes visuales","artes plásticas","bellas artes","artes","educación artística","educación plástica","plástica","educación plástica y visual","expresión plástica"],["artístico"],["escolar"]),
 ("dibujo",AR,"arte",[],[],["escolar"]),
 ("pintura",AR,"arte",[],["pictórico"],[]),
 ("escultura",AR,"arte",[],["escultórico"],[]),
 ("fotografía",AR,"arte",[],["fotográfico"],[]),
 ("cerámica",AR,"arte",["alfarería"],[],[]),
 ("grabado",AR,"arte",[],[],[]),
 ("diseño",AR,None,[],[],[]),
 ("diseño gráfico",AR,"diseño",[],[],[]),
 ("diseño industrial",AR,"diseño",[],[],[]),
 ("diseño de moda",AR,"diseño",["diseño de modas"],[],[]),
 ("diseño de interiores",AR,"diseño",["interiorismo"],[],[]),
 ("arquitectura",AR,None,[],["arquitectónico"],[]),
 ("arquitectura del paisaje",AR,"arquitectura",["paisajismo"],[],[]),
 ("música",AR,None,["educación musical"],["musical"],["escolar"]),
 ("teoría musical",AR,"música",["lenguaje musical","solfeo"],[],["escolar"]),
 ("composición musical",AR,"música",[],[],[]),
 ("teatro",AR,None,["artes escénicas","arte dramático","dramaturgia"],["teatral","dramático"],["escolar"]),
 ("danza",AR,None,["baile"],[],["escolar"]),
 ("cine",AR,None,["cinematografía","estudios cinematográficos"],["cinematográfico"],[]),

 # --- ingeniería -----------------------------------------------------------
 ("ingeniería",IN,None,[],[],[]),
 ("ingeniería civil",IN,"ingeniería",["ingeniería de caminos","ingeniería de caminos canales y puertos"],[],[]),
 ("ingeniería mecánica",IN,"ingeniería",[],[],[]),
 ("ingeniería eléctrica",IN,"ingeniería",[],[],[]),
 ("ingeniería electrónica",IN,"ingeniería",[],[],[]),
 ("ingeniería química",IN,"ingeniería",[],[],[]),
 ("ingeniería aeroespacial",IN,"ingeniería",["ingeniería aeronáutica"],[],[]),
 ("ingeniería biomédica",IN,"ingeniería",["bioingeniería"],[],[]),
 ("ingeniería industrial",IN,"ingeniería",[],[],[]),
 ("ingeniería ambiental",IN,"ingeniería",[],[],[]),
 ("ingeniería nuclear",IN,"ingeniería",[],[],[]),
 ("ingeniería de minas",IN,"ingeniería",[],[],[]),
 ("ingeniería petrolera",IN,"ingeniería",["ingeniería de petróleos","ingeniería en petróleo"],[],[]),
 ("ingeniería estructural",IN,"ingeniería civil",[],[],[]),
 ("ingeniería de sistemas",IN,"ingeniería",["ingeniería en sistemas"],[],[]),
 ("ingeniería informática",IN,"ingeniería",["ingeniería en computación","ingeniería en informática","ingeniería de computadores"],[],[]),
 ("ingeniería de telecomunicaciones",IN,"ingeniería",["ingeniería en telecomunicaciones","telecomunicaciones"],[],[]),
 ("gestión de la ingeniería",IN,"ingeniería",[],[],[]),
 ("ciencia de materiales",IN,"ingeniería",["ingeniería de materiales","ciencia e ingeniería de materiales"],[],[]),
 ("robótica",IN,"ingeniería",[],[],[]),
 ("tecnología",IN,None,[],["tecnológico"],["escolar"]),
 ("talleres",IN,"tecnología",["taller","educación tecnológica"],[],["escolar"]),
 ("dibujo técnico",IN,"tecnología",[],[],["escolar"]),

 # --- salud ----------------------------------------------------------------
 ("medicina",SA,None,["ciencias médicas"],["médico"],[]),
 ("cirugía",SA,"medicina",[],["quirúrgico"],[]),
 ("pediatría",SA,"medicina",[],["pediátrico"],[]),
 ("psiquiatría",SA,"medicina",[],["psiquiátrico"],[]),
 ("cardiología",SA,"medicina",[],[],[]),
 ("oncología",SA,"medicina",[],["oncológico"],[]),
 ("radiología",SA,"medicina",[],[],[]),
 ("neurología",SA,"medicina",[],["neurológico"],[]),
 ("patología",SA,"medicina",["anatomía patológica"],["patológico"],[]),
 ("anestesiología",SA,"medicina",["anestesia"],[],[]),
 ("dermatología",SA,"medicina",[],[],[]),
 ("obstetricia",SA,"medicina",[],[],[]),
 ("ginecología",SA,"medicina",[],["ginecológico"],[]),
 ("traumatología",SA,"medicina",["ortopedia"],[],[]),
 ("geriatría",SA,"medicina",[],["geriátrico"],[]),
 ("medicina familiar",SA,"medicina",["medicina de familia","medicina general"],[],[]),
 ("enfermería",SA,None,[],[],[]),
 ("farmacia",SA,None,["ciencias farmacéuticas","química farmacéutica"],["farmacéutico"],[]),
 ("odontología",SA,None,["estomatología","cirugía dental"],["odontológico","dental"],[]),
 ("veterinaria",SA,None,["medicina veterinaria","medicina veterinaria y zootecnia"],["veterinario"],[]),
 ("optometría",SA,None,["óptica y optometría"],[],[]),
 ("audiología",SA,None,["fonoaudiología"],[],[]),
 ("podología",SA,None,[],[],[]),
 ("quiropráctica",SA,None,[],[],[]),
 ("fisioterapia",SA,None,["kinesiología","terapia física"],[],[]),
 ("terapia ocupacional",SA,None,[],[],[]),
 ("logopedia",SA,None,["terapia del lenguaje","fonoaudiología clínica"],[],[]),
 ("salud pública",SA,None,[],[],[]),
 ("epidemiología",SA,"salud pública",[],["epidemiológico"],[]),
 ("administración de servicios de salud",SA,"salud pública",["gestión sanitaria","administración hospitalaria"],[],[]),
 ("nutrición",SA,None,["nutrición y dietética","dietética"],["nutricional"],[]),
 ("ciencias del deporte",SA,None,["ciencias de la actividad física y del deporte","cafyd"],[],[]),
 ("educación física",SA,None,["educación física y deportes","gimnasia","ed física"],[],["escolar"]),
 ("educación para la salud",SA,None,["salud"],[],["escolar"]),

 # --- negocios -------------------------------------------------------------
 ("administración de empresas",NE,None,["administración","administración y dirección de empresas","ade","empresariales","ciencias empresariales","negocios"],["empresarial"],["escolar"]),
 ("contabilidad",NE,"administración de empresas",["contaduría","contaduría pública"],["contable"],["escolar"]),
 ("finanzas",NE,"administración de empresas",[],["financiero"],[]),
 ("mercadotecnia",NE,"administración de empresas",["marketing","mercadeo"],[],[]),
 ("gestión",NE,"administración de empresas",["dirección","gerencia"],["gerencial"],[]),
 ("emprendimiento",NE,"administración de empresas",[],[],[]),
 ("recursos humanos",NE,"gestión",["gestión de recursos humanos","relaciones laborales"],[],[]),
 ("comercio internacional",NE,"administración de empresas",["negocios internacionales"],[],[]),
 ("logística",NE,"gestión",["gestión de la cadena de suministro","cadena de suministro"],["logístico"],[]),
 ("bienes raíces",NE,"administración de empresas",["gestión inmobiliaria"],["inmobiliario"],[]),
 ("turismo",NE,"gestión",["hotelería","administración hotelera","hotelería y turismo"],["turístico"],[]),
 ("ciencias actuariales",NE,"administración de empresas",["actuaría"],["actuarial"],[]),
 ("tributación",NE,"contabilidad",["fiscalidad"],["tributario","fiscal"],[]),

 # --- educación ------------------------------------------------------------
 ("educación",ED,None,["ciencias de la educación"],["educativo"],[]),
 ("educación infantil",ED,"educación",["educación preescolar","educación inicial","educación parvularia"],[],[]),
 ("educación primaria",ED,"educación",["educación básica"],[],[]),
 ("educación secundaria",ED,"educación",["educación media"],[],[]),
 ("educación especial",ED,"educación",["pedagogía terapéutica"],[],[]),
 ("didáctica",ED,"educación",["currículo y didáctica"],["didáctico"],[]),
 ("pedagogía",ED,"educación",["docencia","magisterio"],["pedagógico"],[]),
 ("orientación",ED,"educación",["tutoría","orientación educativa","orientación vocacional"],[],["escolar"]),

 # --- derecho --------------------------------------------------------------
 ("derecho",DE,None,["ciencias jurídicas","jurisprudencia","leyes"],["jurídico","legal"],[]),
 ("criminalística",DE,"derecho",["ciencias penales","criminalística y ciencias forenses"],[],[]),
 ("derecho internacional",DE,"derecho",[],[],[]),
 ("derecho constitucional",DE,"derecho",[],[],[]),
 ("derecho penal",DE,"derecho",[],[],[]),
 ("derecho civil",DE,"derecho",[],[],[]),
 ("notariado",DE,"derecho",["derecho notarial"],["notarial"],[]),

 # --- agricultura ----------------------------------------------------------
 ("agricultura",AG,None,["ciencias agrarias","ciencias agrícolas","agronomía general"],["agrícola"],[]),
 ("agronomía",AG,"agricultura",["ingeniería agronómica","ingeniería agrícola"],["agronómico"],[]),
 ("horticultura",AG,"agricultura",[],["hortícola"],[]),
 ("zootecnia",AG,"agricultura",["producción animal","ganadería"],["zootécnico"],[]),
 ("ingeniería forestal",AG,"agricultura",["ciencias forestales","silvicultura"],["forestal"],[]),
 ("ciencia de los alimentos",AG,"agricultura",["ciencia y tecnología de los alimentos","ingeniería de alimentos","tecnología de alimentos"],["alimentario"],[]),
 ("pesquerías",AG,"agricultura",["ciencias pesqueras","acuicultura"],["pesquero"],[]),

 # --- interdisciplinario ---------------------------------------------------
 ("estudios generales",IT,None,["estudios liberales","artes liberales"],[],[]),
 ("ciencias aplicadas",IT,None,[],[],[]),
 ("artes aplicadas",IT,None,["artes y oficios"],[],[]),
 ("estudios interdisciplinarios",IT,None,["estudios multidisciplinarios"],[],[]),
 ("estudios ambientales",IT,None,[],[],[]),
 ("sostenibilidad",IT,"estudios ambientales",["sustentabilidad","desarrollo sostenible"],["sostenible","sustentable"],[]),
 ("investigación",IT,None,[],[],[]),
 ("economía doméstica",IT,None,["hogar","educación para el hogar"],[],["escolar"]),
 ("educación vial",IT,None,["seguridad vial"],[],["escolar"]),
 ("mecanografía",IT,None,["mecanografía y taquigrafía"],[],["escolar"]),
]

AREA_ORDER = [CN, CF, CS, HU, AR, IN, SA, NE, ED, DE, AG, IT]

HDR_DICT = """\
# Áreas de estudio en español: asignaturas escolares y disciplinas académicas.
# Una línea por forma de superficie.
#   area=         el nombre canónico de la materia -- en todas las entradas, de
#                 modo que las reglas se unen a es-areas-de-estudio.kbb por este
#                 atributo y no por $text
#   rama=         la gran división en la que se sitúa (ciencias naturales,
#                 ciencias formales, ciencias sociales, humanidades, artes,
#                 ingeniería, salud, negocios, educación, derecho, agricultura,
#                 interdisciplinario)
#   padre=        la materia más amplia de la que depende, si la hay
#   canonico=1    la forma es el nombre canónico    sin=1  un sinónimo
#   adj=1         una forma adjetiva (biológico, matemática)
#   gen=m|f       género de una forma adjetiva que lo marca (biológico /
#                 biológica); los adjetivos invariables (ambiental) no lo llevan
#   escolar=1     una asignatura habitual de primaria o secundaria en España o
#                 Latinoamérica
#   idioma=1      el nombre es también una lengua y un gentilicio (inglés,
#                 francés, latín) -- véanse es-idiomas.dict, es-nacionalidades.dict
#   carrera=1     la forma es también el nombre de un título en
#                 es-grados-academicos.dict (ingeniería civil, arquitectura)
#   ambig=1       la forma es también una entrada de otro diccionario de la
#                 biblioteca
# Casi todos los nombres de materia son también palabras corrientes (arte,
# historia, lectura, diseño, derecho), así que una lectura como materia siempre
# necesita contexto: "licenciado en", "estudió", "clase de", "departamento de"
# o un plan de estudios.  El diccionario no lo marca; solo se marcan las
# colisiones con otros diccionarios de la biblioteca.
# Los nombres canónicos son el vocabulario de area= en
# es-grados-academicos.dict, de modo que un título se une a su materia por ese
# atributo.
# Generado por python/gen_subjects_es.py; no editar a mano.
"""

HDR_KBB = """\
# Áreas de estudio en español, relacionadas con sus grandes ramas.
# Búsqueda directa:  materia -> rama   (concepto "areas area biología" -> rama="ciencias naturales")
# Búsqueda por rama: rama -> sus materias
# El árbol se recorre en ambos sentidos: padre= apunta hacia arriba, hijo= hacia abajo.
#   rama=         ciencias naturales | ciencias formales | ciencias sociales |
#                 humanidades | artes | ingeniería | salud | negocios |
#                 educación | derecho | agricultura | interdisciplinario
#   padre=        la materia más amplia de la que depende
#   hijo=         las materias que dependen directamente de esta
#   sinonimo=     nombres alternativos     adjetivo=  formas adjetivas (masculino)
#   escolar=1     una asignatura habitual de primaria o secundaria
#   idioma=1      el nombre es también una lengua y un gentilicio
# En la rama: total= número de materias, raiz= las que no tienen padre,
# area= todas las materias de la rama.
# Los nombres de materia son el vocabulario de area= en
# es-grados-academicos.dict, de modo que un título se une a su materia por ese
# atributo.
# Todas las formas nombradas aquí están etiquetadas en es-areas-de-estudio.dict.
# Generado por python/gen_subjects_es.py; no editar a mano.
"""


def q(s):
    """Quote a value for a .dict / .kbb attribute when it is not a bare token."""
    # The dictionary loader mangles an unquoted value whose first letter is
    # not ASCII (area=ética loads as a broken byte string), so quote those.
    if s and ord(s[0]) < 128 and all(c.isalnum() or c in "_-." for c in s):
        return s
    return '"' + s.replace('"', '\\"') + '"'


def fem(adj):
    """Feminine of a masculine adjective ending in -o, else None."""
    return adj[:-1] + "a" if adj.endswith("o") else None


def build():
    """form -> (rec, role, gen) over every surface form in T; first reading wins."""
    forms = {}
    for rec in T:
        name, rama, padre, syns, adjs, flags = rec
        cand = [(name, "canonico", None)] + [(s, "sin", None) for s in syns]
        for a in adjs:
            f = fem(a)
            cand.append((a, "adj", "m" if f else None))
            if f:
                cand.append((f, "adj", "f"))
        for form, role, gen in cand:
            if form not in forms:
                forms[form] = (rec, role, gen)
    return forms


def dict_key(line):
    """The entry word of a .dict line: every token before the first attr=."""
    parts = []
    for tok in line.split(" "):
        if "=" in tok:
            break
        parts.append(tok)
    return " ".join(parts).lower()


SIBLINGS = ("es-idiomas.dict", "es-nacionalidades.dict", "es-paises.dict",
            "es-tratamientos.dict",
            "es-function-words.dict", "es-mesesdias.dict", "es-numeros.dict",
            "es-direcciones.dict", "es-complementos.dict")


def skey(s):
    """Sort key that ignores accents, so cálculo sorts next to calculo."""
    base = "".join(c for c in unicodedata.normalize("NFD", s)
                   if unicodedata.category(c) != "Mn")
    return (base, s)


def degree_forms():
    """Every surface form of es-grados-academicos, from gen_degrees_es."""
    sys.dont_write_bytecode = True
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import gen_degrees_es as gd
    return set(gd.build().keys())


def ambiguous(d):
    """Forms that another library dictionary also carries."""
    known = set()
    for fn in SIBLINGS:
        p = os.path.join(d, fn)
        if not os.path.exists(p):
            continue
        with open(p, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#"):
                    known.add(dict_key(line))
    return known


def write_dict(forms, path, known, titulos):
    out = io.StringIO()
    out.write(HDR_DICT)
    for form in sorted(forms, key=skey):
        rec, role, gen = forms[form]
        name, rama, padre, syns, adjs, flags = rec
        attrs = [role + "=1", "area=" + q(name), "rama=" + q(rama)]
        if padre:
            attrs.append("padre=" + q(padre))
        if gen:
            attrs.append("gen=" + gen)
        if "escolar" in flags:
            attrs.append("escolar=1")
        if "idioma" in flags:
            attrs.append("idioma=1")
        if form in titulos:
            attrs.append("carrera=1")
        if form in known:
            attrs.append("ambig=1")
        out.write(form + " " + " ".join(attrs) + "\n")
    save(path, out.getvalue())


def write_kbb(path):
    out = io.StringIO()
    out.write(HDR_KBB)
    out.write("areas\n")

    children = {}
    for rec in T:
        if rec[2]:
            children.setdefault(rec[2], []).append(rec[0])

    # --- forward branch: subject -> rama, padre, hijos -----------------------
    out.write("  area\n")
    for rec in sorted(T, key=lambda r: skey(r[0])):
        name, rama, padre, syns, adjs, flags = rec
        attrs = ["rama=" + q(rama)]
        if padre:
            attrs.append("padre=" + q(padre))
        if len(syns) == 1:
            attrs.append("sinonimo=" + q(syns[0]))
        elif syns:
            attrs.append("sinonimo=[" + ",".join(q(s) for s in syns) + "]")
        if len(adjs) == 1:
            attrs.append("adjetivo=" + q(adjs[0]))
        elif adjs:
            attrs.append("adjetivo=[" + ",".join(q(a) for a in adjs) + "]")
        kids = children.get(name, [])
        if len(kids) == 1:
            attrs.append("hijo=" + q(kids[0]))
        elif kids:
            attrs.append("hijo=[" + ",".join(q(k) for k in kids) + "]")
        if "escolar" in flags:
            attrs.append("escolar=1")
        if "idioma" in flags:
            attrs.append("idioma=1")
        out.write("    " + name + ": " + ", ".join(attrs) + "\n")

    # --- rama branch: rama -> its subjects -----------------------------------
    out.write("  rama\n")
    for rama in AREA_ORDER:
        names = sorted((r[0] for r in T if r[1] == rama), key=skey)
        tops = sorted((r[0] for r in T if r[1] == rama and not r[2]), key=skey)
        attrs = ["total=%d" % len(names)]
        if tops:
            attrs.append("raiz=[" + ",".join(q(t) for t in tops) + "]")
        attrs.append("area=[" + ",".join(q(n) for n in names) + "]")
        out.write("    " + rama + ": " + ", ".join(attrs) + "\n")

    save(path, out.getvalue())


def save(path, text):
    with open(path, "wb") as f:
        f.write(text.replace("\n", "\r\n").encode("utf-8"))
    print("wrote", path, len(text.splitlines()), "lines")


def degree_areas(d):
    """Every area= value in es-grados-academicos.dict, so the join can be checked."""
    p = os.path.join(d, "es-grados-academicos.dict")
    if not os.path.exists(p):
        return []
    vals = set()
    with open(p, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#") or " area=" not in line:
                continue
            rest = line.split(" area=", 1)[1]
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

    print("ramas used but not ordered:",
          sorted({r[1] for r in T if r[1] not in AREA_ORDER}))

    seen = {}
    for rec in T:
        for s in [rec[0]] + rec[3]:
            seen.setdefault(s, []).append(rec[0])
    print("forms claimed by more than one subject (first wins):",
          sorted(s for s in seen if len(set(seen[s])) > 1))

    print("multi-word forms the .dict loader rejects (accented later word):",
          sorted(f for f in forms
                 if any(ord(w[0]) > 127 for w in f.split(" ")[1:])))

    areas = degree_areas(d)
    if areas:
        print("es-grados-academicos area= values that do not join:",
              [a for a in areas if a not in known_names])

    print("subjects:", len(T), " surface forms:", len(forms))


if __name__ == "__main__":
    if len(sys.argv) > 1:
        d = sys.argv[1]
    else:
        here = os.path.dirname(os.path.abspath(__file__))
        d = os.path.join(here, os.pardir, "languages", "Spanish")
    d = os.path.normpath(d)
    forms = build()
    known = ambiguous(d)
    write_dict(forms, os.path.join(d, "es-areas-de-estudio.dict"), known,
               degree_forms())
    write_kbb(os.path.join(d, "es-areas-de-estudio.kbb"))
    report(forms, d)
