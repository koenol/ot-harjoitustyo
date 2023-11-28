```mermaid
classDiagram
    index.py --> ui.MainView
    index.py --> database
    ui.MainView --> pygame
    ui.MainView --> ui.elements
    ui.MainView --> services.GameView
    services.GameView --> pygame
```
