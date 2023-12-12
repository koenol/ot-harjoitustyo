## pakkauskaavio (alustava)
```mermaid
graph TD;
    index.py --> ui.UI;
    index.py --> database;
    UI --> pygame;
    UI --> entities.player.Player
    UI --> ui.elements
    UI --> ui.view --> GameView;
    UI --> ui.view --> MainView;
    UI --> ui.view --> ResultView
```

## sekvenssikaaivo (alustava)
```mermaid
sequenceDiagram
    participant main
    participant db
    participant ui
    participant mainView
    participant gameView
    participant resultView

    main ->> db: Init DB
    db -->> main: DB Init
    main ->> ui: Create UI
    ui -->> main: UI
    main ->> ui: Show Main View
    ui ->> mainView: Init Main View
    mainView -->> ui: Main View Initialized
    loop Game Loop
        ui ->> gameView: Show Game View
        gameView -->> ui: End Game
    end
    ui ->> resultView: Show Result View
    resultView ->> ui: Exit Result View
    ui ->> main: Exit Main View
```

## Päätoiminnallisuus

1. Pelaajalle näytetään aluksi "Main View"-näkymä.
2. Pelaajalle luodaan Player-olio, joka pitää kirjaa pelaajan pelitiedoista (elämät, pisteet, nykyinen combo, pisin combo).
3. Kun pelaaja käynnistää pelin "Play"-painikkeesta, pelaaja siirtyy "Game View"-näkymään, jonka aikana pelaajan tulee osua mahdollisimman moneen sound-block pelin aikana ennen kuin elämät loppuvat (alustavasti 3 elämää)
4. Pelin aikana pelaaja näkee pisteensä vasemmasta yläkulmasta ja pisimmän combonsa
5. Kun pelaajan elämät loppuvat pelaajalle näytetään "Result View", josta pelaaja näkee pistetuloksensa.
6. Kun pelaaja sulkee ikkunan ohjelma palaa "Main View"-näkymään ja pelaajan tilastot nollataan.
7. Pelaaja pystyy nyt käynnistymään uuden pelin tai lopettamaan ohjelman oikeasta yläkulmasta.

