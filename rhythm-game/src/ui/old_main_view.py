import pygame
from ui.elements import Button
from services.game_view import GameView
from ui.view import *

#WINDOW_WIDTH = 800
#WINDOW_HEIGHT = 600
#FPS = 60


class MainView:
    def __init__(self):

        pygame.init()
        test = TestMainView()
        #main_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        #pygame.display.set_caption("Rytmipeli - Main Menu")

        #play_x = (main_surface.get_width() - 200) // 2
        #play_y = (main_surface.get_height() - 60) // 2
        play_x = (test.get_width() - 200) // 2
        play_y = (test.get_height() - 60) // 2

        # refractor this to elements
        banner_font = pygame.font.Font("src/static/RapunledRegular-axZLJ.otf", 32)
        banner_text = banner_font.render("Rhythm Game", True, (0, 0, 0))
        banner_text_rect = banner_text.get_rect()
        #banner_text_rect.center = (WINDOW_WIDTH//2 + 100, WINDOW_HEIGHT//2 - 200)
        banner_text_rect.center = (test.get_width() //2 + 100, test.get_height() //2 - 200)


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

            #main_surface.fill((246, 246, 246))
            #main_surface.blit(banner_text, banner_text_rect)
            #play_button.draw(main_surface)
            test.screen.fill((246, 246, 246))
            test.screen.blit(banner_text, banner_text_rect)
            play_button.draw(test.screen)
            pygame.display.update()
        pygame.quit()
