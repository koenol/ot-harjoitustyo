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
        