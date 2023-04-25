import json
import unittest

from trainer.window.logic.database_handler import DatabaseHandler


class TestDatabaseHandler(unittest.TestCase):
    def setUp(self):
        self.database = DatabaseHandler("database/test.json")
        self.clear_file()

    def clear_file(self):
        with open('database/test.json', 'w') as f:
            json.dump({}, f)

    def test_is_authorised(self):
        self.setUp()
        self.database.authorise("Max")
        self.assertTrue(self.database.is_authorised())

    def test_is_authorised_with_empty_name(self):
        self.setUp()
        self.database.authorise("")
        self.assertFalse(self.database.is_authorised())

    def test_update_user_stats(self):
        self.setUp()
        self.database.authorise("Dan")
        self.database.update_user_stats(3, 230, 0)
        self.assertEqual(self.database.get_user_stats(), (3, 230, 0),
                         "Ошибка в обновлении статуса пользователя")

    def test_update_user_stats_with_non_authorised_user(self):
        self.setUp()
        self.database.update_user_stats(230, 0, 1)
        self.assertIsNone(self.database.get_user_stats())


if __name__ == "__main__":
    unittest.main()
