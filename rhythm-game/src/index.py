import pygame
from ui.elements import Button
from ui.main_view import MainView
from database.init_database_conn import initialize_database


def main():
    initialize_database()
    MainView()


if __name__ == "__main__":
    main()