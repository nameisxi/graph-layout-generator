# Käyttöohje
## Ohjelman suoritus
Kun olet projektin juuressa, navigoi `/src` kansioon:
<br>

```bash
cd src/
```

<br>
Seuraavaksi, suorita main.py tiedosto seuraavanlaisesti:
<br>

```bash
python3 main.py
```

Seuraavaksi, seuraa käyttöliittymän ohjeistusta ja siinä kaikki. Tätä ohjelmaa varten ei tarvita kolmannen osapuolen kirjastoja tai muuta vastaavaa.

## Minkä muotoisia syötteitä ohjelma hyväksyy

Ohjelma tulee kysymään käytettävän verkon polkua, jonka voit antaa absoluuttisena, kuin myös suhteellisena, esim: `./verkko.json`, `../../verkko.json`, jne., mutta voit myös halutettasi painaa `Enter`:iä käyttääksesi esimerkki verkkoa, joka löytyy jo projectin `src/` kansiosta. 

<br>
Jos käytät omaa verkkoa, tulee sen sijaita JSON tiedostossa seuraten seuraavanlaista schemaa:

```json
{
    "root": { 
        "id": "root",
        "depth": 0,
        "parent": null,
        "children": [
            {
                "id": "child_1",
                "depth": 1,
                "parent": "root"
            },
        ]
    },
    "child_1": { 
        "id": "child_1",
        "depth": 1,
        "parent": "root",
        "children": [
            {
                "id": "child_1.1",
                "depth": 2,
                "parent": "child_1"
            },
        ]
    }
}
```
