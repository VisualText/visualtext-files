# -*- coding: utf-8 -*-
# DESC: Generate the Portuguese subject / field-of-study dictionary and knowledge base.
#
# WHAT IT DOES
#   Emits languages/Portuguese/pt-areas-de-estudo.dict and .kbb from the single
#   master table T below, so the two files can never drift apart.  Edit T and
#   re-run; do not hand-edit the generated files.
#   This is the Portuguese counterpart of gen_subjects.py (en-subjects).
#
#   The .dict gets one line per surface form: the subject name, every synonym
#   and every adjective form (masculine and, where it differs, feminine).  The
#   .kbb gets two branches under "areas":
#       area        - forward lookup, area -> grande area, parent, children,
#                     synonyms
#       grandearea  - grande area -> the subjects that sit in it
#   Every .dict line carries "area=<canonical name>", so rules join into the
#   knowledge base on that attribute rather than on $text.
#
#   The broad divisions are the nine "grandes areas" of the CNPq / CAPES table
#   of knowledge areas used by Brazilian universities and the Lattes CV.
#
#   The canonical names are also the vocabulary of area= in
#   pt-graus-academicos.dict: report() checks every area= value there against
#   this table and prints any that would not join.
#
#   Master table row:
#     (name, grande area code, parent, [synonyms], [adjectives], [flags])
#     parent      the broader subject this one sits under, or None
#     adjectives  listed in the masculine; a feminine in -a is derived from an
#                 adjective in -o
#     flags       may hold "escolar" (a primary / secondary school subject in
#                 Brazil or Portugal), "idioma" (the name is also a language,
#                 see pt-idiomas.dict), "br" (Brazil only) and "pt" (Portugal
#                 only)
#
# USAGE
#   python gen_subjects_pt.py [output_dir]
#     output_dir  defaults to ../languages/Portuguese relative to this script

import io, os, sys

GA = {
 "EX":  "ciências exatas e da terra",
 "BIO": "ciências biológicas",
 "ENG": "engenharias",
 "SAU": "ciências da saúde",
 "AGR": "ciências agrárias",
 "SOC": "ciências sociais aplicadas",
 "HUM": "ciências humanas",
 "LLA": "linguística, letras e artes",
 "MUL": "multidisciplinar",
}
GA_ORDER = ["EX", "BIO", "ENG", "SAU", "AGR", "SOC", "HUM", "LLA", "MUL"]

# name, grande area, parent, synonyms, adjectives, flags
T = [
 # --- ciências exatas e da terra --------------------------------------------
 ("ciências","EX",None,["ciência","ciências naturais"],["científico"],["escolar"]),
 ("química","EX","ciências",[],["químico"],["escolar"]),
 ("química orgânica","EX","química",[],[],[]),
 ("química inorgânica","EX","química",[],[],[]),
 ("físico-química","EX","química",["ciências físico-químicas"],[],["escolar"]),
 ("química analítica","EX","química",[],[],[]),
 ("física","EX","ciências",[],[],["escolar"]),
 ("astrofísica","EX","física",[],[],[]),
 ("física nuclear","EX","física",[],[],[]),
 ("física de partículas","EX","física",["física de altas energias"],[],[]),
 ("mecânica quântica","EX","física",["física quântica"],[],[]),
 ("termodinâmica","EX","física",[],[],[]),
 ("óptica","EX","física",["ótica"],["óptico","ótico"],[]),
 ("mecânica","EX","física",[],[],[]),
 ("astronomia","EX","ciências",[],["astronômico","astronómico"],[]),
 ("cosmologia","EX","astronomia",[],["cosmológico"],[]),
 ("ciências planetárias","EX","astronomia",["planetologia"],[],[]),
 ("geociências","EX","ciências",["ciências da terra"],[],[]),
 ("geologia","EX","geociências",[],["geológico"],[]),
 ("meteorologia","EX","geociências",[],["meteorológico"],[]),
 ("oceanografia","EX","geociências",["ciências do mar"],["oceanográfico"],[]),
 ("climatologia","EX","geociências",["ciências do clima"],[],[]),
 ("sismologia","EX","geociências",[],[],[]),
 ("hidrologia","EX","geociências",[],[],[]),
 ("paleontologia","EX","geociências",[],[],[]),
 ("matemática","EX",None,["matemáticas"],["matemático"],["escolar"]),
 ("aritmética","EX","matemática",[],[],["escolar"]),
 ("álgebra","EX","matemática",[],["algébrico"],["escolar"]),
 ("geometria","EX","matemática",[],["geométrico"],["escolar"]),
 ("trigonometria","EX","matemática",[],["trigonométrico"],["escolar"]),
 ("cálculo","EX","matemática",["cálculo diferencial e integral"],[],[]),
 ("estatística","EX","matemática",["probabilidade e estatística"],["estatístico"],[]),
 ("probabilidade","EX","matemática",[],[],[]),
 ("teoria dos números","EX","matemática",[],[],[]),
 ("topologia","EX","matemática",[],[],[]),
 ("álgebra linear","EX","matemática",[],[],[]),
 ("matemática discreta","EX","matemática",[],[],[]),
 ("matemática aplicada","EX","matemática",[],[],[]),
 ("lógica","EX",None,[],["lógico"],[]),
 ("ciência da computação","EX",None,["computação","ciências da computação","informática"],["computacional"],[]),
 ("engenharia de software","EX","ciência da computação",[],[],[]),
 ("inteligência artificial","EX","ciência da computação",["ia"],[],[]),
 ("aprendizado de máquina","EX","inteligência artificial",["aprendizagem de máquina","aprendizagem automática","machine learning"],[],[]),
 ("ciência de dados","EX","ciência da computação",[],[],[]),
 ("segurança da informação","EX","ciência da computação",["cibersegurança","segurança cibernética"],[],[]),
 ("tecnologia da informação","EX","ciência da computação",["ti"],[],[]),
 ("tecnologias da informação e comunicação","EX","tecnologia da informação",["tic"],[],["escolar","pt"]),
 ("sistemas de informação","EX","ciência da computação",[],[],[]),
 ("computação gráfica","EX","ciência da computação",[],[],[]),
 ("interação humano-computador","EX","ciência da computação",["ihc","interação pessoa-computador"],[],[]),

 # --- ciências biológicas ------------------------------------------------------
 ("biologia","BIO","ciências",["bio","ciências biológicas","ciências da vida"],["biológico"],["escolar"]),
 ("botânica","BIO","biologia",["biologia vegetal"],["botânico"],[]),
 ("zoologia","BIO","biologia",[],["zoológico"],[]),
 ("microbiologia","BIO","biologia",[],["microbiológico"],[]),
 ("biologia molecular","BIO","biologia",[],[],[]),
 ("biologia celular","BIO","biologia",["citologia"],[],[]),
 ("genética","BIO","biologia",[],["genético"],[]),
 ("genômica","BIO","genética",["genómica"],["genômico","genómico"],[]),
 ("bioquímica","BIO","biologia",[],["bioquímico"],[]),
 ("biofísica","BIO","biologia",[],["biofísico"],[]),
 ("ecologia","BIO","biologia",[],["ecológico"],[]),
 ("biologia marinha","BIO","biologia",[],[],[]),
 ("neurociência","BIO","biologia",["neurociências","neurobiologia"],[],[]),
 ("fisiologia","BIO","biologia",[],["fisiológico"],[]),
 ("anatomia","BIO","biologia",[],["anatômico","anatómico"],[]),
 ("imunologia","BIO","biologia",[],["imunológico"],[]),
 ("virologia","BIO","biologia",[],[],[]),
 ("bacteriologia","BIO","biologia",[],[],[]),
 ("micologia","BIO","biologia",[],[],[]),
 ("parasitologia","BIO","biologia",[],[],[]),
 ("entomologia","BIO","biologia",[],[],[]),
 ("ornitologia","BIO","biologia",[],[],[]),
 ("biologia evolutiva","BIO","biologia",["biologia evolucionária"],[],[]),
 ("farmacologia","BIO","biologia",[],["farmacológico"],[]),
 ("biotecnologia","MUL","biologia",[],[],[]),

 # --- engenharias ----------------------------------------------------------
 ("engenharia","ENG",None,["engenharias"],[],[]),
 ("engenharia civil","ENG","engenharia",[],[],[]),
 ("engenharia mecânica","ENG","engenharia",[],[],[]),
 ("engenharia elétrica","ENG","engenharia",["engenharia eletrotécnica","engenharia electrotécnica"],[],[]),
 ("engenharia eletrônica","ENG","engenharia elétrica",["engenharia eletrónica"],[],[]),
 ("engenharia de telecomunicações","ENG","engenharia elétrica",[],[],[]),
 ("engenharia química","ENG","engenharia",[],[],[]),
 ("engenharia aeroespacial","ENG","engenharia",["engenharia aeronáutica"],[],[]),
 ("engenharia biomédica","ENG","engenharia",["bioengenharia"],[],[]),
 ("engenharia de produção","ENG","engenharia",["engenharia industrial"],[],[]),
 ("engenharia ambiental","ENG","engenharia",["engenharia sanitária e ambiental"],[],[]),
 ("engenharia sanitária","ENG","engenharia civil",[],[],[]),
 ("engenharia nuclear","ENG","engenharia",[],[],[]),
 ("engenharia de petróleo","ENG","engenharia",["engenharia do petróleo"],[],[]),
 ("engenharia de minas","ENG","engenharia",[],[],[]),
 ("engenharia naval","ENG","engenharia",["engenharia naval e oceânica"],[],[]),
 ("engenharia de estruturas","ENG","engenharia civil",["engenharia estrutural"],[],[]),
 ("engenharia de sistemas","ENG","engenharia",[],[],[]),
 ("engenharia de computação","ENG","engenharia",["engenharia da computação","engenharia informática"],[],[]),
 ("engenharia de controle e automação","ENG","engenharia",["engenharia de automação","engenharia mecatrônica","mecatrônica","mecatrónica"],[],[]),
 ("engenharia de materiais","ENG","engenharia",["ciência dos materiais","ciência de materiais","ciência e engenharia de materiais"],[],[]),
 ("robótica","ENG","engenharia",[],[],[]),
 ("tecnologia","ENG",None,[],["tecnológico"],[]),
 ("educação tecnológica","ENG","tecnologia",[],[],["escolar","pt"]),
 ("desenho técnico","ENG","tecnologia",[],[],[]),

 # --- ciências da saúde -------------------------------------------------------
 ("medicina","SAU",None,[],["médico"],[]),
 ("cirurgia","SAU","medicina",[],["cirúrgico"],[]),
 ("pediatria","SAU","medicina",[],["pediátrico"],[]),
 ("psiquiatria","SAU","medicina",[],["psiquiátrico"],[]),
 ("cardiologia","SAU","medicina",[],[],[]),
 ("oncologia","SAU","medicina",[],[],[]),
 ("radiologia","SAU","medicina",[],[],[]),
 ("neurologia","SAU","medicina",[],[],[]),
 ("patologia","SAU","medicina",[],["patológico"],[]),
 ("anestesiologia","SAU","medicina",[],[],[]),
 ("dermatologia","SAU","medicina",[],[],[]),
 ("obstetrícia","SAU","medicina",[],[],[]),
 ("ginecologia","SAU","medicina",[],[],[]),
 ("ortopedia","SAU","medicina",[],[],[]),
 ("geriatria","SAU","medicina",[],[],[]),
 ("medicina de família","SAU","medicina",["medicina de família e comunidade","medicina geral e familiar"],[],[]),
 ("biomedicina","SAU",None,[],[],["br"]),
 ("enfermagem","SAU",None,[],[],[]),
 ("farmácia","SAU",None,["ciências farmacêuticas"],["farmacêutico"],[]),
 ("odontologia","SAU",None,["medicina dentária"],["odontológico"],[]),
 ("optometria","SAU",None,[],[],[]),
 ("fonoaudiologia","SAU",None,["terapia da fala"],[],[]),
 ("audiologia","SAU","fonoaudiologia",[],[],[]),
 ("podologia","SAU",None,[],[],[]),
 ("quiropraxia","SAU",None,[],[],[]),
 ("fisioterapia","SAU",None,[],[],[]),
 ("terapia ocupacional","SAU",None,[],[],[]),
 ("saúde coletiva","SAU",None,["saúde pública"],[],[]),
 ("epidemiologia","SAU","saúde coletiva",[],["epidemiológico"],[]),
 ("gestão em saúde","SAU","saúde coletiva",["gestão hospitalar","administração hospitalar"],[],[]),
 ("nutrição","SAU",None,["nutrição e dietética","dietética"],["nutricional"],[]),
 ("ciências do esporte","SAU",None,["ciências do desporto","ciência do esporte"],[],[]),
 ("educação física","SAU",None,[],[],["escolar"]),
 ("saúde","SAU",None,["educação para a saúde"],[],[]),

 # --- ciências agrárias -------------------------------------------------------
 ("ciências agrárias","AGR",None,["agricultura"],["agrário","agrícola"],[]),
 ("agronomia","AGR","ciências agrárias",["engenharia agronômica","engenharia agronómica"],["agronômico","agronómico"],[]),
 ("horticultura","AGR","ciências agrárias",[],[],[]),
 ("zootecnia","AGR","ciências agrárias",["produção animal"],[],[]),
 ("engenharia florestal","AGR","ciências agrárias",["ciências florestais","silvicultura"],[],[]),
 ("ciência e tecnologia de alimentos","AGR","ciências agrárias",["ciência dos alimentos","tecnologia de alimentos","engenharia de alimentos"],[],[]),
 ("engenharia de pesca","AGR","ciências agrárias",["recursos pesqueiros","aquicultura"],[],[]),
 ("engenharia agrícola","AGR","ciências agrárias",["engenharia rural"],[],[]),
 ("ciência do solo","AGR","ciências agrárias",["pedologia"],[],[]),
 ("medicina veterinária","AGR",None,["veterinária"],["veterinário"],[]),

 # --- ciências sociais aplicadas ------------------------------------------------
 ("administração","SOC",None,["administração de empresas","gestão","gestão de empresas","negócios"],["administrativo"],[]),
 ("contabilidade","SOC","administração",["ciências contábeis","ciências contabilísticas"],["contábil","contabilístico"],[]),
 ("finanças","SOC","administração",[],["financeiro"],[]),
 ("educação financeira","SOC","finanças",[],[],["escolar"]),
 ("marketing","SOC","administração",["mercadologia"],[],[]),
 ("empreendedorismo","SOC","administração",[],[],[]),
 ("recursos humanos","SOC","administração",["gestão de pessoas","gestão de recursos humanos"],[],[]),
 ("comércio exterior","SOC","administração",["comércio internacional","negócios internacionais"],[],[]),
 ("logística","SOC","administração",["cadeia de suprimentos","gestão da cadeia de suprimentos"],[],[]),
 ("gestão imobiliária","SOC","administração",["negócios imobiliários"],[],[]),
 ("hotelaria","SOC","administração",["gestão hoteleira"],[],[]),
 ("ciências atuariais","SOC","administração",["atuária"],["atuarial"],[]),
 ("secretariado","SOC","administração",["secretariado executivo"],[],[]),
 ("economia","SOC",None,["ciências econômicas","ciências económicas"],["econômico","económico"],[]),
 ("microeconomia","SOC","economia",[],[],[]),
 ("macroeconomia","SOC","economia",[],[],[]),
 ("econometria","SOC","economia",[],[],[]),
 ("direito","SOC",None,["ciências jurídicas","ciências jurídicas e sociais"],["jurídico"],[]),
 ("direito penal","SOC","direito",["direito criminal"],[],[]),
 ("direito civil","SOC","direito",[],[],[]),
 ("direito constitucional","SOC","direito",[],[],[]),
 ("direito internacional","SOC","direito",[],[],[]),
 ("direito tributário","SOC","direito",["direito fiscal"],[],[]),
 ("direito do trabalho","SOC","direito",["direito trabalhista"],[],[]),
 ("direito administrativo","SOC","direito",[],[],[]),
 ("direito empresarial","SOC","direito",["direito comercial"],[],[]),
 ("administração pública","SOC",None,["gestão pública"],[],[]),
 ("políticas públicas","SOC","administração pública",["política pública"],[],[]),
 ("relações internacionais","SOC",None,["estudos internacionais"],[],[]),
 ("serviço social","SOC",None,["assistência social"],[],[]),
 ("demografia","SOC",None,[],["demográfico"],[]),
 ("comunicação","SOC",None,["comunicação social","ciências da comunicação"],[],[]),
 ("jornalismo","SOC","comunicação",[],["jornalístico"],[]),
 ("relações públicas","SOC","comunicação",[],[],[]),
 ("publicidade e propaganda","SOC","comunicação",["publicidade"],["publicitário"],[]),
 ("rádio e televisão","SOC","comunicação",["rádio, tv e internet","estudos de mídia","estudos dos media"],[],[]),
 ("ciência da informação","SOC",None,[],[],[]),
 ("biblioteconomia","SOC","ciência da informação",["biblioteconomia e documentação"],[],[]),
 ("arquivologia","SOC","ciência da informação",["arquivística"],[],[]),
 ("museologia","SOC","ciência da informação",[],[],[]),
 ("arquitetura","SOC",None,["arquitetura e urbanismo","arquitectura"],["arquitetônico","arquitetónico"],[]),
 ("paisagismo","SOC","arquitetura",["arquitetura paisagista","arquitetura paisagística"],[],[]),
 ("planejamento urbano","SOC",None,["planejamento urbano e regional","urbanismo","planeamento urbano"],[],[]),
 ("design","SOC",None,[],[],[]),
 ("design gráfico","SOC","design",["comunicação visual"],[],[]),
 ("design de produto","SOC","design",["desenho industrial","design industrial"],[],[]),
 ("design de moda","SOC","design",[],[],[]),
 ("design de interiores","SOC","design",[],[],[]),
 ("turismo","SOC",None,[],["turístico"],[]),

 # --- ciências humanas ------------------------------------------------------
 ("humanidades","HUM",None,["ciências humanas"],[],[]),
 ("estudos sociais","HUM",None,[],[],["escolar"]),
 ("história","HUM","estudos sociais",[],["histórico"],["escolar"]),
 ("história antiga","HUM","história",[],[],[]),
 ("história geral","HUM","história",["história mundial"],[],["escolar"]),
 ("história do brasil","HUM","história",[],[],["escolar","br"]),
 ("história de portugal","HUM","história",[],[],["escolar","pt"]),
 ("história da arte","HUM","história",[],[],[]),
 ("geografia","HUM","estudos sociais",[],["geográfico"],["escolar"]),
 ("geografia humana","HUM","geografia",[],[],[]),
 ("geografia física","HUM","geografia",[],[],[]),
 ("estudo do meio","HUM","estudos sociais",[],[],["escolar","pt"]),
 ("educação moral e cívica","HUM","estudos sociais",["moral e cívica","emc"],[],["escolar","br"]),
 ("organização social e política brasileira","HUM","estudos sociais",["ospb"],[],["escolar","br"]),
 ("cidadania e desenvolvimento","HUM","estudos sociais",[],[],["escolar","pt"]),
 ("ciência política","HUM",None,["ciências políticas","política"],["político"],[]),
 ("sociologia","HUM",None,[],["sociológico"],["escolar"]),
 ("criminologia","HUM","sociologia",[],[],[]),
 ("psicologia","HUM",None,[],["psicológico"],[]),
 ("psicologia clínica","HUM","psicologia",[],[],[]),
 ("psicologia do desenvolvimento","HUM","psicologia",[],[],[]),
 ("psicologia social","HUM","psicologia",[],[],[]),
 ("psicologia da educação","HUM","psicologia",["psicologia educacional"],[],[]),
 ("ciência cognitiva","HUM","psicologia",["ciências cognitivas"],["cognitivo"],[]),
 ("antropologia","HUM",None,[],["antropológico"],[]),
 ("arqueologia","HUM","antropologia",[],["arqueológico"],[]),
 ("filosofia","HUM","humanidades",[],["filosófico"],["escolar"]),
 ("ética","HUM","filosofia",[],["ético"],[]),
 ("metafísica","HUM","filosofia",[],[],[]),
 ("epistemologia","HUM","filosofia",[],[],[]),
 ("ciências da religião","HUM","humanidades",["ciência da religião","estudos religiosos"],[],[]),
 ("teologia","HUM","ciências da religião",[],["teológico"],[]),
 ("ensino religioso","HUM","ciências da religião",["educação religiosa","educação moral e religiosa"],[],["escolar"]),
 ("educação","HUM",None,[],["educacional"],[]),
 ("pedagogia","HUM","educação",[],["pedagógico"],[]),
 ("educação infantil","HUM","educação",[],[],[]),
 ("educação especial","HUM","educação",["educação inclusiva"],[],[]),
 ("didática","HUM","educação",[],["didático"],[]),
 ("estudos de gênero","HUM",None,["estudos de género","estudos feministas"],[],[]),

 # --- linguística, letras e artes ----------------------------------------------
 ("letras","LLA",None,[],[],[]),
 ("linguística","LLA","letras",["lingüística"],["linguístico"],[]),
 ("língua portuguesa","LLA","letras",["português"],[],["escolar","idioma"]),
 ("redação","LLA","língua portuguesa",["produção de texto","produção textual"],[],["escolar"]),
 ("gramática","LLA","língua portuguesa",[],["gramatical"],["escolar"]),
 ("leitura","LLA","língua portuguesa",[],[],["escolar"]),
 ("literatura","LLA","letras",[],["literário"],["escolar"]),
 ("poesia","LLA","literatura",[],["poético"],[]),
 ("escrita criativa","LLA","letras",[],[],[]),
 ("retórica","LLA","letras",[],["retórico"],[]),
 ("estudos clássicos","LLA","letras",["letras clássicas"],["clássico"],[]),
 ("latim","LLA","estudos clássicos",[],[],["idioma"]),
 ("grego","LLA","estudos clássicos",[],[],["idioma"]),
 ("línguas estrangeiras","LLA","letras",["língua estrangeira","línguas modernas","língua estrangeira moderna"],[],["escolar"]),
 ("inglês","LLA","línguas estrangeiras",["língua inglesa"],[],["escolar","idioma"]),
 ("espanhol","LLA","línguas estrangeiras",["língua espanhola","castelhano"],[],["escolar","idioma"]),
 ("francês","LLA","línguas estrangeiras",["língua francesa"],[],["escolar","idioma"]),
 ("alemão","LLA","línguas estrangeiras",["língua alemã"],[],["escolar","idioma"]),
 ("italiano","LLA","línguas estrangeiras",["língua italiana"],[],["idioma"]),
 ("russo","LLA","línguas estrangeiras",[],[],["idioma"]),
 ("chinês","LLA","línguas estrangeiras",["mandarim"],[],["idioma"]),
 ("japonês","LLA","línguas estrangeiras",[],[],["idioma"]),
 ("coreano","LLA","línguas estrangeiras",[],[],["idioma"]),
 ("árabe","LLA","línguas estrangeiras",[],[],["idioma"]),
 ("hebraico","LLA","línguas estrangeiras",[],[],["idioma"]),
 ("libras","LLA","letras",["língua brasileira de sinais"],[],["escolar","idioma","br"]),
 ("arte","LLA",None,["artes","artes visuais"],["artístico"],["escolar"]),
 ("educação artística","LLA","arte",[],[],["escolar","br"]),
 ("educação visual","LLA","arte",[],[],["escolar","pt"]),
 ("belas-artes","LLA","arte",["belas artes"],[],[]),
 ("desenho","LLA","arte",[],[],["escolar"]),
 ("pintura","LLA","arte",[],[],[]),
 ("escultura","LLA","arte",[],[],[]),
 ("fotografia","LLA","arte",[],["fotográfico"],[]),
 ("cerâmica","LLA","arte",[],[],[]),
 ("gravura","LLA","arte",[],[],[]),
 ("artes aplicadas","LLA","arte",[],[],[]),
 ("música","LLA",None,[],["musical"],["escolar"]),
 ("teoria musical","LLA","música",[],[],[]),
 ("composição musical","LLA","música",[],[],[]),
 ("artes cênicas","LLA",None,["artes cénicas","artes do espetáculo","artes performativas"],["cênico"],[]),
 ("teatro","LLA","artes cênicas",["arte dramática"],["teatral"],["escolar"]),
 ("dança","LLA","artes cênicas",[],[],["escolar"]),
 ("cinema","LLA",None,["cinema e audiovisual","audiovisual","estudos de cinema"],["cinematográfico"],[]),

 # --- multidisciplinar --------------------------------------------------------
 ("estudos interdisciplinares","MUL",None,["estudos multidisciplinares","interdisciplinar"],[],[]),
 ("artes liberais","MUL",None,["estudos liberais"],[],[]),
 ("ciências aplicadas","MUL",None,[],[],[]),
 ("ciências ambientais","MUL",None,["ciência ambiental","estudos ambientais","gestão ambiental"],["ambiental"],[]),
 ("sustentabilidade","MUL","ciências ambientais",[],[],[]),
 ("educação ambiental","MUL","ciências ambientais",[],[],["escolar"]),
 ("pesquisa","MUL",None,["investigação"],[],[]),
 ("economia doméstica","MUL",None,["ciências domésticas"],[],["escolar"]),
 ("educação para o trânsito","MUL",None,["educação no trânsito","educação rodoviária"],[],["escolar"]),
 ("datilografia","MUL",None,["digitação"],[],["escolar"]),
 ("projeto de vida","MUL",None,[],[],["escolar","br"]),
]

HDR_DICT = """\
# Áreas de estudo em português: disciplinas escolares e áreas académicas.
# Uma linha por forma.
#   area=         o nome canónico da área -- em toda entrada, para que as
#                 regras façam a junção com pt-areas-de-estudo.kbb por este
#                 atributo e não por $text
#   grandearea=   a grande área do CNPq / CAPES em que a área se encaixa
#                 (ciências exatas e da terra, ciências biológicas,
#                 engenharias, ciências da saúde, ciências agrárias, ciências
#                 sociais aplicadas, ciências humanas, linguística, letras e
#                 artes, multidisciplinar)
#   pai=          a área mais ampla de que esta faz parte, quando existe
#   nome=1        a forma é o nome canónico           sin=1  um sinónimo
#   adj=1         uma forma adjetiva (biológico, matemática)
#   gen=m|f       género, nas formas adjetivas
#   escolar=1     disciplina comum do ensino fundamental / médio (Brasil) ou
#                 básico / secundário (Portugal)
#   idioma=1      o nome é também um idioma e uma nacionalidade (português,
#                 inglês, latim) -- ver pt-idiomas.dict, pt-nacionalidades.dict
#   br=1          nome usado só no Brasil       pt=1  usado só em Portugal
#   ambig=1       a forma é também entrada de outro dicionário da biblioteca
# Quase todo nome de área é também uma palavra comum (arte, história,
# leitura, desenho, direito), por isso a leitura como área precisa de
# contexto: "formado em", "graduação em", "aula de", "departamento de" ou uma
# grade curricular.  O dicionário não marca isso; só marca as colisões entre
# dicionários da biblioteca.
# Os nomes canónicos daqui são o vocabulário de area= em
# pt-graus-academicos.dict, para que um grau se ligue à sua área por esse
# atributo.
"""

HDR_KBB = """\
# Áreas de estudo em português, ligadas às grandes áreas do CNPq / CAPES.
# Consulta direta:  área -> grande área   (conceito "areas area biologia" -> grandearea="ciências biológicas")
# Grandes áreas:    grande área -> as suas áreas
# A árvore percorre-se nos dois sentidos: pai= aponta para cima, filho= para baixo.
#   grandearea=   ciências exatas e da terra | ciências biológicas |
#                 engenharias | ciências da saúde | ciências agrárias |
#                 ciências sociais aplicadas | ciências humanas |
#                 linguística, letras e artes | multidisciplinar
#   pai=          a área mais ampla de que esta faz parte
#   filho=        os filhos imediatos desta área
#   sinonimo=     nomes alternativos       adjetivo=  formas adjetivas
#   escolar=1     disciplina escolar comum
#   idioma=1      o nome é também um idioma e uma nacionalidade
#   br=1          só no Brasil             pt=1  só em Portugal
# Os nomes de área daqui são o vocabulário de area= em
# pt-graus-academicos.dict, para que um grau se ligue à sua área por esse
# atributo.
# Toda forma aqui citada é etiquetada por pt-areas-de-estudo.dict.
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


def adj_forms(adjs):
    """(form, gen) for every adjective: the masculine and a derived feminine."""
    out = []
    for a in adjs:
        if a.endswith("o"):
            out.append((a, "m"))
            out.append((a[:-1] + "a", "f"))
        else:
            out.append((a, None))
    return out


def build():
    """form -> (rec, role, gen) over every surface form in T; first reading wins."""
    forms = {}
    for rec in T:
        name, ga, parent, syns, adjs, flags = rec
        for form, role, gen in ([(name, "nome", None)] + [(s, "sin", None) for s in syns]
                                + [(a, "adj", g) for a, g in adj_forms(adjs)]):
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


SIBLINGS = ("pt-idiomas.dict", "pt-nacionalidades.dict", "pt-paises.dict",
            "pt-estados.dict", "pt-tratamentos.dict", "pt-graus-academicos.dict")


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


def flag_attrs(flags):
    return [f + "=1" for f in ("escolar", "idioma", "br", "pt") if f in flags]


def write_dict(forms, path, known):
    out = io.StringIO()
    out.write(HDR_DICT)
    for form in sorted(forms):
        rec, role, gen = forms[form]
        name, ga, parent, syns, adjs, flags = rec
        attrs = [role + "=1", "area=" + q(name), "grandearea=" + q(GA[ga])]
        if parent:
            attrs.append("pai=" + q(parent))
        if gen:
            attrs.append("gen=" + gen)
        attrs += flag_attrs(flags)
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

    # --- forward branch: area -> grande area, parent, children -------------------
    out.write("  area\n")
    for rec in sorted(T):
        name, ga, parent, syns, adjs, flags = rec
        attrs = ["grandearea=" + q(GA[ga])]
        if parent:
            attrs.append("pai=" + q(parent))
        if syns:
            attrs.append("sinonimo=" + lst(syns))
        if adjs:
            attrs.append("adjetivo=" + lst(a for a, g in adj_forms(adjs)))
        kids = children.get(name, [])
        if kids:
            attrs.append("filho=" + lst(kids))
        attrs += flag_attrs(flags)
        out.write("    " + name + ": " + ", ".join(attrs) + "\n")

    # --- grande area branch: grande area -> its subjects -------------------------
    out.write("  grandearea\n")
    for code in GA_ORDER:
        names = sorted(r[0] for r in T if r[1] == code)
        tops = sorted(r[0] for r in T if r[1] == code and not r[2])
        attrs = ["total=%d" % len(names)]
        if tops:
            attrs.append("topo=[" + ",".join(q(t) for t in tops) + "]")
        attrs.append("area=[" + ",".join(q(n) for n in names) + "]")
        out.write("    " + GA[code] + ": " + ", ".join(attrs) + "\n")

    save(path, out.getvalue())


def save(path, text):
    with open(path, "wb") as f:
        f.write(text.replace("\n", "\r\n").encode("utf-8"))
    print("wrote", path, len(text.splitlines()), "lines")


def degree_areas(d):
    """Every area= value in pt-graus-academicos.dict, so the join can be checked."""
    p = os.path.join(d, "pt-graus-academicos.dict")
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
    print("duplicate area names:",
          sorted({n for n in names if names.count(n) > 1}))

    known_names = set(names)
    print("parents with no area of their own:",
          sorted({r[2] for r in T if r[2] and r[2] not in known_names}))

    print("grandes areas used but not ordered:",
          sorted({r[1] for r in T if r[1] not in GA_ORDER}))

    shadowed = []
    for rec in T:
        name, ga, parent, syns, adjs, flags = rec
        for s in list(syns) + [a for a, g in adj_forms(adjs)]:
            if forms[s][0] is not rec:
                shadowed.append(s)
    print("synonym / adjective forms claimed by an earlier area:", sorted(shadowed))

    areas = degree_areas(d)
    if areas:
        print("pt-graus-academicos area= values that do not join:",
              [a for a in areas if a not in known_names])

    print("areas:", len(T), " surface forms:", len(forms))


if __name__ == "__main__":
    if len(sys.argv) > 1:
        d = sys.argv[1]
    else:
        here = os.path.dirname(os.path.abspath(__file__))
        d = os.path.join(here, os.pardir, "languages", "Portuguese")
    d = os.path.normpath(d)
    forms = build()
    known = ambiguous(d)
    write_dict(forms, os.path.join(d, "pt-areas-de-estudo.dict"), known)
    write_kbb(os.path.join(d, "pt-areas-de-estudo.kbb"))
    report(forms, d)
