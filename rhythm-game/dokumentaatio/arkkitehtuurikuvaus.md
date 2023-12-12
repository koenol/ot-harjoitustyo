## pakkauskaavio (alustava / tämän hetkinen)
```mermaid
graph TD;
    index.py --> UI;
    index.py --> database;
    UI --> pygame;
    UI --> Player
    UI --> elements
    UI --> View --> GameView;
    UI --> View --> MainView;
    UI --> View --> ResultView
```
