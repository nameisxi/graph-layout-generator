# Viikkoraportti 4

### Työaika
6h. Olin hyvin kiireinen tällä viikolla, mutta tulen käyttämään projektin edistämiseen huomattavasti enemmän aikaa tulevana viikkona.

### Mitä olen tehnyt tällä viikolla?
Kirjoittanut dokumentaatiota, päivittänyt testausdokumenttia empiirisillä todisteilla, tutkinut dict/hashmap/hashtable implementaatioita, aloittanut toteutusraporttia, aloittanut oman dict tietorakenteen toteutusta ja testausta.

### Miten ohjelma on edistynyt?
Ohjelman ydintoiminta on valmis ja olen keskittynyt tietorakenteiden toteutukseen, sekä testaukseen.

### Mitä opin tällä viikolla / tänään?
Dictionary ja hashmappien toteutusta hashtaulujen avulla.

### Mikä jäi epäselväksi tai on tuottanut vaikeuksia?
1. Voiko Pythonin toteuttamaa dict objektia käyttää siinä määrin, että sen ottaa vastaan standardikirjaston tiedostonluku metodilta, mutta se sen jälkeen muunnetaan suoraan omaksi tietorakenteekseen? Joudun käyttämään Pythonin standardikirjaston pakettia nimeltä json ja sen metodia json.loads(), joka lukee JSON tiedoston ja palauttaa sen dictionary objektina. Tarkoituksenani on muuntaa palautettu dict objekti välittömästi itseni toteuttamaksi tietorakenteeksi seuraavanlaisesti:

```python
graph = json.loads(file_path)
graph = dict_to_dictionary(graph) # dictionary on oma vastineeni Pythonin dict objektille
```

2. Tarkoitettiinko viikko 4 ohjeen "Aloitettu suorituskyky- tai muu aiheeseen sopiva testaus (kirjoita näistä testausdokumenttiin)." yleistä testausta jota tira labran dokumentaatio sivun testausdokumentin kohdalla kutsuttiin "Mitä on testattu, miten tämä tehtiin?" osioksi?

### Mitä teen seuraavaksi?
Viimeistelen tietorakenteet, niiden testauksen, layout-algoritmin satunnaisesti generoidut testit, sekä jatkan toteutusdokumentin kirjoittamista.
