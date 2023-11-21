import pygame
import sqlite3
import os
from elements import Button

def main():

    if not os.path.isfile("scores.db"):
        conn = sqlite3.connect("scores.db")
        create_tables(conn)
        conn.commit()
    else:
        conn = sqlite3.connect("scores.db")

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
                conn.close()
        screen.fill((255, 255, 255))
        play_button.draw(screen)
        pygame.display.update()

def create_tables(crs):
    crs.execute('''
        CREATE TABLE Scores (
            id integer primary key,
            username TEXT,
            score INTEGER
        );
        
    ''')

if __name__ == "__main__":
    main()