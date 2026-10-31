# -*- coding: utf-8 -*-
# DESC: Generate the Spanish country, language and nationality dictionaries and knowledge bases.
#
# WHAT IT DOES
#   Emits, in languages/Spanish:
#       es-paises.dict          es-paises.kbb           (parallel of en-countries)
#       es-idiomas.dict         es-idiomas.kbb          (parallel of en-languages)
#       es-nacionalidades.dict  es-nacionalidades.kbb   (parallel of en-nationalities)
#   from the master tables PAISES, IDIOMAS and NAC below, so the six files can
#   never drift apart.  Edit the tables and re-run; do not hand-edit the
#   generated files.
#
#   Canonical forms follow the RAE (Diccionario panhispanico de dudas,
#   apendice 5 "Paises y capitales, con sus gentilicios") and Fundeu; common
#   Latin American, older and alternative forms are listed as variants and are
#   emitted with sin=1 and raiz=<canonical>.
#
#   Attribute names are Spanish (as in languages/Portuguese); the ISO codes
#   keep the English attribute names so the Spanish and English knowledge bases
#   join on them:
#       countries      iso2= iso3=   (ISO 3166-1, as in en-countries.dict)
#       languages      laiso2= iso3= in the .dict, iso2= iso3= in the .kbb
#                      (ISO 639-1 / 639-2/B, exactly as en-languages spells them)
#
#   Gentilicios inflect for gender and number.  The master table gives the
#   masculine singular; inflect() derives the feminine and plurals (francés ->
#   francesa, franceses, francesas; belga -> belgas; marroquí -> marroquíes).
#   Forms that are the same for both genders get gen=c (comun en cuanto al
#   genero), the value pt-full.kbb uses.  Irregular words give all four forms
#   as a tuple (ms, fs, mp, fp).
#
#   A gentilicio naming more than one country (congoleño) is marked ambig=1 and
#   its further readings hang below it in the .kbb as <name>1, <name>2, ... (the
#   same convention as en-nationalities.kbb and timezones.kbb).
#
# USAGE
#   python gen_geo_es.py [output_dir]
#     output_dir  defaults to ../languages/Spanish relative to this script
#   A sanity report is printed against the English files in ../languages/English.

import io, os, sys, unicodedata

# ---------------------------------------------------------------------------
# PAISES: (canonical name, iso2, iso3, [variants])
# Every ISO 3166-1 code in en-countries.dict has one canonical row.  Korea and
# Congo keep the short name as its own row, as en-countries does ("korea" is kr,
# "congo" is cg).
# ---------------------------------------------------------------------------
PAISES = [
 ("afganistán","af","afg",[]),
 ("albania","al","alb",[]),
 ("alemania","de","deu",[]),
 ("andorra","ad","and",[]),
 ("angola","ao","ago",[]),
 ("anguila","ai","aia",["anguilla"]),
 ("antártida","aq","ata",["antártica"]),
 ("antigua y barbuda","ag","atg",[]),
 ("arabia saudí","sa","sau",["arabia saudita"]),
 ("argelia","dz","dza",[]),
 ("argentina","ar","arg",[]),
 ("armenia","am","arm",[]),
 ("aruba","aw","abw",[]),
 ("australia","au","aus",[]),
 ("austria","at","aut",[]),
 ("azerbaiyán","az","aze",[]),
 ("bahamas","bs","bhs",[]),
 ("bangladés","bd","bgd",["bangladesh"]),
 ("barbados","bb","brb",[]),
 ("baréin","bh","bhr",["bahréin","bahrein"]),
 ("bélgica","be","bel",[]),
 ("belice","bz","blz",[]),
 ("benín","bj","ben",[]),
 ("bermudas","bm","bmu",["bermuda"]),
 ("bielorrusia","by","blr",["belarús"]),
 ("birmania","mm","mmr",["myanmar"]),
 ("bolivia","bo","bol",["estado plurinacional de bolivia"]),
 ("bonaire, san eustaquio y saba","bq","bes",["caribe neerlandés"]),
 ("bosnia y herzegovina","ba","bih",["bosnia-herzegovina","bosnia"]),
 ("botsuana","bw","bwa",["botswana"]),
 ("brasil","br","bra",[]),
 ("brunéi","bn","brn",["brunei","brunéi darusalam","brunei darussalam"]),
 ("bulgaria","bg","bgr",[]),
 ("burkina faso","bf","bfa",[]),
 ("burundi","bi","bdi",[]),
 ("bután","bt","btn",[]),
 ("cabo verde","cv","cpv",[]),
 ("camboya","kh","khm",[]),
 ("camerún","cm","cmr",[]),
 ("canadá","ca","can",[]),
 ("catar","qa","qat",["qatar"]),
 ("chad","td","tcd",[]),
 ("chequia","cz","cze",["república checa"]),
 ("chile","cl","chl",[]),
 ("china","cn","chn",["república popular china"]),
 ("chipre","cy","cyp",[]),
 ("colombia","co","col",[]),
 ("comoras","km","com",[]),
 ("congo","cg","cog",["república del congo","congo-brazzaville"]),
 ("corea","kr","kor",[]),
 ("corea del norte","kp","prk",["república popular democrática de corea"]),
 ("corea del sur","kr","kor",["república de corea"]),
 ("costa de marfil","ci","civ",["côte d'ivoire"]),
 ("costa rica","cr","cri",[]),
 ("croacia","hr","hrv",[]),
 ("cuba","cu","cub",[]),
 ("curazao","cw","cuw",["curaçao"]),
 ("dinamarca","dk","dnk",[]),
 ("dominica","dm","dma",[]),
 ("ecuador","ec","ecu",[]),
 ("egipto","eg","egy",[]),
 ("el salvador","sv","slv",[]),
 ("emiratos árabes unidos","ae","are",[]),
 ("eritrea","er","eri",[]),
 ("eslovaquia","sk","svk",[]),
 ("eslovenia","si","svn",[]),
 ("españa","es","esp",[]),
 ("estados unidos","us","usa",["estados unidos de américa"]),
 ("estonia","ee","est",[]),
 ("esuatini","sz","swz",["suazilandia","eswatini"]),
 ("etiopía","et","eth",[]),
 ("filipinas","ph","phl",[]),
 ("finlandia","fi","fin",[]),
 ("fiyi","fj","fji",["fiji"]),
 ("francia","fr","fra",[]),
 ("gabón","ga","gab",[]),
 ("gambia","gm","gmb",[]),
 ("georgia","ge","geo",[]),
 ("ghana","gh","gha",[]),
 ("gibraltar","gi","gib",[]),
 ("granada","gd","grd",[]),
 ("grecia","gr","grc",[]),
 ("groenlandia","gl","grl",[]),
 ("guadalupe","gp","glp",[]),
 ("guam","gu","gum",[]),
 ("guatemala","gt","gtm",[]),
 ("guayana francesa","gf","guf",[]),
 ("guernsey","gg","ggy",["guernesey"]),
 ("guinea","gn","gin",[]),
 ("guinea ecuatorial","gq","gnq",[]),
 ("guinea-bisáu","gw","gnb",["guinea-bissau","guinea bisáu"]),
 ("guyana","gy","guy",[]),
 ("haití","ht","hti",[]),
 ("honduras","hn","hnd",[]),
 ("hong kong","hk","hkg",[]),
 ("hungría","hu","hun",[]),
 ("india","in","ind",[]),
 ("indonesia","id","idn",[]),
 ("irak","iq","irq",["iraq"]),
 ("irán","ir","irn",["república islámica de irán"]),
 ("irlanda","ie","irl",[]),
 ("isla bouvet","bv","bvt",[]),
 ("isla de man","im","imn",[]),
 ("isla de navidad","cx","cxr",[]),
 ("isla norfolk","nf","nfk",[]),
 ("islandia","is","isl",[]),
 ("islas åland","ax","ala",["åland","islas aland"]),
 ("islas caimán","ky","cym",[]),
 ("islas cocos","cc","cck",["islas keeling"]),
 ("islas cook","ck","cok",[]),
 ("islas feroe","fo","fro",[]),
 ("islas georgias del sur y sandwich del sur","gs","sgs",[]),
 ("islas heard y mcdonald","hm","hmd",[]),
 ("islas malvinas","fk","flk",["malvinas","islas falkland"]),
 ("islas marianas del norte","mp","mnp",[]),
 ("islas marshall","mh","mhl",[]),
 ("islas pitcairn","pn","pcn",[]),
 ("islas salomón","sb","slb",[]),
 ("islas turcas y caicos","tc","tca",[]),
 ("islas ultramarinas menores de los estados unidos","um","umi",[]),
 ("islas vírgenes británicas","vg","vgb",[]),
 ("islas vírgenes de los estados unidos","vi","vir",[]),
 ("israel","il","isr",[]),
 ("italia","it","ita",[]),
 ("jamaica","jm","jam",[]),
 ("japón","jp","jpn",[]),
 ("jersey","je","jey",[]),
 ("jordania","jo","jor",[]),
 ("kazajistán","kz","kaz",["kazajstán"]),
 ("kenia","ke","ken",["kenya"]),
 ("kirguistán","kg","kgz",["kirguizistán"]),
 ("kiribati","ki","kir",[]),
 ("kuwait","kw","kwt",[]),
 ("laos","la","lao",["república democrática popular lao"]),
 ("lesoto","ls","lso",["lesotho"]),
 ("letonia","lv","lva",[]),
 ("líbano","lb","lbn",[]),
 ("liberia","lr","lbr",[]),
 ("libia","ly","lby",[]),
 ("liechtenstein","li","lie",[]),
 ("lituania","lt","ltu",[]),
 ("luxemburgo","lu","lux",[]),
 ("macao","mo","mac",[]),
 ("macedonia del norte","mk","mkd",["macedonia","república de macedonia del norte"]),
 ("madagascar","mg","mdg",[]),
 ("malasia","my","mys",[]),
 ("malaui","mw","mwi",["malawi"]),
 ("maldivas","mv","mdv",[]),
 ("malí","ml","mli",[]),
 ("malta","mt","mlt",[]),
 ("marruecos","ma","mar",[]),
 ("martinica","mq","mtq",[]),
 ("mauricio","mu","mus",[]),
 ("mauritania","mr","mrt",[]),
 ("mayotte","yt","myt",[]),
 ("méxico","mx","mex",["méjico"]),
 ("micronesia","fm","fsm",["estados federados de micronesia"]),
 ("moldavia","md","mda",["moldova","república de moldavia"]),
 ("mónaco","mc","mco",[]),
 ("mongolia","mn","mng",[]),
 ("montenegro","me","mne",[]),
 ("montserrat","ms","msr",[]),
 ("mozambique","mz","moz",[]),
 ("namibia","na","nam",[]),
 ("nauru","nr","nru",[]),
 ("nepal","np","npl",[]),
 ("nicaragua","ni","nic",[]),
 ("níger","ne","ner",[]),
 ("nigeria","ng","nga",[]),
 ("niue","nu","niu",[]),
 ("noruega","no","nor",[]),
 ("nueva caledonia","nc","ncl",[]),
 ("nueva zelanda","nz","nzl",["nueva zelandia"]),
 ("omán","om","omn",[]),
 ("países bajos","nl","nld",["holanda"]),
 ("pakistán","pk","pak",["paquistán"]),
 ("palaos","pw","plw",["palau"]),
 ("palestina","ps","pse",["estado de palestina"]),
 ("panamá","pa","pan",[]),
 ("papúa nueva guinea","pg","png",[]),
 ("paraguay","py","pry",[]),
 ("perú","pe","per",[]),
 ("polinesia francesa","pf","pyf",[]),
 ("polonia","pl","pol",[]),
 ("portugal","pt","prt",[]),
 ("puerto rico","pr","pri",[]),
 ("reino unido","gb","gbr",["reino unido de gran bretaña e irlanda del norte","gran bretaña"]),
 ("república centroafricana","cf","caf",[]),
 ("república democrática del congo","cd","cod",["congo-kinsasa","rd del congo"]),
 ("república dominicana","do","dom",[]),
 ("reunión","re","reu",["la reunión","isla de la reunión"]),
 ("ruanda","rw","rwa",["rwanda"]),
 ("rumanía","ro","rou",["rumania"]),
 ("rusia","ru","rus",["federación de rusia","federación rusa"]),
 ("sahara occidental","eh","esh",["sáhara occidental"]),
 ("samoa","ws","wsm",[]),
 ("samoa americana","as","asm",["samoa estadounidense"]),
 ("san bartolomé","bl","blm",[]),
 ("san cristóbal y nieves","kn","kna",["saint kitts y nevis"]),
 ("san marino","sm","smr",[]),
 ("san martín","mf","maf",[]),
 ("san pedro y miquelón","pm","spm",[]),
 ("san vicente y las granadinas","vc","vct",[]),
 ("santa elena, ascensión y tristán de acuña","sh","shn",["santa elena"]),
 ("santa lucía","lc","lca",[]),
 ("santa sede","va","vat",["ciudad del vaticano","vaticano"]),
 ("santo tomé y príncipe","st","stp",[]),
 ("senegal","sn","sen",[]),
 ("serbia","rs","srb",[]),
 ("seychelles","sc","syc",[]),
 ("sierra leona","sl","sle",[]),
 ("singapur","sg","sgp",[]),
 ("sint maarten","sx","sxm",[]),
 ("siria","sy","syr",["república árabe siria"]),
 ("somalia","so","som",[]),
 ("sri lanka","lk","lka",[]),
 ("sudáfrica","za","zaf",[]),
 ("sudán","sd","sdn",[]),
 ("sudán del sur","ss","ssd",[]),
 ("suecia","se","swe",[]),
 ("suiza","ch","che",[]),
 ("surinam","sr","sur",["suriname"]),
 ("svalbard y jan mayen","sj","sjm",[]),
 ("tailandia","th","tha",[]),
 ("taiwán","tw","twn",[]),
 ("tanzania","tz","tza",["república unida de tanzania"]),
 ("tayikistán","tj","tjk",[]),
 ("territorio británico del océano índico","io","iot",[]),
 ("tierras australes y antárticas francesas","tf","atf",["territorios australes franceses"]),
 ("timor oriental","tl","tls",["timor-leste","timor leste"]),
 ("togo","tg","tgo",[]),
 ("tokelau","tk","tkl",[]),
 ("tonga","to","ton",[]),
 ("trinidad y tobago","tt","tto",[]),
 ("túnez","tn","tun",[]),
 ("turkmenistán","tm","tkm",[]),
 ("turquía","tr","tur",["türkiye"]),
 ("tuvalu","tv","tuv",[]),
 ("ucrania","ua","ukr",[]),
 ("uganda","ug","uga",[]),
 ("uruguay","uy","ury",[]),
 ("uzbekistán","uz","uzb",[]),
 ("vanuatu","vu","vut",[]),
 ("venezuela","ve","ven",["república bolivariana de venezuela"]),
 ("vietnam","vn","vnm",["viet nam"]),
 ("wallis y futuna","wf","wlf",[]),
 ("yemen","ye","yem",[]),
 ("yibuti","dj","dji",["djibouti"]),
 ("zambia","zm","zmb",[]),
 ("zimbabue","zw","zwe",["zimbabwe"]),
 # --- not ISO 3166-1 countries ----------------------------------------------
 # Present so every gentilicio in es-nacionalidades has a pais= entry here.
 # The constituent nations of the United Kingdom carry the UK's gb/gbr codes;
 # Kosovo carries xk/xkx, the user-assigned code in common use.  Marked noiso=1.
 ("inglaterra","gb","gbr",[]),
 ("escocia","gb","gbr",[]),
 ("gales","gb","gbr",["país de gales"]),
 ("irlanda del norte","gb","gbr",[]),
 ("kosovo","xk","xkx",[]),
]
NOISO = {"inglaterra", "escocia", "gales", "irlanda del norte", "kosovo"}

# ---------------------------------------------------------------------------
# IDIOMAS: (canonical name, laiso2, iso3, [variants])
# One row per ISO 639-1 code in en-languages.dict; iso3 is the ISO 639-2/B
# code exactly as en-languages.dict has it.
# ---------------------------------------------------------------------------
IDIOMAS = [
 ("abjasio","ab","abk",["abjaso"]),
 ("afar","aa","aar",[]),
 ("afrikáans","af","afr",["afrikaans"]),
 ("aimara","ay","aym",["aimará","aymara"]),
 ("akan","ak","aka",[]),
 ("albanés","sq","alb",[]),
 ("alemán","de","ger",[]),
 ("amhárico","am","amh",[]),
 ("árabe","ar","ara",[]),
 ("aragonés","an","arg",[]),
 ("armenio","hy","arm",[]),
 ("asamés","as","asm",[]),
 ("avar","av","ava",[]),
 ("avéstico","ae","ave",[]),
 ("azerí","az","aze",["azerbaiyano"]),
 ("bambara","bm","bam",[]),
 ("baskir","ba","bak",[]),
 ("bengalí","bn","ben",["bangla"]),
 ("bielorruso","be","bel",[]),
 ("birmano","my","bur",[]),
 ("bislama","bi","bis",[]),
 ("bosnio","bs","bos",[]),
 ("bretón","br","bre",[]),
 ("búlgaro","bg","bul",[]),
 ("cachemir","ks","kas",["cachemiro","cachemiri"]),
 ("canarés","kn","kan",["kannada"]),
 ("catalán","ca","cat",["valenciano"]),
 ("chamorro","ch","cha",[]),
 ("checheno","ce","che",[]),
 ("checo","cs","cze",[]),
 ("chichewa","ny","nya",["chewa","nyanja"]),
 ("chino","zh","chi",[]),
 ("chuang","za","zha",["zhuang"]),
 ("chuvasio","cv","chv",[]),
 ("cingalés","si","sin",[]),
 ("coreano","ko","kor",[]),
 ("córnico","kw","cor",[]),
 ("corso","co","cos",[]),
 ("cree","cr","cre",[]),
 ("criollo haitiano","ht","hat",["haitiano"]),
 ("croata","hr","hrv",[]),
 ("danés","da","dan",[]),
 ("divehi","dv","div",["dhivehi","maldivo"]),
 ("dzongkha","dz","dzo",[]),
 ("eslavo eclesiástico","cu","chu",["eslavo eclesiástico antiguo","antiguo eslavo eclesiástico"]),
 ("eslovaco","sk","slo",[]),
 ("esloveno","sl","slv",[]),
 ("español","es","spa",["castellano"]),
 ("esperanto","eo","epo",[]),
 ("estonio","et","est",[]),
 ("euskera","eu","baq",["vasco","vascuence","euskara"]),
 ("ewe","ee","ewe",[]),
 ("feroés","fo","fao",[]),
 ("finés","fi","fin",["finlandés"]),
 ("fiyiano","fj","fij",[]),
 ("francés","fr","fre",[]),
 ("frisón","fy","fry",["frisón occidental"]),
 ("fula","ff","ful",["fulani","peul"]),
 ("gaélico escocés","gd","gla",["gaélico"]),
 ("galés","cy","wel",[]),
 ("gallego","gl","glg",[]),
 ("georgiano","ka","geo",[]),
 ("griego","el","gre",[]),
 ("groenlandés","kl","kal",["kalaallisut"]),
 ("guaraní","gn","grn",[]),
 ("guyaratí","gu","guj",["gujarati"]),
 ("hausa","ha","hau",[]),
 ("hebreo","he","heb",[]),
 ("herero","hz","her",[]),
 ("hindi","hi","hin",[]),
 ("hiri motu","ho","hmo",[]),
 ("húngaro","hu","hun",["magiar"]),
 ("ido","io","ido",[]),
 ("igbo","ig","ibo",[]),
 ("indonesio","id","ind",[]),
 ("inglés","en","eng",[]),
 ("interlingua","ia","ina",[]),
 ("interlingue","ie","ile",["occidental"]),
 ("inuktitut","iu","iku",[]),
 ("inupiaq","ik","ipk",[]),
 ("irlandés","ga","gle",["gaélico irlandés"]),
 ("islandés","is","ice",[]),
 ("italiano","it","ita",[]),
 ("japonés","ja","jpn",[]),
 ("javanés","jv","jav",[]),
 ("jemer","km","khm",["camboyano","khmer"]),
 ("kanuri","kr","kau",[]),
 ("kazajo","kk","kaz",["kazako"]),
 ("kikongo","kg","kon",["kongo"]),
 ("kikuyu","ki","kik",["gikuyu"]),
 ("kinyarwanda","rw","kin",[]),
 ("kirguís","ky","kir",["kirguiso"]),
 ("kirundi","rn","run",["rundi"]),
 ("komi","kv","kom",[]),
 ("kuanyama","kj","kua",["kwanyama"]),
 ("kurdo","ku","kur",[]),
 ("lao","lo","lao",["laosiano"]),
 ("latín","la","lat",[]),
 ("letón","lv","lav",[]),
 ("limburgués","li","lim",[]),
 ("lingala","ln","lin",[]),
 ("lituano","lt","lit",[]),
 ("luba-katanga","lu","lub",[]),
 ("luganda","lg","lug",["ganda"]),
 ("luxemburgués","lb","ltz",[]),
 ("macedonio","mk","mac",[]),
 ("malayalam","ml","mal",[]),
 ("malayo","ms","may",[]),
 ("malgache","mg","mlg",[]),
 ("maltés","mt","mlt",[]),
 ("manés","gv","glv",[]),
 ("maorí","mi","mao",[]),
 ("maratí","mr","mar",["marathi"]),
 ("marshalés","mh","mah",[]),
 ("mongol","mn","mon",[]),
 ("nauruano","na","nau",[]),
 ("navajo","nv","nav",["navaho"]),
 ("ndebele del norte","nd","nde",[]),
 ("ndebele del sur","nr","nbl",[]),
 ("ndonga","ng","ndo",[]),
 ("neerlandés","nl","dut",["holandés","flamenco"]),
 ("nepalí","ne","nep",[]),
 ("noruego","no","nor",[]),
 ("noruego bokmål","nb","nob",["bokmål"]),
 ("noruego nynorsk","nn","nno",["nynorsk"]),
 ("occitano","oc","oci",[]),
 ("ojibwa","oj","oji",["ojibwe"]),
 ("oriya","or","ori",["odia"]),
 ("oromo","om","orm",[]),
 ("osetio","os","oss",["oseta","osético"]),
 ("pali","pi","pli",[]),
 ("panyabí","pa","pan",["punyabí","panjabi","punjabi"]),
 ("pastún","ps","pus",["pastó","pashto"]),
 ("persa","fa","per",["farsi"]),
 ("polaco","pl","pol",[]),
 ("portugués","pt","por",[]),
 ("quechua","qu","que",[]),
 ("romanche","rm","roh",[]),
 ("rumano","ro","rum",["moldavo"]),
 ("ruso","ru","rus",[]),
 ("sami septentrional","se","sme",["sami del norte"]),
 ("samoano","sm","smo",[]),
 ("sango","sg","sag",[]),
 ("sánscrito","sa","san",[]),
 ("sardo","sc","srd",[]),
 ("serbio","sr","srp",[]),
 ("sesotho","st","sot",["sotho del sur"]),
 ("setsuana","tn","tsn",["tswana"]),
 ("shona","sn","sna",[]),
 ("sindi","sd","snd",[]),
 ("somalí","so","som",[]),
 ("suajili","sw","swa",["swahili"]),
 ("suazi","ss","ssw",["swati"]),
 ("sueco","sv","swe",[]),
 ("sundanés","su","sun",[]),
 ("tagalo","tl","tgl",[]),
 ("tahitiano","ty","tah",[]),
 ("tailandés","th","tha",[]),
 ("tamil","ta","tam",[]),
 ("tártaro","tt","tat",[]),
 ("tayiko","tg","tgk",[]),
 ("telugu","te","tel",[]),
 ("tibetano","bo","tib",[]),
 ("tigriña","ti","tir",[]),
 ("tongano","to","ton",[]),
 ("tsonga","ts","tso",[]),
 ("turco","tr","tur",[]),
 ("turcomano","tk","tuk",["turkmeno"]),
 ("twi","tw","twi",[]),
 ("ucraniano","uk","ukr",[]),
 ("uigur","ug","uig",[]),
 ("urdu","ur","urd",[]),
 ("uzbeko","uz","uzb",[]),
 ("valón","wa","wln",[]),
 ("venda","ve","ven",[]),
 ("vietnamita","vi","vie",[]),
 ("volapük","vo","vol",[]),
 ("wolof","wo","wol",[]),
 ("xhosa","xh","xho",[]),
 ("yi de sichuan","ii","iii",["nuosu"]),
 ("yidis","yi","yid",["yiddish","ídish"]),
 ("yoruba","yo","yor",[]),
]

# ---------------------------------------------------------------------------
# NAC: (pais, gentilicio, [variants])
#   pais        canonical name as keyed in PAISES (iso2/iso3 come from there)
#   gentilicio  masculine singular, or a tuple (ms, fs, mp, fp) when irregular
#   variants    other gentilicios for the same country, same notation
# ---------------------------------------------------------------------------
NAC = [
 ("afganistán","afgano",[]),
 ("albania","albanés",[]),
 ("alemania","alemán",[]),
 ("andorra","andorrano",[]),
 ("angola","angoleño",["angolano"]),
 ("anguila","anguilense",[]),
 ("antigua y barbuda","antiguano",["barbudense"]),
 ("arabia saudí","saudí",["saudita"]),
 ("argelia","argelino",[]),
 ("argentina","argentino",[]),
 ("armenia","armenio",[]),
 ("aruba","arubeño",[]),
 ("australia","australiano",[]),
 ("austria","austriaco",["austríaco"]),
 ("azerbaiyán","azerbaiyano",["azerí"]),
 ("bahamas","bahameño",[]),
 ("bangladés","bangladesí",[]),
 ("barbados","barbadense",[]),
 ("baréin","bareiní",["bahreiní"]),
 ("bélgica","belga",[]),
 ("belice","beliceño",[]),
 ("benín","beninés",[]),
 ("bermudas","bermudeño",[]),
 ("bielorrusia","bielorruso",[]),
 ("birmania","birmano",[]),
 ("bolivia","boliviano",[]),
 ("bosnia y herzegovina","bosnio",["bosnioherzegovino"]),
 ("botsuana","botsuano",[]),
 ("brasil","brasileño",["brasilero"]),
 ("brunéi","bruneano",[]),
 ("bulgaria","búlgaro",[]),
 ("burkina faso","burkinés",[]),
 ("burundi","burundés",[]),
 ("bután","butanés",[]),
 ("cabo verde","caboverdiano",[]),
 ("camboya","camboyano",["jemer"]),
 ("camerún","camerunés",[]),
 ("canadá","canadiense",[]),
 ("catar","catarí",["qatarí"]),
 ("chad","chadiano",[]),
 ("chequia","checo",[]),
 ("chile","chileno",[]),
 ("china","chino",[]),
 ("chipre","chipriota",[]),
 ("colombia","colombiano",[]),
 ("comoras","comorense",[]),
 ("congo","congoleño",["congolés"]),
 ("república democrática del congo","congoleño",["congolés"]),
 ("corea","coreano",[]),
 ("corea del norte","norcoreano",[]),
 ("corea del sur","surcoreano",[]),
 ("costa de marfil","marfileño",[]),
 ("costa rica","costarricense",["costarriqueño"]),
 ("croacia","croata",[]),
 ("cuba","cubano",[]),
 ("curazao","curazoleño",[]),
 ("dinamarca","danés",["dinamarqués"]),
 ("dominica","dominiqués",[]),
 ("ecuador","ecuatoriano",[]),
 ("egipto","egipcio",[]),
 ("el salvador","salvadoreño",[]),
 ("emiratos árabes unidos","emiratí",[]),
 ("eritrea","eritreo",[]),
 ("eslovaquia","eslovaco",[]),
 ("eslovenia","esloveno",[]),
 ("españa","español",[]),
 ("estados unidos","estadounidense",["norteamericano"]),
 ("estonia","estonio",[]),
 ("esuatini","suazi",["suazilandés"]),
 ("etiopía","etíope",[]),
 ("filipinas","filipino",[]),
 ("finlandia","finlandés",["finés"]),
 ("fiyi","fiyiano",[]),
 ("francia","francés",[]),
 ("gabón","gabonés",[]),
 ("gambia","gambiano",[]),
 ("georgia","georgiano",[]),
 ("ghana","ghanés",[]),
 ("gibraltar","gibraltareño",[]),
 ("granada","granadino",[]),
 ("grecia","griego",["heleno"]),
 ("groenlandia","groenlandés",[]),
 ("guadalupe","guadalupeño",[]),
 ("guam","guameño",[]),
 ("guatemala","guatemalteco",[]),
 ("guayana francesa","guayanés",[]),
 ("guinea","guineano",[]),
 ("guinea ecuatorial","ecuatoguineano",["guineoecuatoriano"]),
 ("guinea-bisáu","bisauguineano",[]),
 ("guyana","guyanés",[]),
 ("haití","haitiano",[]),
 ("honduras","hondureño",[]),
 ("hong kong","hongkonés",[]),
 ("hungría","húngaro",["magiar"]),
 ("india","indio",["hindú"]),
 ("indonesia","indonesio",[]),
 ("irak","iraquí",[]),
 ("irán","iraní",["persa"]),
 ("irlanda","irlandés",[]),
 ("isla de man","manés",[]),
 ("islandia","islandés",[]),
 ("islas caimán","caimanés",[]),
 ("islas feroe","feroés",[]),
 ("islas malvinas","malvinense",[]),
 ("islas marshall","marshalés",[]),
 ("islas salomón","salomonense",[]),
 ("israel","israelí",[]),
 ("italia","italiano",[]),
 ("jamaica","jamaicano",["jamaiquino"]),
 ("japón","japonés",["nipón"]),
 ("jordania","jordano",[]),
 ("kazajistán","kazajo",["kazako"]),
 ("kenia","keniano",["keniata"]),
 ("kirguistán",("kirguís","kirguís","kirguises","kirguises"),["kirguiso"]),
 ("kiribati","kiribatiano",[]),
 ("kuwait","kuwaití",[]),
 ("laos","laosiano",[]),
 ("lesoto","lesotense",[]),
 ("letonia","letón",[]),
 ("líbano","libanés",[]),
 ("liberia","liberiano",[]),
 ("libia","libio",[]),
 ("liechtenstein","liechtensteiniano",[]),
 ("lituania","lituano",[]),
 ("luxemburgo","luxemburgués",[]),
 ("macao","macaense",[]),
 ("macedonia del norte","macedonio",["normacedonio"]),
 ("madagascar","malgache",[]),
 ("malasia","malasio",[]),
 ("malaui","malauí",[]),
 ("maldivas","maldivo",[]),
 ("malí","maliense",["malí"]),
 ("malta","maltés",[]),
 ("marruecos","marroquí",[]),
 ("martinica","martiniqués",[]),
 ("mauricio","mauriciano",[]),
 ("mauritania","mauritano",[]),
 ("mayotte","mahorés",[]),
 ("méxico","mexicano",["mejicano"]),
 ("micronesia","micronesio",[]),
 ("moldavia","moldavo",[]),
 ("mónaco","monegasco",[]),
 ("mongolia","mongol",[]),
 ("montenegro","montenegrino",[]),
 ("montserrat","montserratense",[]),
 ("mozambique","mozambiqueño",[]),
 ("namibia","namibio",[]),
 ("nauru","nauruano",[]),
 ("nepal","nepalí",["nepalés"]),
 ("nicaragua","nicaragüense",[]),
 ("níger","nigerino",[]),
 ("nigeria","nigeriano",[]),
 ("niue","niuano",[]),
 ("noruega","noruego",[]),
 ("nueva caledonia","neocaledonio",[]),
 ("nueva zelanda","neozelandés",[]),
 ("omán","omaní",[]),
 ("países bajos","neerlandés",["holandés"]),
 ("pakistán","pakistaní",["paquistaní"]),
 ("palaos","palauano",[]),
 ("palestina","palestino",[]),
 ("panamá","panameño",[]),
 ("papúa nueva guinea","papú",["papuano"]),
 ("paraguay","paraguayo",[]),
 ("perú","peruano",[]),
 ("polinesia francesa","polinesio",[]),
 ("polonia","polaco",[]),
 ("portugal","portugués",["luso"]),
 ("puerto rico","puertorriqueño",["portorriqueño","boricua"]),
 ("reino unido","británico",[]),
 ("república centroafricana","centroafricano",[]),
 ("república dominicana","dominicano",[]),
 ("reunión","reunionés",[]),
 ("ruanda","ruandés",[]),
 ("rumanía","rumano",[]),
 ("rusia","ruso",[]),
 ("sahara occidental","saharaui",[]),
 ("samoa","samoano",[]),
 ("samoa americana","samoano",[]),
 ("san cristóbal y nieves","sancristobaleño",[]),
 ("san marino","sanmarinense",[]),
 ("san vicente y las granadinas","sanvicentino",[]),
 ("santa lucía","santalucense",[]),
 ("santa sede","vaticano",[]),
 ("santo tomé y príncipe","santotomense",[]),
 ("senegal","senegalés",[]),
 ("serbia","serbio",[]),
 ("seychelles","seychellense",[]),
 ("sierra leona","sierraleonés",[]),
 ("singapur","singapurense",[]),
 ("siria","sirio",[]),
 ("somalia","somalí",[]),
 ("sri lanka","ceilanés",["esrilanqués"]),
 ("sudáfrica","sudafricano",[]),
 ("sudán","sudanés",[]),
 ("sudán del sur","sursudanés",[]),
 ("suecia","sueco",[]),
 ("suiza","suizo",[]),
 ("surinam","surinamés",[]),
 ("tailandia","tailandés",[]),
 ("taiwán","taiwanés",[]),
 ("tanzania","tanzano",[]),
 ("tayikistán","tayiko",[]),
 ("timor oriental","timorense",[]),
 ("togo","togolés",[]),
 ("tokelau","tokelauano",[]),
 ("tonga","tongano",[]),
 ("trinidad y tobago","trinitense",[]),
 ("túnez","tunecino",[]),
 ("turkmenistán","turcomano",["turkmeno"]),
 ("turquía","turco",[]),
 ("tuvalu","tuvaluano",[]),
 ("ucrania","ucraniano",["ucranio"]),
 ("uganda","ugandés",[]),
 ("uruguay","uruguayo",[]),
 ("uzbekistán","uzbeko",[]),
 ("vanuatu","vanuatuense",[]),
 ("venezuela","venezolano",[]),
 ("vietnam","vietnamita",[]),
 ("yemen","yemení",[]),
 ("yibuti","yibutiano",[]),
 ("zambia","zambiano",[]),
 ("zimbabue","zimbabuense",[]),
 # --- not ISO countries (see NOISO) -------------------------------------------
 ("inglaterra","inglés",[]),
 ("escocia","escocés",[]),
 ("gales","galés",[]),
 ("irlanda del norte","norirlandés",[]),
 ("kosovo","kosovar",[]),
]

# ISO entries with no established Spanish gentilicio.  Left out of
# es-nacionalidades on purpose (the sanity report checks this list).  The
# English file lists the inhabited ones with "X islander" style demonyms,
# which have no settled Spanish equivalent in the RAE or Fundeu lists.
SIN_GENTILICIO = {
    "bq": "bonaire, san eustaquio y saba",
    "cc": "islas cocos", "ck": "islas cook", "cx": "isla de navidad",
    "gg": "guernsey", "je": "jersey", "nf": "isla norfolk", "pn": "islas pitcairn",
    "tc": "islas turcas y caicos", "vg": "islas vírgenes británicas",
    "vi": "islas vírgenes de los estados unidos", "mp": "islas marianas del norte",
    "bl": "san bartolomé", "mf": "san martín", "sx": "sint maarten",
    "pm": "san pedro y miquelón", "wf": "wallis y futuna", "ax": "islas åland",
    "sh": "santa elena, ascensión y tristán de acuña",
    # uninhabited (also absent from en-nationalities)
    "aq": "antártida", "bv": "isla bouvet", "hm": "islas heard y mcdonald",
    "tf": "tierras australes y antárticas francesas",
    "gs": "islas georgias del sur y sandwich del sur",
    "um": "islas ultramarinas menores de los estados unidos",
    "io": "territorio británico del océano índico", "sj": "svalbard y jan mayen",
}


# ---------------------------------------------------------------------------
HDR_PAISES_DICT = """# Nombres de países en español.
# Una línea por forma: el nombre canónico (RAE / Fundéu) y sus variantes de uso
# común (formas latinoamericanas, antiguas, oficiales largas o en otra grafía).
#   pais=1         toda entrada
#   sin=1          variante o sinónimo del nombre canónico
#   raiz=          nombre canónico de una variante
#   iso2= iso3=    códigos ISO 3166-1, los mismos de en-countries.dict
#   noiso=1        no es un país ISO 3166-1 (ver abajo)
# "corea" (kr) y "congo" (cg) son entradas propias, como "korea" y "congo" en
# en-countries.dict.  Cinco entradas no son países ISO y llevan noiso=1:
# inglaterra, escocia, gales e irlanda del norte (con los códigos gb/gbr del
# Reino Unido) y kosovo (xk/xkx, el código de uso común); existen para que
# cada pais= de es-nacionalidades.dict tenga su entrada aquí.
# Generado por python/gen_geo_es.py: no editar a mano.
"""

HDR_PAISES_KBB = """# Nombres de países en español.
# Cada país canónico lleva sus códigos ISO 3166-1 (los mismos de en-countries.kbb,
# para unir las dos bases de conocimiento) y, si las tiene, sus variantes en
# sinonimo=.  Cada variante es también un concepto propio con sin=1 y raiz=
# (el nombre canónico).  noiso=1 marca las cinco entradas que no son países ISO
# (inglaterra, escocia, gales, irlanda del norte, kosovo).
# Generado por python/gen_geo_es.py: no editar a mano.
"""

HDR_IDIOMAS_DICT = """# Nombres de idiomas en español.
# Una línea por forma: el nombre canónico (RAE / Fundéu) y sus variantes.
#   idioma=1       toda entrada
#   sin=1          variante o sinónimo del nombre canónico
#   laiso2=        código ISO 639-1, como en en-languages.dict
#   iso3=          código ISO 639-2/B, como en en-languages.dict
#   raiz=          nombre canónico de una variante
# Muchas formas coinciden con el gentilicio masculino singular (español,
# francés); esas lecturas de nacionalidad están en es-nacionalidades.dict.
# Generado por python/gen_geo_es.py: no editar a mano.
"""

HDR_IDIOMAS_KBB = """# Nombres de idiomas en español.
# Cada idioma canónico lleva sus códigos ISO 639-1 (iso2=) e ISO 639-2/B (iso3=),
# los mismos de en-languages.kbb, y sus variantes en sinonimo=.  Cada variante es
# también un concepto propio con sin=1 y raiz= (el nombre canónico).
# Generado por python/gen_geo_es.py: no editar a mano.
"""

HDR_NAC_DICT = """# Gentilicios (nacionalidades) en español.
# Una línea por forma: masculino y femenino, singular y plural, y cada variante.
# Todas las formas sirven como adjetivo y como sustantivo.
#   nacionalidad=1 toda entrada
#   gen=           m (masculino), f (femenino) o c (común: misma forma para los dos)
#   num=           s (singular) o p (plural)
#   sin=1          gentilicio alternativo (variante de la forma canónica)
#   ambig=1        la forma nombra más de un país (ver es-nacionalidades.kbb)
#   raiz=          forma canónica (masculino singular) de toda forma que no lo es
#   pais=          nombre del país tal como figura en es-paises.dict
#   iso2= iso3=    códigos ISO 3166-1, los mismos de es-paises.dict y en-countries.dict
# Formas canónicas según el Diccionario panhispánico de dudas y Fundéu.  Los
# gentilicios en -í/-ú hacen el plural en -íes/-úes; la variante en -ís/-ús
# figura con sin=1.
# Los territorios ISO sin gentilicio asentado en español no figuran: islas
# cocos, islas cook, isla de navidad, isla norfolk, islas pitcairn, islas
# turcas y caicos, islas vírgenes (británicas y estadounidenses), islas
# marianas del norte, guernsey, jersey, san bartolomé, san martín, sint
# maarten, san pedro y miquelón, wallis y futuna, islas åland, santa elena y
# bonaire, san eustaquio y saba.  Tampoco los territorios deshabitados.
# Generado por python/gen_geo_es.py: no editar a mano.
"""

HDR_NAC_KBB = """# Gentilicios (nacionalidades) en español, relacionados con sus países.
# Búsqueda directa:  nacionalidad -> país  (concepto "nacionalidades nacionalidad francés" -> pais=francia)
# Búsqueda inversa:  país -> nacionalidad  (concepto "nacionalidades pais francia" -> nacionalidad=francés)
# Cada gentilicio lleva el masculino singular (nombre del concepto), el
# femenino singular (fs=), los plurales masculino y femenino (mp=, fp=) y los
# códigos ISO 3166-1 de su país.  gen=c marca los de forma común a los dos
# géneros (belga, estadounidense).  Los nombres de país coinciden con
# es-paises.dict / es-paises.kbb para que las dos bases de conocimiento se unan.
# Una forma que nombra más de un país lleva ambig=1 y sus otras lecturas
# cuelgan debajo como <nombre>1, <nombre>2, ... (la misma convención de
# en-nationalities.kbb y timezones.kbb).
# Los países con alias=1 son variantes de es-paises (holanda, birmania,
# república checa, ...) y no el nombre canónico.
# Generado por python/gen_geo_es.py: no editar a mano.
"""


def q(s):
    """Quote a value the way KBFuncs QuoteIfNeeded does."""
    if s == "":
        return '""'
    if any(c in s for c in " \t") or any(not (c.isalnum() or c == "_") for c in s):
        return '"' + s.replace('"', '\\"') + '"'
    return s


def strip_accent(s):
    """Drop the acute accent on the last vowel (francés -> frances)."""
    return unicodedata.normalize("NFC", "".join(
        c for c in unicodedata.normalize("NFD", s) if c != "́"))


def inflect(g):
    """Return (ms, fs, mp, fp) for a masculine singular gentilicio."""
    if isinstance(g, tuple):
        return g
    w = g
    if w.endswith("o"):
        b = w[:-1]
        return (w, b + "a", w + "s", b + "as")
    if w[-1] in "íú":                       # marroquí, hindú: común, -íes
        return (w, w, w + "es", w + "es")
    if w[-1] in "aei":                      # belga, estadounidense, saharaui
        return (w, w, w + "s", w + "s")
    if w[-2:] in ("és", "án", "ín", "ón"):  # francés, alemán, letón
        b = w[:-2] + strip_accent(w[-2]) + w[-1]
        return (w, b + "a", b + "es", b + "as")
    if w.endswith("l"):                     # español, mongol
        return (w, w + "a", w + "es", w + "as")
    if w.endswith("r"):                     # kosovar, magiar, jemer: común
        return (w, w, w + "es", w + "es")
    raise ValueError("cannot inflect " + w)


def gennum(forms4):
    """Map each surface form of (ms, fs, mp, fp) to its gen/num values."""
    ms, fs, mp, fp = forms4
    out = {}
    for form, gen, num in ((ms, "m", "s"), (fs, "f", "s"), (mp, "m", "p"), (fp, "f", "p")):
        out.setdefault(form, (set(), num))[0].add(gen)
    return {f: ("c" if len(g) > 1 else g.pop(), n) for f, (g, n) in out.items()}


def save(path, text):
    with open(path, "wb") as f:
        f.write(text.replace("\n", "\r\n").encode("utf-8"))
    print("wrote", path, len(text.splitlines()), "lines")


# ---------------------------------------------------------------------------
# es-paises / es-idiomas (same shape: canonical rows plus variants)
# ---------------------------------------------------------------------------
def write_names(rows, flag, iso2name, hdr_dict, hdr_kbb, kbroot, dpath, kpath, noiso=()):
    lines = {}
    for name, c2, c3, variants in rows:
        for form, root in [(name, None)] + [(v, name) for v in variants]:
            if form in lines:
                raise ValueError("duplicate %s form %s" % (flag, form))
            attrs = [flag + "=1"]
            if root:
                attrs.append("sin=1")
            if name in noiso:
                attrs.append("noiso=1")
            attrs += [iso2name + "=" + c2, "iso3=" + c3]
            if root:
                attrs.append("raiz=" + q(root))
            lines[form] = form + " " + " ".join(attrs)
    save(dpath, hdr_dict + "".join(lines[k] + "\n" for k in sorted(lines)))

    kb = {}
    for name, c2, c3, variants in rows:
        attrs = []
        if name in noiso:
            attrs.append("noiso=1")
        attrs += ["iso2=" + c2, "iso3=" + c3]
        if len(variants) == 1:
            attrs.append("sinonimo=" + q(variants[0]))
        elif variants:
            attrs.append("sinonimo=[" + ",".join(q(v) for v in variants) + "]")
        kb[name] = attrs
        for v in variants:
            kb[v] = ["sin=1", "raiz=" + q(name), "iso2=" + c2, "iso3=" + c3]
    save(kpath, hdr_kbb + kbroot + "\n" +
         "".join("  " + k + ": " + ", ".join(kb[k]) + "\n" for k in sorted(kb)))
    return lines


# ---------------------------------------------------------------------------
# es-nacionalidades
# ---------------------------------------------------------------------------
def build_nac(pais_iso):
    """surface form -> {gen, num, sin, root, recs}"""
    forms = {}

    def add(form, gen, num, sin, rec, root):
        e = forms.setdefault(form, {"gen": gen, "num": num, "sin": sin,
                                    "recs": [], "root": root})
        if (e["gen"], e["num"]) != (gen, num):
            # same spelling, different features across records: widen gender
            if e["num"] != num:
                raise ValueError("number clash on " + form)
            e["gen"] = "c"
        e["sin"] = e["sin"] and sin
        if rec not in e["recs"]:
            e["recs"].append(rec)
        if root is None:
            e["root"] = None

    for rec in NAC:
        pais, g, syns = rec
        canon = inflect(g)
        ms = canon[0]
        for form, (gen, num) in gennum(canon).items():
            add(form, gen, num, False, rec, None if form == ms else ms)
        for s in syns:
            sf = inflect(s)
            for form, (gen, num) in gennum(sf).items():
                add(form, gen, num, True, rec, ms)
            # accepted -ís / -ús plural of an -í / -ú gentilicio
        for s in [g] + syns:
            m = inflect(s)[0]
            if m[-1] in "íú":
                add(m + "s", "c", "p", True, rec, ms)
    return forms


def write_nac(forms, pais_iso, dpath, kpath):
    out = io.StringIO()
    out.write(HDR_NAC_DICT)
    for form in sorted(forms):
        e = forms[form]
        pais = e["recs"][0][0]
        c2, c3 = pais_iso[pais]
        attrs = ["nacionalidad=1", "gen=" + e["gen"], "num=" + e["num"]]
        if e["sin"]:
            attrs.append("sin=1")
        if len(e["recs"]) > 1:
            attrs.append("ambig=1")
        if e["root"]:
            attrs.append("raiz=" + q(e["root"]))
        attrs += ["pais=" + q(pais), "iso2=" + c2, "iso3=" + c3]
        out.write(form + " " + " ".join(attrs) + "\n")
    save(dpath, out.getvalue())

    out = io.StringIO()
    out.write(HDR_NAC_KBB)
    out.write("nacionalidades\n")

    def forms_attrs(rec):
        ms, fs, mp, fp = inflect(rec[1])
        a = []
        if ms == fs:
            a.append("gen=c")
        a += ["fs=" + q(fs), "mp=" + q(mp), "fp=" + q(fp)]
        syn = [inflect(s)[0] for s in rec[2]]
        if len(syn) == 1:
            a.append("sinonimo=" + q(syn[0]))
        elif syn:
            a.append("sinonimo=[" + ",".join(q(s) for s in syn) + "]")
        return a

    # --- forward branch: nacionalidad -> pais ------------------------------
    by_ms = {}
    for rec in NAC:
        by_ms.setdefault(inflect(rec[1])[0], []).append(rec)
    out.write("  nacionalidad\n")
    for ms in sorted(by_ms):
        recs = by_ms[ms]
        for i, rec in enumerate(recs):
            c2, c3 = pais_iso[rec[0]]
            name = ms if i == 0 else ms + str(i)
            indent = "    " if i == 0 else "      "
            attrs = []
            if i == 0 and len(recs) > 1:
                attrs.append("ambig=1")
            attrs += ["pais=" + q(rec[0]), "iso2=" + c2, "iso3=" + c3]
            attrs += forms_attrs(rec)
            out.write(indent + name + ": " + ", ".join(attrs) + "\n")

    # --- reverse branch: pais -> nacionalidad ------------------------------
    # canonical countries, plus every es-paises variant whose canonical
    # country has a gentilicio (marked alias=1)
    by_pais = {rec[0]: rec for rec in NAC}
    rows = [(rec[0], rec, 0) for rec in NAC]
    for name, c2, c3, variants in PAISES:
        if name in by_pais:
            rows += [(v, by_pais[name], 1) for v in variants]
    out.write("  pais\n")
    written = set()
    for pais, rec, is_alias in sorted(rows):
        if pais in written:
            continue
        written.add(pais)
        c2, c3 = pais_iso[rec[0]]
        attrs = []
        if is_alias:
            attrs.append("alias=1")
        attrs += ["nacionalidad=" + q(inflect(rec[1])[0]), "iso2=" + c2, "iso3=" + c3]
        attrs += [a for a in forms_attrs(rec) if not a.startswith("sinonimo=")]
        out.write("    " + pais + ": " + ", ".join(attrs) + "\n")
    save(kpath, out.getvalue())


# ---------------------------------------------------------------------------
def read_english(path, flag):
    """Return {code: [names]} from an English .dict (iso2= or laiso2=)."""
    res = {}
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            # skip a bare "word pos=verb" line: dict_addpos.py writes one per
            # extra part of speech, and it carries none of the entry's data
            if " " + flag + "=1" not in line:
                continue
            i = line.index(" " + flag + "=1")
            name, attrs = line[:i], line[i:].split()
            a = dict(x.split("=", 1) for x in attrs if "=" in x)
            code = a.get("iso2") or a.get("laiso2")
            res.setdefault((code, a["iso3"]), []).append(name)
    return res


if __name__ == "__main__":
    here = os.path.dirname(os.path.abspath(__file__))
    d = os.path.normpath(sys.argv[1] if len(sys.argv) > 1 else
                         os.path.join(here, os.pardir, "languages", "Spanish"))
    en = os.path.normpath(os.path.join(here, os.pardir, "languages", "English"))

    pais_iso = {}
    for name, c2, c3, _ in PAISES:
        if name in pais_iso:
            raise ValueError("duplicate pais " + name)
        pais_iso[name] = (c2, c3)

    plines = write_names(PAISES, "pais", "iso2", HDR_PAISES_DICT, HDR_PAISES_KBB,
                         "paises", os.path.join(d, "es-paises.dict"),
                         os.path.join(d, "es-paises.kbb"), NOISO)
    ilines = write_names(IDIOMAS, "idioma", "laiso2", HDR_IDIOMAS_DICT, HDR_IDIOMAS_KBB,
                         "idiomas", os.path.join(d, "es-idiomas.dict"),
                         os.path.join(d, "es-idiomas.kbb"))
    missing_pais = [r[0] for r in NAC if r[0] not in pais_iso]
    if missing_pais:
        raise SystemExit("gentilicio with no es-paises entry: %s" % missing_pais)
    forms = build_nac(pais_iso)
    write_nac(forms, pais_iso, os.path.join(d, "es-nacionalidades.dict"),
              os.path.join(d, "es-nacionalidades.kbb"))

    # --- sanity report -----------------------------------------------------
    print()
    en_c = read_english(os.path.join(en, "en-countries.dict"), "country")
    es_c = {(c2, c3) for n, c2, c3, _ in PAISES if n not in NOISO}
    print("es-paises: canonical", len(PAISES), " forms", len(plines),
          " ISO codes", len(es_c), "(en-countries:", len(en_c), ")")
    print("  English countries with no Spanish row:",
          sorted("%s/%s %s" % (k[0], k[1], v[0]) for k, v in en_c.items() if k not in es_c))
    print("  Spanish ISO rows not in en-countries:",
          sorted("%s/%s" % k for k in es_c if k not in en_c))

    en_l = read_english(os.path.join(en, "en-languages.dict"), "language")
    es_l = {(c2, c3) for n, c2, c3, _ in IDIOMAS}
    print("es-idiomas: canonical", len(IDIOMAS), " forms", len(ilines),
          " ISO codes", len(es_l), "(en-languages:", len(en_l), ")")
    print("  English languages with no Spanish row:",
          sorted("%s/%s %s" % (k[0], k[1], v[0]) for k, v in en_l.items() if k not in es_l))
    print("  Spanish codes not in en-languages:", sorted("%s/%s" % k for k in es_l if k not in en_l))

    en_n = read_english(os.path.join(en, "en-nationalities.dict"), "nationality")
    en_n_codes = {k[0] for k in en_n}
    es_n_codes = {pais_iso[r[0]][0] for r in NAC}
    print("es-nacionalidades: gentilicios", len(NAC), " surface forms", len(forms))
    print("  pais= with no es-paises entry:", missing_pais)
    print("  English nationality codes with no Spanish gentilicio (and not in SIN_GENTILICIO):",
          sorted(c for c in en_n_codes if c not in es_n_codes and c not in SIN_GENTILICIO))
    print("  English nationality codes deliberately left out (SIN_GENTILICIO):",
          sorted(c for c in en_n_codes if c not in es_n_codes and c in SIN_GENTILICIO))
    print("  ISO codes with neither a gentilicio nor a SIN_GENTILICIO entry:",
          sorted(c for c, _ in es_c if c not in es_n_codes and c not in SIN_GENTILICIO))
    print("  SIN_GENTILICIO codes that do have a gentilicio:",
          sorted(c for c in SIN_GENTILICIO if c in es_n_codes))
    amb = {}
    for r in NAC:
        amb.setdefault(inflect(r[1])[0], []).append(r[0])
    print("  ambiguous gentilicios:", {k: v for k, v in amb.items() if len(v) > 1})
    print("  ambiguous surface forms:", sorted(f for f, e in forms.items() if len(e["recs"]) > 1))
