**Tam tikromis ligomis sergančių suaugusių (18 metų ir vyresnių) asmenų duomenų analizė**

Paruošėme savo baigiamąjį projektą Vilnius Coding School mokykloje.

Projekto tema: Tam tikromis ligomis sergančių suaugusiųjų (18 metų ir vyresnių) asmenų duomenų analizė.

Pagrindinis projekto tikslas – išsiaiškinti tam tikrų ligų tendenciją Lietuvoje penkių metų laikotarpyje, išsiaiškint, kurios ligos pasitaiko dažniausiai ir rečiausiai, palyginti sergamumo skirtumus tarp moterų ir vyrų.

Šiam projektui naudojame Python kalbą. Analizė daroma iš mūsų pačių sukurtų CSV failų.

**scrap.py**

Naudojamos bibliotekos: Selenium, Webdriver_manager.chrome, Pandas.

Žingsniai:

1. Susirandame mums reikalingus duomenis, URL: <https://osp.stat.gov.lt/lt/statistiniu-rodikliu-analize?hash=4b9681f1-aa53-47ad-832b-ef4b56eb3a22>
1. Su Selenium pagalba, įsikeliame mūsų norimos lentelės reikšmes.
1. Sukuriame CSV failą su duomenimis.

**pavadininimų screipinimas.py**

Naudojamos bibliotekos: Selenium, Pandas.

Žingsniai:

1. Susirandame mums reikalingus duomenis, URL: <https://osp.stat.gov.lt/lt/statistiniu-rodikliu-analize?hash=4b9681f1-aa53-47ad-832b-ef4b56eb3a22>
1. Su Selenium pagalba, įsikeliame mūsų norimos lentelės reikšmių pavadinimus.
1. Sukuriame CSV failą su duomenimis.

**scrap\_tvarkymas.py**

Naudojama biblioteka: Pandas

Žingsniai:

1. Pilnai sutvarkome duomenų reikšmes ir pašaliname nereikalingus stulpelius bei eilutes.
1. Sukuriame tvarkingą CSV failą su 2018-2022 susirgimų duomenimis.

**pavadinimai\_tvarkymas.py**

Naudojama biblioteka: Pandas

1. Pilnai sutvarkome pavadinimus ir pašaliname nereikalingus stulpelius bei eilutes.
1. Sukuriame tvarkingą CSV failą su 2018-2022 susirgimų pavadinimais.
1. Apjungiame mūsų 2 sukurtus CSV failus į vieną bendrą CSV – ligų pavadinimai ir 2018-2022 sergančiųjų skaičiai.

**csv\_failu\_tvarkymas.py**

Naudojama biblioteka: Pandas

1. Mūsų bendrą lentelę išskirstome į 3 atskiras lenteles: Vyrų ir moterų susirgimų skaičiai bendrai, vyrų susirgimai ir moterų susirgimai.
1. Pašaliname iš visų lentelių nulines reikšmes.
1. Apskaičiuojame sergamumų tam tikromis ligomis 2018-2022 metais vidurkius.

**final\_project.py**

Naudojamos bibliotekos: Matplotlib, Pandas.

Šiame faile yra atliekama mūsų duomenų analizė.

Žingsniai:

1. Sudarome pasirinkimų meniu, kuriame įvedus savo pasirinkimą, yra matoma tam tikra informacija.
1. Pasirinkus 1 matome 5 dažniausiai pasitaikančias ligas tarp vyrų ir moterų.
1. Pasirinkus 2 matome 5 rečiausiai pasitaikančias ligas tarp vyrų ir moterų.
1. Pasirinkus 3 matome grafiką, kuris parodo, koks yra penkių metų laikotarpio vidutinis sergamumas tam tikromis ligomis tarp vyrų ir moterų. 



![myplot3](https://github.com/PaulDavis04/Final-project/assets/149395819/3046b157-cc5d-40e1-8048-40651f0b4168)








1. Pasirinkus 4 matome grafiką, kuris parodo tris dažniausiai ir tris rečiausiai pasitaikančias ligas tarp vyrų.
![myplot4](https://github.com/PaulDavis04/Final-project/assets/149395819/4976f3f6-b14e-44d8-93f7-04ffd5bed165)

1. Pasirinkus 5 matome grafiką, kuris parodo tris dažniausiai ir tris rečiausiai pasitaikančias ligas tarp moterų.

![myplot5](https://github.com/PaulDavis04/Final-project/assets/149395819/43a33391-995a-48e6-ba61-60c2e2b70dd9)

1. Pasirinkus 6 matome grafiką, kuris parodo susirgimų vidurkius per 2018-2022 metus: viena kreivė rodo vyrų susirgimus, kita kreivė – moterų.
![myplot6](https://github.com/PaulDavis04/Final-project/assets/149395819/5c121eff-4f1f-4384-9214-753a75a19d9f)


1. Pasirinkus 7, galite išeiti iš meniu.

**IŠVADOS**

Kad ir kaip būtų liūdna, pagal susirgimų statistiką matome, kad, greičiausiai, kas antras žmogus, gyvenantis Lietuvoje, serga tam tikra liga. Sergančiųjų skaičiai tikrai yra dideli. Iš mūsų padarytos analizės matome, kad tarp vyrų ir moterų rečiausiai pasitaiko tos pačios ligos, tačiau prie dominuojančių yra tam tikri skirtumai (endokrininės sistemos ir medžiagų apykaitos ligos įeina į moterų TOP3, o kvėpavimo sistemos ligos – į vyrų TOP3.). Taip pat, praktiškai visomis ligomis moterys serga dažniau negu vyrai. Be to, panagrinėjus 2018-2022 metų duomenis, net plika akimi yra matoma daugumos ligų auganti tendencija. Todėl svarbu saugoti tiek save – laikytis miego režimo, sportuoti, sveikai maitintis, tiek savo aplinką – neteršti gamtos ir stengtis gyventi ekologiškiau.








