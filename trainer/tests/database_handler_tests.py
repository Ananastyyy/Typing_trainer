import unittest

from trainer.window.logic.database_handler import DatabaseHandler


class TestDatabaseHandler(unittest.TestCase):
    def __init__(self):
        super().__init__()
        self.test_db_file_path = "database/test.json"

    def setUp(self):
        self.db_handler = DatabaseHandler(self.test_db_file_path)

    def test_is_authorised_returns_false_when_user_name_is_none(self):
        database = DatabaseHandler(self.test_db_file_path)
        database.authorise("Max")
        self.assertFalse(database.is_authorised())


if __name__ == "__main__":
    unittest.main()
