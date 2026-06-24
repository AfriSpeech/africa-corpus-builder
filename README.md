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

**693 African languages** (by ISO code) across **949 Bible versions**, **15,974,671 sentences** in total. Counts are summed across all versions of each language (sentences = harvested verses available for alignment).

<details>
<summary>Per-language sentence counts (click to expand)</summary>

| Language | Code | Versions | Sentences |
|---|---|--:|--:|
| Swahili | swh | 13 | 356,708 |
| Afrikaans | afr | 9 | 279,114 |
| Shona | sna | 8 | 224,417 |
| Malgache | plt | 7 | 216,384 |
| Ganda | lug | 6 | 186,020 |
| Twi | twi | 5 | 154,554 |
| Oromo, Arsi / Oromo, Borana-Arsi-Guji | gax | 8 | 153,267 |
| Amharic | amh | 5 | 149,730 |
| Masai | mas | 5 | 131,770 |
| Rwandan | kin | 5 | 131,531 |
| Nyanja | nya | 5 | 130,148 |
| Xhosa | xho | 4 | 123,914 |
| Kikuyu | kik | 4 | 122,087 |
| Dawro | dwr | 5 | 108,043 |
| Zulu | zul | 4 | 101,217 |
| Setswana | tsn | 4 | 100,904 |
| West Central Oromo | gaz | 3 | 93,307 |
| Yoruba | yor | 3 | 93,205 |
| Guinea Kpelle | gkp | 3 | 92,843 |
| Éwé | ewe | 3 | 92,774 |
| Kamba (Kenya) | kam | 3 | 92,746 |
| Kalenjin | kln | 3 | 92,740 |
| Wanga | lwg | 3 | 92,718 |
| Ekegusii | guz | 3 | 92,699 |
| Hausa / Hausa Arabic script | hau | 3 | 92,666 |
| Adamawa Fulfulde / Fulfulde (Adamawa) | fub | 3 | 92,574 |
| Southern Sotho | sot | 4 | 78,155 |
| Nyakyusa-Ngonde | nyy | 4 | 77,931 |
| Gofa | gof | 4 | 77,810 |
| Gidar | gid | 3 | 70,238 |
| Dyula | dyu | 3 | 70,170 |
| Somali | som | 3 | 70,123 |
| Kuria | kuj | 3 | 70,104 |
| Tsonga | tso | 3 | 70,018 |
| Mossi | mos | 3 | 69,449 |
| Susu (Roman script) / Susu (Arabic Script) | sus | 3 | 62,465 |
| Mbay | myb | 2 | 62,307 |
| Tupuri | tui | 2 | 62,254 |
| Lunda | lun | 2 | 62,207 |
| Seselwa Creole French | crs | 2 | 62,206 |
| Ga | gaa | 2 | 62,199 |
| Rundi | run | 2 | 62,181 |
| Fon | fon | 2 | 62,176 |
| Nyankole | nyn | 2 | 62,172 |
| Igbo | ibo | 2 | 62,164 |
| North Ndebele | nde | 2 | 62,164 |
| Nyoro | nyo | 2 | 62,163 |
| Tonga (Zambia) | toi | 2 | 62,161 |
| Embu | ebu | 2 | 62,122 |
| Gitonga | toh | 2 | 62,113 |
| Obolo | ann | 2 | 62,076 |
| Chadian Arabic (Roman script) | shu | 2 | 62,044 |
| Gbaya, Northwest | gya | 2 | 62,040 |
| Lulogooli | rag | 2 | 61,994 |
| Gourmanchéma | gux | 2 | 61,982 |
| Psikye | kvj | 2 | 61,966 |
| Luo (Kenya and Tanzania) | luo | 2 | 61,959 |
| Luba-Lulua | lua | 2 | 61,870 |
| Gamo | gmv | 2 | 61,812 |
| Kimîîru | mer | 2 | 61,674 |
| Tsotso | lto | 2 | 61,654 |
| Fanti | fat | 2 | 61,636 |
| Saamia | lsm | 2 | 61,606 |
| Dagbani | dag | 2 | 61,592 |
| Sar | mwm | 2 | 61,586 |
| Adhola | adh | 2 | 61,581 |
| Bukusu | bxk | 2 | 61,578 |
| Masaaba | myx | 2 | 61,504 |
| Sotho, Northern | nso | 2 | 61,340 |
| Kumam | kdi | 2 | 61,328 |
| Chokwe | cjk | 2 | 61,062 |
| Samo, Southern | sbd | 2 | 61,044 |
| Khoekhoe | naq | 2 | 60,722 |
| Bulu (Cameroon) | bum | 2 | 59,911 |
| Yao | yao | 3 | 50,503 |
| Sukuma | suk | 3 | 46,989 |
| Burkina Faso Fulfulde / Maasina Fulfulde | ffm | 3 | 44,152 |
| Teso | teo | 2 | 42,415 |
| Iraqw | irk | 2 | 41,509 |
| Kinandi (Ndandi) | nnb | 2 | 41,509 |
| Mafa | maf | 2 | 39,109 |
| Beembe (Congo) | beq | 2 | 39,106 |
| Kim | kia | 2 | 39,085 |
| Mongo | lol | 2 | 39,050 |
| Efik | efi | 2 | 39,049 |
| Machame | jmc | 2 | 39,046 |
| Lango (Uganda) | laj | 2 | 39,044 |
| Sehwi | sfw | 2 | 39,043 |
| Luvale | lue | 2 | 39,040 |
| Ndau | ndc | 2 | 39,037 |
| Datooga | tcc | 2 | 39,033 |
| Wolof (Senegal) | wol | 2 | 39,024 |
| Nkoya | nka | 2 | 39,017 |
| Gogo | gog | 2 | 39,006 |
| Lambya | lai | 2 | 38,990 |
| Southern Dagaare | dga | 2 | 38,983 |
| Kalanga | kck | 2 | 38,975 |
| Ngiemboon | nnh | 2 | 38,788 |
| Baoulé | bci | 2 | 38,743 |
| Kasem | xsm | 2 | 38,665 |
| Maale | mdy | 2 | 38,448 |
| Bimoba | bim | 2 | 38,209 |
| Adangme | ada | 2 | 38,177 |
| Konkomba | xon | 2 | 38,094 |
| Nzima | nzi | 2 | 36,220 |
| Pogolo | poy | 2 | 34,407 |
| Ngulu | ngp | 2 | 34,404 |
| Aringa | luc | 3 | 32,415 |
| Yalunka | yal | 2 | 32,215 |
| Myene | mye | 1 | 31,163 |
| Medumba | byv | 1 | 31,150 |
| Masana | mcn | 1 | 31,149 |
| Lingala | lin | 1 | 31,146 |
| Toma | tod | 1 | 31,144 |
| Sénoufo, Cebaara | sef | 1 | 31,141 |
| Musey | mse | 1 | 31,132 |
| Ngambay | sba | 1 | 31,125 |
| Djimini Senoufo | dyi | 1 | 31,122 |
| Punu (Ipounou) | puu | 1 | 31,117 |
| Shi | shr | 1 | 31,115 |
| Sénoufo, Tagwana | tgw | 1 | 31,111 |
| Vagla | vag | 1 | 31,104 |
| Kambaata | ktb | 1 | 31,103 |
| Buli (Ghana) | bwu | 1 | 31,102 |
| Mochi | old | 1 | 31,102 |
| Swazi | ssw | 1 | 31,101 |
| Turkana | tuv | 1 | 31,101 |
| Kuanyama | kua | 1 | 31,100 |
| Tiv | tiv | 1 | 31,100 |
| Deg | mzw | 1 | 31,098 |
| Chopi | cce | 1 | 31,097 |
| Tswa | tsc | 1 | 31,097 |
| Bemba (Zambia) | bem | 1 | 31,095 |
| Alur | alz | 1 | 31,094 |
| Izii | izz | 1 | 31,094 |
| Haya | hay | 1 | 31,093 |
| Kimbundu | kmb | 1 | 31,093 |
| Akan | aka | 1 | 31,092 |
| Basa | bzw | 1 | 31,092 |
| Ezaa | eza | 1 | 31,092 |
| Gedeo | drs | 1 | 31,092 |
| Ikwo | iqw | 1 | 31,092 |
| Acholi (Acoli) | ach | 1 | 31,091 |
| Mambwe (ichi-): Lungu | mgr | 1 | 31,091 |
| Tumbuka | tum | 1 | 31,089 |
| Umbundu | umb | 1 | 31,089 |
| Zande | zne | 1 | 31,089 |
| Sango | sag | 1 | 31,088 |
| Tetela | tll | 1 | 31,088 |
| Urhobo | urh | 1 | 31,086 |
| Igala | igl | 1 | 31,085 |
| Makhuwa-Shirima | vmk | 1 | 31,085 |
| Lugbara | lgg | 1 | 31,083 |
| Tonga (Nyasa) | tog | 1 | 31,082 |
| Bari | bfa | 1 | 31,079 |
| Lamba | lam | 1 | 31,079 |
| Ntcham | bud | 1 | 31,078 |
| Ebira | igb | 1 | 31,076 |
| Idoma | idu | 1 | 31,075 |
| Taita | dav | 1 | 31,075 |
| Nuer | nus | 1 | 31,073 |
| Ika | ikk | 1 | 31,071 |
| Kalabari | ijn | 1 | 31,067 |
| Bura-Pabir | bwr | 1 | 31,063 |
| Nyore | nyd | 1 | 31,063 |
| Gun | guw | 1 | 31,061 |
| Ibibio | ibb | 1 | 31,060 |
| Lozi | loz | 1 | 31,059 |
| Krio | kri | 1 | 31,056 |
| Ng’akarimojong | kdj | 1 | 31,056 |
| Mbunda | mck | 1 | 31,054 |
| Sisaala, Tumulung | sil | 1 | 31,050 |
| Kabyle | kab | 1 | 31,049 |
| Kissi | kqs | 1 | 31,047 |
| Guro | goa | 1 | 31,037 |
| Igede | ige | 1 | 31,037 |
| South Ndebele | nbl | 1 | 31,036 |
| Pidgin, Nigerian | pcm | 1 | 31,014 |
| Lomwe, Malawi | lon | 1 | 31,010 |
| Mandinka | mnk | 1 | 30,999 |
| Chidigo | dig | 1 | 30,998 |
| Kusaal | kus | 1 | 30,995 |
| Konso | kxc | 1 | 30,991 |
| Serer (Senegal) | srr | 1 | 30,977 |
| Lamnso’ | lns | 1 | 30,967 |
| South Giziga | giz | 1 | 30,950 |
| Marba | mpg | 1 | 30,940 |
| Mousgoum | mug | 1 | 30,940 |
| Nyamwanga | mwn | 1 | 30,903 |
| Soga | xog | 1 | 30,903 |
| Boko (Benin) | bqc | 1 | 30,902 |
| Herero | her | 1 | 30,902 |
| Lenje | leh | 1 | 30,897 |
| Fuliiru | flr | 1 | 30,858 |
| Mokole | mkl | 1 | 30,857 |
| Fulfulde, Borgu | fue | 1 | 30,847 |
| Bassa | bsq | 1 | 30,831 |
| Klao | klu | 1 | 30,825 |
| Tigrinya | tir | 1 | 30,736 |
| Liberia Kpelle | xpe | 1 | 30,730 |
| Lelemi | lef | 1 | 30,729 |
| Hadiyya | hdy | 1 | 30,717 |
| Crioulo, Upper Guinea | pov | 1 | 30,706 |
| Wolaytta | wal | 1 | 30,704 |
| Venda | ven | 1 | 30,687 |
| Kwere | cwe | 2 | 30,682 |
| Gen | gej | 1 | 30,595 |
| Kafa | kbr | 1 | 30,588 |
| Baatonum | bba | 1 | 30,565 |
| Kupsapiiny | kpz | 1 | 30,558 |
| Congo Swahili | swc | 1 | 30,550 |
| Sena (Malawi) | swk | 1 | 30,534 |
| Mundang | mua | 1 | 30,515 |
| Southern Kisi | kss | 1 | 30,468 |
| Pökoot | pko | 1 | 30,448 |
| Northeastern Dinka | dip | 1 | 30,436 |
| Gonja | gjn | 1 | 30,419 |
| Sidamo | sid | 1 | 30,403 |
| Berom | bom | 1 | 30,358 |
| Ndonga | ndo | 1 | 30,303 |
| Dagara, Northern | dgi | 1 | 30,302 |
| Shilluk | shk | 1 | 30,293 |
| Kwangali | kwn | 1 | 30,245 |
| Ngbaka | nga | 1 | 30,236 |
| Sebat Bet Gurage | sgw | 1 | 30,218 |
| Bokyi | bky | 1 | 30,216 |
| Abua | abn | 1 | 30,184 |
| Edo | bin | 1 | 30,177 |
| Kirike | okr | 1 | 30,140 |
| Tsishingini | tsw | 2 | 30,117 |
| Kuranko | knk | 1 | 29,947 |
| Kituba | mkw | 1 | 28,806 |
| Anuak | anu | 1 | 28,620 |
| Talinga-Bwisi | tlj | 2 | 27,155 |
| Cishingini | asg | 2 | 27,089 |
| Luguru | ruf | 1 | 26,446 |
| Nyole | nuj | 2 | 26,022 |
| Mbula-Bwazza | mbu | 2 | 25,985 |
| Mauritian | mfe | 3 | 25,687 |
| Koyraboro Senni Songhai | ses | 1 | 25,611 |
| Selee | snw | 2 | 25,599 |
| Busa | bqp | 1 | 25,463 |
| Tashelhayt | shi | 3 | 24,405 |
| Ekajuk | eka | 2 | 23,842 |
| Makhuwa-Meetto | mgh | 2 | 23,421 |
| Vidunda | vid | 1 | 22,631 |
| Hdi | xed | 1 | 21,200 |
| Ngombe (Democratic Republic of Congo) | ngc | 4 | 20,680 |
| Gwere | gwr | 1 | 20,249 |
| Kutu | kdc | 1 | 20,053 |
| Bokobaru | bus | 1 | 19,334 |
| Bɛŋga | bng | 1 | 18,704 |
| Zaramo - Zalamo | zaj | 2 | 18,639 |
| ILolo | llb | 1 | 18,620 |
| Makonde | kde | 2 | 17,420 |
| Budu | buu | 2 | 17,405 |
| Sena | seh | 3 | 16,969 |
| Sénoufo, Nyarafolo | sev | 1 | 16,299 |
| Bedjond | bjv | 2 | 16,195 |
| Matengo | mgv | 1 | 16,120 |
| Arabic, Sudanese (Latin) | apd | 2 | 15,916 |
| Laka (Chad) | lap | 2 | 15,915 |
| Meta' | mgo | 2 | 15,914 |
| Moroccan Arabic | ary | 2 | 15,914 |
| Nyiha, Tanzania | nih | 2 | 15,909 |
| Nyaturu | rim | 2 | 15,904 |
| Farefare | gur | 2 | 15,895 |
| Bena (Tanzania) | bez | 2 | 15,893 |
| Fulani | fuv | 2 | 15,889 |
| Nsenga | nse | 2 | 15,889 |
| Jita | jit | 2 | 15,884 |
| Kinga | zga | 2 | 15,876 |
| Melo | mfx | 2 | 15,874 |
| Oyda | oyd | 2 | 15,862 |
| Otuho | lot | 2 | 15,858 |
| Yemsa | jnj | 2 | 15,848 |
| Tuareg | ttq | 2 | 15,847 |
| Koonzime | ozm | 2 | 15,798 |
| Tarifit | rif | 2 | 15,766 |
| Mwani | wmw | 1 | 15,691 |
| Gbagyi | gbr | 2 | 15,600 |
| Ndendeule | dne | 1 | 15,425 |
| Yombe | yom | 2 | 15,183 |
| Irigwe | iri | 2 | 14,883 |
| Nkangala | nkn | 2 | 14,734 |
| Bekwarra | bkv | 1 | 14,626 |
| Hwana | hwo | 2 | 14,583 |
| Baiso | bsw | 2 | 14,576 |
| Ibaas | cen | 2 | 14,040 |
| Nafusi | jbn | 3 | 13,283 |
| Gungu | rub | 1 | 13,122 |
| Kaba | ksp | 2 | 12,798 |
| Mbembe, Cross River | mfn | 2 | 12,483 |
| Uduk | udu | 1 | 12,480 |
| Kutep | kub | 1 | 11,895 |
| Taveta | tvs | 1 | 11,630 |
| Nyamwezi | nym | 2 | 11,629 |
| Mankanya | knf | 1 | 11,514 |
| Nyala | nle | 1 | 11,330 |
| Bangi | bni | 1 | 11,233 |
| Sankaran Maninka | msc | 1 | 10,717 |
| Baga Sitemu | bsp | 1 | 10,715 |
| Nyungwe | nyu | 1 | 10,692 |
| Saafi-Saafi | sav | 1 | 10,670 |
| Takwane | tke | 1 | 10,658 |
| Jur Modo | bex | 1 | 10,603 |
| Mogofin | mfg | 1 | 10,545 |
| Mbukushu | mhw | 1 | 10,476 |
| Pévé | lme | 1 | 10,476 |
| Peere | pfe | 1 | 10,441 |
| Lomwe | ngl | 1 | 10,397 |
| Nkonya | nko | 1 | 10,322 |
| Didinga | did | 1 | 10,288 |
| Koti | eko | 1 | 10,192 |
| Gbaya (South Sudan) | krs | 1 | 10,168 |
| Keliko | kbo | 1 | 10,165 |
| Tennet | tex | 1 | 10,147 |
| Logoti | log | 2 | 9,680 |
| Bakwé | bjw | 1 | 9,575 |
| Bandial | bqj | 1 | 9,574 |
| kiNgoni | xnj | 1 | 9,534 |
| Supyire Senoufo | spp | 1 | 9,493 |
| Baka (Sudan) | bdh | 1 | 9,486 |
| Oniyan | bsc | 1 | 9,484 |
| Omi | omi | 1 | 9,474 |
| Wandala | mfi | 1 | 9,465 |
| Tem | kdh | 1 | 9,454 |
| Wamey | cou | 1 | 9,453 |
| Sangu | sbp | 1 | 9,441 |
| Mofu-Gudur | mif | 2 | 9,406 |
| Ndut | ndv | 1 | 9,398 |
| Murle | mur | 1 | 9,308 |
| Mündü | muh | 1 | 8,874 |
| Thur | lth | 1 | 8,393 |
| Mbe | mfo | 1 | 8,098 |
| Mamara Senoufo | myk | 1 | 8,090 |
| Katcha-Kadugli-Miri | xtc | 1 | 8,088 |
| Jowulu | jow | 1 | 8,066 |
| Kakwa | keo | 1 | 7,960 |
| Benemanga | egm | 1 | 7,959 |
| Bondei | bou | 1 | 7,959 |
| Grebo, Northern | gbo | 1 | 7,959 |
| Gwandara | gwn | 1 | 7,959 |
| Lobi | lob | 1 | 7,959 |
| Manga Kanuri | kby | 1 | 7,959 |
| Mbunga | mgy | 1 | 7,959 |
| Mpoto | mpa | 1 | 7,959 |
| Mwera (Chimwera) | mwe | 1 | 7,959 |
| Ndwewe | nww | 1 | 7,959 |
| Ngie | ngj | 1 | 7,959 |
| Ngindo | nnq | 1 | 7,959 |
| Zigula | ziw | 1 | 7,959 |
| Alago | ala | 1 | 7,958 |
| Banda-Bambari | liy | 1 | 7,958 |
| Eastern Krahn | kqo | 1 | 7,958 |
| Fipa | fip | 1 | 7,958 |
| Ge'ez (Ethiopic). | gez | 1 | 7,958 |
| Godié | god | 1 | 7,958 |
| Gulay | gvl | 1 | 7,958 |
| Ila | ilb | 1 | 7,958 |
| Luyana | lyn | 1 | 7,958 |
| Mandjak | mfv | 1 | 7,958 |
| Ndamba | ndj | 1 | 7,958 |
| Ngiti | niy | 1 | 7,958 |
| Otoro | otr | 1 | 7,958 |
| Tula | tul | 1 | 7,958 |
| Weh | weh | 1 | 7,958 |
| Yansi | yns | 1 | 7,958 |
| Alumu-Tesu | aab | 1 | 7,957 |
| Anyin | any | 1 | 7,957 |
| Avatime | avn | 1 | 7,957 |
| Bafia | ksf | 1 | 7,957 |
| Ikizu | ikz | 1 | 7,957 |
| Kare | kbn | 1 | 7,957 |
| Kituba (Democratic Republic of Congo) | ktu | 1 | 7,957 |
| Mashi | mho | 1 | 7,957 |
| Teke-Tyee | tyx | 1 | 7,957 |
| Vengo | bav | 1 | 7,957 |
| Yocoboué Dida | gud | 1 | 7,957 |
| Bedawiyet | bej | 1 | 7,956 |
| Lala-Bisa | leb | 1 | 7,956 |
| Langi | lag | 1 | 7,956 |
| Makaa | mcp | 1 | 7,956 |
| Nilamba | nim | 1 | 7,956 |
| Ronga | rng | 1 | 7,956 |
| Soli | sby | 1 | 7,956 |
| Tamasheq | taq | 1 | 7,956 |
| Tigon Mbembe | nza | 1 | 7,956 |
| Timne | tem | 1 | 7,956 |
| Zemba | dhm | 1 | 7,956 |
| Asu (Tanzania) | asa | 1 | 7,955 |
| Bamunka | bvm | 1 | 7,955 |
| Bwamu, Láá Láá | bwj | 1 | 7,955 |
| Comorian, Maore | swb | 1 | 7,955 |
| Cuvok | cuv | 1 | 7,955 |
| Doondo | dde | 1 | 7,955 |
| Gavar | gou | 1 | 7,955 |
| Ikoma-Nata-Isenye | ntk | 1 | 7,955 |
| Majang | mpe | 1 | 7,955 |
| Moloko | mlw | 1 | 7,955 |
| Tunen | tvu | 1 | 7,955 |
| Yaouré | yre | 1 | 7,955 |
| Bakoko | bkh | 1 | 7,954 |
| Banda, South Central | lnl | 1 | 7,954 |
| Ghomálá' | bbj | 1 | 7,954 |
| Gor | gqr | 1 | 7,954 |
| Kagulu | kki | 1 | 7,954 |
| Mengaka | xmg | 1 | 7,954 |
| Nawuri | naw | 1 | 7,954 |
| Pinyin | pny | 1 | 7,954 |
| Tera | ttr | 1 | 7,954 |
| Tsaangi | tsa | 1 | 7,954 |
| Eten | etx | 1 | 7,953 |
| Manda (Tanzania) | mgs | 1 | 7,953 |
| Ndo | ndp | 1 | 7,953 |
| Buwal | bhs | 1 | 7,952 |
| Hehe | heh | 1 | 7,952 |
| Ibani | iby | 1 | 7,952 |
| Lega-Mwenga | lgm | 1 | 7,952 |
| Ngungwel | ngz | 1 | 7,952 |
| North Mofu | mfk | 1 | 7,952 |
| Aghem | agq | 1 | 7,951 |
| Dadiya | dbd | 1 | 7,951 |
| Elip | ekm | 1 | 7,951 |
| Ewondo | ewo | 1 | 7,951 |
| Gayil | gyl | 1 | 7,951 |
| Kaonde | kqn | 1 | 7,951 |
| Ngombale | nla | 1 | 7,951 |
| Oshikwambi | kwm | 1 | 7,951 |
| Sagalla | tga | 1 | 7,951 |
| Bongili | bui | 1 | 7,950 |
| C’lela | dri | 1 | 7,950 |
| Ikwere | ikw | 1 | 7,950 |
| Kwaya | kya | 1 | 7,950 |
| Lumun | lmd | 1 | 7,950 |
| Mbudum | xmd | 1 | 7,950 |
| Nambya | nmq | 1 | 7,950 |
| Ngwo | ngn | 1 | 7,950 |
| Songe | sop | 1 | 7,950 |
| Bali (Nigeria) | bcn | 1 | 7,949 |
| Bambalang | bmo | 1 | 7,949 |
| Bekwel | bkw | 1 | 7,949 |
| Bété, Gagnoa | btg | 1 | 7,949 |
| Gabri | gab | 1 | 7,949 |
| Merey | meq | 1 | 7,949 |
| Ncane | ncr | 1 | 7,949 |
| Oku | oku | 1 | 7,949 |
| Sari | asj | 1 | 7,949 |
| Yemba | ybb | 1 | 7,949 |
| Borna | bwo | 1 | 7,948 |
| Bukerebe (Kerebe) | ked | 1 | 7,948 |
| Dinka, Southeastern | dks | 1 | 7,948 |
| Kenyang | ken | 1 | 7,948 |
| Mango | mge | 1 | 7,948 |
| Niellim | nie | 1 | 7,948 |
| Tuki | bag | 1 | 7,948 |
| Vunjo | vun | 1 | 7,948 |
| Ajiri | afo | 1 | 7,947 |
| Bissa | bib | 1 | 7,947 |
| Ivbie North-Okpela-Arhe | atg | 1 | 7,947 |
| Noone | nhu | 1 | 7,947 |
| Yaka | iyx | 1 | 7,947 |
| Yala | yba | 1 | 7,947 |
| Arabic, Algerian | arq | 1 | 7,946 |
| Bu (Kaduna State) | jid | 1 | 7,946 |
| Etkywan | ich | 1 | 7,946 |
| Kako | kkj | 1 | 7,946 |
| Komo | kmw | 1 | 7,946 |
| Miyobe | soy | 1 | 7,946 |
| Mmaala | mmu | 1 | 7,946 |
| Mwan | moa | 1 | 7,946 |
| Ndali | ndh | 1 | 7,946 |
| Ngomba | jgo | 1 | 7,946 |
| Yangben | yav | 1 | 7,946 |
| Bafaw-Balong | bwt | 1 | 7,945 |
| Bete-Bendi | btt | 1 | 7,945 |
| Konni | kma | 1 | 7,945 |
| Ngangam | gng | 1 | 7,945 |
| Zinza | zin | 1 | 7,945 |
| Abron | abr | 1 | 7,944 |
| Bafut | bfd | 1 | 7,944 |
| Eggon | ego | 1 | 7,944 |
| Jibu | jib | 1 | 7,944 |
| Kimré | kqp | 1 | 7,944 |
| Loma (Liberia) | lom | 1 | 7,944 |
| Pana | pnz | 1 | 7,944 |
| Shambala | ksb | 1 | 7,944 |
| Tafi | tcd | 1 | 7,944 |
| Esimbi | ags | 1 | 7,943 |
| Hungworo | nat | 1 | 7,943 |
| Hyam | jab | 1 | 7,943 |
| Lika | lik | 1 | 7,943 |
| Limbum | lmp | 1 | 7,943 |
| Mpumpong | mgg | 1 | 7,943 |
| Vili | vif | 1 | 7,943 |
| Awing | azo | 1 | 7,942 |
| Cibak | ckl | 1 | 7,942 |
| Izere | izr | 1 | 7,942 |
| Mano | mev | 1 | 7,942 |
| Matal | mfh | 1 | 7,942 |
| Mokpwe | bri | 1 | 7,942 |
| Mundani | mnf | 1 | 7,942 |
| Ngando (Democratic Republic of Congo) | nxd | 1 | 7,942 |
| Ninzo | nin | 1 | 7,942 |
| Rendille | rel | 1 | 7,942 |
| Ron | cla | 1 | 7,942 |
| Southern Birifor | biv | 1 | 7,942 |
| Leelau | ldk | 1 | 7,941 |
| Duya | ldb | 1 | 7,940 |
| Dzùùngoo | dnn | 1 | 7,940 |
| Gbaya, Southwest | gso | 1 | 7,940 |
| Gude | gde | 1 | 7,940 |
| Luna | luj | 1 | 7,940 |
| Denya | anv | 1 | 7,939 |
| Fulfulde (Central-Eastern Niger) | fuq | 1 | 7,939 |
| Lame | bma | 1 | 7,939 |
| Matumbi | mgw | 1 | 7,939 |
| Nugunu | yas | 1 | 7,939 |
| Northern Gabri | tng | 1 | 7,938 |
| Cameroon Mambila | mcu | 1 | 7,937 |
| Jola-Kasa | csk | 1 | 7,937 |
| Mumuye | mzm | 1 | 7,937 |
| Muyang | muy | 1 | 7,937 |
| Siwu | akp | 1 | 7,937 |
| Zanaki | zak | 1 | 7,937 |
| Daasanach | dsh | 1 | 7,936 |
| Kenga | kyq | 1 | 7,936 |
| Kera | ker | 1 | 7,936 |
| Mada (Nigeria) | mda | 1 | 7,936 |
| Pular | fuf | 1 | 7,936 |
| Rwa | rwk | 1 | 7,936 |
| Tembo | tbt | 1 | 7,936 |
| Tsogo | tsv | 1 | 7,936 |
| Alladian | ald | 1 | 7,935 |
| Bacama | bcy | 1 | 7,935 |
| Etulo | utr | 1 | 7,935 |
| Kamo | kcq | 1 | 7,935 |
| Malila | mgq | 1 | 7,934 |
| Manya | mzj | 1 | 7,934 |
| Tyap | kcg | 1 | 7,934 |
| Vwanji | wbi | 1 | 7,934 |
| Heiban (Sudan) | hbn | 1 | 7,933 |
| Ndogo | ndz | 1 | 7,933 |
| Noon | snf | 1 | 7,933 |
| Western Krahn | krw | 1 | 7,933 |
| Tharaka | thk | 1 | 7,932 |
| Zulgo-Gemzek | gnd | 1 | 7,932 |
| Delo | ntr | 1 | 7,931 |
| Suba | sxb | 1 | 7,931 |
| Vute | vut | 1 | 7,931 |
| Yambeta | yat | 1 | 7,931 |
| Doyayo | dow | 1 | 7,929 |
| Moba | mfq | 1 | 7,929 |
| Ngemba | nge | 1 | 7,929 |
| Huba | hbb | 1 | 7,928 |
| Kabwa | cwa | 1 | 7,928 |
| Nomaande | lem | 1 | 7,928 |
| Ejagham | etu | 1 | 7,927 |
| Wè Northern | wob | 1 | 7,927 |
| Babanki | bbk | 1 | 7,926 |
| Suba-Simbiti | ssc | 1 | 7,926 |
| Akoose | bss | 1 | 7,925 |
| Burunge | bds | 1 | 7,925 |
| Bété, Daloa | bev | 1 | 7,925 |
| Eastern Karaboro | xrb | 1 | 7,925 |
| Ebrié | ebr | 1 | 7,925 |
| Isu | szv | 1 | 7,925 |
| Jju | kaj | 1 | 7,925 |
| Yamba | yam | 1 | 7,925 |
| Lobala | loq | 1 | 7,923 |
| Mmen | bfm | 1 | 7,923 |
| West-Central Limba | lia | 1 | 7,923 |
| Kabiyè | kbp | 1 | 7,922 |
| Mbuko | mqb | 1 | 7,922 |
| Mukulu | moz | 1 | 7,921 |
| Bum | bmv | 1 | 7,920 |
| Cerma | cme | 1 | 7,920 |
| Giryama | nyf | 1 | 7,920 |
| Kele (Democratic Republic of Congo) | khy | 1 | 7,920 |
| Naro | nhr | 1 | 7,920 |
| Tampulma | tpm | 1 | 7,919 |
| Alaba-K’abeena | alw | 1 | 7,917 |
| Safwa | sbk | 1 | 7,917 |
| Samba Leko | ndi | 1 | 7,917 |
| Dii | dur | 1 | 7,915 |
| Mayogo | mdm | 1 | 7,915 |
| Mende | men | 1 | 7,914 |
| Anufo | cko | 1 | 7,913 |
| Odual | odu | 1 | 7,913 |
| Buamu | box | 1 | 7,912 |
| Lyélé | lee | 1 | 7,912 |
| Saho | ssy | 1 | 7,912 |
| Tuwuli | bov | 1 | 7,912 |
| Xamtanga | xan | 1 | 7,912 |
| Vai | vai | 1 | 7,911 |
| Dan | dnj | 1 | 7,910 |
| Ifè | ife | 1 | 7,910 |
| Migaama | mmy | 1 | 7,910 |
| Dangaléat | daa | 1 | 7,909 |
| Birifor, Malba | bfo | 1 | 7,908 |
| Western Niger Fulfulde | fuh | 1 | 7,908 |
| Shoo-Minda-Nye | bcv | 1 | 7,907 |
| Kuo | xuo | 1 | 7,905 |
| Gikyode | acd | 1 | 7,904 |
| Adioukrou | adj | 1 | 7,902 |
| Basketo | bst | 1 | 7,902 |
| Northern Ngbandi | ngb | 1 | 7,901 |
| Samburu | saq | 1 | 7,901 |
| Sekpele | lip | 1 | 7,900 |
| Tsikimba | kdl | 1 | 7,900 |
| Bana | bcw | 1 | 7,898 |
| Dinka Southwestern | dik | 1 | 7,897 |
| Pokomo | pkb | 1 | 7,895 |
| Kuwaataay | cwt | 1 | 7,894 |
| Paasaal | sig | 1 | 7,894 |
| Southern Nuni | nnw | 1 | 7,893 |
| Hun-Saare | uth | 1 | 7,891 |
| Mampruli | maw | 1 | 7,891 |
| Bandi | bza | 1 | 7,887 |
| Kono (Sierra Leone) | kno | 1 | 7,877 |
| Dan | daf | 1 | 7,876 |
| Kouya | kyf | 1 | 7,875 |
| Plapo Krumen | ktj | 1 | 7,874 |
| Shekkacho | moy | 1 | 7,874 |
| Tepo Krumen | ted | 1 | 7,874 |
| Duruma | dug | 1 | 7,869 |
| Bété, Guiberoua | bet | 1 | 7,860 |
| Koorete | kqy | 1 | 7,852 |
| Kaansa | gna | 1 | 7,834 |
| Luwo | lwo | 1 | 7,814 |
| Nyabwa | nwb | 1 | 7,734 |
| Chumburung | ncu | 1 | 7,687 |
| Ménik | tnr | 1 | 7,681 |
| Karang | kzr | 1 | 7,680 |
| Avokaya | avu | 1 | 7,588 |
| Gola | gol | 1 | 7,243 |
| Ruuli | ruc | 1 | 7,219 |
| Yaka | yaf | 1 | 7,106 |
| Southern Toussian | wib | 1 | 6,987 |
| Karon | krx | 1 | 6,706 |
| Isanzu | isn | 1 | 6,217 |
| Sagala | sbm | 1 | 6,217 |
| Kami | kcu | 1 | 6,216 |
| Lala-Roba | lla | 1 | 6,068 |
| Ndonde Hamba | njd | 1 | 5,960 |
| Suri | suq | 1 | 5,868 |
| Marghi South | mfm | 1 | 5,835 |
| Geji | gyz | 1 | 5,735 |
| Mahou | mxx | 1 | 5,287 |
| ut-Ma’in | gel | 1 | 5,250 |
| Gbanu | gbv | 1 | 5,216 |
| Mono | mnh | 1 | 5,156 |
| Taabwa | tap | 1 | 5,060 |
| Tangale | tan | 1 | 4,886 |
| Verre | ver | 1 | 4,875 |
| Ndrulo | dno | 1 | 4,721 |
| Somrai | sor | 1 | 4,717 |
| Kunda | kdn | 1 | 4,652 |
| Ga’anda | gqa | 1 | 4,186 |
| Glavda | glw | 1 | 3,995 |
| Chala | cll | 1 | 3,907 |
| Abureni | mgj | 1 | 3,889 |
| Cakfem-Mushere | cky | 1 | 3,878 |
| Morokodo | mgc | 1 | 3,827 |
| Jumjum | jum | 1 | 3,801 |
| Neyo | ney | 1 | 3,779 |
| Kenzi Nubian | xnz | 1 | 3,778 |
| Ajiya | idc | 1 | 3,777 |
| Havu | hav | 1 | 3,226 |
| Nyanga | nyj | 1 | 3,192 |
| Tuareg | thv | 1 | 2,803 |
| Kimbu | kiv | 1 | 2,628 |
| Mbugu | mhd | 1 | 2,628 |
| Shama-Sambuga | sqa | 1 | 2,380 |
| Gusilay | gsl | 1 | 2,277 |
| Duupa | dae | 1 | 2,222 |
| Sanga | xsn | 1 | 2,221 |
| Ma’di, Southern | snm | 1 | 2,144 |
| Amba | rwm | 1 | 2,078 |
| Wolof (Gambia) | wof | 1 | 1,968 |
| Sala | shq | 1 | 1,945 |
| Waja | wja | 1 | 1,764 |
| Guduf-Gava | gdf | 1 | 1,749 |
| Hassaniyya | mey | 1 | 1,533 |
| Nyangbo | nyb | 1 | 1,531 |
| Saba | saa | 1 | 1,522 |
| Hanga | hag | 1 | 1,320 |
| Aushi | auh | 1 | 1,226 |
| Bwile | bwc | 1 | 1,226 |
| Basa-Gurmana | buj | 1 | 1,071 |
| Wannu | jub | 1 | 1,071 |
| Lubila | kcc | 1 | 1,068 |
| Bullom So | buy | 1 | 1,066 |

</details>

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

The dataset covers **949 Bible versions across 693 African languages**,
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
