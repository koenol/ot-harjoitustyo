import pygame
import random

class View:
    def __init__(self):
        self.width = 800
        self.height = 600
        self.fps = 60
        self.screen = pygame.display.set_mode((self.width, self.height))

    def get_height(self):
        return self.screen.get_height()
    
    def get_width(self):
        return self.screen.get_width()
    
class MainView(View):
    def __init__(self):
        super().__init__()
        pygame.display.set_caption("Rytmipeli - Main Menu")

class ResultView(View):
    def __init__(self, connection, player):
        super().__init__()
        pygame.display.set_caption("Rytmipeli - Result")
        self.player = player
        self.conn = connection
        self._start()

    def _start(self):
        result_font = pygame.font.SysFont("gabriola", 76)
        result_text = result_font.render(f"Result", True, (0, 0, 0), (246, 246, 246))
        result_rect = result_text.get_rect()
        result_rect.topleft = (10, 10)

        score_font = pygame.font.SysFont("gabriola", 32)
        score_text = score_font.render(f"Final Score: {str(self.player.get_score())}", True, (0, 0, 0), (246, 246, 246))
        score_rect = score_text.get_rect()
        score_rect.topleft = (10, 100)

        combo_font = pygame.font.SysFont("gabriola", 32)
        combo_text = combo_font.render(f"Longest Combo: {str(self.player.get_longest_combo())}", True, (0, 0, 0), (246, 246, 246))
        combo_rect = combo_text.get_rect()
        combo_rect.topleft = (10, 132)

        if self.conn.check_highscore(self.player.get_score()):
            print("yeo")
            self.conn.add_new_highscore(self.player)
        else:
            print("nope!")

        running = True
        while running:
            self.screen.fill((246, 246, 246))
            self.screen.blit(result_text, result_rect)
            self.screen.blit(score_text, score_rect)
            self.screen.blit(combo_text, combo_rect)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False




class GameView(View):
    def __init__(self, player):
        pygame.init()
        super().__init__()
        pygame.display.set_caption("Rytmipeli - Game")
        self.player = player
        self._start()

    def _start(self):
        WINDOW_HEIGHT = self.height
        WINDOW_WIDTH = self.width
        BUTTON_SIZE = 48
        BLOCK_SPEED = 5

        clock = pygame.time.Clock()
        score_font = pygame.font.SysFont("gabriola", 48)
        score_text = score_font.render(f"Score: {str(self.player.get_score())}", True, (0, 0, 0), (246, 246, 246))
        score_rect = score_text.get_rect()
        score_rect.topleft = (10, 10)

        combo_font = pygame.font.SysFont("gabriola", 48)
        combo_text = combo_font.render(f"Combo: {str(self.player.get_current_combo())}", True, (0, 0, 0), (246, 246, 246))
        combo_rect = combo_text.get_rect()
        combo_rect.topleft = (10, 50)

        button1_x = WINDOW_WIDTH // 2 - 256 - BUTTON_SIZE
        button1_y = WINDOW_HEIGHT // 2 + 164
        button1_coord = (button1_x, button1_y, BUTTON_SIZE + 32, BUTTON_SIZE)

        button2_x = WINDOW_WIDTH // 2 - BUTTON_SIZE
        button2_y = WINDOW_HEIGHT // 2 + 164
        button2_coord = (button2_x, button2_y, BUTTON_SIZE + 32, BUTTON_SIZE)

        button3_x = WINDOW_WIDTH // 2 + 256 - BUTTON_SIZE
        button3_y = WINDOW_HEIGHT // 2 + 164
        button3_coord = (button3_x, button3_y, BUTTON_SIZE + 32, BUTTON_SIZE)

        x_spawn_coords = [
            (WINDOW_WIDTH // 2 - 256 - BUTTON_SIZE),
            (WINDOW_WIDTH // 2 - BUTTON_SIZE),
            (WINDOW_WIDTH // 2 + 256 - BUTTON_SIZE),
        ]
        pygame.mixer.music.load("src/static/Reminiscent-Of-Spring.mp3")
        pygame.mixer.music.play(1, 0.0, 8000)
        pygame.mixer.music.set_volume(0.40)
        block_y = -100
        block_x = random.choice(x_spawn_coords)
        running = True
        button1_rect = pygame.draw.rect(self.screen, (255, 0, 0), button1_coord)
        button2_rect = pygame.draw.rect(self.screen, (0, 255, 0), button2_coord)
        button3_rect = pygame.draw.rect(self.screen, (0, 0, 255), button3_coord)

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.mixer.music.stop()
                    running = False
                if event.type == pygame.KEYDOWN:
                    if (
                        (event.key == pygame.K_a and button1_rect.colliderect(
                            block_x, block_y, BUTTON_SIZE + 32, BUTTON_SIZE)) or
                        (event.key == pygame.K_s and button2_rect.colliderect(
                            block_x, block_y, BUTTON_SIZE + 32, BUTTON_SIZE)) or
                        (event.key == pygame.K_d and button3_rect.colliderect(
                            block_x, block_y, BUTTON_SIZE + 32, BUTTON_SIZE))
                    ):
                        self.player.increase_score()
                        self.player.increase_combo()
                        block_y = -100
                        block_x = random.choice(x_spawn_coords)

            self.screen.fill((246, 246, 246))

            if block_y > WINDOW_HEIGHT:
                block_y = -100
                block_x = random.choice(x_spawn_coords)
                self.player.reset_combo()
                self.player.decrease_lives()

                if self.player.get_lives() == 0:
                    pygame.mixer.music.stop()
                    running = False
            else:
                block_y += BLOCK_SPEED

            pygame.draw.rect(
                self.screen, (0, 0, 0), (block_x, block_y, BUTTON_SIZE + 32, BUTTON_SIZE)
                )

            button1_rect = pygame.draw.rect(self.screen, (255, 0, 0), button1_coord)
            button2_rect = pygame.draw.rect(self.screen, (0, 255, 0), button2_coord)
            button3_rect = pygame.draw.rect(self.screen, (0, 0, 255), button3_coord)

            score_text = score_font.render(f"Score: {str(self.player.get_score())}", True, (0, 0, 0), (246, 246, 246))
            combo_text = combo_font.render(f"Combo: {str(self.player.get_current_combo())}", True, (0, 0, 0), (246, 246, 246))
            self.screen.blit(score_text, score_rect)
            self.screen.blit(combo_text, combo_rect)
            clock.tick(self.fps)
            pygame.display.update()