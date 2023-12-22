import os
import sqlite3
from database.db_commands import DatabaseCommands

class DatabaseConnection:
    def __init__(self):
        '''
        Alustaa tietokanta toiminnot
        '''
        self.conn = self._init_database_conn()

    def _init_database_conn(self):
        '''
        Tarkistaa onko tietokanta vielä luotu ja yrittää yhdistää tietokantaan
        '''
        if not os.path.isfile("src/data/scores.db"):
            self._create_database_connection()
        return self._get_database_connection()

    def _create_database_connection(self):
        '''
        Luo tietokanta yhteyden
        '''
        conn = sqlite3.connect("src/data/scores.db")
        DatabaseCommands.create_tables(conn)
        conn.commit()

    def _get_database_connection(self):
        return sqlite3.connect("src/data/scores.db")

    def check_highscore(self, score):
        '''
        Vertailee pelaajan tulosta tietokannasta löytyviin top10 tuloksiin
        '''
        highscores = DatabaseCommands.get_highscores(self.conn)
        if len(highscores) < 10 and score > 0:
            return True
        return score > highscores[-1][1]

    def add_new_highscore(self, player):
        '''
        Lisää uuden highscoren tietokantaan
        '''
        nickname = player.get_name()
        score = player.get_final_score()
        DatabaseCommands.insert_new_highscore(self.conn, nickname, score)
        DatabaseCommands.remove_old_highscore(self.conn)
        self.conn.commit()

    def display_highscores(self):
        '''
        Palauttaa highscoresit tietokannasta
        '''
        highscores = DatabaseCommands.get_highscores(self.conn)
        return highscores

    def close(self):
        '''
        Sulkee yhteyden tietokantaan
        '''
        self.conn.close()
