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
        crs.execute('SELECT username, score FROM Scores ORDER by score DESC LIMIt 10')
        return crs.fetchall()