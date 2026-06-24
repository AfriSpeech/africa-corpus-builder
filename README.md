# Africa Corpus Builder

A toolkit and small Python library for **retrieving parallel and monolingual
text corpora for African languages**. Pick any African language and pair it
with English, with another African language, or with one of several other world
languages — or pull a monolingual corpus for a single language. Output is
clean, sentence-aligned CSV, ready for machine-translation training and NLP
research.

The corpora are hosted on HuggingFace at
[`michsethowusu/africa-corpus`](https://huggingface.co/datasets/michsethowusu/africa-corpus).
The library downloads only the files you actually use and caches them locally,
so the repository itself stays lightweight. New languages pushed to the dataset
are picked up automatically — no code change or update needed.

---

## What you can build

| Corpus type | Example | Notes |
|---|---|---|
| African ↔ English | Swahili ↔ English | English ships cached; the default target |
| African ↔ African | Twi ↔ Yoruba, Hausa ↔ Amharic | align two local languages directly |
| African ↔ other language | Twi ↔ French, Zulu ↔ Arabic | French, Arabic, Chinese, Portuguese are cached |
| Monolingual | all Swahili sentences | any single language |

Every language's text is aligned on a shared verse key, so **any** two
languages can be turned into a parallel corpus by a simple join. That is what
makes African ↔ African and African ↔ other-language pairs possible.

## Dataset statistics

**693 African languages**, **15,974,671 sentences** in total. Sentences = harvested verses available for alignment, summed across all Bible versions of each language.

| Language | Code | Sentences |
|---|---|--:|
| Swahili | swh | 356,708 |
| Afrikaans | afr | 279,114 |
| Shona | sna | 224,417 |
| Malgache | plt | 216,384 |
| Ganda | lug | 186,020 |
| Twi | twi | 154,554 |
| Oromo, Arsi / Oromo, Borana-Arsi-Guji | gax | 153,267 |
| Amharic | amh | 149,730 |
| Masai | mas | 131,770 |
| Rwandan | kin | 131,531 |
| Nyanja | nya | 130,148 |
| Xhosa | xho | 123,914 |
| Kikuyu | kik | 122,087 |
| Dawro | dwr | 108,043 |
| Zulu | zul | 101,217 |
| Setswana | tsn | 100,904 |
| West Central Oromo | gaz | 93,307 |
| Yoruba | yor | 93,205 |
| Guinea Kpelle | gkp | 92,843 |
| Éwé | ewe | 92,774 |
| Kamba (Kenya) | kam | 92,746 |
| Kalenjin | kln | 92,740 |
| Wanga | lwg | 92,718 |
| Ekegusii | guz | 92,699 |
| Hausa / Hausa Arabic script | hau | 92,666 |
| Adamawa Fulfulde / Fulfulde (Adamawa) | fub | 92,574 |
| Southern Sotho | sot | 78,155 |
| Nyakyusa-Ngonde | nyy | 77,931 |
| Gofa | gof | 77,810 |
| Gidar | gid | 70,238 |
| Dyula | dyu | 70,170 |
| Somali | som | 70,123 |
| Kuria | kuj | 70,104 |
| Tsonga | tso | 70,018 |
| Mossi | mos | 69,449 |
| Susu (Roman script) / Susu (Arabic Script) | sus | 62,465 |
| Mbay | myb | 62,307 |
| Tupuri | tui | 62,254 |
| Lunda | lun | 62,207 |
| Seselwa Creole French | crs | 62,206 |
| Ga | gaa | 62,199 |
| Rundi | run | 62,181 |
| Fon | fon | 62,176 |
| Nyankole | nyn | 62,172 |
| Igbo | ibo | 62,164 |
| North Ndebele | nde | 62,164 |
| Nyoro | nyo | 62,163 |
| Tonga (Zambia) | toi | 62,161 |
| Embu | ebu | 62,122 |
| Gitonga | toh | 62,113 |
| Obolo | ann | 62,076 |
| Chadian Arabic (Roman script) | shu | 62,044 |
| Gbaya, Northwest | gya | 62,040 |
| Lulogooli | rag | 61,994 |
| Gourmanchéma | gux | 61,982 |
| Psikye | kvj | 61,966 |
| Luo (Kenya and Tanzania) | luo | 61,959 |
| Luba-Lulua | lua | 61,870 |
| Gamo | gmv | 61,812 |
| Kimîîru | mer | 61,674 |
| Tsotso | lto | 61,654 |
| Fanti | fat | 61,636 |
| Saamia | lsm | 61,606 |
| Dagbani | dag | 61,592 |
| Sar | mwm | 61,586 |
| Adhola | adh | 61,581 |
| Bukusu | bxk | 61,578 |
| Masaaba | myx | 61,504 |
| Sotho, Northern | nso | 61,340 |
| Kumam | kdi | 61,328 |
| Chokwe | cjk | 61,062 |
| Samo, Southern | sbd | 61,044 |
| Khoekhoe | naq | 60,722 |
| Bulu (Cameroon) | bum | 59,911 |
| Yao | yao | 50,503 |
| Sukuma | suk | 46,989 |
| Burkina Faso Fulfulde / Maasina Fulfulde | ffm | 44,152 |
| Teso | teo | 42,415 |
| Iraqw | irk | 41,509 |
| Kinandi (Ndandi) | nnb | 41,509 |
| Mafa | maf | 39,109 |
| Beembe (Congo) | beq | 39,106 |
| Kim | kia | 39,085 |
| Mongo | lol | 39,050 |
| Efik | efi | 39,049 |
| Machame | jmc | 39,046 |
| Lango (Uganda) | laj | 39,044 |
| Sehwi | sfw | 39,043 |
| Luvale | lue | 39,040 |
| Ndau | ndc | 39,037 |
| Datooga | tcc | 39,033 |
| Wolof (Senegal) | wol | 39,024 |
| Nkoya | nka | 39,017 |
| Gogo | gog | 39,006 |
| Lambya | lai | 38,990 |
| Southern Dagaare | dga | 38,983 |
| Kalanga | kck | 38,975 |
| Ngiemboon | nnh | 38,788 |
| Baoulé | bci | 38,743 |
| Kasem | xsm | 38,665 |
| Maale | mdy | 38,448 |
| Bimoba | bim | 38,209 |
| Adangme | ada | 38,177 |
| Konkomba | xon | 38,094 |
| Nzima | nzi | 36,220 |
| Pogolo | poy | 34,407 |
| Ngulu | ngp | 34,404 |
| Aringa | luc | 32,415 |
| Yalunka | yal | 32,215 |
| Myene | mye | 31,163 |
| Medumba | byv | 31,150 |
| Masana | mcn | 31,149 |
| Lingala | lin | 31,146 |
| Toma | tod | 31,144 |
| Sénoufo, Cebaara | sef | 31,141 |
| Musey | mse | 31,132 |
| Ngambay | sba | 31,125 |
| Djimini Senoufo | dyi | 31,122 |
| Punu (Ipounou) | puu | 31,117 |
| Shi | shr | 31,115 |
| Sénoufo, Tagwana | tgw | 31,111 |
| Vagla | vag | 31,104 |
| Kambaata | ktb | 31,103 |
| Buli (Ghana) | bwu | 31,102 |
| Mochi | old | 31,102 |
| Swazi | ssw | 31,101 |
| Turkana | tuv | 31,101 |
| Kuanyama | kua | 31,100 |
| Tiv | tiv | 31,100 |
| Deg | mzw | 31,098 |
| Chopi | cce | 31,097 |
| Tswa | tsc | 31,097 |
| Bemba (Zambia) | bem | 31,095 |
| Alur | alz | 31,094 |
| Izii | izz | 31,094 |
| Haya | hay | 31,093 |
| Kimbundu | kmb | 31,093 |
| Akan | aka | 31,092 |
| Basa | bzw | 31,092 |
| Ezaa | eza | 31,092 |
| Gedeo | drs | 31,092 |
| Ikwo | iqw | 31,092 |
| Acholi (Acoli) | ach | 31,091 |
| Mambwe (ichi-): Lungu | mgr | 31,091 |
| Tumbuka | tum | 31,089 |
| Umbundu | umb | 31,089 |
| Zande | zne | 31,089 |
| Sango | sag | 31,088 |
| Tetela | tll | 31,088 |
| Urhobo | urh | 31,086 |
| Igala | igl | 31,085 |
| Makhuwa-Shirima | vmk | 31,085 |
| Lugbara | lgg | 31,083 |
| Tonga (Nyasa) | tog | 31,082 |
| Bari | bfa | 31,079 |
| Lamba | lam | 31,079 |
| Ntcham | bud | 31,078 |
| Ebira | igb | 31,076 |
| Idoma | idu | 31,075 |
| Taita | dav | 31,075 |
| Nuer | nus | 31,073 |
| Ika | ikk | 31,071 |
| Kalabari | ijn | 31,067 |
| Bura-Pabir | bwr | 31,063 |
| Nyore | nyd | 31,063 |
| Gun | guw | 31,061 |
| Ibibio | ibb | 31,060 |
| Lozi | loz | 31,059 |
| Krio | kri | 31,056 |
| Ng’akarimojong | kdj | 31,056 |
| Mbunda | mck | 31,054 |
| Sisaala, Tumulung | sil | 31,050 |
| Kabyle | kab | 31,049 |
| Kissi | kqs | 31,047 |
| Guro | goa | 31,037 |
| Igede | ige | 31,037 |
| South Ndebele | nbl | 31,036 |
| Pidgin, Nigerian | pcm | 31,014 |
| Lomwe, Malawi | lon | 31,010 |
| Mandinka | mnk | 30,999 |
| Chidigo | dig | 30,998 |
| Kusaal | kus | 30,995 |
| Konso | kxc | 30,991 |
| Serer (Senegal) | srr | 30,977 |
| Lamnso’ | lns | 30,967 |
| South Giziga | giz | 30,950 |
| Marba | mpg | 30,940 |
| Mousgoum | mug | 30,940 |
| Nyamwanga | mwn | 30,903 |
| Soga | xog | 30,903 |
| Boko (Benin) | bqc | 30,902 |
| Herero | her | 30,902 |
| Lenje | leh | 30,897 |
| Fuliiru | flr | 30,858 |
| Mokole | mkl | 30,857 |
| Fulfulde, Borgu | fue | 30,847 |
| Bassa | bsq | 30,831 |
| Klao | klu | 30,825 |
| Tigrinya | tir | 30,736 |
| Liberia Kpelle | xpe | 30,730 |
| Lelemi | lef | 30,729 |
| Hadiyya | hdy | 30,717 |
| Crioulo, Upper Guinea | pov | 30,706 |
| Wolaytta | wal | 30,704 |
| Venda | ven | 30,687 |
| Kwere | cwe | 30,682 |
| Gen | gej | 30,595 |
| Kafa | kbr | 30,588 |
| Baatonum | bba | 30,565 |
| Kupsapiiny | kpz | 30,558 |
| Congo Swahili | swc | 30,550 |
| Sena (Malawi) | swk | 30,534 |
| Mundang | mua | 30,515 |
| Southern Kisi | kss | 30,468 |
| Pökoot | pko | 30,448 |
| Northeastern Dinka | dip | 30,436 |
| Gonja | gjn | 30,419 |
| Sidamo | sid | 30,403 |
| Berom | bom | 30,358 |
| Ndonga | ndo | 30,303 |
| Dagara, Northern | dgi | 30,302 |
| Shilluk | shk | 30,293 |
| Kwangali | kwn | 30,245 |
| Ngbaka | nga | 30,236 |
| Sebat Bet Gurage | sgw | 30,218 |
| Bokyi | bky | 30,216 |
| Abua | abn | 30,184 |
| Edo | bin | 30,177 |
| Kirike | okr | 30,140 |
| Tsishingini | tsw | 30,117 |
| Kuranko | knk | 29,947 |
| Kituba | mkw | 28,806 |
| Anuak | anu | 28,620 |
| Talinga-Bwisi | tlj | 27,155 |
| Cishingini | asg | 27,089 |
| Luguru | ruf | 26,446 |
| Nyole | nuj | 26,022 |
| Mbula-Bwazza | mbu | 25,985 |
| Mauritian | mfe | 25,687 |
| Koyraboro Senni Songhai | ses | 25,611 |
| Selee | snw | 25,599 |
| Busa | bqp | 25,463 |
| Tashelhayt | shi | 24,405 |
| Ekajuk | eka | 23,842 |
| Makhuwa-Meetto | mgh | 23,421 |
| Vidunda | vid | 22,631 |
| Hdi | xed | 21,200 |
| Ngombe (Democratic Republic of Congo) | ngc | 20,680 |
| Gwere | gwr | 20,249 |
| Kutu | kdc | 20,053 |
| Bokobaru | bus | 19,334 |
| Bɛŋga | bng | 18,704 |
| Zaramo - Zalamo | zaj | 18,639 |
| ILolo | llb | 18,620 |
| Makonde | kde | 17,420 |
| Budu | buu | 17,405 |
| Sena | seh | 16,969 |
| Sénoufo, Nyarafolo | sev | 16,299 |
| Bedjond | bjv | 16,195 |
| Matengo | mgv | 16,120 |
| Arabic, Sudanese (Latin) | apd | 15,916 |
| Laka (Chad) | lap | 15,915 |
| Meta' | mgo | 15,914 |
| Moroccan Arabic | ary | 15,914 |
| Nyiha, Tanzania | nih | 15,909 |
| Nyaturu | rim | 15,904 |
| Farefare | gur | 15,895 |
| Bena (Tanzania) | bez | 15,893 |
| Fulani | fuv | 15,889 |
| Nsenga | nse | 15,889 |
| Jita | jit | 15,884 |
| Kinga | zga | 15,876 |
| Melo | mfx | 15,874 |
| Oyda | oyd | 15,862 |
| Otuho | lot | 15,858 |
| Yemsa | jnj | 15,848 |
| Tuareg | ttq | 15,847 |
| Koonzime | ozm | 15,798 |
| Tarifit | rif | 15,766 |
| Mwani | wmw | 15,691 |
| Gbagyi | gbr | 15,600 |
| Ndendeule | dne | 15,425 |
| Yombe | yom | 15,183 |
| Irigwe | iri | 14,883 |
| Nkangala | nkn | 14,734 |
| Bekwarra | bkv | 14,626 |
| Hwana | hwo | 14,583 |
| Baiso | bsw | 14,576 |
| Ibaas | cen | 14,040 |
| Nafusi | jbn | 13,283 |
| Gungu | rub | 13,122 |
| Kaba | ksp | 12,798 |
| Mbembe, Cross River | mfn | 12,483 |
| Uduk | udu | 12,480 |
| Kutep | kub | 11,895 |
| Taveta | tvs | 11,630 |
| Nyamwezi | nym | 11,629 |
| Mankanya | knf | 11,514 |
| Nyala | nle | 11,330 |
| Bangi | bni | 11,233 |
| Sankaran Maninka | msc | 10,717 |
| Baga Sitemu | bsp | 10,715 |
| Nyungwe | nyu | 10,692 |
| Saafi-Saafi | sav | 10,670 |
| Takwane | tke | 10,658 |
| Jur Modo | bex | 10,603 |
| Mogofin | mfg | 10,545 |
| Mbukushu | mhw | 10,476 |
| Pévé | lme | 10,476 |
| Peere | pfe | 10,441 |
| Lomwe | ngl | 10,397 |
| Nkonya | nko | 10,322 |
| Didinga | did | 10,288 |
| Koti | eko | 10,192 |
| Gbaya (South Sudan) | krs | 10,168 |
| Keliko | kbo | 10,165 |
| Tennet | tex | 10,147 |
| Logoti | log | 9,680 |
| Bakwé | bjw | 9,575 |
| Bandial | bqj | 9,574 |
| kiNgoni | xnj | 9,534 |
| Supyire Senoufo | spp | 9,493 |
| Baka (Sudan) | bdh | 9,486 |
| Oniyan | bsc | 9,484 |
| Omi | omi | 9,474 |
| Wandala | mfi | 9,465 |
| Tem | kdh | 9,454 |
| Wamey | cou | 9,453 |
| Sangu | sbp | 9,441 |
| Mofu-Gudur | mif | 9,406 |
| Ndut | ndv | 9,398 |
| Murle | mur | 9,308 |
| Mündü | muh | 8,874 |
| Thur | lth | 8,393 |
| Mbe | mfo | 8,098 |
| Mamara Senoufo | myk | 8,090 |
| Katcha-Kadugli-Miri | xtc | 8,088 |
| Jowulu | jow | 8,066 |
| Kakwa | keo | 7,960 |
| Benemanga | egm | 7,959 |
| Bondei | bou | 7,959 |
| Grebo, Northern | gbo | 7,959 |
| Gwandara | gwn | 7,959 |
| Lobi | lob | 7,959 |
| Manga Kanuri | kby | 7,959 |
| Mbunga | mgy | 7,959 |
| Mpoto | mpa | 7,959 |
| Mwera (Chimwera) | mwe | 7,959 |
| Ndwewe | nww | 7,959 |
| Ngie | ngj | 7,959 |
| Ngindo | nnq | 7,959 |
| Zigula | ziw | 7,959 |
| Alago | ala | 7,958 |
| Banda-Bambari | liy | 7,958 |
| Eastern Krahn | kqo | 7,958 |
| Fipa | fip | 7,958 |
| Ge'ez (Ethiopic). | gez | 7,958 |
| Godié | god | 7,958 |
| Gulay | gvl | 7,958 |
| Ila | ilb | 7,958 |
| Luyana | lyn | 7,958 |
| Mandjak | mfv | 7,958 |
| Ndamba | ndj | 7,958 |
| Ngiti | niy | 7,958 |
| Otoro | otr | 7,958 |
| Tula | tul | 7,958 |
| Weh | weh | 7,958 |
| Yansi | yns | 7,958 |
| Alumu-Tesu | aab | 7,957 |
| Anyin | any | 7,957 |
| Avatime | avn | 7,957 |
| Bafia | ksf | 7,957 |
| Ikizu | ikz | 7,957 |
| Kare | kbn | 7,957 |
| Kituba (Democratic Republic of Congo) | ktu | 7,957 |
| Mashi | mho | 7,957 |
| Teke-Tyee | tyx | 7,957 |
| Vengo | bav | 7,957 |
| Yocoboué Dida | gud | 7,957 |
| Bedawiyet | bej | 7,956 |
| Lala-Bisa | leb | 7,956 |
| Langi | lag | 7,956 |
| Makaa | mcp | 7,956 |
| Nilamba | nim | 7,956 |
| Ronga | rng | 7,956 |
| Soli | sby | 7,956 |
| Tamasheq | taq | 7,956 |
| Tigon Mbembe | nza | 7,956 |
| Timne | tem | 7,956 |
| Zemba | dhm | 7,956 |
| Asu (Tanzania) | asa | 7,955 |
| Bamunka | bvm | 7,955 |
| Bwamu, Láá Láá | bwj | 7,955 |
| Comorian, Maore | swb | 7,955 |
| Cuvok | cuv | 7,955 |
| Doondo | dde | 7,955 |
| Gavar | gou | 7,955 |
| Ikoma-Nata-Isenye | ntk | 7,955 |
| Majang | mpe | 7,955 |
| Moloko | mlw | 7,955 |
| Tunen | tvu | 7,955 |
| Yaouré | yre | 7,955 |
| Bakoko | bkh | 7,954 |
| Banda, South Central | lnl | 7,954 |
| Ghomálá' | bbj | 7,954 |
| Gor | gqr | 7,954 |
| Kagulu | kki | 7,954 |
| Mengaka | xmg | 7,954 |
| Nawuri | naw | 7,954 |
| Pinyin | pny | 7,954 |
| Tera | ttr | 7,954 |
| Tsaangi | tsa | 7,954 |
| Eten | etx | 7,953 |
| Manda (Tanzania) | mgs | 7,953 |
| Ndo | ndp | 7,953 |
| Buwal | bhs | 7,952 |
| Hehe | heh | 7,952 |
| Ibani | iby | 7,952 |
| Lega-Mwenga | lgm | 7,952 |
| Ngungwel | ngz | 7,952 |
| North Mofu | mfk | 7,952 |
| Aghem | agq | 7,951 |
| Dadiya | dbd | 7,951 |
| Elip | ekm | 7,951 |
| Ewondo | ewo | 7,951 |
| Gayil | gyl | 7,951 |
| Kaonde | kqn | 7,951 |
| Ngombale | nla | 7,951 |
| Oshikwambi | kwm | 7,951 |
| Sagalla | tga | 7,951 |
| Bongili | bui | 7,950 |
| C’lela | dri | 7,950 |
| Ikwere | ikw | 7,950 |
| Kwaya | kya | 7,950 |
| Lumun | lmd | 7,950 |
| Mbudum | xmd | 7,950 |
| Nambya | nmq | 7,950 |
| Ngwo | ngn | 7,950 |
| Songe | sop | 7,950 |
| Bali (Nigeria) | bcn | 7,949 |
| Bambalang | bmo | 7,949 |
| Bekwel | bkw | 7,949 |
| Bété, Gagnoa | btg | 7,949 |
| Gabri | gab | 7,949 |
| Merey | meq | 7,949 |
| Ncane | ncr | 7,949 |
| Oku | oku | 7,949 |
| Sari | asj | 7,949 |
| Yemba | ybb | 7,949 |
| Borna | bwo | 7,948 |
| Bukerebe (Kerebe) | ked | 7,948 |
| Dinka, Southeastern | dks | 7,948 |
| Kenyang | ken | 7,948 |
| Mango | mge | 7,948 |
| Niellim | nie | 7,948 |
| Tuki | bag | 7,948 |
| Vunjo | vun | 7,948 |
| Ajiri | afo | 7,947 |
| Bissa | bib | 7,947 |
| Ivbie North-Okpela-Arhe | atg | 7,947 |
| Noone | nhu | 7,947 |
| Yaka | iyx | 7,947 |
| Yala | yba | 7,947 |
| Arabic, Algerian | arq | 7,946 |
| Bu (Kaduna State) | jid | 7,946 |
| Etkywan | ich | 7,946 |
| Kako | kkj | 7,946 |
| Komo | kmw | 7,946 |
| Miyobe | soy | 7,946 |
| Mmaala | mmu | 7,946 |
| Mwan | moa | 7,946 |
| Ndali | ndh | 7,946 |
| Ngomba | jgo | 7,946 |
| Yangben | yav | 7,946 |
| Bafaw-Balong | bwt | 7,945 |
| Bete-Bendi | btt | 7,945 |
| Konni | kma | 7,945 |
| Ngangam | gng | 7,945 |
| Zinza | zin | 7,945 |
| Abron | abr | 7,944 |
| Bafut | bfd | 7,944 |
| Eggon | ego | 7,944 |
| Jibu | jib | 7,944 |
| Kimré | kqp | 7,944 |
| Loma (Liberia) | lom | 7,944 |
| Pana | pnz | 7,944 |
| Shambala | ksb | 7,944 |
| Tafi | tcd | 7,944 |
| Esimbi | ags | 7,943 |
| Hungworo | nat | 7,943 |
| Hyam | jab | 7,943 |
| Lika | lik | 7,943 |
| Limbum | lmp | 7,943 |
| Mpumpong | mgg | 7,943 |
| Vili | vif | 7,943 |
| Awing | azo | 7,942 |
| Cibak | ckl | 7,942 |
| Izere | izr | 7,942 |
| Mano | mev | 7,942 |
| Matal | mfh | 7,942 |
| Mokpwe | bri | 7,942 |
| Mundani | mnf | 7,942 |
| Ngando (Democratic Republic of Congo) | nxd | 7,942 |
| Ninzo | nin | 7,942 |
| Rendille | rel | 7,942 |
| Ron | cla | 7,942 |
| Southern Birifor | biv | 7,942 |
| Leelau | ldk | 7,941 |
| Duya | ldb | 7,940 |
| Dzùùngoo | dnn | 7,940 |
| Gbaya, Southwest | gso | 7,940 |
| Gude | gde | 7,940 |
| Luna | luj | 7,940 |
| Denya | anv | 7,939 |
| Fulfulde (Central-Eastern Niger) | fuq | 7,939 |
| Lame | bma | 7,939 |
| Matumbi | mgw | 7,939 |
| Nugunu | yas | 7,939 |
| Northern Gabri | tng | 7,938 |
| Cameroon Mambila | mcu | 7,937 |
| Jola-Kasa | csk | 7,937 |
| Mumuye | mzm | 7,937 |
| Muyang | muy | 7,937 |
| Siwu | akp | 7,937 |
| Zanaki | zak | 7,937 |
| Daasanach | dsh | 7,936 |
| Kenga | kyq | 7,936 |
| Kera | ker | 7,936 |
| Mada (Nigeria) | mda | 7,936 |
| Pular | fuf | 7,936 |
| Rwa | rwk | 7,936 |
| Tembo | tbt | 7,936 |
| Tsogo | tsv | 7,936 |
| Alladian | ald | 7,935 |
| Bacama | bcy | 7,935 |
| Etulo | utr | 7,935 |
| Kamo | kcq | 7,935 |
| Malila | mgq | 7,934 |
| Manya | mzj | 7,934 |
| Tyap | kcg | 7,934 |
| Vwanji | wbi | 7,934 |
| Heiban (Sudan) | hbn | 7,933 |
| Ndogo | ndz | 7,933 |
| Noon | snf | 7,933 |
| Western Krahn | krw | 7,933 |
| Tharaka | thk | 7,932 |
| Zulgo-Gemzek | gnd | 7,932 |
| Delo | ntr | 7,931 |
| Suba | sxb | 7,931 |
| Vute | vut | 7,931 |
| Yambeta | yat | 7,931 |
| Doyayo | dow | 7,929 |
| Moba | mfq | 7,929 |
| Ngemba | nge | 7,929 |
| Huba | hbb | 7,928 |
| Kabwa | cwa | 7,928 |
| Nomaande | lem | 7,928 |
| Ejagham | etu | 7,927 |
| Wè Northern | wob | 7,927 |
| Babanki | bbk | 7,926 |
| Suba-Simbiti | ssc | 7,926 |
| Akoose | bss | 7,925 |
| Burunge | bds | 7,925 |
| Bété, Daloa | bev | 7,925 |
| Eastern Karaboro | xrb | 7,925 |
| Ebrié | ebr | 7,925 |
| Isu | szv | 7,925 |
| Jju | kaj | 7,925 |
| Yamba | yam | 7,925 |
| Lobala | loq | 7,923 |
| Mmen | bfm | 7,923 |
| West-Central Limba | lia | 7,923 |
| Kabiyè | kbp | 7,922 |
| Mbuko | mqb | 7,922 |
| Mukulu | moz | 7,921 |
| Bum | bmv | 7,920 |
| Cerma | cme | 7,920 |
| Giryama | nyf | 7,920 |
| Kele (Democratic Republic of Congo) | khy | 7,920 |
| Naro | nhr | 7,920 |
| Tampulma | tpm | 7,919 |
| Alaba-K’abeena | alw | 7,917 |
| Safwa | sbk | 7,917 |
| Samba Leko | ndi | 7,917 |
| Dii | dur | 7,915 |
| Mayogo | mdm | 7,915 |
| Mende | men | 7,914 |
| Anufo | cko | 7,913 |
| Odual | odu | 7,913 |
| Buamu | box | 7,912 |
| Lyélé | lee | 7,912 |
| Saho | ssy | 7,912 |
| Tuwuli | bov | 7,912 |
| Xamtanga | xan | 7,912 |
| Vai | vai | 7,911 |
| Dan | dnj | 7,910 |
| Ifè | ife | 7,910 |
| Migaama | mmy | 7,910 |
| Dangaléat | daa | 7,909 |
| Birifor, Malba | bfo | 7,908 |
| Western Niger Fulfulde | fuh | 7,908 |
| Shoo-Minda-Nye | bcv | 7,907 |
| Kuo | xuo | 7,905 |
| Gikyode | acd | 7,904 |
| Adioukrou | adj | 7,902 |
| Basketo | bst | 7,902 |
| Northern Ngbandi | ngb | 7,901 |
| Samburu | saq | 7,901 |
| Sekpele | lip | 7,900 |
| Tsikimba | kdl | 7,900 |
| Bana | bcw | 7,898 |
| Dinka Southwestern | dik | 7,897 |
| Pokomo | pkb | 7,895 |
| Kuwaataay | cwt | 7,894 |
| Paasaal | sig | 7,894 |
| Southern Nuni | nnw | 7,893 |
| Hun-Saare | uth | 7,891 |
| Mampruli | maw | 7,891 |
| Bandi | bza | 7,887 |
| Kono (Sierra Leone) | kno | 7,877 |
| Dan | daf | 7,876 |
| Kouya | kyf | 7,875 |
| Plapo Krumen | ktj | 7,874 |
| Shekkacho | moy | 7,874 |
| Tepo Krumen | ted | 7,874 |
| Duruma | dug | 7,869 |
| Bété, Guiberoua | bet | 7,860 |
| Koorete | kqy | 7,852 |
| Kaansa | gna | 7,834 |
| Luwo | lwo | 7,814 |
| Nyabwa | nwb | 7,734 |
| Chumburung | ncu | 7,687 |
| Ménik | tnr | 7,681 |
| Karang | kzr | 7,680 |
| Avokaya | avu | 7,588 |
| Gola | gol | 7,243 |
| Ruuli | ruc | 7,219 |
| Yaka | yaf | 7,106 |
| Southern Toussian | wib | 6,987 |
| Karon | krx | 6,706 |
| Isanzu | isn | 6,217 |
| Sagala | sbm | 6,217 |
| Kami | kcu | 6,216 |
| Lala-Roba | lla | 6,068 |
| Ndonde Hamba | njd | 5,960 |
| Suri | suq | 5,868 |
| Marghi South | mfm | 5,835 |
| Geji | gyz | 5,735 |
| Mahou | mxx | 5,287 |
| ut-Ma’in | gel | 5,250 |
| Gbanu | gbv | 5,216 |
| Mono | mnh | 5,156 |
| Taabwa | tap | 5,060 |
| Tangale | tan | 4,886 |
| Verre | ver | 4,875 |
| Ndrulo | dno | 4,721 |
| Somrai | sor | 4,717 |
| Kunda | kdn | 4,652 |
| Ga’anda | gqa | 4,186 |
| Glavda | glw | 3,995 |
| Chala | cll | 3,907 |
| Abureni | mgj | 3,889 |
| Cakfem-Mushere | cky | 3,878 |
| Morokodo | mgc | 3,827 |
| Jumjum | jum | 3,801 |
| Neyo | ney | 3,779 |
| Kenzi Nubian | xnz | 3,778 |
| Ajiya | idc | 3,777 |
| Havu | hav | 3,226 |
| Nyanga | nyj | 3,192 |
| Tuareg | thv | 2,803 |
| Kimbu | kiv | 2,628 |
| Mbugu | mhd | 2,628 |
| Shama-Sambuga | sqa | 2,380 |
| Gusilay | gsl | 2,277 |
| Duupa | dae | 2,222 |
| Sanga | xsn | 2,221 |
| Ma’di, Southern | snm | 2,144 |
| Amba | rwm | 2,078 |
| Wolof (Gambia) | wof | 1,968 |
| Sala | shq | 1,945 |
| Waja | wja | 1,764 |
| Guduf-Gava | gdf | 1,749 |
| Hassaniyya | mey | 1,533 |
| Nyangbo | nyb | 1,531 |
| Saba | saa | 1,522 |
| Hanga | hag | 1,320 |
| Aushi | auh | 1,226 |
| Bwile | bwc | 1,226 |
| Basa-Gurmana | buj | 1,071 |
| Wannu | jub | 1,071 |
| Lubila | kcc | 1,068 |
| Bullom So | buy | 1,066 |

---

## Quick start

```bash
git clone https://github.com/michsethowusu/africa-corpus-builder.git
cd africa-corpus-builder
```

Requires Python 3.10+ and `huggingface_hub` (used to download the data the
first time you reference a language):

```bash
pip install huggingface_hub
```

Downloaded files are cached, so each language is only fetched once. The dataset
is public — no HuggingFace login is needed to read it.

### List what's available

```bash
python africa_corpus.py --list
```

### Build a corpus for one language (the common case)

```bash
# Swahili ↔ English (English is the default target)
python africa_corpus.py --source swc

# Twi ↔ Yoruba (two African languages)
python africa_corpus.py --source twi --target yor

# Hausa ↔ French
python africa_corpus.py --source hau --target fr

# Monolingual Amharic
python africa_corpus.py --source amh --monolingual
```

Each writes a CSV named after the languages (e.g. `swc_en_parallel.csv`,
`amh_monolingual.csv`). Use `--out PATH` to choose the filename.

### Limit the number of samples

```bash
# first 5,000 Swahili–English pairs (in scripture order, deterministic)
python africa_corpus.py --source swc --limit 5000

# a random 5,000-pair sample (reproducible via --seed)
python africa_corpus.py --source swc --limit 5000 --sample --seed 42
```

### Build for many languages at once

`--source` accepts a comma-separated list or the keyword `all`. With more than
one source, one file per language is written into `--out-dir` (default
`corpora/`).

```bash
# every African language paired with English, 10k samples each
python africa_corpus.py --source all --limit 10000 --out-dir corpora/

# a selected set, paired with French
python africa_corpus.py --source twi,swc,yor,hau --target fr --out-dir corpora/

# monolingual corpora for every African language
python africa_corpus.py --source all --monolingual --out-dir corpora/
```

### Use it as a library

```python
import africa_corpus as ac

ac.list_languages()                               # (african, reference) language lists
rows  = ac.parallel("swc", "en", limit=1000)      # [(verse_key, swc, en), ...]
rows  = ac.parallel("twi", "yor")                 # twi ↔ Yoruba
sents = ac.monolingual("hau", limit=500, sample=True)

ac.write_parallel_csv("swc", "fr", "swahili_french.csv", limit=2000)
ac.write_monolingual_csv("amh", "amharic.csv")

# one file per language
ac.build_batch(ac.all_african_codes(), target="en",
               limit=10000, out_dir="corpora/")
```

Languages are referenced by code (`swc`, `yor`, `fr`) or by name
(`"Swahili"`, `"French"`).

---

## Available languages

**African languages** — 693 languages across the continent are available. Run
`python africa_corpus.py --list` to see all codes and names.

**Reference languages** that can be used as the non-African side of a parallel corpus:

| Code | Language | Version |
|---|---|---|
| `en` | English | CEB (v37) |
| `fr` | French | LSG (v93) |
| `ar` | Arabic | AVD (v13) |
| `zh` | Chinese | CUNPSS (v48) |
| `pt` | Portuguese | ARA (v1608) |

### Adding more reference languages

The reference set is fully self-describing — no index and no code changes. Each
cache is stored as `reference_caches/{Name}_{code}_v{id}.csv`, and the library
learns the language straight from that filename on HuggingFace.

To add one, find its YouVersion numeric version id (a full-Bible version works
best), then:

```bash
# 1. fetch and cache it locally
python scripts/build_pivot_caches.py   # edit PIVOTS dict to add your language first

# 2. convert to corpus format
python scripts/prepare_reference_caches.py

# 3. push to HuggingFace
python scripts/push_to_hf.py
```

It's immediately selectable in `africa_corpus.py` once on HuggingFace — nothing
to commit.

---

## Coverage

The dataset covers **693 African languages**,
sourced from [YouVersion](https://www.bible.com) and cross-referenced against
[Glottolog](https://glottolog.org)'s Africa macroarea.

Languages span all major African language families: Niger-Congo, Afro-Asiatic,
Nilo-Saharan, Khoisan, and Austronesian (Madagascar). Total verse records: ~16
million.

---

## Maintainer tooling (building the datasets)

The raw CSVs in `michsethowusu/africa-corpus` were produced by the scripts
below — **regular users do not need to run them.** For maintainers extending
coverage:

- `youversion_parallel_text_builder.py` — automated CSV-driven scraper; reads
  `youversion_africa_versions.csv` and scrapes every version, one at a time.
  Resume-safe: interrupted runs pick up exactly where they left off.
- `youversion_common.py` — shared API helpers (chapter fetcher, text cleaner,
  session pool).
- `scripts/build_pivot_caches.py` — fetches the five pivot/reference Bibles (en/fr/ar/zh/pt)
  into `pivots/`.
- `scripts/prepare_reference_caches.py` — converts `pivots/` into the corpus format
  expected by `africa_corpus.py`.
- `scripts/push_to_hf.py` — incremental sync of `african_bible_parallel_text_datasets/`
  to `michsethowusu/africa-corpus`; only uploads files not already on HF.

Typical workflow for extending coverage:

```bash
# scrape new versions (or re-run after adding rows to the CSV)
python youversion_parallel_text_builder.py youversion_africa_versions.csv

# then push new files to HuggingFace
python scripts/push_to_hf.py --dry-run   # preview what's new
python scripts/push_to_hf.py             # sync to HF
```

---

## Data source

Verse text comes from public **Bible translations**, which are among the best
naturally-occurring sources of sentence-aligned parallel text for low-resource
languages.

> Text was retrieved from [YouVersion](https://www.bible.com) (bible.com).
> Please review YouVersion's terms of service before publishing or
> redistributing derived data.

---

## License

Code in this repository is released under the MIT License. Dataset content is
derived from third-party Bible translations; review the source's terms before
publishing or distributing.

---

## Acknowledgements

Inspired by [ghana-corpus-builder](https://github.com/GhanaNLP/ghana-corpus-builder)
by the [Ghana NLP Community](https://ghananlp.org). Language–macroarea mapping
from [Glottolog](https://glottolog.org). If you use this data in research,
please cite the underlying Bible-translation sources.
