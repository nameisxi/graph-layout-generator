# Testausdokumentti
### Yksikkötestauksen kattavuusraportti

| Name             | Stmts | Miss | Cover |
|------------------|-------|------|-------|
| radial_layout.py | 48    | 0    | 100%  |
| TOTAL            | 48    | 0    | 100%  |

### Mitä on testattu, miten tämä tehtiin?

Koodissa testaus keskittyy pääasiassa /src/layouts/ kansion sisältöön, silla muu koodi liittyy käytännössa vain käyttöliittymään. Täma kansio sisältää ohjelman layout algoritmit, joita toistaiseksi on vain yksi: radial_layout.py.
<br>
Radial_layout.py jakautuu kahteen osaan:
<br>
1. radial_positions() metodi
2. get_leaf_count() metodi
<br>
Niitä testataan yksikkötesteillä.

### Minkälaisilla syötteillä testaus tehtiin?
Ensinnäkin, koska molemmat metodit kuuluvat RadiaLayout objektin alaisuuteen - joka saa syötteena verkon, josta tulee globaali muuttuja - tulee meidan määritellä esimerkki verkkoja itse metodien syötteiden lisäksi:
<br>

Verkko 1 - tyhjä verkko: 
<br>
{}
<br>

Verkko 2 - matala (shallow) verkko:
<br>
![](https://github.com/nameisxi/graph-layout-generator/blob/master/documentation/graph2.png?raw=true)
<br>

Verkko 3 - syvä verkko:
<br>
![](https://github.com/nameisxi/graph-layout-generator/blob/master/documentation/graph3.png?raw=true)
<br>

#### radial_positions() metodin syötteet
Radial_positions() metodia testataan toistaiseksi kolmella edellä mainitulla verkolla.

#### get_leaf_count() metodin syötteet:
Get_leaf_count() metodia testataan toistaiseksi seuraavanlaisilla syötteillä:

- Verkko 1: tyhjä solmu
- Verkko 2: Verkko 2:n juuri solmu
- Verkko 3: Verkko 3:n juuri solmu ja verkko 3:n solmu 2.1

### Miten testit voidaan toistaa?
Kaikki testit voidaan toistaa navigoimalla /src/layouts/ kansioon ja ajamalle seuraava komento:
<br>
```bash
> python3 -m unittest discover
```
<br>

Yksittäiset testit voidaan toistaa ajamalla /src/layouts/ kansion "test" nimellä alkavat tiedostot. Pythonissa on tapana nimeta testit siten, että testattavan tiedoston nimen eteen lisätään "test" etuliite.
<br>
<br>
Esimerkki:
<br>
```bash
> python3 test_radial_layout.py
```
### Ohjelman toiminnan empiirisen testauksen tulosten esittäminen graafisessa muodossa.
Ohjelman empiirinen testaus tarkoittaa käytännössä RadialLayout objektin get_coordinates() metodin testausta.
<br>
Tässä graafiset tulokset edellä mainituille esimerkkitesteille käyttäen verkkoja 2 ja 3 (verkko 1 on tyhjä, eikä algoritmi täten palauta sen olemattomille solmuille koordinaatteja), sekä lisäksi muita isompia verkkoja joita ei yksikkötestauksella voi testata:
#### Verkko 2:
![](https://github.com/nameisxi/graph-layout-generator/blob/master/documentation/graph2-empirical.png?raw=true)
#### Verkko 3:
![](https://github.com/nameisxi/graph-layout-generator/blob/master/documentation/graph3-empirical.png?raw=true)
#### Verkko 4:
![](https://github.com/nameisxi/graph-layout-generator/blob/master/documentation/graph4-empirical.png?raw=true)
#### Verkko 5:
![](https://github.com/nameisxi/graph-layout-generator/blob/master/documentation/graph5-empirical.png?raw=true)
#### Verkko 6:
![](https://github.com/nameisxi/graph-layout-generator/blob/master/documentation/graph6-empirical.png?raw=true)
