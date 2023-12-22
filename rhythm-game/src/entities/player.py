class Player:
    '''Luokka, jonka avulla pidetään kirjaa pelaajan tiedoista

    Attributes:
        score (int): pelaajan pisteet
        lives (int): pelaajan elämät
        combo (int): pelaajan nykyinen combo
        best_combo (int): pelaajan pisin combo pelin aikana
    '''
    def __init__(self):
        '''Luokan konstruktori, joka alustaa pelaajan attribuutit'''
        self.score = 0
        self.lives = 2
        self.combo = 0
        self.best_combo = 0
        self.name = "ABC"
        self.game_state = False
        self.final_score = 0

    def set_final_score(self, score):
        self.final_score = score

    def get_final_score(self):
        return self.final_score

    def get_name(self):
        return self.name

    def get_game_state(self):
        return self.game_state

    def set_game_state_start(self):
        self.game_state = True

    def set_game_state_end(self):
        self.game_state = False

    def get_score(self):
        '''Palauttaa pelaajan nykyisen pistemäärän
        
        Returns:
            score (int): pelaajan pistemäärä
        '''
        return self.score

    def increase_score_normal(self):
        '''Kasvattaa pelaajan pistemäärää yhdellä.'''
        self.score += 100

    def increase_score_perfect(self):
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
        self.name = nick

    def get_rank(self, score):
        max_score = 2200

        if score >= 0.9 * max_score:
            return 'A'
        if score >= 0.8 * max_score:
            return 'B'
        if score >= 0.75 * max_score:
            return 'C'
        return 'D'
    