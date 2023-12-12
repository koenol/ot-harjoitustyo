import os
import sqlite3

class DatabaseConnection:
    def __init__(self):
        pass

    def get_database_connection(self):
        if not os.path.isfile("src/data/scores.db"):
            conn = sqlite3.connect("src/data/scores.db")
            #DatabaseCommands.create_tables(conn)
            conn.commit()
        else:
            conn = sqlite3.connect("src/data/scores.db")
