import unittest
from database.database_connection import DatabaseConnection

class TestDatabaseConnection(unittest.TestCase):
    def setUp(self):
        self.conn = DatabaseConnection()

