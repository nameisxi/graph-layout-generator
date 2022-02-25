# Testausdokumentti
## Yksikkötestauksen kattavuusraportti

| Name             | Stmts | Miss | Cover |
|------------------|-------|------|-------|
| radial_layout.py | 48    | 0    | 100%  |
| TOTAL            | 48    | 0    | 100%  |

## Mitä on testattu, miten tämä tehtiin?

Koodissa testaus keskittyy pääasiassa /src/layouts/ kansion sisältöön, silla muu koodi liittyy käytännössa vain käyttöliittymään. Täma kansio sisältää ohjelman layout algoritmit, joita toistaiseksi on vain yksi: radial_layout.py.
<br>
Radial_layout.py jakautuu kahteen osaan:
<br>
1. `radial_positions()` metodi
2. `get_leaf_count()` metodi
<br>
Niitä testataan yksikkötesteillä.
<br>
<br>
Tätä algoritmia on kuitenkin hyvin hankala yksikkötestata, joten sen lisäksi `radial_positions()` ja `get_leaf_count()` komboa testataan kokonaisuutena empiirisillä testeillä, joista tuloksina kuvat dokumentin lopussa.

## Yksikkötestaus
### Syötteet
Ensinnäkin, koska molemmat metodit kuuluvat RadiaLayout objektin alaisuuteen, joka saa syötteena verkon - josta tulee globaali muuttuja -, tulee meidan määritellä esimerkki verkkoja itse metodien syötteiden lisäksi:
<br>

Verkko 1 - tyhjä verkko: 
<br>
{}
<br>

Verkko 2 - matala verkko:
<br>
![](https://github.com/nameisxi/graph-layout-generator/blob/master/documentation/graph2.png?raw=true)
<br>

Verkko 3 - syvä verkko:
<br>
![](https://github.com/nameisxi/graph-layout-generator/blob/master/documentation/graph3.png?raw=true)
<br>

#### radial_positions() metodin syötteet
`radial_positions()` metodia testataan toistaiseksi kolmella edellä mainitulla verkolla, jotka tämä metodi saa samaan objektiin kuuluvalta konstruktorilta.

#### get_leaf_count() metodin syötteet
`get_leaf_count()` metodia testataan toistaiseksi seuraavanlaisilla syötteillä:

- Verkko 1: tyhjä solmu
- Verkko 2: Verkko 2:n juuri solmu
- Verkko 3: Verkko 3:n juuri solmu ja verkko 3:n solmu 2.1

### Yksikkötestien toisto
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
## Empiirinen testaus
Ohjelman empiirinen testaus tarkoittaa käytännössä RadialLayout objektin `get_coordinates()` metodin ja `get_leaf_count()` metodin samanaikaista testausta.
<br>
### Syötteet

| Verkko   | Syvyys | Lapsisolmuja per solmu | Solmuja yhteensä |
|----------|--------|------------------------|------------------|
| Verkko 1 | 0      | 0                      | 0                |
| Verkko 2 | 1      | 3                      | 4                |
| Verkko 3 | 3      | 1-3                    | 13               |
| Verkko 4 | 5      | 3                      | 364              |
| Verkko 5 | 10     | 3                      | 88572            |
| Verkko 6 | 5      | 5                      | 3905             |
### Tulokset
#### Verkko 1:
![](https://github.com/nameisxi/graph-layout-generator/blob/master/documentation/graph1-empirical.png?raw=true)
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
### Empiiristen testien toisto
Samat visualisaatiot voi toistaa käyttämällä projektin juuressa olevaa `prototyping.ipynb` notebookkia, jota käytin myös algoritmin prototyyping kehitykseen. Se on kuitenkin lisätty bonuksena, enkä suunnitellut sitä muiden käytettäväksi, joten se ei ole dokumentoitu.

<br>
N-syvyisen verkon jolla on N-lapsisolmua per solmu voi generoida muuntamalla muuttujien `n_levels` ja `n_children` arvot. 
<br>
Esimerkkinä seuraavat arvot generoivat empiirisen esimerkin Verkko 2:
<br>
```python
n_levels = 1
n_children = 3
```
<br>

