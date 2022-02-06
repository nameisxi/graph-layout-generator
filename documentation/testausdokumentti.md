# Testausdokumentti
### Yksikkötestauksen kattavuusraportti

| Name             | Stmts | Miss | Cover |
|------------------|-------|------|-------|
| radial_layout.py | 48    | 0    | 100%  |
| TOTAL            | 48    | 0    | 100%  |

### Mitä on testattu, miten tämä tehtiin?

Koodissa testaus käsittyy pääasiassa /src/layouts/ kansion sisältöön, silla muu koodi liittyy käytännössa käyttöliittymään. Täma kansio sisältää ohjelman layout algoritmit, joita toistaiseksi on vain yksi: radial_layout.py.
<br>
Radial_layout.py jakautuu kahteen osaan:
<br>
1. radial_positions() metodi
2. get_leaf_count() metodi
<br>
Niitä testataan yksikkötesteillä.

### Minkälaisilla syötteillä testaus tehtiin?
Toistaiseksi testausta on tehty seuraavanlaisilla syötteillä:
<br>
Ensinnäkin, koska molemmat metodit kuuluvat RadiaLayout objektin alaisuuteen - joka saa syötteena verkon, josta tulee globaali muuttuja - tulee meidan määritellä esimerkki verkkoja itse metodien syötteiden lisäksi:
<br>

Verkko 1 - tyhjä verkko: 
<br>
{}
<br>

Verkko 2 - matala (shallow) verkko:
<br>
Verkko 3 - syvä verkko:

### Miten testit voidaan toistaa?
### Ohjelman toiminnan empiirisen testauksen tulosten esittäminen graafisessa muodossa.
