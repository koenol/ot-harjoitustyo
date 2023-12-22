import pygame
from ui.elements import *
from ui.view import *
from entities.player import Player
from database.database_connection import DatabaseConnection

class UI:
    def __init__(self):
        self.current_view = None
        self.player = Player()
        self.conn = DatabaseConnection()
        self.highscores = self.conn.display_highscores()
        self._start()

    def _start(self):
        pygame.init()
        self._show_main_view()
        self._main_loop()
        pygame.quit()
        self.conn.close()

    def _main_loop(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self._check_play_button_collision(event)
            self._update_display()

    def _check_play_button_collision(self, event):
        play_button = Button(
            (self.current_view.get_width() - 100) // 2,
            (self.current_view.get_height()) // 2,
            100,
            50,
            "Play",
            "play"
        )
        if event.button == 1 and play_button.rect.collidepoint(event.pos):
            self.player.set_game_state_start()
            self._show_game_view()
            if not self.player.get_game_state():
                self._show_result_view()
                self._update_highscore_view()
            self.player.__init__()
            self._show_main_view()

    def _update_display(self):
        pygame.display.update()

    def _update_highscore_view(self):
        self.highscores = self.conn.display_highscores()

    def _show_main_view(self):
        self.current_view = MainView()
        MainViewElements.display_elements(
            self.current_view.screen,
            self.current_view.get_width(),
            self.current_view.get_height(),
            self.highscores
        )

    def _show_game_view(self):
        self.current_view = GameView(self.player)

    def _show_result_view(self):
        self.current_view = ResultView(self.conn, self.player)