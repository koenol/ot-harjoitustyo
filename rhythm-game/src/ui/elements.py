import pygame

class Button:
    def __init__(self, x, y, width, height, text, action):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.action = action
        self.color = (246, 246, 246)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        font = pygame.font.Font(None, 24)
        text = font.render(self.text, True, (0,0,0))
        text_rect = text.get_rect(center=self.rect.center)
        screen.blit(text, text_rect)

class Score:
    def __init__(self, x, y, width, height, score):
        self.rect = pygame.Rect(x, y, width, height)
        for x in score:
            self.text = str(x)
        self.color = (255, 255, 255)
    
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        font = pygame.font.Font(None, 24)
        text = font.render(self.text, True, (0,0,0))
        text_rect = text.get_rect(center=self.rect.center)
        screen.blit(text, text_rect)