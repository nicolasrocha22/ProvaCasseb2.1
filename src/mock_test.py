import unittest
from unittest.mock import MagicMock
from database_class import Database


class TestMockLocadoraDatabase(unittest.TestCase):
    def setUp(self):
        self.instance = Database()

    def test_1_connection(self):
        self.instance.connect_db = MagicMock(name="database connection")
        self.instance.connect_db()

    def test_2_create_table_db(self):
        self.instance.create_table_db = MagicMock(name="database create table")
        self.instance.create_table_db()

    def test_3_add_values_db(self):
        self.instance.add_values_db = MagicMock(name="database add values")
        self.instance.add_values_db("Filme3", 5555, "Cliente1", 1616)

    def test_4_modify_values_db(self):
        self.instance.modify_values_db = MagicMock(name="database modify values")
        self.instance.modify_values_db("Filme4", 4444, 1616)

    def test_5_delete_values_db(self):
        self.instance.delete_values_db = MagicMock(name="database delete values")
        self.instance.delete_values_db(1616)


if __name__ == "__main__":
    unittest.main()
