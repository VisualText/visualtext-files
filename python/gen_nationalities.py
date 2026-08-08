# -*- coding: utf-8 -*-
# DESC: Generate the English nationality (demonym) dictionary and knowledge base.
#
# WHAT IT DOES
#   Emits languages/English/en-nationalities.dict and en-nationalities.kbb from
#   the single master table T below, so the two files can never drift apart.
#   Edit T (or ALIASES) and re-run; do not hand-edit the generated files.
#
#   The .dict gets one line per surface form (adjective, singular noun, plural
#   noun and every synonym).  The .kbb gets two branches under "nationalities":
#       nationality  - forward lookup, nationality -> country
#       country      - reverse lookup, country -> nationality
#   Country names are keyed exactly as in en-countries.dict so the "country="
#   attribute joins straight into that dictionary.
#
#   Master table row:
#     (country, iso2, iso3, adj, noun_singular, noun_plural, [(synonym, role)...])
#     role is "adj", "noun", "plural" or "adjnoun".
#
#   A nationality naming more than one country (dominican, congolese) is marked
#   ambig=1 and its further readings hang below it as <name>1, <name>2, ...
#   (the same convention timezones.kbb uses).
#
#   Uninhabited / no-permanent-population ISO entries (Antarctica, Bouvet
#   Island, Heard & McDonald, French Southern Territories, South Georgia, US
#   Minor Outlying Islands, British Indian Ocean Territory, Svalbard) have no
#   demonym and are deliberately left out.
#
# USAGE
#   python gen_nationalities.py [output_dir]
#     output_dir  defaults to ../languages/English relative to this script

import io, os, sys

# country, iso2, iso3, adj, noun, plural, synonyms
T = [
 ("afghanistan","af","afg","afghan","afghan","afghans",[]),
 ("albania","al","alb","albanian","albanian","albanians",[]),
 ("algeria","dz","dza","algerian","algerian","algerians",[]),
 ("american samoa","as","asm","american samoan","american samoan","american samoans",[]),
 ("andorra","ad","and","andorran","andorran","andorrans",[]),
 ("angola","ao","ago","angolan","angolan","angolans",[]),
 ("anguilla","ai","aia","anguillan","anguillan","anguillans",[("anguillian","adjnoun")]),
 ("antigua and barbuda","ag","atg","antiguan","antiguan","antiguans",[("barbudan","adjnoun"),("antiguans and barbudans","plural")]),
 ("argentina","ar","arg","argentine","argentine","argentines",[("argentinian","adjnoun"),("argentinians","plural")]),
 ("armenia","am","arm","armenian","armenian","armenians",[]),
 ("aruba","aw","abw","aruban","aruban","arubans",[]),
 ("australia","au","aus","australian","australian","australians",[("aussie","adjnoun"),("aussies","plural")]),
 ("austria","at","aut","austrian","austrian","austrians",[]),
 ("azerbaijan","az","aze","azerbaijani","azerbaijani","azerbaijanis",[("azeri","adjnoun"),("azeris","plural")]),
 ("bahamas","bs","bhs","bahamian","bahamian","bahamians",[]),
 ("bahrain","bh","bhr","bahraini","bahraini","bahrainis",[]),
 ("bangladesh","bd","bgd","bangladeshi","bangladeshi","bangladeshis",[]),
 ("barbados","bb","brb","barbadian","barbadian","barbadians",[("bajan","noun"),("bajans","plural")]),
 ("belarus","by","blr","belarusian","belarusian","belarusians",[("byelorussian","adjnoun")]),
 ("belgium","be","bel","belgian","belgian","belgians",[]),
 ("belize","bz","blz","belizean","belizean","belizeans",[]),
 ("benin","bj","ben","beninese","beninese","beninese",[]),
 ("bermuda","bm","bmu","bermudian","bermudian","bermudians",[("bermudan","adjnoun")]),
 ("bhutan","bt","btn","bhutanese","bhutanese","bhutanese",[]),
 ("bolivia","bo","bol","bolivian","bolivian","bolivians",[]),
 ("bonaire, sint eustatius and saba","bq","bes","bonairean","bonairean","bonaireans",[]),
 ("bosnia and herzegovina","ba","bih","bosnian","bosnian","bosnians",[("herzegovinian","adjnoun")]),
 ("botswana","bw","bwa","botswanan","motswana","batswana",[("tswana","adjnoun")]),
 ("brazil","br","bra","brazilian","brazilian","brazilians",[]),
 ("brunei darussalam","bn","brn","bruneian","bruneian","bruneians",[]),
 ("bulgaria","bg","bgr","bulgarian","bulgarian","bulgarians",[]),
 ("burkina faso","bf","bfa","burkinabe","burkinabe","burkinabe",[("burkinabé","adjnoun")]),
 ("burundi","bi","bdi","burundian","burundian","burundians",[]),
 ("cabo verde","cv","cpv","cape verdean","cape verdean","cape verdeans",[("cabo verdean","adjnoun")]),
 ("cambodia","kh","khm","cambodian","cambodian","cambodians",[("khmer","adjnoun")]),
 ("cameroon","cm","cmr","cameroonian","cameroonian","cameroonians",[]),
 ("canada","ca","can","canadian","canadian","canadians",[]),
 ("cayman islands","ky","cym","caymanian","caymanian","caymanians",[]),
 ("central african republic","cf","caf","central african","central african","central africans",[]),
 ("chad","td","tcd","chadian","chadian","chadians",[]),
 ("chile","cl","chl","chilean","chilean","chileans",[]),
 ("china","cn","chn","chinese","chinese","chinese",[]),
 ("christmas island","cx","cxr","christmas island","christmas islander","christmas islanders",[]),
 ("cocos","cc","cck","cocos island","cocos islander","cocos islanders",[]),
 ("colombia","co","col","colombian","colombian","colombians",[]),
 ("comoros","km","com","comorian","comorian","comorians",[("comoran","adjnoun")]),
 ("congo","cg","cog","congolese","congolese","congolese",[]),
 ("the democratic republic of the congo","cd","cod","congolese","congolese","congolese",[]),
 ("cook islands","ck","cok","cook island","cook islander","cook islanders",[]),
 ("costa rica","cr","cri","costa rican","costa rican","costa ricans",[]),
 ("croatia","hr","hrv","croatian","croat","croats",[("croatians","plural")]),
 ("cuba","cu","cub","cuban","cuban","cubans",[]),
 ("curaçao","cw","cuw","curacaoan","curacaoan","curacaoans",[("curaçaoan","adjnoun")]),
 ("cyprus","cy","cyp","cypriot","cypriot","cypriots",[]),
 ("czechia","cz","cze","czech","czech","czechs",[]),
 ("côte d'ivoire","ci","civ","ivorian","ivorian","ivorians",[("ivoirian","adjnoun")]),
 ("denmark","dk","dnk","danish","dane","danes",[]),
 ("djibouti","dj","dji","djiboutian","djiboutian","djiboutians",[]),
 ("dominica","dm","dma","dominican","dominican","dominicans",[]),
 ("dominican republic","do","dom","dominican","dominican","dominicans",[]),
 ("ecuador","ec","ecu","ecuadorian","ecuadorian","ecuadorians",[("ecuadorean","adjnoun")]),
 ("egypt","eg","egy","egyptian","egyptian","egyptians",[]),
 ("el salvador","sv","slv","salvadoran","salvadoran","salvadorans",[("salvadorian","adjnoun"),("salvadorean","adjnoun")]),
 ("equatorial guinea","gq","gnq","equatorial guinean","equatoguinean","equatoguineans",[("equatorial guineans","plural")]),
 ("eritrea","er","eri","eritrean","eritrean","eritreans",[]),
 ("estonia","ee","est","estonian","estonian","estonians",[]),
 ("eswatini","sz","swz","swazi","swazi","swazis",[]),
 ("ethiopia","et","eth","ethiopian","ethiopian","ethiopians",[]),
 ("falkland islands","fk","flk","falkland island","falkland islander","falkland islanders",[]),
 ("faroe islands","fo","fro","faroese","faroese","faroese",[("faeroese","adjnoun")]),
 ("fiji","fj","fji","fijian","fijian","fijians",[]),
 ("finland","fi","fin","finnish","finn","finns",[]),
 ("france","fr","fra","french","frenchman","frenchmen",[("frenchwoman","noun"),("frenchwomen","plural")]),
 ("french guiana","gf","guf","french guianese","french guianese","french guianese",[]),
 ("french polynesia","pf","pyf","french polynesian","french polynesian","french polynesians",[]),
 ("gabon","ga","gab","gabonese","gabonese","gabonese",[]),
 ("gambia","gm","gmb","gambian","gambian","gambians",[]),
 ("georgia","ge","geo","georgian","georgian","georgians",[]),
 ("germany","de","deu","german","german","germans",[]),
 ("ghana","gh","gha","ghanaian","ghanaian","ghanaians",[]),
 ("gibraltar","gi","gib","gibraltarian","gibraltarian","gibraltarians",[]),
 ("greece","gr","grc","greek","greek","greeks",[("hellenic","adj")]),
 ("greenland","gl","grl","greenlandic","greenlander","greenlanders",[]),
 ("grenada","gd","grd","grenadian","grenadian","grenadians",[]),
 ("guadeloupe","gp","glp","guadeloupean","guadeloupean","guadeloupeans",[]),
 ("guam","gu","gum","guamanian","guamanian","guamanians",[]),
 ("guatemala","gt","gtm","guatemalan","guatemalan","guatemalans",[]),
 ("guernsey","gg","ggy","guernsey","guernseyman","guernseymen",[]),
 ("guinea","gn","gin","guinean","guinean","guineans",[]),
 ("guinea-bissau","gw","gnb","bissau-guinean","bissau-guinean","bissau-guineans",[]),
 ("guyana","gy","guy","guyanese","guyanese","guyanese",[]),
 ("haiti","ht","hti","haitian","haitian","haitians",[]),
 ("holy see","va","vat","vatican","vatican citizen","vatican citizens",[]),
 ("honduras","hn","hnd","honduran","honduran","hondurans",[]),
 ("hong kong","hk","hkg","hong kong","hong konger","hong kongers",[("hongkongese","adjnoun")]),
 ("hungary","hu","hun","hungarian","hungarian","hungarians",[("magyar","adjnoun"),("magyars","plural")]),
 ("iceland","is","isl","icelandic","icelander","icelanders",[]),
 ("india","in","ind","indian","indian","indians",[]),
 ("indonesia","id","idn","indonesian","indonesian","indonesians",[]),
 ("iran","ir","irn","iranian","iranian","iranians",[("persian","adjnoun"),("persians","plural")]),
 ("iraq","iq","irq","iraqi","iraqi","iraqis",[]),
 ("ireland","ie","irl","irish","irishman","irishmen",[("irishwoman","noun"),("irishwomen","plural")]),
 ("isle of man","im","imn","manx","manxman","manxmen",[]),
 ("israel","il","isr","israeli","israeli","israelis",[]),
 ("italy","it","ita","italian","italian","italians",[]),
 ("jamaica","jm","jam","jamaican","jamaican","jamaicans",[]),
 ("japan","jp","jpn","japanese","japanese","japanese",[]),
 ("jersey","je","jey","jersey","jerseyman","jerseymen",[]),
 ("jordan","jo","jor","jordanian","jordanian","jordanians",[]),
 ("kazakhstan","kz","kaz","kazakh","kazakh","kazakhs",[("kazakhstani","adjnoun")]),
 ("kenya","ke","ken","kenyan","kenyan","kenyans",[]),
 ("kiribati","ki","kir","i-kiribati","i-kiribati","i-kiribati",[("kiribatian","adjnoun")]),
 ("korea","kr","kor","korean","korean","koreans",[]),
 ("the democratic people's republic of korea","kp","prk","north korean","north korean","north koreans",[]),
 ("south korea","kr","kor","south korean","south korean","south koreans",[]),
 ("kuwait","kw","kwt","kuwaiti","kuwaiti","kuwaitis",[]),
 ("kyrgyzstan","kg","kgz","kyrgyz","kyrgyz","kyrgyz",[("kyrgyzstani","adjnoun"),("kirghiz","adjnoun")]),
 ("lao people's democratic republic","la","lao","laotian","lao","lao",[("laotians","plural")]),
 ("latvia","lv","lva","latvian","latvian","latvians",[]),
 ("lebanon","lb","lbn","lebanese","lebanese","lebanese",[]),
 ("lesotho","ls","lso","basotho","mosotho","basotho",[("sotho","adjnoun")]),
 ("liberia","lr","lbr","liberian","liberian","liberians",[]),
 ("libya","ly","lby","libyan","libyan","libyans",[]),
 ("liechtenstein","li","lie","liechtenstein","liechtensteiner","liechtensteiners",[]),
 ("lithuania","lt","ltu","lithuanian","lithuanian","lithuanians",[]),
 ("luxembourg","lu","lux","luxembourgish","luxembourger","luxembourgers",[]),
 ("macao","mo","mac","macanese","macanese","macanese",[]),
 ("madagascar","mg","mdg","malagasy","malagasy","malagasy",[("madagascan","adjnoun")]),
 ("malawi","mw","mwi","malawian","malawian","malawians",[]),
 ("malaysia","my","mys","malaysian","malaysian","malaysians",[]),
 ("maldives","mv","mdv","maldivian","maldivian","maldivians",[]),
 ("mali","ml","mli","malian","malian","malians",[]),
 ("malta","mt","mlt","maltese","maltese","maltese",[]),
 ("marshall islands","mh","mhl","marshallese","marshallese","marshallese",[]),
 ("martinique","mq","mtq","martinican","martiniquais","martiniquais",[]),
 ("mauritania","mr","mrt","mauritanian","mauritanian","mauritanians",[]),
 ("mauritius","mu","mus","mauritian","mauritian","mauritians",[]),
 ("mayotte","yt","myt","mahoran","mahoran","mahorans",[("mahorais","adjnoun")]),
 ("mexico","mx","mex","mexican","mexican","mexicans",[]),
 ("micronesia","fm","fsm","micronesian","micronesian","micronesians",[]),
 ("moldova","md","mda","moldovan","moldovan","moldovans",[("moldavian","adjnoun")]),
 ("monaco","mc","mco","monegasque","monegasque","monegasques",[("monacan","adjnoun")]),
 ("mongolia","mn","mng","mongolian","mongolian","mongolians",[("mongol","adjnoun"),("mongols","plural")]),
 ("montenegro","me","mne","montenegrin","montenegrin","montenegrins",[]),
 ("montserrat","ms","msr","montserratian","montserratian","montserratians",[]),
 ("morocco","ma","mar","moroccan","moroccan","moroccans",[]),
 ("mozambique","mz","moz","mozambican","mozambican","mozambicans",[]),
 ("myanmar","mm","mmr","burmese","burmese","burmese",[("myanmarese","adjnoun")]),
 ("namibia","na","nam","namibian","namibian","namibians",[]),
 ("nauru","nr","nru","nauruan","nauruan","nauruans",[]),
 ("nepal","np","npl","nepali","nepali","nepalis",[("nepalese","adjnoun")]),
 ("netherlands","nl","nld","dutch","dutchman","dutchmen",[("netherlandish","adj"),("dutchwoman","noun"),("dutchwomen","plural")]),
 ("new caledonia","nc","ncl","new caledonian","new caledonian","new caledonians",[]),
 ("new zealand","nz","nzl","new zealand","new zealander","new zealanders",[("kiwi","adjnoun"),("kiwis","plural")]),
 ("nicaragua","ni","nic","nicaraguan","nicaraguan","nicaraguans",[]),
 ("niger","ne","ner","nigerien","nigerien","nigeriens",[]),
 ("nigeria","ng","nga","nigerian","nigerian","nigerians",[]),
 ("niue","nu","niu","niuean","niuean","niueans",[]),
 ("norfolk island","nf","nfk","norfolk island","norfolk islander","norfolk islanders",[]),
 ("northern mariana islands","mp","mnp","northern marianan","northern marianan","northern marianans",[("chamorro","adjnoun")]),
 ("norway","no","nor","norwegian","norwegian","norwegians",[]),
 ("oman","om","omn","omani","omani","omanis",[]),
 ("pakistan","pk","pak","pakistani","pakistani","pakistanis",[]),
 ("palau","pw","plw","palauan","palauan","palauans",[]),
 ("palestine, state of","ps","pse","palestinian","palestinian","palestinians",[]),
 ("panama","pa","pan","panamanian","panamanian","panamanians",[]),
 ("papua new guinea","pg","png","papua new guinean","papua new guinean","papua new guineans",[]),
 ("paraguay","py","pry","paraguayan","paraguayan","paraguayans",[]),
 ("peru","pe","per","peruvian","peruvian","peruvians",[]),
 ("philippines","ph","phl","filipino","filipino","filipinos",[("philippine","adj"),("filipina","noun"),("filipinas","plural")]),
 ("pitcairn","pn","pcn","pitcairn island","pitcairn islander","pitcairn islanders",[]),
 ("poland","pl","pol","polish","pole","poles",[]),
 ("portugal","pt","prt","portuguese","portuguese","portuguese",[]),
 ("puerto rico","pr","pri","puerto rican","puerto rican","puerto ricans",[]),
 ("qatar","qa","qat","qatari","qatari","qataris",[]),
 ("republic of north macedonia","mk","mkd","macedonian","macedonian","macedonians",[]),
 ("romania","ro","rou","romanian","romanian","romanians",[("rumanian","adjnoun")]),
 ("russian federation","ru","rus","russian","russian","russians",[]),
 ("rwanda","rw","rwa","rwandan","rwandan","rwandans",[("rwandese","adjnoun")]),
 ("réunion","re","reu","reunionese","reunionese","reunionese",[("réunionese","adjnoun")]),
 ("saint barthélemy","bl","blm","barthelemois","barthelemois","barthelemois",[]),
 ("saint helena, ascension and tristan da cunha","sh","shn","saint helenian","saint helenian","saint helenians",[]),
 ("saint kitts and nevis","kn","kna","kittitian","kittitian","kittitians",[("nevisian","adjnoun")]),
 ("saint lucia","lc","lca","saint lucian","saint lucian","saint lucians",[("st. lucian","adjnoun")]),
 ("saint martin","mf","maf","saint-martinois","saint-martinois","saint-martinois",[]),
 ("saint pierre and miquelon","pm","spm","saint-pierrais","saint-pierrais","saint-pierrais",[("miquelonnais","adjnoun")]),
 ("saint vincent and the grenadines","vc","vct","vincentian","vincentian","vincentians",[]),
 ("samoa","ws","wsm","samoan","samoan","samoans",[]),
 ("san marino","sm","smr","sammarinese","sammarinese","sammarinese",[]),
 ("sao tome and principe","st","stp","sao tomean","sao tomean","sao tomeans",[]),
 ("saudi arabia","sa","sau","saudi","saudi","saudis",[("saudi arabian","adjnoun"),("saudi arabians","plural")]),
 ("senegal","sn","sen","senegalese","senegalese","senegalese",[]),
 ("serbia","rs","srb","serbian","serb","serbs",[("serbians","plural")]),
 ("seychelles","sc","syc","seychellois","seychellois","seychellois",[]),
 ("sierra leone","sl","sle","sierra leonean","sierra leonean","sierra leoneans",[]),
 ("singapore","sg","sgp","singaporean","singaporean","singaporeans",[]),
 ("sint maarten","sx","sxm","sint maarten","sint maartener","sint maarteners",[]),
 ("slovakia","sk","svk","slovak","slovak","slovaks",[("slovakian","adjnoun")]),
 ("slovenia","si","svn","slovenian","slovene","slovenes",[("slovenians","plural")]),
 ("solomon islands","sb","slb","solomon island","solomon islander","solomon islanders",[]),
 ("somalia","so","som","somali","somali","somalis",[]),
 ("south africa","za","zaf","south african","south african","south africans",[]),
 ("south sudan","ss","ssd","south sudanese","south sudanese","south sudanese",[]),
 ("spain","es","esp","spanish","spaniard","spaniards",[]),
 ("sri lanka","lk","lka","sri lankan","sri lankan","sri lankans",[]),
 ("sudan","sd","sdn","sudanese","sudanese","sudanese",[]),
 ("suriname","sr","sur","surinamese","surinamese","surinamese",[("surinamer","noun"),("surinamers","plural")]),
 ("sweden","se","swe","swedish","swede","swedes",[]),
 ("switzerland","ch","che","swiss","swiss","swiss",[]),
 ("syrian arab republic","sy","syr","syrian","syrian","syrians",[]),
 ("taiwan","tw","twn","taiwanese","taiwanese","taiwanese",[]),
 ("tajikistan","tj","tjk","tajik","tajik","tajiks",[("tadzhik","adjnoun"),("tajikistani","adjnoun")]),
 ("tanzania","tz","tza","tanzanian","tanzanian","tanzanians",[]),
 ("thailand","th","tha","thai","thai","thais",[]),
 ("timor-leste","tl","tls","timorese","timorese","timorese",[("east timorese","adjnoun")]),
 ("togo","tg","tgo","togolese","togolese","togolese",[]),
 ("tokelau","tk","tkl","tokelauan","tokelauan","tokelauans",[]),
 ("tonga","to","ton","tongan","tongan","tongans",[]),
 ("trinidad and tobago","tt","tto","trinidadian","trinidadian","trinidadians",[("tobagonian","adjnoun"),("tobagonians","plural")]),
 ("tunisia","tn","tun","tunisian","tunisian","tunisians",[]),
 ("turkey","tr","tur","turkish","turk","turks",[("turkiye","adj")]),
 ("turkmenistan","tm","tkm","turkmen","turkmen","turkmens",[("turkmenistani","adjnoun")]),
 ("turks and caicos islands","tc","tca","turks and caicos island","turks and caicos islander","turks and caicos islanders",[]),
 ("tuvalu","tv","tuv","tuvaluan","tuvaluan","tuvaluans",[]),
 ("uganda","ug","uga","ugandan","ugandan","ugandans",[]),
 ("ukraine","ua","ukr","ukrainian","ukrainian","ukrainians",[]),
 ("united arab emirates","ae","are","emirati","emirati","emiratis",[("emirian","adjnoun")]),
 ("united kingdom of great britain and northern ireland","gb","gbr","british","briton","britons",[("brit","noun"),("brits","plural")]),
 ("united states of america","us","usa","american","american","americans",[]),
 ("uruguay","uy","ury","uruguayan","uruguayan","uruguayans",[]),
 ("uzbekistan","uz","uzb","uzbek","uzbek","uzbeks",[("uzbekistani","adjnoun")]),
 ("vanuatu","vu","vut","vanuatuan","ni-vanuatu","ni-vanuatu",[]),
 ("venezuela","ve","ven","venezuelan","venezuelan","venezuelans",[]),
 ("viet nam","vn","vnm","vietnamese","vietnamese","vietnamese",[]),
 ("virgin islands","vg","vgb","british virgin island","british virgin islander","british virgin islanders",[]),
 ("united states virgin islands","vi","vir","us virgin island","us virgin islander","us virgin islanders",[]),
 ("wallis and futuna","wf","wlf","wallisian","wallisian","wallisians",[("futunan","adjnoun")]),
 ("western sahara","eh","esh","sahrawi","sahrawi","sahrawis",[("sahraouian","adjnoun")]),
 ("yemen","ye","yem","yemeni","yemeni","yemenis",[]),
 ("zambia","zm","zmb","zambian","zambian","zambians",[]),
 ("zimbabwe","zw","zwe","zimbabwean","zimbabwean","zimbabweans",[]),
 ("åland islands","ax","ala","alandic","alander","alanders",[("åland island","adj"),("åland islander","noun")]),
 # --- constituent nations of the United Kingdom -------------------------
 # Not ISO countries, but among the most frequent nationality words in
 # English text.  They carry the sovereign state's ISO codes.
 ("england","gb","gbr","english","englishman","englishmen",[("englishwoman","noun"),("englishwomen","plural")]),
 ("scotland","gb","gbr","scottish","scot","scots",[("scotsman","noun"),("scotsmen","plural"),("scotswoman","noun"),("scotswomen","plural")]),
 ("wales","gb","gbr","welsh","welshman","welshmen",[("welshwoman","noun"),("welshwomen","plural")]),
 ("northern ireland","gb","gbr","northern irish","northern irishman","northern irishmen",[("ulsterman","noun"),("ulstermen","plural")]),
 # --- widely used non-ISO nationality --------------------------------------
 ("kosovo","xk","xkx","kosovar","kosovar","kosovars",[("kosovan","adjnoun")]),
]

# Extra keys for the reverse (country -> nationality) branch: the common
# short names that readers actually write, mapped to the ISO entry above.
ALIASES = [
 ("united states","us"), ("usa","us"), ("america","us"),
 ("united kingdom","gb"), ("uk","gb"), ("great britain","gb"), ("britain","gb"),
 ("russia","ru"), ("vietnam","vn"), ("north macedonia","mk"), ("macedonia","mk"),
 ("laos","la"), ("syria","sy"), ("vatican city","va"), ("ivory coast","ci"),
 ("east timor","tl"), ("burma","mm"), ("cape verde","cv"), ("swaziland","sz"),
 ("czech republic","cz"), ("holland","nl"), ("north korea","kp"),
 ("democratic republic of the congo","cd"), ("cocos islands","cc"),
 ("saint vincent","vc"), ("bosnia","ba"), ("brunei","bn"),
 ("north korea","kp"), ("republic of korea","kr"),
]

# Adjectives that also serve as the collective plural noun ("the French",
# "the British").  Derived from the ending, but only for entries whose
# singular noun differs from the adjective.
COLLECTIVE_ENDINGS = ("sh", "ch", "ss", "se", "x")

HDR_DICT = """# Nationality (demonym) names in English.
# One line per surface form:  adjective, singular noun and plural noun.
#   nationality=1  every entry            adj=1 / noun=1 / plural=1  word role
#   collective=1   the adjective is also the plural people ("the French")
#   syn=1          a variant spelling or an alternate demonym
#   root=          canonical nationality for a variant or synonym form
#   country=       country name as keyed in en-countries.dict
#   iso2= iso3=    ISO 3166-1 codes, matching en-countries.dict
#   ambig=1        the form names more than one country (see en-nationalities.kbb)
# Uninhabited ISO territories (Antarctica, Bouvet Island, Heard and McDonald
# Islands, French Southern Territories, South Georgia, US Minor Outlying
# Islands, British Indian Ocean Territory, Svalbard) have no demonym and are
# not listed.
# Five entries are not ISO countries and so have no en-countries.dict entry:
# england, scotland, wales and northern ireland (which carry the UK's gb/gbr
# codes) and kosovo (xk/xkx, the user-assigned code in common use).
"""

HDR_KBB = """# Nationality (demonym) names in English, related to their countries.
# Forward lookup:  nationality -> country   (concept "nationalities nationality french" -> country=france)
# Reverse lookup:  country -> nationality   (concept "nationalities country france" -> nationality=french)
# Each nationality carries the adjective (the concept name), the singular
# noun, the plural noun and the ISO 3166-1 codes of its country.  Country
# names are keyed exactly as in en-countries.dict / en-countries.kbb so the
# two knowledge bases join.
# A form naming more than one country is marked ambig=1 and its further
# readings hang below it as <name>1, <name>2, ... (same convention as
# timezones.kbb).
# Country entries marked alias=1 are common short names (usa, uk, russia,
# holland, ...) rather than the ISO name.  England, scotland, wales, northern
# ireland and kosovo are not ISO countries and have no en-countries.dict entry.
"""


def q(s):
    """Quote a value the way KBFuncs QuoteIfNeeded does."""
    if s == "":
        return '""'
    if any(c in s for c in " \t") or any(not (c.isalnum() or c == "_") for c in s):
        return '"' + s.replace('"', '\\"') + '"'
    return s


def build():
    # surface form -> {flags, root, records}
    forms = {}

    def add(form, flags, rec, root):
        e = forms.setdefault(form, {"flags": set(), "recs": [], "root": root})
        e["flags"] |= set(flags)
        if rec not in e["recs"]:
            e["recs"].append(rec)
        # a form that is canonical for some record has no root of its own
        if root is None:
            e["root"] = None

    for rec in T:
        country, iso2, iso3, adj, noun, plural, syns = rec
        adj_flags = ["adj"]
        if adj != noun and adj.endswith(COLLECTIVE_ENDINGS):
            adj_flags.append("collective")
        add(adj, adj_flags, rec, None)
        add(noun, ["noun"], rec, None if noun == adj else adj)
        add(plural, ["noun", "plural"], rec, None if plural == adj else adj)
        for form, role in syns:
            flags = {"adjnoun": ["adj", "noun"], "adj": ["adj"],
                     "noun": ["noun"], "plural": ["noun", "plural"]}[role]
            add(form, flags + ["syn"], rec, adj)

    return forms


def write_dict(forms, path):
    out = io.StringIO()
    out.write(HDR_DICT)
    for form in sorted(forms):
        e = forms[form]
        rec = e["recs"][0]
        country, iso2, iso3 = rec[0], rec[1], rec[2]
        attrs = ["nationality=1"]
        for f in ("adj", "collective", "noun", "plural", "syn"):
            if f in e["flags"]:
                attrs.append(f + "=1")
        if len(e["recs"]) > 1:
            attrs.append("ambig=1")
        if e["root"]:
            attrs.append("root=" + q(e["root"]))
        attrs.append("country=" + q(country))
        attrs.append("iso2=" + iso2)
        attrs.append("iso3=" + iso3)
        out.write(form + " " + " ".join(attrs) + "\n")
    save(path, out.getvalue())


def write_kbb(forms, path):
    out = io.StringIO()
    out.write(HDR_KBB)
    out.write("nationalities\n")

    # --- forward branch: nationality -> country ---------------------------
    # group records by their canonical adjective so ambiguous names collapse
    by_adj = {}
    for rec in T:
        by_adj.setdefault(rec[3], []).append(rec)

    out.write("  nationality\n")
    for adj in sorted(by_adj):
        recs = by_adj[adj]
        for i, rec in enumerate(recs):
            country, iso2, iso3, _, noun, plural, syns = rec
            name = adj if i == 0 else adj + str(i)
            indent = "    " if i == 0 else "      "
            attrs = []
            if i == 0 and len(recs) > 1:
                attrs.append("ambig=1")
            attrs.append("country=" + q(country))
            attrs.append("iso2=" + iso2)
            attrs.append("iso3=" + iso3)
            attrs.append("noun=" + q(noun))
            attrs.append("plural=" + q(plural))
            if adj != noun and adj.endswith(COLLECTIVE_ENDINGS):
                attrs.append("collective=" + q(adj))
            syn_forms = [s for s, r in syns]
            if len(syn_forms) == 1:
                attrs.append("synonym=" + q(syn_forms[0]))
            elif syn_forms:
                attrs.append("synonym=[" + ",".join(q(s) for s in syn_forms) + "]")
            out.write(indent + name + ": " + ", ".join(attrs) + "\n")

    # --- reverse branch: country -> nationality ---------------------------
    by_iso = {rec[1]: rec for rec in T}
    out.write("  country\n")
    rows = [(rec[0], rec, 0) for rec in T]
    rows += [(alias, by_iso[iso], 1) for alias, iso in ALIASES if iso in by_iso]
    for country, rec, is_alias in sorted(rows):
        _, iso2, iso3, adj, noun, plural, _ = rec
        attrs = []
        if is_alias:
            attrs.append("alias=1")
        attrs.append("nationality=" + q(adj))
        attrs.append("iso2=" + iso2)
        attrs.append("iso3=" + iso3)
        attrs.append("noun=" + q(noun))
        attrs.append("plural=" + q(plural))
        out.write("    " + country + ": " + ", ".join(attrs) + "\n")

    save(path, out.getvalue())


def save(path, text):
    with open(path, "wb") as f:
        f.write(text.replace("\n", "\r\n").encode("utf-8"))
    print("wrote", path, len(text.splitlines()), "lines")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        d = sys.argv[1]
    else:
        here = os.path.dirname(os.path.abspath(__file__))
        d = os.path.join(here, os.pardir, "languages", "English")
    d = os.path.normpath(d)
    forms = build()
    write_dict(forms, os.path.join(d, "en-nationalities.dict"))
    write_kbb(forms, os.path.join(d, "en-nationalities.kbb"))

    # sanity report
    missing = [a for a, iso in ALIASES if iso not in {r[1] for r in T}]
    print("alias with no record:", missing)
    dups = {}
    for r in T:
        dups.setdefault(r[3], []).append(r[0])
    print("ambiguous nationalities:", {k: v for k, v in dups.items() if len(v) > 1})
    print("countries:", len(T), " surface forms:", len(forms))
