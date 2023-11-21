import pygame
from elements import Button

def main():

    pygame.init()
    screen = pygame.display.set_mode((1024, 768))
    pygame.display.set_caption("Rytmipeli")

    x = (screen.get_width() - 200) // 2
    y = (screen.get_height() - 60) // 2
    play_button = Button(x, y, 200, 100, "Play", "play")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        screen.fill((255, 255, 255))
        play_button.draw(screen)
        pygame.display.update()


if __name__ == "__main__":
    main()