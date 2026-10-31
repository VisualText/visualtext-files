# -*- coding: utf-8 -*-
# DESC: Generate the Portuguese country, language and nationality dictionaries and knowledge bases.
#
# WHAT IT DOES
#   Emits, in languages/Portuguese:
#       pt-paises.dict         pt-paises.kbb           countries
#       pt-idiomas.dict        pt-idiomas.kbb          human languages
#       pt-nacionalidades.dict pt-nacionalidades.kbb   nationalities (demonyms)
#   from the master tables PAISES, IDIOMAS and NACIONALIDADES below, so the six
#   files can never drift apart.  Edit the tables and re-run; do not hand-edit
#   the generated files.
#
#   These are the Portuguese counterparts of en-countries, en-languages and
#   en-nationalities.  They join to the English files on the ISO codes:
#   iso2=/iso3= (ISO 3166-1) for countries and nationalities, laiso2=/iso3=
#   (ISO 639-1 / 639-2B) for languages, spelled exactly as the English files
#   spell them.
#
#   Brazilian spelling is primary.  European Portuguese spellings that differ
#   (irão, quénia, vietname, polaco, checo ...) and other alternate names are
#   variants: sin=1 with raiz= naming the Brazilian canonical form.
#
#   Attribute scheme (Portuguese names, as in pt-estados and pt-full):
#     pais=1 / idioma=1 / nacionalidade=1   entry flag of each dictionary
#     pais="..."        canonical country name (nacionalidades -> paises join key)
#     nacionalidade=    canonical demonym (country -> nationality branch)
#     gen=m|f|c         gender (c = comum de dois: belga, canadense)
#     num=s|p           number
#     sin=1             variant / synonym;   raiz= its canonical form
#     naoiso=1          not an ISO 3166-1 country (inglaterra, kosovo, ...)
#     ambig=1           a demonym naming more than one country
#
# USAGE
#   python gen_geo_pt.py [output_dir]
#     output_dir  defaults to ../languages/Portuguese relative to this script
#   The sanity report compares coverage against ../languages/English and
#   gen_nationalities.py.

import io, os, sys, unicodedata

# ---------------------------------------------------------------------------
# PAISES
#   (iso2, iso3, canonical name, gender/number, [variants])
#   gender/number: "m", "f", "mp", "fp", or "" when the name takes no article
#   and its gender is not settled (barbados, jersey, kiribati ...).
#   variant: "name:gn" with the same gender/number code.
# ---------------------------------------------------------------------------
PAISES = [
 ("af","afg","afeganistão","m",[]),
 ("al","alb","albânia","f",[]),
 ("dz","dza","argélia","f",[]),
 ("as","asm","samoa americana","f",[]),
 ("ad","and","andorra","f",[]),
 ("ao","ago","angola","f",[]),
 ("ai","aia","anguila","f",[]),
 ("aq","ata","antártida","f",["antártica:f"]),
 ("ag","atg","antígua e barbuda","f",[]),
 ("ar","arg","argentina","f",[]),
 ("am","arm","armênia","f",["arménia:f"]),
 ("aw","abw","aruba","f",[]),
 ("au","aus","austrália","f",[]),
 ("at","aut","áustria","f",[]),
 ("az","aze","azerbaijão","m",[]),
 ("bs","bhs","bahamas","fp",[]),
 ("bh","bhr","bahrein","m",["barein:m","barém:m"]),
 ("bd","bgd","bangladesh","m",[]),
 ("bb","brb","barbados","",[]),
 ("by","blr","bielorrússia","f",["belarus:"]),
 ("be","bel","bélgica","f",[]),
 ("bz","blz","belize","m",[]),
 ("bj","ben","benin","m",["benim:m"]),
 ("bm","bmu","bermudas","fp",["bermuda:f"]),
 ("bt","btn","butão","m",[]),
 ("bo","bol","bolívia","f",["estado plurinacional da bolívia:m"]),
 ("bq","bes","bonaire, santo eustáquio e saba","",["países baixos caribenhos:mp"]),
 ("ba","bih","bósnia e herzegovina","f",["bósnia-herzegovina:f","bósnia:f"]),
 ("bw","bwa","botsuana","m",["botswana:m"]),
 ("bv","bvt","ilha bouvet","f",[]),
 ("br","bra","brasil","m",["república federativa do brasil:f"]),
 ("io","iot","território britânico do oceano índico","m",[]),
 ("bn","brn","brunei","m",["brunei darussalam:m"]),
 ("bg","bgr","bulgária","f",[]),
 ("bf","bfa","burkina faso","m",[]),
 ("bi","bdi","burundi","m",[]),
 ("cv","cpv","cabo verde","m",[]),
 ("kh","khm","camboja","m",[]),
 ("cm","cmr","camarões","mp",[]),
 ("ca","can","canadá","m",[]),
 ("ky","cym","ilhas cayman","fp",["ilhas caimão:fp"]),
 ("cf","caf","república centro-africana","f",[]),
 ("td","tcd","chade","m",[]),
 ("cl","chl","chile","m",[]),
 ("cn","chn","china","f",["república popular da china:f"]),
 ("cx","cxr","ilha christmas","f",["ilha do natal:f"]),
 ("cc","cck","ilhas cocos","fp",["ilhas cocos keeling:fp"]),
 ("co","col","colômbia","f",[]),
 ("km","com","comores","fp",["união das comores:f"]),
 ("cg","cog","congo","m",["república do congo:f","congo-brazzaville:m"]),
 ("cd","cod","república democrática do congo","f",["congo-kinshasa:m"]),
 ("ck","cok","ilhas cook","fp",[]),
 ("cr","cri","costa rica","f",[]),
 ("hr","hrv","croácia","f",[]),
 ("cu","cub","cuba","f",[]),
 ("cw","cuw","curaçao","",["curaçau:"]),
 ("cy","cyp","chipre","m",[]),
 ("cz","cze","tchéquia","f",["república tcheca:f","chéquia:f","república checa:f"]),
 ("ci","civ","costa do marfim","f",["côte d'ivoire:f"]),
 ("dk","dnk","dinamarca","f",[]),
 ("dj","dji","djibuti","m",["jibuti:m"]),
 ("dm","dma","dominica","f",[]),
 ("do","dom","república dominicana","f",[]),
 ("ec","ecu","equador","m",[]),
 ("eg","egy","egito","m",["egipto:m"]),
 ("sv","slv","el salvador","m",[]),
 ("gq","gnq","guiné equatorial","f",[]),
 ("er","eri","eritreia","f",["eritréia:f"]),
 ("ee","est","estônia","f",["estónia:f"]),
 ("sz","swz","essuatíni","m",["eswatini:m","suazilândia:f"]),
 ("et","eth","etiópia","f",[]),
 ("fk","flk","ilhas malvinas","fp",["ilhas falkland:fp","malvinas:fp"]),
 ("fo","fro","ilhas faroé","fp",["ilhas feroé:fp"]),
 ("fj","fji","fiji","m",["fidji:m"]),
 ("fi","fin","finlândia","f",[]),
 ("fr","fra","frança","f",[]),
 ("gf","guf","guiana francesa","f",[]),
 ("pf","pyf","polinésia francesa","f",[]),
 ("tf","atf","terras austrais e antárticas francesas","fp",[]),
 ("ga","gab","gabão","m",[]),
 ("gm","gmb","gâmbia","f",[]),
 ("ge","geo","geórgia","f",[]),
 ("de","deu","alemanha","f",[]),
 ("gh","gha","gana","m",[]),
 ("gi","gib","gibraltar","m",[]),
 ("gr","grc","grécia","f",[]),
 ("gl","grl","groenlândia","f",["gronelândia:f"]),
 ("gd","grd","granada","f",[]),
 ("gp","glp","guadalupe","f",[]),
 ("gu","gum","guam","",[]),
 ("gt","gtm","guatemala","f",[]),
 ("gg","ggy","guernsey","",[]),
 ("gn","gin","guiné","f",["guiné-conacri:f"]),
 ("gw","gnb","guiné-bissau","f",[]),
 ("gy","guy","guiana","f",[]),
 ("ht","hti","haiti","m",[]),
 ("hm","hmd","ilha heard e ilhas mcdonald","f",["ilhas heard e mcdonald:fp"]),
 ("va","vat","santa sé","f",["vaticano:m","cidade do vaticano:f"]),
 ("hn","hnd","honduras","",[]),
 ("hk","hkg","hong kong","m",[]),
 ("hu","hun","hungria","f",[]),
 ("is","isl","islândia","f",[]),
 ("in","ind","índia","f",[]),
 ("id","idn","indonésia","f",[]),
 ("ir","irn","irã","m",["irão:m","república islâmica do irã:f","república islâmica do irão:f"]),
 ("iq","irq","iraque","m",[]),
 ("ie","irl","irlanda","f",[]),
 ("im","imn","ilha de man","f",[]),
 ("il","isr","israel","m",[]),
 ("it","ita","itália","f",[]),
 ("jm","jam","jamaica","f",[]),
 ("jp","jpn","japão","m",[]),
 ("je","jey","jersey","",[]),
 ("jo","jor","jordânia","f",[]),
 ("kz","kaz","cazaquistão","m",[]),
 ("ke","ken","quênia","m",["quénia:m"]),
 ("ki","kir","kiribati","",["quiribati:"]),
 # "coreia" alone is its own row on the kr codes, as "korea" is in English
 ("kr","kor","coreia","f",[]),
 ("kp","prk","coreia do norte","f",["república popular democrática da coreia:f"]),
 ("kr","kor","coreia do sul","f",["república da coreia:f"]),
 ("kw","kwt","kuwait","m",["kuweit:m","koweit:m"]),
 ("kg","kgz","quirguistão","m",["quirguízia:f"]),
 ("la","lao","laos","m",["república democrática popular do laos:f"]),
 ("lv","lva","letônia","f",["letónia:f"]),
 ("lb","lbn","líbano","m",[]),
 ("ls","lso","lesoto","m",[]),
 ("lr","lbr","libéria","f",[]),
 ("ly","lby","líbia","f",[]),
 ("li","lie","liechtenstein","m",[]),
 ("lt","ltu","lituânia","f",[]),
 ("lu","lux","luxemburgo","m",[]),
 ("mo","mac","macau","m",[]),
 ("mg","mdg","madagascar","m",["madagáscar:m"]),
 ("mw","mwi","malawi","m",["malaui:m"]),
 ("my","mys","malásia","f",[]),
 ("mv","mdv","maldivas","fp",[]),
 ("ml","mli","mali","m",[]),
 ("mt","mlt","malta","f",[]),
 ("mh","mhl","ilhas marshall","fp",[]),
 ("mq","mtq","martinica","f",[]),
 ("mr","mrt","mauritânia","f",[]),
 ("mu","mus","maurício","m",["maurícia:f","ilhas maurício:fp"]),
 ("yt","myt","mayotte","",["maiote:"]),
 ("mx","mex","méxico","m",[]),
 ("fm","fsm","micronésia","f",["estados federados da micronésia:mp"]),
 ("md","mda","moldávia","f",["república da moldávia:f","moldova:f"]),
 ("mc","mco","mônaco","m",["mónaco:m"]),
 ("mn","mng","mongólia","f",[]),
 ("me","mne","montenegro","m",[]),
 ("ms","msr","montserrat","",["monserrate:"]),
 ("ma","mar","marrocos","m",[]),
 ("mz","moz","moçambique","m",[]),
 ("mm","mmr","mianmar","m",["myanmar:m","birmânia:f"]),
 ("na","nam","namíbia","f",[]),
 ("nr","nru","nauru","",[]),
 ("np","npl","nepal","m",[]),
 ("nl","nld","países baixos","mp",["holanda:f"]),
 ("nc","ncl","nova caledônia","f",["nova caledónia:f"]),
 ("nz","nzl","nova zelândia","f",[]),
 ("ni","nic","nicarágua","f",[]),
 ("ne","ner","níger","m",[]),
 ("ng","nga","nigéria","f",[]),
 ("nu","niu","niue","",[]),
 ("nf","nfk","ilha norfolk","f",[]),
 ("mp","mnp","ilhas marianas do norte","fp",[]),
 ("no","nor","noruega","f",[]),
 ("om","omn","omã","m",[]),
 ("pk","pak","paquistão","m",[]),
 ("pw","plw","palau","m",[]),
 ("ps","pse","palestina","f",["estado da palestina:m"]),
 ("pa","pan","panamá","m",[]),
 ("pg","png","papua-nova guiné","f",["papua nova guiné:f"]),
 ("py","pry","paraguai","m",[]),
 ("pe","per","peru","m",[]),
 ("ph","phl","filipinas","fp",[]),
 ("pn","pcn","ilhas pitcairn","fp",["pitcairn:"]),
 ("pl","pol","polônia","f",["polónia:f"]),
 ("pt","prt","portugal","m",[]),
 ("pr","pri","porto rico","m",[]),
 ("qa","qat","catar","m",["qatar:m"]),
 ("mk","mkd","macedônia do norte","f",["macedónia do norte:f","república da macedônia do norte:f","república da macedónia do norte:f","macedônia:f","macedónia:f"]),
 ("ro","rou","romênia","f",["roménia:f"]),
 ("ru","rus","rússia","f",["federação russa:f"]),
 ("rw","rwa","ruanda","",[]),
 ("re","reu","reunião","f",["ilha da reunião:f"]),
 ("bl","blm","são bartolomeu","m",["saint-barthélemy:m"]),
 ("sh","shn","santa helena, ascensão e tristão da cunha","f",["santa helena:f"]),
 ("kn","kna","são cristóvão e névis","m",["são cristóvão e neves:m"]),
 ("lc","lca","santa lúcia","f",[]),
 ("mf","maf","são martinho","m",["saint-martin:m"]),
 ("pm","spm","são pedro e miquelão","m",["saint-pierre e miquelon:m"]),
 ("vc","vct","são vicente e granadinas","m",["são vicente e as granadinas:m"]),
 ("ws","wsm","samoa","f",[]),
 ("sm","smr","san marino","m",["são marinho:m"]),
 ("st","stp","são tomé e príncipe","m",[]),
 ("sa","sau","arábia saudita","f",[]),
 ("sn","sen","senegal","m",[]),
 ("rs","srb","sérvia","f",[]),
 ("sc","syc","seicheles","fp",["seychelles:fp"]),
 ("sl","sle","serra leoa","f",[]),
 ("sg","sgp","singapura","f",["cingapura:f"]),
 ("sx","sxm","sint maarten","",[]),
 ("sk","svk","eslováquia","f",[]),
 ("si","svn","eslovênia","f",["eslovénia:f"]),
 ("sb","slb","ilhas salomão","fp",[]),
 ("so","som","somália","f",[]),
 ("za","zaf","áfrica do sul","f",[]),
 ("gs","sgs","ilhas geórgia do sul e sandwich do sul","fp",[]),
 ("ss","ssd","sudão do sul","m",[]),
 ("es","esp","espanha","f",[]),
 ("lk","lka","sri lanka","m",[]),
 ("sd","sdn","sudão","m",[]),
 ("sr","sur","suriname","m",[]),
 ("sj","sjm","svalbard e jan mayen","",[]),
 ("se","swe","suécia","f",[]),
 ("ch","che","suíça","f",[]),
 ("sy","syr","síria","f",["república árabe síria:f"]),
 ("tw","twn","taiwan","m",[]),
 ("tj","tjk","tajiquistão","m",[]),
 ("tz","tza","tanzânia","f",["república unida da tanzânia:f"]),
 ("th","tha","tailândia","f",[]),
 ("tl","tls","timor-leste","m",["timor leste:m"]),
 ("tg","tgo","togo","m",[]),
 ("tk","tkl","tokelau","",["toquelau:"]),
 ("to","ton","tonga","f",[]),
 ("tt","tto","trinidad e tobago","m",[]),
 ("tn","tun","tunísia","f",[]),
 ("tr","tur","turquia","f",[]),
 ("tm","tkm","turcomenistão","m",["turquemenistão:m"]),
 ("tc","tca","ilhas turcas e caicos","fp",[]),
 ("tv","tuv","tuvalu","m",[]),
 ("ug","uga","uganda","f",[]),
 ("ua","ukr","ucrânia","f",[]),
 ("ae","are","emirados árabes unidos","mp",[]),
 ("gb","gbr","reino unido","m",["reino unido da grã-bretanha e irlanda do norte:m","grã-bretanha:f"]),
 ("um","umi","ilhas menores distantes dos estados unidos","fp",[]),
 ("us","usa","estados unidos","mp",["estados unidos da américa:mp","eua:mp"]),
 ("vi","vir","ilhas virgens americanas","fp",["ilhas virgens dos estados unidos:fp"]),
 ("uy","ury","uruguai","m",[]),
 ("uz","uzb","uzbequistão","m",["usbequistão:m"]),
 ("vu","vut","vanuatu","m",[]),
 ("ve","ven","venezuela","f",["república bolivariana da venezuela:f"]),
 ("vn","vnm","vietnã","m",["vietname:m","vietnam:m"]),
 ("vg","vgb","ilhas virgens britânicas","fp",[]),
 ("wf","wlf","wallis e futuna","",[]),
 ("eh","esh","saara ocidental","m",["sara ocidental:m"]),
 ("ye","yem","iêmen","m",["iémen:m"]),
 ("zm","zmb","zâmbia","f",[]),
 ("zw","zwe","zimbábue","m",["zimbabué:m","zimbabwe:m"]),
 ("ax","ala","ilhas åland","fp",["ilhas aland:fp"]),
]

# Not ISO 3166-1 countries, but frequent as the country of a nationality.
# The UK's constituent nations carry gb/gbr; kosovo carries xk/xkx (the
# user-assigned code in common use), as in en-nationalities.
PAISES_NAOISO = [
 ("gb","gbr","inglaterra","f",[]),
 ("gb","gbr","escócia","f",[]),
 ("gb","gbr","país de gales","m",["gales:m"]),
 ("gb","gbr","irlanda do norte","f",[]),
 ("xk","xkx","kosovo","m",[]),
]

# ---------------------------------------------------------------------------
# IDIOMAS
#   (laiso2, iso3, canonical name, [variants])   all language names are masculine
#   iso3 is the ISO 639-2/B code exactly as en-languages.dict has it.
# ---------------------------------------------------------------------------
IDIOMAS = [
 ("ab","abk","abcásio",["abecásio","abcázio"]),
 ("aa","aar","afar",[]),
 ("af","afr","africâner",["africânder"]),
 ("ak","aka","akan",[]),
 ("sq","alb","albanês",[]),
 ("am","amh","amárico",[]),
 ("ar","ara","árabe",[]),
 ("an","arg","aragonês",[]),
 ("hy","arm","armênio",["arménio"]),
 ("as","asm","assamês",[]),
 ("av","ava","avar",["avárico"]),
 ("ae","ave","avéstico",[]),
 ("ay","aym","aimará",[]),
 ("az","aze","azerbaijano",["azeri"]),
 ("bm","bam","bambara",[]),
 ("ba","bak","basquir",[]),
 ("eu","baq","basco",["euskera"]),
 ("be","bel","bielorrusso",[]),
 ("bn","ben","bengali",["bangla"]),
 ("bi","bis","bislamá",["bislama"]),
 ("bs","bos","bósnio",[]),
 ("br","bre","bretão",[]),
 ("bg","bul","búlgaro",[]),
 ("my","bur","birmanês",[]),
 ("ca","cat","catalão",["valenciano"]),
 ("km","khm","khmer",["cmer","cambojano"]),
 ("ch","cha","chamorro",[]),
 ("ce","che","checheno",[]),
 ("ny","nya","chichewa",["chewa","nianja"]),
 ("zh","chi","chinês",[]),
 ("za","zha","zhuang",["chuang"]),
 ("cu","chu","eslavo eclesiástico",["eslavo eclesiástico antigo","antigo eslavo eclesiástico"]),
 ("cv","chv","tchuvache",[]),
 ("kw","cor","córnico",[]),
 ("co","cos","corso",[]),
 ("cr","cre","cree",[]),
 ("hr","hrv","croata",[]),
 ("cs","cze","tcheco",["checo"]),
 ("da","dan","dinamarquês",[]),
 ("dv","div","divehi",["maldívio"]),
 ("nl","dut","neerlandês",["holandês","flamengo"]),
 ("dz","dzo","dzongkha",[]),
 ("en","eng","inglês",[]),
 ("eo","epo","esperanto",[]),
 ("et","est","estoniano",["estónio"]),
 ("ee","ewe","ewe",["jeje"]),
 ("fo","fao","feroês",[]),
 ("fj","fij","fijiano",[]),
 ("fi","fin","finlandês",["finês"]),
 ("fr","fre","francês",[]),
 ("ff","ful","fula",["fulani","fulfulde"]),
 ("gd","gla","gaélico escocês",["gaélico"]),
 ("gl","glg","galego",[]),
 ("lg","lug","luganda",["ganda"]),
 ("ka","geo","georgiano",[]),
 ("de","ger","alemão",[]),
 ("el","gre","grego",[]),
 ("kl","kal","groenlandês",["kalaallisut","gronelandês"]),
 ("gn","grn","guarani",[]),
 ("gu","guj","guzerate",["gujarati"]),
 ("ht","hat","crioulo haitiano",["haitiano"]),
 ("ha","hau","hauçá",["haussá"]),
 ("he","heb","hebraico",[]),
 ("hz","her","herero",[]),
 ("hi","hin","hindi",[]),
 ("ho","hmo","hiri motu",[]),
 ("hu","hun","húngaro",[]),
 ("is","ice","islandês",[]),
 ("io","ido","ido",[]),
 ("ig","ibo","igbo",["ibo"]),
 ("id","ind","indonésio",[]),
 ("ia","ina","interlíngua",[]),
 ("ie","ile","interlingue",["occidental"]),
 ("iu","iku","inuktitut",[]),
 ("ik","ipk","inupiaq",[]),
 ("ga","gle","irlandês",["gaélico irlandês"]),
 ("it","ita","italiano",[]),
 ("ja","jpn","japonês",[]),
 ("jv","jav","javanês",[]),
 ("kn","kan","canarês",["kannada"]),
 ("kr","kau","kanuri",["canúri"]),
 ("ks","kas","caxemiri",["kashmiri"]),
 ("kk","kaz","cazaque",[]),
 ("ki","kik","quicuio",["kikuyu","gikuyu"]),
 ("rw","kin","quiniaruanda",["kinyarwanda"]),
 ("ky","kir","quirguiz",[]),
 ("kv","kom","komi",[]),
 ("kg","kon","quicongo",["kongo"]),
 ("ko","kor","coreano",[]),
 ("kj","kua","cuanhama",["kuanyama","kwanyama"]),
 ("ku","kur","curdo",[]),
 ("lo","lao","laosiano",["lao"]),
 ("la","lat","latim",[]),
 ("lv","lav","letão",[]),
 ("li","lim","limburguês",[]),
 ("ln","lin","lingala",[]),
 ("lt","lit","lituano",[]),
 ("lu","lub","luba-catanga",["luba-katanga"]),
 ("lb","ltz","luxemburguês",[]),
 ("mk","mac","macedônio",["macedónio"]),
 ("mg","mlg","malgaxe",[]),
 ("ms","may","malaio",[]),
 ("ml","mal","malaiala",["malayalam"]),
 ("mt","mlt","maltês",[]),
 ("gv","glv","manês",["manx"]),
 ("mi","mao","maori",[]),
 ("mr","mar","marati",["marathi"]),
 ("mh","mah","marshallês",[]),
 ("mn","mon","mongol",[]),
 ("na","nau","nauruano",[]),
 ("nv","nav","navajo",["navaho"]),
 ("ng","ndo","ndonga",[]),
 ("ne","nep","nepalês",["nepali"]),
 ("nd","nde","ndebele do norte",["ndebele setentrional"]),
 ("se","sme","sami setentrional",["sami do norte"]),
 ("no","nor","norueguês",[]),
 ("nb","nob","norueguês bokmål",["bokmål"]),
 ("nn","nno","norueguês nynorsk",["nynorsk"]),
 ("ii","iii","yi de sichuan",["nuosu"]),
 ("oc","oci","occitano",[]),
 ("oj","oji","ojíbua",["ojibwa","ojibwe"]),
 ("or","ori","oriá",["odia","oriya"]),
 ("om","orm","oromo",[]),
 ("os","oss","osseto",["ossético"]),
 ("pi","pli","páli",["pali"]),
 ("pa","pan","panjabi",["punjabi"]),
 ("ps","pus","pashto",["pachto","pastó"]),
 ("fa","per","persa",["farsi"]),
 ("pl","pol","polonês",["polaco"]),
 ("pt","por","português",[]),
 ("qu","que","quíchua",["quéchua"]),
 ("rm","roh","romanche",[]),
 ("rn","run","kirundi",["rundi"]),
 ("ro","rum","romeno",["moldávio","moldavo"]),
 ("ru","rus","russo",[]),
 ("sm","smo","samoano",[]),
 ("sg","sag","sango",[]),
 ("sa","san","sânscrito",[]),
 ("sc","srd","sardo",[]),
 ("sr","srp","sérvio",[]),
 ("sn","sna","xona",["shona"]),
 ("sd","snd","sindi",["sindhi"]),
 ("si","sin","cingalês",[]),
 ("sk","slo","eslovaco",[]),
 ("sl","slv","esloveno",[]),
 ("so","som","somali",[]),
 ("nr","nbl","ndebele do sul",["ndebele meridional"]),
 ("st","sot","soto do sul",["sesoto"]),
 ("es","spa","espanhol",["castelhano"]),
 ("su","sun","sundanês",[]),
 ("sw","swa","suaíli",["swahili","suahili"]),
 ("ss","ssw","suázi",["swati"]),
 ("sv","swe","sueco",[]),
 ("tl","tgl","tagalo",["tagalog"]),
 ("ty","tah","taitiano",[]),
 ("tg","tgk","tajique",[]),
 ("ta","tam","tâmil",[]),
 ("tt","tat","tártaro",[]),
 ("te","tel","télugo",[]),
 ("th","tha","tailandês",[]),
 ("bo","tib","tibetano",[]),
 ("ti","tir","tigrínia",[]),
 ("to","ton","tonganês",[]),
 ("ts","tso","tsonga",[]),
 ("tn","tsn","tswana",["setswana"]),
 ("tr","tur","turco",[]),
 ("tk","tuk","turcomeno",[]),
 ("tw","twi","twi",[]),
 ("ug","uig","uigur",[]),
 ("uk","ukr","ucraniano",[]),
 ("ur","urd","urdu",[]),
 ("uz","uzb","uzbeque",[]),
 ("ve","ven","venda",[]),
 ("vi","vie","vietnamita",[]),
 ("vo","vol","volapuque",["volapük"]),
 ("wa","wln","valão",[]),
 ("cy","wel","galês",[]),
 ("fy","fry","frísio ocidental",["frísio"]),
 ("wo","wol","uolofe",["wolof"]),
 ("xh","xho","xhosa",["xossa"]),
 ("yi","yid","iídiche",[]),
 ("yo","yor","iorubá",["yoruba"]),
]

# ---------------------------------------------------------------------------
# NACIONALIDADES
#   (pais, demonym, [variant demonyms])
#   pais is a canonical name from PAISES / PAISES_NAOISO.
#   A demonym is either a string, inflected by inflect() below, or an explicit
#   tuple: (ms, fs, mp, fp) for a two-gender word, (s, p) for a common-gender
#   word.  The masculine singular is the canonical form.
# ---------------------------------------------------------------------------
NACIONALIDADES = [
 ("afeganistão",("afegão","afegã","afegãos","afegãs"),[]),
 ("albânia","albanês",[]),
 ("argélia","argelino",[]),
 ("samoa americana","samoano-americano",[]),
 ("andorra","andorrano",[]),
 ("angola","angolano",[]),
 ("anguila","anguilano",[]),
 ("antígua e barbuda","antiguano",["barbudano"]),
 ("argentina","argentino",[]),
 ("armênia","armênio",["arménio"]),
 ("aruba","arubano",[]),
 ("austrália","australiano",[]),
 ("áustria","austríaco",[]),
 ("azerbaijão","azerbaijano",["azeri"]),
 ("bahamas","baamiano",["bahamense"]),
 ("bahrein","bareinita",[]),
 ("bangladesh","bengali",["bangladeshiano"]),
 ("barbados","barbadiano",["barbadense"]),
 ("bielorrússia","bielorrusso",[]),
 ("bélgica","belga",[]),
 ("belize","belizenho",["belizense"]),
 ("benin","beninense",[]),
 ("bermudas","bermudense",["bermudiano"]),
 ("butão","butanês",[]),
 ("bolívia","boliviano",[]),
 ("bósnia e herzegovina","bósnio",["herzegovino"]),
 ("botsuana","botsuano",["bechuano"]),
 ("brasil","brasileiro",[]),
 ("brunei","bruneano",[]),
 ("bulgária","búlgaro",[]),
 ("burkina faso","burquinense",["burquinês"]),
 ("burundi","burundiano",["burundinês"]),
 ("cabo verde","cabo-verdiano",[]),
 ("camboja","cambojano",[]),
 ("camarões","camaronês",[]),
 ("canadá","canadense",["canadiano"]),
 ("ilhas cayman","caimanês",[]),
 ("república centro-africana","centro-africano",[]),
 ("chade","chadiano",[]),
 ("chile","chileno",[]),
 ("china","chinês",[]),
 ("colômbia","colombiano",[]),
 ("comores","comorense",[]),
 ("congo","congolês",["congolense"]),
 ("república democrática do congo","congolês",["congolense"]),
 ("costa rica","costarriquenho",["costa-riquenho","costarricense"]),
 ("croácia","croata",[]),
 ("cuba","cubano",[]),
 ("chipre","cipriota",[]),
 ("tchéquia","tcheco",["checo"]),
 ("costa do marfim","marfinense",["costa-marfinense"]),
 ("dinamarca","dinamarquês",[]),
 ("djibuti","djibutiano",["jibutiano"]),
 ("dominica","dominiquense",[]),
 ("república dominicana","dominicano",[]),
 ("equador","equatoriano",[]),
 ("egito","egípcio",[]),
 ("el salvador","salvadorenho",[]),
 ("guiné equatorial","equato-guineense",[]),
 ("eritreia",("eritreu","eritreia","eritreus","eritreias"),[]),
 ("estônia","estoniano",["estónio"]),
 ("essuatíni","suázi",["suazi"]),
 ("etiópia","etíope",[]),
 ("ilhas malvinas","malvinense",[]),
 ("ilhas faroé","feroês",["faroês"]),
 ("fiji","fijiano",[]),
 ("finlândia","finlandês",[]),
 ("frança","francês",[]),
 ("guiana francesa","franco-guianense",[]),
 ("polinésia francesa","polinésio",["franco-polinésio"]),
 ("gabão","gabonês",[]),
 ("gâmbia","gambiano",[]),
 ("geórgia","georgiano",[]),
 ("alemanha",("alemão","alemã","alemães","alemãs"),[]),
 ("gana","ganês",[]),
 ("gibraltar","gibraltarino",[]),
 ("grécia","grego",["heleno"]),
 ("groenlândia","groenlandês",["gronelandês"]),
 ("granada","granadino",[]),
 ("guadalupe","guadalupense",[]),
 ("guatemala","guatemalteco",[]),
 ("guiné","guineense",[]),
 ("guiné-bissau","guineense",["bissau-guineense"]),
 ("guiana","guianense",[]),
 ("haiti","haitiano",[]),
 ("santa sé","vaticano",[]),
 ("honduras","hondurenho",[]),
 ("hong kong","honconguês",[]),
 ("hungria","húngaro",[("magiar","magiares")]),
 ("islândia","islandês",[]),
 ("índia","indiano",[]),
 ("indonésia","indonésio",[]),
 ("irã","iraniano",["persa"]),
 ("iraque","iraquiano",[]),
 ("irlanda","irlandês",[]),
 ("ilha de man","manês",[]),
 ("israel","israelense",["israelita"]),
 ("itália","italiano",[]),
 ("jamaica","jamaicano",[]),
 ("japão","japonês",[]),
 ("jordânia","jordaniano",[]),
 ("cazaquistão","cazaque",["cazaquistanês"]),
 ("quênia","queniano",[]),
 ("kiribati","kiribatiano",["quiribatiano"]),
 ("coreia","coreano",[]),
 ("coreia do norte","norte-coreano",[]),
 ("coreia do sul","sul-coreano",[]),
 ("kuwait","kuwaitiano",["koweitiano"]),
 ("quirguistão",("quirguiz","quirguizes"),["quirguistanês"]),
 ("laos","laosiano",["laociano"]),
 ("letônia",("letão","letã","letões","letãs"),[]),
 ("líbano","libanês",[]),
 ("lesoto","lesotiano",[]),
 ("libéria","liberiano",[]),
 ("líbia","líbio",[]),
 ("liechtenstein","liechtensteinense",[]),
 ("lituânia","lituano",[]),
 ("luxemburgo","luxemburguês",[]),
 ("macau","macaense",[]),
 ("madagascar","malgaxe",[]),
 ("malawi","malawiano",["malauiano"]),
 ("malásia","malaio",["malásio"]),
 ("maldivas","maldívio",[]),
 ("mali","malinês",["maliano"]),
 ("malta","maltês",[]),
 ("ilhas marshall","marshallino",[]),
 ("martinica","martinicano",[]),
 ("mauritânia","mauritano",[]),
 ("maurício","mauriciano",[]),
 ("méxico","mexicano",[]),
 ("micronésia","micronésio",[]),
 ("moldávia","moldávio",["moldavo"]),
 ("mônaco","monegasco",[]),
 ("mongólia",("mongol","mongóis"),["mongoliano"]),
 ("montenegro","montenegrino",[]),
 ("marrocos","marroquino",[]),
 ("moçambique","moçambicano",[]),
 ("mianmar","birmanês",["mianmarense"]),
 ("namíbia","namibiano",[]),
 ("nauru","nauruano",[]),
 ("nepal","nepalês",[]),
 ("países baixos","neerlandês",["holandês"]),
 ("nova caledônia","neocaledônio",["neocaledónio"]),
 ("nova zelândia","neozelandês",[]),
 ("nicarágua","nicaraguense",["nicaraguano"]),
 ("níger","nigerino",[]),
 ("nigéria","nigeriano",[]),
 ("noruega","norueguês",[]),
 ("omã","omanense",["omani"]),
 ("paquistão","paquistanês",[]),
 ("palau","palauano",[]),
 ("palestina","palestino",["palestiniano"]),
 ("panamá","panamenho",[]),
 ("papua-nova guiné","papuásio",[]),
 ("paraguai","paraguaio",[]),
 ("peru","peruano",[]),
 ("filipinas","filipino",[]),
 ("polônia","polonês",["polaco"]),
 ("portugal","português",[]),
 ("porto rico","porto-riquenho",["portorriquenho"]),
 ("catar","catariano",["catari"]),
 ("macedônia do norte","macedônio",["macedónio","norte-macedônio","norte-macedónio"]),
 ("romênia","romeno",[]),
 ("rússia","russo",[]),
 ("ruanda","ruandês",[]),
 ("reunião","reunionense",[]),
 ("são cristóvão e névis","são-cristovense",[]),
 ("santa lúcia","santa-lucense",[]),
 ("são vicente e granadinas","são-vicentino",[]),
 ("samoa","samoano",[]),
 ("san marino","são-marinense",["samarinês"]),
 ("são tomé e príncipe","são-tomense",[]),
 ("arábia saudita","saudita",["árabe-saudita"]),
 ("senegal","senegalês",[]),
 ("sérvia","sérvio",[]),
 ("seicheles","seichelense",[]),
 ("serra leoa","serra-leonês",[]),
 ("singapura","singapurense",["cingapuriano"]),
 ("eslováquia","eslovaco",[]),
 ("eslovênia","esloveno",[]),
 ("ilhas salomão","salomonense",[]),
 ("somália","somali",["somaliano"]),
 ("áfrica do sul","sul-africano",[]),
 ("sudão do sul","sul-sudanês",[]),
 ("espanha",("espanhol","espanhola","espanhóis","espanholas"),[]),
 ("sri lanka","cingalês",["srilanquês"]),
 ("sudão","sudanês",[]),
 ("suriname","surinamês",[]),
 ("suécia","sueco",[]),
 ("suíça","suíço",[]),
 ("síria","sírio",[]),
 ("taiwan","taiwanês",["formosano"]),
 ("tajiquistão","tajique",["tajiquistanês"]),
 ("tanzânia","tanzaniano",[]),
 ("tailândia","tailandês",[]),
 ("timor-leste","timorense",[]),
 ("togo","togolês",[]),
 ("tonga","tonganês",[]),
 ("trinidad e tobago","trinitino",["tobaguiano"]),
 ("tunísia","tunisiano",["tunisino"]),
 ("turquia","turco",[]),
 ("turcomenistão","turcomeno",["turcomano"]),
 ("tuvalu","tuvaluano",[]),
 ("uganda","ugandense",["ugandês"]),
 ("ucrânia","ucraniano",[]),
 ("emirados árabes unidos","emiradense",["emiratense"]),
 ("reino unido","britânico",[]),
 ("estados unidos","americano",["norte-americano","estadunidense","estado-unidense"]),
 ("uruguai","uruguaio",[]),
 ("uzbequistão","uzbeque",["uzbequistanês"]),
 ("vanuatu","vanuatuense",[]),
 ("venezuela","venezuelano",[]),
 ("vietnã","vietnamita",[]),
 ("saara ocidental","saarauí",["sarauí"]),
 ("iêmen","iemenita",[]),
 ("zâmbia","zambiano",[]),
 ("zimbábue","zimbabuano",["zimbabueano"]),
 ("ilhas åland","alandês",[]),
 # --- non-ISO, as in en-nationalities ---------------------------------
 ("inglaterra","inglês",[]),
 ("escócia","escocês",[]),
 ("país de gales","galês",[]),
 ("irlanda do norte","norte-irlandês",[]),
 ("kosovo",("kosovar","kosovares"),["kosovano"]),
]

# English nationality records deliberately left without a Portuguese demonym:
# small territories for which no established Portuguese gentílico exists (a
# coined word would be worse than none).  Keyed by English country name.
SEM_GENTILICO = [
 "bonaire, sint eustatius and saba", "christmas island", "cocos",
 "cook islands", "curaçao", "guam", "guernsey", "jersey", "mayotte",
 "montserrat", "niue", "norfolk island", "northern mariana islands",
 "pitcairn", "saint barthélemy", "saint helena, ascension and tristan da cunha",
 "saint martin", "saint pierre and miquelon", "sint maarten", "tokelau",
 "turks and caicos islands", "virgin islands", "united states virgin islands",
 "wallis and futuna",
]

HDR_PAISES_DICT = """# Nomes de países em português (grafia brasileira; variantes europeias como sinônimos).
# Uma linha por forma:
#   pais=1         toda entrada
#   gen=m|f num=s|p  gênero e número do nome (ausentes quando o nome não leva
#                  artigo e o gênero não é fixo: barbados, jersey, kiribati ...)
#   sin=1          variante, nome oficial longo ou grafia europeia
#   raiz=          nome canônico (brasileiro) de uma variante
#   iso2= iso3=    códigos ISO 3166-1, os mesmos de en-countries.dict
#   naoiso=1       não é país ISO 3166-1 (inglaterra, escócia, país de gales,
#                  irlanda do norte com os códigos gb/gbr; kosovo com xk/xkx);
#                  incluídos porque são o país de nacionalidades frequentes
# Gerado por python/gen_geo_pt.py; não editar à mão.
"""

HDR_PAISES_KBB = """# Nomes de países em português, com códigos ISO 3166-1 (os mesmos de en-countries.kbb).
# Cada nome canônico traz gen=/num= e a lista sinonimo=[...] de suas variantes;
# cada variante traz raiz= apontando para o nome canônico.
# naoiso=1 marca nomes que não são países ISO 3166-1 (inglaterra, kosovo ...).
# Gerado por python/gen_geo_pt.py; não editar à mão.
"""

HDR_IDIOMAS_DICT = """# Idiomas humanos em português (grafia brasileira; variantes europeias como sinônimos).
# Uma linha por forma; todos os nomes de idiomas são masculinos.
#   idioma=1       toda entrada
#   sin=1          variante, nome alternativo ou grafia europeia
#   raiz=          nome canônico (brasileiro) de uma variante
#   laiso2= iso3=  códigos ISO 639-1 e ISO 639-2/B, como em en-languages.dict
# Gerado por python/gen_geo_pt.py; não editar à mão.
"""

HDR_IDIOMAS_KBB = """# Idiomas humanos em português, com códigos ISO 639-1 / 639-2/B (os mesmos de en-languages.kbb).
# Cada nome canônico traz a lista sinonimo=[...] de suas variantes;
# cada variante traz raiz= apontando para o nome canônico.
# Gerado por python/gen_geo_pt.py; não editar à mão.
"""

HDR_NAC_DICT = """# Nacionalidades (gentílicos) em português (grafia brasileira; variantes europeias como sinônimos).
# Uma linha por forma flexionada: masculino e feminino, singular e plural.
# Os gentílicos são ao mesmo tempo adjetivo e substantivo.
#   nacionalidade=1  toda entrada
#   gen=m|f|c      gênero (c = comum de dois gêneros: belga, canadense)
#   num=s|p        número
#   sin=1          variante, gentílico alternativo ou grafia europeia
#   raiz=          gentílico canônico (masculino singular) da forma
#   pais=          nome do país como em pt-paises.dict (chave de junção)
#   iso2= iso3=    códigos ISO 3166-1, os mesmos de pt-paises.dict e en-nationalities.dict
#   ambig=1        a forma designa mais de um país (ver pt-nacionalidades.kbb)
# Territórios desabitados (antártida, ilha bouvet, ilhas heard e mcdonald, terras
# austrais francesas, geórgia do sul, ilhas menores distantes dos estados unidos,
# território britânico do oceano índico, svalbard) não têm gentílico.  Também ficam
# de fora pequenos territórios sem gentílico consagrado em português (guernsey,
# jersey, ilhas cook, ilha christmas, ilhas cocos, ilha norfolk, pitcairn, curaçao,
# sint maarten, ilhas virgens, ...).
# Gerado por python/gen_geo_pt.py; não editar à mão.
"""

HDR_NAC_KBB = """# Nacionalidades (gentílicos) em português, relacionadas a seus países.
# Consulta direta:   nacionalidade -> país  (conceito "nacionalidades nacionalidade francês" -> pais=frança)
# Consulta inversa:  país -> nacionalidade  (conceito "nacionalidades pais frança" -> nacionalidade=francês)
# Cada nacionalidade é nomeada pelo masculino singular e traz fem= (feminino
# singular), plural= (masculino plural), fempl= (feminino plural), gen=m ou
# gen=c (comum de dois) e os códigos ISO 3166-1 do país.  Os nomes de país são
# os de pt-paises.dict / pt-paises.kbb, de modo que as duas bases se juntam.
# Uma forma que designa mais de um país leva ambig=1 e suas demais leituras
# ficam abaixo dela como <nome>1, <nome>2, ... (mesma convenção de en-nationalities.kbb).
# Entradas de país com sin=1 são variantes (holanda, eua, birmânia, irão ...)
# com raiz= apontando para o nome canônico.
# Gerado por python/gen_geo_pt.py; não editar à mão.
"""


def q(s):
    """Quote a value the way KBFuncs QuoteIfNeeded does."""
    if s == "":
        return '""'
    # The dictionary loader mangles an unquoted value whose first letter is
    # not ASCII (area=ética loads as a broken byte string), so quote those.
    if ord(s[0]) >= 128 or any(c in s for c in " \t") or any(not (c.isalnum() or c == "_") for c in s):
        return '"' + s.replace('"', '\\"') + '"'
    return s


def key(s):
    """Accent-insensitive sort key so 'áfrica' sorts with 'a'."""
    d = unicodedata.normalize("NFD", s)
    return ("".join(c for c in d if not unicodedata.combining(c)), s)


def gn(code):
    """'mp' -> ('m','p'); 'f' -> ('f','s'); '' -> (None, None)."""
    if not code:
        return None, None
    return code[0], ("p" if code.endswith("p") else "s")


def save(path, text):
    with open(path, "wb") as f:
        f.write(text.replace("\n", "\r\n").encode("utf-8"))
    print("wrote", path, len(text.splitlines()), "lines")


# ---------------------------------------------------------------------------
# countries
# ---------------------------------------------------------------------------
def pais_rows():
    """[(name, iso2, iso3, gen, num, raiz, naoiso, canonical_syns)]"""
    rows = []
    for table, naoiso in ((PAISES, False), (PAISES_NAOISO, True)):
        for iso2, iso3, name, g, vars_ in table:
            gen, num = gn(g)
            vnames = []
            for v in vars_:
                vname, vg = v.rsplit(":", 1)
                vgen, vnum = gn(vg)
                rows.append((vname, iso2, iso3, vgen, vnum, name, naoiso, []))
                vnames.append(vname)
            rows.append((name, iso2, iso3, gen, num, None, naoiso, vnames))
    return rows


def write_paises(rows, d):
    out = io.StringIO()
    out.write(HDR_PAISES_DICT)
    for name, iso2, iso3, gen, num, raiz, naoiso, _ in sorted(rows, key=lambda r: key(r[0])):
        a = ["pais=1"]
        if naoiso:
            a.append("naoiso=1")
        if raiz:
            a += ["sin=1", "raiz=" + q(raiz)]
        if gen:
            a += ["gen=" + gen, "num=" + num]
        a += ["iso2=" + iso2, "iso3=" + iso3]
        out.write(name + " " + " ".join(a) + "\n")
    save(os.path.join(d, "pt-paises.dict"), out.getvalue())

    out = io.StringIO()
    out.write(HDR_PAISES_KBB)
    out.write("paises\n")
    for name, iso2, iso3, gen, num, raiz, naoiso, syns in sorted(rows, key=lambda r: key(r[0])):
        a = ["iso2=" + iso2, "iso3=" + iso3]
        if gen:
            a += ["gen=" + gen, "num=" + num]
        if naoiso:
            a.append("naoiso=1")
        if raiz:
            a += ["sin=1", "raiz=" + q(raiz)]
        if len(syns) == 1:
            a.append("sinonimo=" + q(syns[0]))
        elif syns:
            a.append("sinonimo=[" + ",".join(q(s) for s in syns) + "]")
        out.write("  " + name + ": " + ", ".join(a) + "\n")
    save(os.path.join(d, "pt-paises.kbb"), out.getvalue())


# ---------------------------------------------------------------------------
# languages
# ---------------------------------------------------------------------------
def idioma_rows():
    rows = []
    for iso2, iso3, name, vars_ in IDIOMAS:
        rows.append((name, iso2, iso3, None, vars_))
        for v in vars_:
            rows.append((v, iso2, iso3, name, []))
    return rows


def write_idiomas(rows, d):
    out = io.StringIO()
    out.write(HDR_IDIOMAS_DICT)
    for name, iso2, iso3, raiz, _ in sorted(rows, key=lambda r: key(r[0])):
        a = ["idioma=1"]
        if raiz:
            a += ["sin=1", "raiz=" + q(raiz)]
        a += ["laiso2=" + iso2, "iso3=" + iso3]
        out.write(name + " " + " ".join(a) + "\n")
    save(os.path.join(d, "pt-idiomas.dict"), out.getvalue())

    out = io.StringIO()
    out.write(HDR_IDIOMAS_KBB)
    out.write("idiomas\n")
    for name, iso2, iso3, raiz, syns in sorted(rows, key=lambda r: key(r[0])):
        a = ["iso2=" + iso2, "iso3=" + iso3]
        if raiz:
            a += ["sin=1", "raiz=" + q(raiz)]
        if len(syns) == 1:
            a.append("sinonimo=" + q(syns[0]))
        elif syns:
            a.append("sinonimo=[" + ",".join(q(s) for s in syns) + "]")
        out.write("  " + name + ": " + ", ".join(a) + "\n")
    save(os.path.join(d, "pt-idiomas.kbb"), out.getvalue())


# ---------------------------------------------------------------------------
# nationalities
# ---------------------------------------------------------------------------
def inflect(w):
    """Return (gen, ms, fs, mp, fp); gen is 'm' (two-gender) or 'c' (common)."""
    if isinstance(w, tuple):
        if len(w) == 4:
            return ("m",) + w
        s, p = w
        return ("c", s, s, p, p)
    if w.endswith("ês"):
        st = w[:-2] + "es"
        return ("m", w, st + "a", st + "es", st + "as")
    if w.endswith("eu"):
        raise ValueError("give -eu demonym explicitly: " + w)
    if w.endswith("o"):
        st = w[:-1]
        return ("m", w, st + "a", w + "s", st + "as")
    if w[-1] in "aeií":
        return ("c", w, w, w + "s", w + "s")
    raise ValueError("cannot inflect " + w)


def nac_records():
    """[(pais, iso2, iso3, canonical inflection, [variant inflections])]"""
    canon = {}
    for iso2, iso3, name, g, vars_ in PAISES + PAISES_NAOISO:
        canon[name] = (iso2, iso3)
    recs = []
    for pais, dem, vars_ in NACIONALIDADES:
        iso2, iso3 = canon[pais]          # KeyError = pais not in pt-paises
        recs.append((pais, iso2, iso3, inflect(dem), [inflect(v) for v in vars_]))
    return recs


def write_nacionalidades(recs, rows, d):
    # surface form -> entry
    forms = {}

    def add(form, gen, num, rec, raiz, sin):
        e = forms.setdefault(form, {"gen": gen, "num": num, "recs": [],
                                    "raiz": raiz, "sin": sin})
        if rec not in e["recs"]:
            e["recs"].append(rec)
        if raiz is None:
            e["raiz"] = None
        if not sin:
            e["sin"] = False

    for rec in recs:
        pais, iso2, iso3, inf, vinfs = rec
        canon = inf[1]
        for infl, sin in [(inf, False)] + [(v, True) for v in vinfs]:
            gen, ms, fs, mp, fp = infl
            if gen == "c":
                add(ms, "c", "s", rec, None if (ms == canon) else canon, sin)
                add(mp, "c", "p", rec, canon, sin)
            else:
                add(ms, "m", "s", rec, None if (ms == canon) else canon, sin)
                add(fs, "f", "s", rec, canon, sin)
                add(mp, "m", "p", rec, canon, sin)
                add(fp, "f", "p", rec, canon, sin)

    out = io.StringIO()
    out.write(HDR_NAC_DICT)
    for form in sorted(forms, key=key):
        e = forms[form]
        pais, iso2, iso3 = e["recs"][0][:3]
        a = ["nacionalidade=1", "gen=" + e["gen"], "num=" + e["num"]]
        if e["sin"]:
            a.append("sin=1")
        if len(e["recs"]) > 1:
            a.append("ambig=1")
        if e["raiz"]:
            a.append("raiz=" + q(e["raiz"]))
        a += ["pais=" + q(pais), "iso2=" + iso2, "iso3=" + iso3]
        out.write(form + " " + " ".join(a) + "\n")
    save(os.path.join(d, "pt-nacionalidades.dict"), out.getvalue())

    def forms_attrs(inf):
        gen, ms, fs, mp, fp = inf
        return ["gen=" + gen, "fem=" + q(fs), "plural=" + q(mp), "fempl=" + q(fp)]

    out = io.StringIO()
    out.write(HDR_NAC_KBB)
    out.write("nacionalidades\n")

    # --- forward branch: nacionalidade -> pais -----------------------------
    by_dem = {}
    for rec in recs:
        by_dem.setdefault(rec[3][1], []).append(rec)
    out.write("  nacionalidade\n")
    for dem in sorted(by_dem, key=key):
        group = by_dem[dem]
        for i, rec in enumerate(group):
            pais, iso2, iso3, inf, vinfs = rec
            name = dem if i == 0 else dem + str(i)
            indent = "    " if i == 0 else "      "
            a = []
            if i == 0 and len(group) > 1:
                a.append("ambig=1")
            a += ["pais=" + q(pais), "iso2=" + iso2, "iso3=" + iso3]
            a += forms_attrs(inf)
            syn = [v[1] for v in vinfs]
            if len(syn) == 1:
                a.append("sinonimo=" + q(syn[0]))
            elif syn:
                a.append("sinonimo=[" + ",".join(q(s) for s in syn) + "]")
            out.write(indent + name + ": " + ", ".join(a) + "\n")

    # --- reverse branch: pais -> nacionalidade -----------------------------
    by_pais = {rec[0]: rec for rec in recs}
    out.write("  pais\n")
    entries = []
    for name, iso2, iso3, gen, num, raiz, naoiso, _ in rows:
        target = raiz or name
        if target in by_pais:
            entries.append((name, raiz, by_pais[target]))
    for name, raiz, rec in sorted(entries, key=lambda e: key(e[0])):
        pais, iso2, iso3, inf, _ = rec
        a = []
        if raiz:
            a += ["sin=1", "raiz=" + q(raiz)]
        a += ["nacionalidade=" + q(inf[1]), "iso2=" + iso2, "iso3=" + iso3]
        a += forms_attrs(inf)
        out.write("    " + name + ": " + ", ".join(a) + "\n")
    save(os.path.join(d, "pt-nacionalidades.kbb"), out.getvalue())
    return forms


# ---------------------------------------------------------------------------
# sanity report
# ---------------------------------------------------------------------------
def read_dict_attrs(path):
    """Yield (surface, {attr: value}) from a .dict (values unquoted)."""
    import shlex
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            i = line.index("=")
            head = line[:i].rsplit(" ", 1)
            surface = head[0]
            toks = shlex.split(head[1] + line[i:].replace("'", "\\'"))
            attrs = dict(t.split("=", 1) for t in toks)
            # skip a bare "word pos=verb" line: dict_addpos.py writes one per
            # extra part of speech, and it carries none of the entry's data
            if set(attrs) == {"pos"}:
                continue
            yield surface, attrs


def report(prows, irows, recs, forms, d):
    here = os.path.dirname(os.path.abspath(__file__))
    en = os.path.normpath(os.path.join(here, os.pardir, "languages", "English"))
    print()
    print("pt-paises:         %d names (%d canonical, %d variants)" %
          (len(prows), sum(1 for r in prows if not r[5]), sum(1 for r in prows if r[5])))
    print("pt-idiomas:        %d names (%d canonical, %d variants)" %
          (len(irows), len(IDIOMAS), len(irows) - len(IDIOMAS)))
    print("pt-nacionalidades: %d records, %d surface forms" % (len(recs), len(forms)))

    def dups(names):
        seen, out = set(), set()
        for n in names:
            (out if n in seen else seen).add(n)
        return sorted(out)
    print("duplicate country names:", dups(r[0] for r in prows))
    print("duplicate language names:", dups(r[0] for r in irows))
    print("ambiguous nationality forms:",
          sorted(f for f, e in forms.items() if len(e["recs"]) > 1))

    # A surface form in two dictionaries gets both attribute sets merged on one
    # token by dicttok, and a repeated attribute name keeps only the first value
    # (alemão: iso3=ger from pt-idiomas hides iso3=deu; eritreia: pais=1 vs
    # pais=eritreia).  English has the same overlap (french, jersey ...).
    pn = {r[0] for r in prows}
    ln = {r[0] for r in irows}
    print("forms in pt-paises and pt-nacionalidades:", sorted(pn & set(forms), key=key))
    print("forms in pt-idiomas and pt-nacionalidades:", len(ln & set(forms)))
    print("forms in pt-paises and pt-idiomas:", sorted(pn & ln, key=key))

    # nationality pais= must be a canonical pt-paises name
    canon = {r[0] for r in prows if not r[5]}
    print("nationality pais= with no pt-paises entry:",
          sorted({r[0] for r in recs if r[0] not in canon}))

    # English countries: every iso2 needs a Portuguese row
    pt_iso = {r[1] for r in prows}
    en_c = os.path.join(en, "en-countries.dict")
    if os.path.exists(en_c):
        miss = sorted({s for s, a in read_dict_attrs(en_c) if a["iso2"] not in pt_iso})
        bad3 = sorted({s for s, a in read_dict_attrs(en_c)
                       if any(r[1] == a["iso2"] and r[2] != a["iso3"] for r in prows)})
        print("en-countries names with no Portuguese row:", miss)
        print("en-countries names whose iso3 disagrees:", bad3)

    en_l = os.path.join(en, "en-languages.dict")
    if os.path.exists(en_l):
        pt_l = {r[1]: r[2] for r in irows}
        miss = sorted({s for s, a in read_dict_attrs(en_l) if a["laiso2"] not in pt_l})
        bad3 = sorted({s for s, a in read_dict_attrs(en_l)
                       if a["laiso2"] in pt_l and pt_l[a["laiso2"]] != a["iso3"]})
        print("en-languages names with no Portuguese row:", miss)
        print("en-languages names whose iso3 disagrees:", bad3)

    try:
        sys.path.insert(0, here)
        sys.dont_write_bytecode = True      # no __pycache__ beside the scripts
        import gen_nationalities as gn_en
        pt_n = {}
        for r in recs:
            pt_n[r[1]] = pt_n.get(r[1], 0) + 1
        en_n = {}
        for r in gn_en.T:
            en_n[r[1]] = en_n.get(r[1], 0) + 1
        missing = sorted(r[0] for r in gn_en.T
                         if pt_n.get(r[1], 0) < en_n[r[1]])
        print("en-nationalities countries with no Portuguese demonym (expected):",
              sorted(set(missing) & set(SEM_GENTILICO)))
        print("en-nationalities countries with no Portuguese demonym (UNEXPECTED):",
              sorted(set(missing) - set(SEM_GENTILICO)))
        extra = sorted(c for c in pt_n if c not in en_n)
        print("Portuguese demonym countries absent from English:", extra)
    except ImportError:
        print("gen_nationalities.py not found; English nationality coverage not checked")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        d = sys.argv[1]
    else:
        here = os.path.dirname(os.path.abspath(__file__))
        d = os.path.join(here, os.pardir, "languages", "Portuguese")
    d = os.path.normpath(d)
    prows = pais_rows()
    write_paises(prows, d)
    irows = idioma_rows()
    write_idiomas(irows, d)
    recs = nac_records()
    forms = write_nacionalidades(recs, prows, d)
    report(prows, irows, recs, forms, d)
