
class DatabaseCommands:

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