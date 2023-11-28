import os
import sqlite3
from database.db_commands import DatabaseCommands

def get_database_connection():
    if not os.path.isfile("rhythm-game/src/data/scores.db"):
        conn = sqlite3.connect("rhythm-game/src/data/scores.db")
        DatabaseCommands.create_tables(conn)
        return conn
    else:
        conn = sqlite3.connect("rhythm-game/src/data/scores.db")
        return conn
    
