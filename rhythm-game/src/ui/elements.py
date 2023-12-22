import pygame

class Button:
    def __init__(self, x, y, width, height, text, action):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.action = action
        self.color = (246, 246, 246)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        pygame.draw.rect(screen, (0, 0, 0), self.rect, 3)
        font = pygame.font.Font(None, 24)
        text = font.render(self.text, True, (0, 0, 0))
        text_rect = text.get_rect(center=self.rect.center)
        screen.blit(text, text_rect)

class MainViewElements:
    @staticmethod
    def display_elements(screen, width, height, highscores):
        play_x = (width - 100) // 2
        play_y = height // 2

        banner_font = pygame.font.Font("src/static/RapunledRegular-axZLJ.otf", 32)
        banner_text = banner_font.render("Rhythm Game", True, (0, 0, 0))
        banner_text_rect = banner_text.get_rect()
        banner_text_rect.center = (width // 2 + 100, height // 2 - 150)

        highscore_font = pygame.font.SysFont("gabriola", 24)
        play_button = Button(play_x, play_y, 100, 50, "Play", "play")
        
        screen.fill((246, 246, 246))
        y_position = 10
        for position, (name, score) in enumerate(highscores, start=1):
            text = f"{position}. {name} | Score: {score}"
            score_text = highscore_font.render(text, True, (0, 0, 0), (246, 246, 246))
            screen.blit(score_text, (10, y_position))
            y_position += 24

        screen.blit(banner_text, banner_text_rect)
        play_button.draw(screen)