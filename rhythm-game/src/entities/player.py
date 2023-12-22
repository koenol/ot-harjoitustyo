class Player:
    '''Luokka, jonka avulla pidetään kirjaa pel9aajan tiedoista

    Attributes:
        score (int): pelaajan pisteet
        lives (int): pelaajan elämät
        combo (int): pelaajan nykyinen combo
        best_combo (int): pelaajan pisin combo pelin aikana
        name (str): pelaajan nimi
        game_state (boolean): pelin tila käynnissä/ei käynnissä
        final_score (int): lopulliset pisteet
    '''
    def __init__(self):
        '''Luokan konstruktori, joka alustaa pelaajan attribuutit'''
        self.score = 0
        self.lives = 3
        self.combo = 0
        self.best_combo = 0
        self.name = ""
        self.game_state = False
        self.final_score = 0

    def calculate_final_score(self):
        '''
        Laskee pelaajan final scoren
        '''
        multiplier = 1 + (self.best_combo / 100)
        self.final_score = int(self.score * multiplier)

    def get_final_score(self):
        '''
        Palauttaa pelaajan final scoren
        '''
        return self.final_score

    def get_name(self):
        '''
        Palauttaa pelaajan nimen
        '''
        return self.name

    def get_game_state(self):
        '''
        Palauttaa pelin tilan
        '''
        return self.game_state

    def set_game_state_start(self):
        '''
        Asettaa pelin tilaksi käynnissä
        '''
        self.game_state = True

    def set_game_state_end(self):
        '''
        Asettaa pelin seis tilaan
        '''
        self.game_state = False

    def get_score(self):
        '''Palauttaa pelaajan nykyisen pistemäärän
        
        Returns:
            score (int): pelaajan pistemäärä
        '''
        return self.score

    def increase_score_normal(self):
        '''Kasvattaa pelaajan pistemäärää 100:lla.'''
        self.score += 100

    def increase_score_perfect(self):
        '''Kasvattaa pelaajan pistemäärää 200:lla'''
        self.score += 200

    def get_lives(self):
        '''Palauttaa pelaajan jäljellä olevat elämät
        
        Returns:
            lives (int): pelaajan jäljellä olevat elämät
        '''
        return self.lives

    def decrease_lives(self):
        '''Vähentää pelaajan jäljellä olevia elämiä yhdellä'''
        self.lives -= 1

    def increase_combo(self):
        '''Kasvattaa pelaajan aktiivista comboa yhdellä'''
        self.combo += 1

    def reset_combo(self):
        '''Tallettaa pelaajan pisimmän combon ja resetoi aktiivisen combon nollaan
    
        '''
        self._save_longest_combo()
        self.combo = 0

    def _save_longest_combo(self):
        '''Tallettaa pelaajan nykyisen combon vanhan pisimmän kombon tilalle jos se on pidempi kuin 
        edellinen
        
        '''
        if self.combo >= self.best_combo:
            self.best_combo = self.combo
    def get_current_combo(self):
        '''Palauttaa pelaajan nykyisen combon
        
        Returns:
            combo (int): pelaajan aktiivinen combo
        '''
        return self.combo

    def get_longest_combo(self):
        '''Palauttaa pelaajan parhaimman combon

        Returns:
            longest_combo (int): pelaajan pisin combo
        '''
        return self.best_combo

    def add_new_nickname(self, nick):
        '''Asettaa pelaajalle nimimerkin'''
        self.name = nick

    def get_rank(self):
        '''
        Palauttaa pelaajan Rankin pisteisiin perustuen
        '''
        max_score = 6250

        if self.final_score >= 0.9 * max_score:
            return 'A'
        if self.final_score >= 0.8 * max_score:
            return 'B'
        if self.final_score >= 0.7 * max_score:
            return 'C'
        return 'D'
    