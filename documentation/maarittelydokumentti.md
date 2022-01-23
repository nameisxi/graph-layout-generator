# Määrittelydokumentti

### Ohjelmointikieli
Projektin käyttäma ohjelmointikieli on Python 3. Pystyn vertaisarvioimaan Pythonilla, Javalla, sekä Javascriptillä toteutettuja projekteja.

### Käytetyt algoritmit & tietorakenteet
Aikeenani on toteuttaa Andrew Pavlovin radial graph layout algoritmi, radial positions, hyödyntämällä Pythonin lista ja dictionary tietorakenteita. Lisää mainitusta algoritmista sivulla 18: https://scholarworks.rit.edu/cgi/viewcontent.cgi?referer=&httpsredir=1&article=1355&context=theses.

### Ongelman määrittely
Haluan luoda ohjelman joka laskee annetun verkon solmuille koordinaatit, eli toinsin sanottuna, haluan luoda verkon asetelma generaattorin.
Valitsin erityisesti radiaali asetelman, koska se on minusta verkkojen asetelmista kiinnostavin, mutta myös koska minulla ei luultavasti
riitä aikaa implementoida muita asetelma algoritmeja. Valitsin erityisesti Andrew Pavlovin radial positions algoritmin tuottamaan täman radiaali
asetelman, sillä se oli ainut radiaali asetelma algoritmi jonka löysin ja joka ei ollut uskomattoman monimutkainen.
Mitä taas ohjelman tietorakenteisiin tulee, niin valitsin Pythonin dictionaryn siita syystä, että se muistuttaa hyvin läheisesti JSONia, jonka ohjelma 
vastaanottaa syötteenä, jolla on myös hyvin helppoa määritellä verkon rakenne. Listaa puolestaan joudun käyttämään solmujen säilytyksen kannalta, eikä
silla oli projektin kannalta suurempaa roolia.

### Syötteet ja niiden kayttö
Ohjelman on tarkoituksena saada syötteenä JSON muotoinen verkko, jonka solmuille koordinaatit lasketaan.

### Tavoite aika- ja tilavaativuudet
Tavoite aikavaativuuteni on O(V * (V + E)) ja tavoite tilavaativuuteni on O((V - len(V.children) == 0) * V), olettaen, että verkolla on V solmua ja E kaarta. 

### Lähteet
https://scholarworks.rit.edu/cgi/viewcontent.cgi?referer=&httpsredir=1&article=1355&context=theses, sivu 18.

### Opinto-ohjelma
Tietojenkäsittelytieteen kandidaatti (TKT).

### Kielivalinnat
Toteutan dokumentaation suomenkielellä, mutta koodin muuttujien, että kommenttien kielenä toimii englanninkieli.
