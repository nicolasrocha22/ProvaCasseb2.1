import unittest
import sys

sys.path.insert(1, "..")

from database.database import Database

class TestLocadoraDatabase(unittest.TestCase):
    def setUp(self):
        self.db = Database()
        self.db.connect_db()

    def test_1_add_values(self):
        self.db.drop_table_db()
        self.db.create_table_db()
        self.db.add_values_db("Filme1", 2020, "Paula", 1919)

        self.assertEqual(self.db.show_table_db(), (('Filme1', 2020, 'Paula', 1919),))

    def test_2_modify_values(self):
        self.db.modify_values_db("Filme2", 2121, 1919)
        self.assertEqual(self.db.show_table_db(), (('Filme2', 2121, 'Paula', 1919),))

    def test_3_delete_values(self):
        self.db.delete_values_db(1919)
        self.assertEqual(self.db.show_table_db(), ())

    @unittest.expectedFailure
    def test_4_fail_add_values(self):
        self.db.drop_table_db()
        self.db.create_table_db()
        self.db.add_values_db("Filme1", 2020, "Paula", 1919)

        self.assertEqual(self.db.show_table_db(), ('Filme1', 2020, 'Paula', 1919))

    @unittest.expectedFailure
    def test_5_fail_modify_values(self):
        self.db.modify_values_db("Filme2", 2121, 1919)
        self.assertEqual(self.db.show_table_db(), (('Filme2', 2020, 'Paula', 1919),))

    @unittest.expectedFailure
    def test_6_fail_delete_values(self):
        self.db.drop_table_db()
        self.assertEqual(self.db.show_table_db(), ())

if __name__ == '__main__':
    unittest.main()
