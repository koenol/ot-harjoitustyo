class Player:
    def __init__(self):
        self.score = 0
        self.lives = 3
        self.combo = 0
        self.best_combo = 0
    
    def reset_all(self):
        self.score = 0
        self.lives = 3
        self.combo = 0
        self.best_combo = 0

    def get_score(self):
        return self.score

    def increase_score(self):
        self.score += 1

    def reset_score(self):
        self.score = 0

    def get_lives(self):
        return self.lives

    def decrease_lives(self):
        self.lives -= 1
    
    def reset_live(self):
        self.lives = 1

    def increase_combo(self):
        self.combo += 1

    def reset_combo(self):
        self._save_longest_combo()
        self.combo = 0

    def _save_longest_combo(self):
        if self.combo > self.best_combo:
            self.best_combo = self.combo
    
    def get_current_combo(self):
        return self.combo

    def get_longest_combo(self):
        return self.best_combo