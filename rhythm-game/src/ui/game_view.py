import pygame

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
FPS = 60

class GameView:
    def __init__(self):
            pygame.init()
            game_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
            pygame.display.set_caption("Rytmipeli - Game")

            #refractor this to elements
            pygame.mixer.music.load("rhythm-game\src\static\Reminiscent-Of-Spring.mp3")
            pygame.mixer.music.play(1, 0.0, 8000)
            pygame.mixer.music.set_volume(0.40)

            running = True
            while running:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.mixer.music.stop()
                        running = False

                game_surface.fill((246, 246, 246))
                pygame.display.update()
            