from database.database_connection import get_database_connection


def initialize_database():
    get_database_connection()


if __name__ == "__main__":
    initialize_database()