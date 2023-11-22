import pygame
import sqlite3
import os
from ui.elements import Button, Score

def create_tables(connection):
    crs = connection
    crs.execute('''
        CREATE TABLE Scores (
            id INTEGER PRIMARY KEY,
            username TEXT,
            score INTEGER
        );
        
    ''')

def insert_score(connection, username, score):
    crs = connection
    result = username, score
    sql = "INSERT INTO Scores(username, score) VALUES(?,?)"
    crs.execute(sql, result)

def get_score(connection):
    crs = connection
    sql = "SELECT username, score FROM Scores WHERE id == 1"
    return crs.execute(sql)

def main():

    ## test init
    if not os.path.isfile("scores.db"):
        conn = sqlite3.connect("scores.db")
        create_tables(conn)
        conn.commit()
    else:
        conn = sqlite3.connect("scores.db")

    ## test data
    insert_score(conn, "ABC", 123)
    conn.commit()
    test_score = get_score(conn)

    ## test pygame init
    pygame.init()
    screen = pygame.display.set_mode((1024, 768))
    pygame.display.set_caption("Rytmipeli")

    play_x = (screen.get_width() - 200) // 2
    play_y = (screen.get_height() - 60) // 2
    high_score_x = (screen.get_width() - 1000) // 2
    high_score_y = (screen.get_height() - 700) // 2

    play_button = Button(play_x, play_y, 200, 100, "Play", "play")
    high_score = Score(high_score_x, high_score_y, 200, 100, test_score)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                conn.close()
        screen.fill((255, 255, 255))
        play_button.draw(screen)
        high_score.draw(screen)
        pygame.display.update()

if __name__ == "__main__":
    main()