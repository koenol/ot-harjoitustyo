from database.init_database_conn import DatabaseInit
from ui.ui import *


def main():
    DatabaseInit.initialize_database()
    UI()

if __name__ == "__main__":
    main()
