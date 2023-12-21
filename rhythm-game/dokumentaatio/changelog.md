## Viikko3

-   Pelin ensimmäinen aloitusnäkymä luotu (index.py)
-   Lisätty elementti-luokka joka sisältää pelin elementtejä (elements.py)
-   Pelaaja pystyy käynnistämään pelin alkuvalikon ja ruudulle renderöityy Play-button (ei varsinaista toiminallisuutta vielä)
-   Tietokanta yhteys alustettu (vain yhteyden luonti testattu)

## Viikko4

-   main_view refraktorointia, high-score testidata poistettu käytöstä toistaiseksi
-   resoluutio vaihto 1024x768 > 800x600
-   pelaaja pystyy käynnistämään nyt uuden näkymän play-painikkeesta (game_view), mutta ei vielä pysty pelaamaan (ruksista pelaaja palaa toistaiseksi alkuvalikkoon)
-   alkuvalikkoon lisättiin pelin banneri
-   lisättiin game_view taustamusiikki
-   muokattiin bgm-väriä vähemmän silmiä rasittavaks: white (255, 255, 255) -> white smoke (246, 246, 246)

## Viikko5

-   Lisättiin satunnaisesti spawnaavat sound-blockit
-   Pelaaja pystyy kontrolloimaan player_buttoneita näppäimillä (A,S,D)
-   Pelaaja pystyy keräämään pisteitä ajoittamalla player_button painikkeen sound-blockin kanssa

## Viikko6

-   Pelaaja meneillä olevasta combosta pidetään kirjaa
-   Peli päättyy jos pelaaja missaa 3 sound-blockkia
-   Pelaajalle esitetään pelin tulos sen päätyttyä (Score + Longest Combo)

