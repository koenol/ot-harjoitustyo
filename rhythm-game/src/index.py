from ui.main_view import MainView
from database.init_database_conn import DatabaseInit


def main():
    DatabaseInit.initialize_database()
    MainView()

if __name__ == "__main__":
    main()
