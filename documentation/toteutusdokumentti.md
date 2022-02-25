# Toteutusdokumentti

### Ohjelman yleisrakenne
![](https://github.com/nameisxi/graph-layout-generator/blob/master/documentation/ohjelman-rakenne.png?raw=true)

### Saavutetut aika- ja tilavaativuudet
Olen toteuttanut koodin juuri niinkuin suunnittelinkin ja sanoisin päässeeni tavoite aikavaativuuteen ja tilavaativuuteen koodintarkastelun pohjalta, mutta piirsin sen lisäksi kuvaajat odotetulle, että saavutetulle aikavaativuudelle.

#### Empiirinen aikavaativuus todiste
Kuten alkuperäisesti suunnittelinkin, layout algoritmini aikavaativuus on O(V * (V + E)), jossa V = solmujen lukumäärä ja E = kaarien lukumäärä. Tässä tapauksessa on hyva huomioida, että E = V, sillä verkot joita algoritmille on tarkoitus syöttää eivät sisällä ristiin meneviä kaarien yhteyksiä. Toisin sanottuna, ainoat kaaret joita on olemassa, ovat sellaiset kaaret jotka ovat yhteyksissä lähtöpisteenä toimivan solmun vanhempi-, tai lapsisolmu. Otin tämän oletuksen myös huomioon luodessani seuraavat aikavaativuus kuvaajat, joissa x-akseli kuvaa solmujen lukumäärää ja y-akseli suoritusaikaa:
<br>
<br>
Odotettu aikavaativuuskuvaaja:
<br>
![](https://github.com/nameisxi/graph-layout-generator/blob/master/documentation/performance-testing-expected.png?raw=true)
<br>
<br>
Saavutettu aikavaativuuskuvaaja:
<br>
![](https://github.com/nameisxi/graph-layout-generator/blob/master/documentation/performance-testing-result.png?raw=true)
<br>
<br>
Olen tyytyväinen tuloksiin, vaikka niistä saavutettua kuvaajaa varten olisi ollut parempi kerätä enemmän näytteitä väliltä 10,000 < V < 15,000, jotta kuvaajan kaarevuus olisi tarkempi.

### Puutteet ja parannusehdotukset
Olisin lisännyt muita layout algoritmeja, jos aika olisi riittänyt. Lisäisin myös jonkinlaisen graafisen käyttöliittymän, jossa käyttäjä näkee luodun layoutin ohjelman suorituksen lopuksi.

### Lähteet
- https://scholarworks.rit.edu/cgi/viewcontent.cgi?referer=&httpsredir=1&article=1355&context=theses, sivu 18.
