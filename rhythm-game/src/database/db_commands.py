class DatabaseCommands:
    def __init__(self):
        pass

    @staticmethod
    def create_tables(connection):
        crs = connection.cursor()
        crs.execute('''
            CREATE TABLE Scores (
                id INTEGER PRIMARY KEY,
                username TEXT,
                score INTEGER);
                ''')

    def insert_new_highscore(connection, nickname, score):
        crs = connection.cursor()
        crs.execute('INSERT INTO Scores (username, score) VALUES (?, ?)', (nickname, score))

    def get_highscores(connection):
        crs = connection.cursor()
        crs.execute('SELECT username, score FROM Scores ORDER BY score DESC LIMIt 10')
        return crs.fetchall()
    
    def remove_old_highscore(connection):
        crs = connection.cursor()
        crs.execute('SELECT id FROM Scores ORDER BY score DESC LIMIT -1 OFFSET 10')
        list_of_removeable_highscores = crs.fetchall()
        for id in list_of_removeable_highscores:
            crs.execute('DELETE FROM Scores WHERE id = (?)', (id))