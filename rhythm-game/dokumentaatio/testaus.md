### Testauskattavuus

Ohjelmalta löytyy riittävät unit-testit player.py luokalle.

<img src="https://github.com/koenol/ot-harjoitustyo/blob/main/rhythm-game/dokumentaatio/kuvat/coverage_report.png" width="750">


### Parannettavaa testauksessa

Testauksesta jäänyt paljon testaamatta:
- Tietokantayhteydet ja toiminnot
- pygame-toimintoja view.py näkymästä, ohjelman refaktorointi jäi kesken eikä GameView ja ResultView keretty erottelemaan MainView tasolle joka vaikeutti testien tekoa
