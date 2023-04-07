import unittest

from trainer.window.logic.database_handler import DatabaseHandler


class TestDatabaseHandler(unittest.TestCase):

    def test_is_authorised(self):
        database = DatabaseHandler("database/test.json")
        database.authorise("Max")
        self.assertTrue(database.is_authorised())

    def test_is_authorised_with_empty_name(self):
        database = DatabaseHandler("database/test.json")
        database.authorise("")
        self.assertFalse(database.is_authorised())

    def test_update_user_stats(self):
        database = DatabaseHandler("database/test.json")
        database.authorise("Dan")
        database.update_user_stats(3, 230, 0)
        self.assertEqual(database.get_user_stats(), (3, 230, 0),
                         "Ошибка в обновлении статуса пользователя")

    def test_update_user_stats_with_non_authorised_user(self):
        database = DatabaseHandler("database/test.json")
        database.update_user_stats(230, 0, 1)
        self.assertIsNone(database.get_user_stats())


if __name__ == "__main__":
    unittest.main()
