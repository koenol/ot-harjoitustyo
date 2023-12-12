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


class GameView(View):
    def __init__(self):
        pygame.init()
        super().__init__()
        pygame.display.set_caption("Rytmipeli - Game View")
        self._start()

    def _start(self):
        WINDOW_HEIGHT = self.height
        WINDOW_WIDTH = self.width
        FPS = self.fps
        BUTTON_SIZE = 48
        BLOCK_SPEED = 5

        clock = pygame.time.Clock()
        score = 0
        score_font = pygame.font.SysFont("gabriola", 48)
        score_text = score_font.render(f"Score: {str(score)}", True, (0, 0, 0), (246, 246, 246))
        score_rect = score_text.get_rect()
        score_rect.topleft = (10, 10)

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
        game_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Rytmipeli - Game")
        pygame.mixer.music.load("src/static/Reminiscent-Of-Spring.mp3")
        pygame.mixer.music.play(1, 0.0, 8000)
        pygame.mixer.music.set_volume(0.40)
        block_x = -100
        block_y = random.choice(x_spawn_coords)
        running = True
        button1_rect = pygame.draw.rect(game_surface, (255, 0, 0), button1_coord)
        button2_rect = pygame.draw.rect(game_surface, (0, 255, 0), button2_coord)
        button3_rect = pygame.draw.rect(game_surface, (0, 0, 255), button3_coord)

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
                        score += 1
                        block_y = -100
                        block_x = random.choice(x_spawn_coords)

            game_surface.fill((246, 246, 246))

            if block_y > WINDOW_HEIGHT:
                block_y = -100
                block_x = random.choice(x_spawn_coords)
            else:
                block_y += BLOCK_SPEED

            pygame.draw.rect(
                game_surface, (0, 0, 0), (block_x, block_y, BUTTON_SIZE + 32, BUTTON_SIZE)
                )

            button1_rect = pygame.draw.rect(game_surface, (255, 0, 0), button1_coord)
            button2_rect = pygame.draw.rect(game_surface, (0, 255, 0), button2_coord)
            button3_rect = pygame.draw.rect(game_surface, (0, 0, 255), button3_coord)

            score_text = score_font.render(f"Score: {str(score)}", True, (0, 0, 0), (246, 246, 246))
            game_surface.blit(score_text, score_rect)
            clock.tick(FPS)
            pygame.display.update()