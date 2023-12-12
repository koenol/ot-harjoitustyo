class Player:
    def __init__(self):
        self.score = 0
        self.lives = 3
    
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
        self.lives = 3
