import pygame
from ui.elements import Button
from ui.game_view import GameView

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
FPS = 60

class MainView:
    def __init__(self):

        pygame.init()
        main_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Rytmipeli - Main Menu")

        play_x = (main_surface.get_width() - 200) // 2
        play_y = (main_surface.get_height() - 60) // 2


        play_button = Button(play_x, play_y, 200, 100, "Play", "play")

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if play_button.rect.collidepoint(event.pos):
                            GameView()
                            

            main_surface.fill((255, 255, 255))
            play_button.draw(main_surface)
            pygame.display.update()
        pygame.quit()
