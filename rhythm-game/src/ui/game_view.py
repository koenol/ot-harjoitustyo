import pygame

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
FPS = 60
class GameView:
    def __init__(self):
            pygame.init()
            game_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
            pygame.display.set_caption("Rytmipeli - Game")

            running = True
            while running:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False

                game_surface.fill((255, 255, 255))
                pygame.display.update()
            