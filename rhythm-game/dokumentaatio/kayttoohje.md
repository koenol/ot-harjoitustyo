## Ohjelman käynnistäminen

Asenna riippuvuudet komennolla:

```bash
poetry install
```

Käynnistä ohjelma komennolla:

```
poetry run invoke start
```

## Peliohjeet

### Alkunäkymä
Ekaa kertaa peliä käynnistäessä pelaajalle näytetään alkunäkymä, josta pelaaja voi käynnistää pelin.
- Jos pelaaja on aikaisemmin pelannut hän näkee myös top10 tulokset

### Pelin aloitus
Pelaaja pystyy käynnistämään pelin 'Play'-painikkeesta.
- Pelaaja kontrollit vasemmalta oikealla: A, S, D
- Pelaajan pitää yrittää soundblockkeihin, mitä tarkemmin pelaaja osuu sitä enemän pisteitä
- Pelaajan kannattaa kerätä mahdollisimman hyvä combo saadakseen enemmän pisteitä

### Pelin päätös
Peli päättyy jos pelaaja pääsee pelin loppuun tai häneltä loppuvat elämät (3 elämää). Pelaaja pystyy myös keskeyttämään pelin 'x' painikkeesta.
- Pelaajalle näytetään pelin lopputulos
- Final score muodostuu kaavalla: Scoren ja Parhaimman kombon yhteistuloksesta (Score * 1.longest_combo, esim: score * 1.15)
- Jos pelaajan tulos on suurempi kuin nolla ja se yltää top10 listalle se rekisteröidään jos pelaaja antaa 3-merkkisen nimimerkin
- Pelaajalle näytetään myös Rank (A, B, C, D) saatuun pistemäärään perustuen
