import pygame
from ui.elements import Button
from database.init_database_conn import initialize_database

def main():
    conn = initialize_database()
    


    ## test pygame init
    pygame.init()
    screen = pygame.display.set_mode((1024, 768))
    pygame.display.set_caption("Rytmipeli")

    play_x = (screen.get_width() - 200) // 2
    play_y = (screen.get_height() - 60) // 2


    play_button = Button(play_x, play_y, 200, 100, "Play", "play")


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                conn.close()
        screen.fill((255, 255, 255))
        play_button.draw(screen)
        pygame.display.update()

if __name__ == "__main__":
    main()