import pygame
from ui.elements import Button
from ui.view import *
from services.main_loop import MainLoopService
from entities.player import Player
from database.database_connection import DatabaseConnection

class UI:
    def __init__(self):
        self.current_view = None
        self.player = Player()
        self.conn = DatabaseConnection()
        self.highscores = self.conn.display_highscores()
        self._start()

    def _update_highscores(self):
        self.highscores = self.conn.display_highscores()

    def _start(self):
        pygame.init()
        self._show_main_view()
        play_x = (self.current_view.get_width() - 200) // 2
        play_y = (self.current_view.get_height() - 60) // 2

        # refractor this to elements
        banner_font = pygame.font.Font("src/static/RapunledRegular-axZLJ.otf", 32)
        banner_text = banner_font.render("Rhythm Game", True, (0, 0, 0))
        banner_text_rect = banner_text.get_rect()
        banner_text_rect.center = (self.current_view.get_width() //2 + 100, self.current_view.get_height() //2 - 200)

        highscore_font = pygame.font.SysFont("gabriola", 24)      

        play_button = Button(play_x, play_y, 200, 100, "Play", "play")

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if play_button.rect.collidepoint(event.pos):
                            self._show_game_view()
                            if self.player.get_lives() == 0:
                                self._show_result_view()
                                self.conn.add_new_highscore(self.player)
                                self._update_highscores()
                            self.player.__init__()
                            self._show_main_view()

            self.current_view.screen.fill((246, 246, 246))

            y_position = 10
            for position, (name, score) in enumerate(self.highscores, start=1):
                text = f"{position}. {name}: {score}"
                score_text = highscore_font.render(text, True, (0, 0, 0), (246, 246, 246))
                self.current_view.screen.blit(score_text, (10, y_position))
                y_position += 24
            self.current_view.screen.blit(banner_text, banner_text_rect)
            play_button.draw(self.current_view.screen)
            pygame.display.update()
        pygame.quit()
        self.conn.close()

    def _show_main_view(self):
        self.current_view = MainView()

    def _show_game_view(self):
        self.current_view = GameView(self.player)

    def _show_result_view(self):
        self.current_view = ResultView(self.player)