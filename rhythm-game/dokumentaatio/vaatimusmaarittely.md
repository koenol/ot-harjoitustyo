## Vaatimusmäärittely

### Sovelluksen tarkoitus

Sovelluksena toimii perinteinen rytmipeli jossa pelaajan tavoitteena on painaa näppäimiä sovelluksen esittämässä järjestyksessä. Pelissä kerätään pisteitä ja pelaajan 10 parasta tulosta tallennetaan
ja esitetään pelin etusivulla.

### Käyttäjät

Jokainen pelisessio on uniikki. Pelisessiosta tallennetaan vain pistetulokset ja pelaajan antama nimimerkki jos ne saavuttavat top 10 listan. Myöhemmin sovellukseen saatetaan lisätä pelaajan kustomoidut
konfiguraatio-asetukset (kts. Jatkokehitysideoita)

### Käyttöliittymäluonnos

Sovellus koostuu alustavasti kolmesta eri näkymästä (v1).

<img src="https://github.com/koenol/ot-harjoitustyo/blob/main/rhythm-game/dokumentaatio/kuvat/kayttoliittyma-hahmotelma-v1.png" width="750">

Sovellus aukeaa main-näkymään jossa pelaaja näkee parhaat tulokset. Pelaaja pystyy aloittamaan uuden pelin painamalla "Play" näppäintä, jonka jälkeen sovellus siirtyy game-näkymään, joka aloittaa pelin. Kun peli päättyy
näkymä vaihtuu result-näkymään josta pelaaja näkee tuloksen ja antamaan nimimerkin (huom. alustava suunnitelmassa jos tulos ei yllä top10 listalle niin tulosta tai nimeä ei tallenneta mihinkään, muita vaihtoehtoja näkymälle kts. Jatkokehitysideoita).
Tämän jälkeen näkymä palaa main-näkymään.

### Perusversion tarjoama toiminnallisuus

## Ennen pelaamista

-   Pelaaja pystyy tarkastelemaan top10 tuloksia | TEHTY |
    -   Tulos sisältää tuloksen ja pelaajan nimimerkin | TEHTY |
-   Pelaaja pystyy aloittamaan uuden pelin päävalikosta | TEHTY |
    -   Peli käynnistyy Play nappulasta | TEHTY |

## Pelin aikana

-   Pelaajan tavoitteena on painaa näppäimiä sovelluksen esittämässä järjestyksessä kun hit block osuu kohdalle. | TEHTY |
    -   Alustavat näppäimet ovat vasemmalta oikealla "A, S, D" | TEHTY |
    -   Hit blockit putoavat ylhäältä alas | TEHTY |
-   Pelaaja näkee tuloksensa vasemmasta yläkulmasta | TEHTY |
    -   Hit blockkeihin osuminen kasvattaa pisteitä | TEHTY |
    -   Combo pitää kirjaa siitä kuinka moneen hit blockkiin pelaaja on osunut jaksossa. | TEHTY |
-   Pelillä on taustamusiikki | TEHTY |

## Pelin päättyminen

-   Kun peli päättyy pelaajalle esitetään pelin tulos | TEHTY |
    -   Peli siirtyy result-näkymään | TEHTY |
    -   Pelaajalle näytetään pelin lopputulos, pisin combo, rank ja mahdolliset multiplierit | TEHTY |
-   Pelaajalta pyydetään nimimerkki jos se yltää top10 tulokseen | TEHTY |
    - Pelimerkin maksimipituus: 3 merkkiä | TEHTY |
-   Pelin tiedot tallennetaan | TEHTY |
    -   Nimimerkki ja tulos tallennetaan top10 tilastoihin vain jos tulos on tarpeeksi hyvä | TEHTY |

### Jatkokehitysideoita

Perusversion jälkeen peliin on suunnitteilla lisätoimintoja jotka parantavat pelaajan pelikokemusta (ei tärkeysjärjestyksessä):

-   Setttings-näkymä, josta pelaaja pystyy muokkaamaan peliasetuksia esim. vaihtamaan pelinäppäimet
-   Pelaajan konfiguraatio-asetukset voidaan tallentaan tekstitiedostoon ja ladata tarvittaessa
-   Lisätään settingseihin offset/timing calibration
-   Muutetaan result-näkymä huomioimaan top10 tulokset erikseen normaalista näkymästä
-   Parannetaan pelielementtejä
    -   Pelielementteihin osuma-efektejä | TEHTY |
    -   Score multipliers | TEHTY |
