import pygame
import random
import pydualsense

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

        final_score_multiplier = (1 + ((self.player.get_longest_combo() / 100)))
        final_score = int(self.player.get_score() * final_score_multiplier)


        self.player.set_final_score(final_score)

        final_font = pygame.font.SysFont("gabriola", 32)
        final_text = final_font.render(f"Final Score: {final_score}", True, (0, 0, 0), (246, 246, 246))
        final_rect = final_text.get_rect()
        final_rect.topleft = (10, 196)

        new_highscore_font = pygame.font.SysFont("gabriola", 32)
        new_highscore_text = new_highscore_font.render(f"NEW HIGHSCORE!", True, (0, 0, 0), (246, 246, 246))
        new_highscore_rect = new_highscore_text.get_rect()
        new_highscore_rect.topleft = (10, 164)

        rank_font = pygame.font.SysFont("gabriola", 64)
        rank_text = rank_font.render(f"{self.player.get_rank(final_score)}", True, (0, 0, 0), (246, 246, 246))
        rank_rect = rank_text.get_rect()
        rank_rect.topleft = (40, 300)


        self.screen.fill((246, 246, 246))

        if self.conn.check_highscore(self.player.get_final_score()):
            self.screen.blit(new_highscore_text, new_highscore_rect)
            self.conn.add_new_highscore(self.player)
    
        running = True
        while running:
            self.screen.blit(result_text, result_rect)
            self.screen.blit(score_text, score_rect)
            self.screen.blit(combo_text, combo_rect)
            self.screen.blit(final_text, final_rect)
            self.screen.blit(rank_text, rank_rect)
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

        nice_font = pygame.font.SysFont("gabriola", 24)
        nice_text = nice_font.render(f"Nice! +100", True, (0, 0, 0), (246, 246, 246))
        nice_rect = nice_text.get_rect()
        nice_rect.topleft = (120, 200)

        perfect_font = pygame.font.SysFont("gabriola", 24)
        perfect_text = perfect_font.render(f"Perfect! +200", True, (0, 0, 0), (246, 246, 246))
        perfect_rect = perfect_text.get_rect()
        perfect_rect.topleft = (110, 200)

        button1_x = WINDOW_WIDTH // 2 - 128 - BUTTON_SIZE
        button1_y = WINDOW_HEIGHT // 2 + 164
        button1_coord = (button1_x, button1_y, BUTTON_SIZE + 32, BUTTON_SIZE)

        button2_x = WINDOW_WIDTH // 2 - BUTTON_SIZE
        button2_y = WINDOW_HEIGHT // 2 + 164
        button2_coord = (button2_x, button2_y, BUTTON_SIZE + 32, BUTTON_SIZE)

        button3_x = WINDOW_WIDTH // 2 + 128 - BUTTON_SIZE
        button3_y = WINDOW_HEIGHT // 2 + 164
        button3_coord = (button3_x, button3_y, BUTTON_SIZE + 32, BUTTON_SIZE)

        x_spawn_coords = [
            (WINDOW_WIDTH // 2 - 128 - BUTTON_SIZE),
            (WINDOW_WIDTH // 2 - BUTTON_SIZE),
            (WINDOW_WIDTH // 2 + 128 - BUTTON_SIZE),
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

        ### this formula was converted from my other project written in C# to python/pygame using ChatGPT
        button1_middle_47_5_percent = button1_rect.top + (button1_rect.height * 0.475)
        button1_middle_range = pygame.Rect(
            button1_rect.left,
            button1_middle_47_5_percent - (button1_rect.height * 0.025),
            button1_rect.width,
            button1_rect.height * 0.05
        )
        ###

        button2_middle_47_5_percent = button2_rect.top + (button2_rect.height * 0.475)
        button2_middle_range = pygame.Rect(
            button2_rect.left,
            button2_middle_47_5_percent - (button2_rect.height * 0.025),
            button2_rect.width,
            button2_rect.height * 0.05
        )

        button3_middle_47_5_percent = button3_rect.top + (button3_rect.height * 0.475)
        button3_middle_range = pygame.Rect(
            button3_rect.left,
            button3_middle_47_5_percent - (button3_rect.height * 0.025),
            button3_rect.width,
            button3_rect.height * 0.05
        )
        hit_blocks = 10
        hit_nice = 100
        hit_perfect = 100
        end_timer = 0

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
                        if (
                            (button1_middle_range.colliderect(
                                block_x, block_y, BUTTON_SIZE + 32, BUTTON_SIZE)) and
                            (event.key == pygame.K_a)
                        ) or (
                            (button2_middle_range.colliderect(
                                block_x, block_y, BUTTON_SIZE + 32, BUTTON_SIZE)) and
                            (event.key == pygame.K_s)
                        ) or (
                            (button3_middle_range.colliderect(
                                block_x, block_y, BUTTON_SIZE + 32, BUTTON_SIZE)) and
                            (event.key == pygame.K_d)
                        ):
                            self.player.increase_score_perfect()                            
                            self.player.increase_combo()
                            hit_perfect = 0
                                
                            block_y = -100
                            block_x = random.choice(x_spawn_coords)
                            hit_blocks -= 1
                            
                        else:
                            self.player.increase_score_normal()
                            self.player.increase_combo()
                            hit_nice = 0
                            block_y = -100
                            block_x = random.choice(x_spawn_coords)
                            hit_blocks -= 1

            self.screen.fill((246, 246, 246))
            if hit_nice < 100:
                self.screen.blit(nice_text, nice_rect)
                hit_nice += 1

            if hit_perfect < 100:
                self.screen.blit(perfect_text, perfect_rect)
                hit_perfect += 1

            if block_y > WINDOW_HEIGHT and hit_blocks != 0:
                block_y = -100
                block_x = random.choice(x_spawn_coords)
                hit_blocks -= 1
                self.player.reset_combo()
                self.player.decrease_lives()

                if self.player.get_lives() == 0:
                    self.player.set_game_state_end()
                    pygame.mixer.music.stop()
                    running = False
            else:
                block_y += BLOCK_SPEED

            if hit_blocks == 0:
                end_timer += 1
            if end_timer == 400:
                self.player.reset_combo()
                self.player.set_game_state_end()
                pygame.mixer.music.stop()
                running = False

            if hit_blocks != 0:
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