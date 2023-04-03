import unittest
import os

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

    # def test_authorise_adds_new_user_when_user_name_is_not_in_data(self):
    #     self.db_handler.authorise(self.user_name)
    #     self.assertIn(self.user_name, self.db_handler.data)
    #
    # def test_authorise_does_not_add_new_user_when_user_name_is_in_data(self):
    #     self.db_handler.authorise(self.user_name)
    #     self.db_handler.authorise(self.user_name)
    #     self.assertEqual(len(self.db_handler.data), 1)
    #
    # def test_update_user_stats_updates_user_stats_when_user_is_authorised(
    #         self):
    #     self.db_handler.authorise(self.user_name)
    #     self.db_handler.update_user_stats(self.sentences_solved,
    #                                       self.avg_speed, self.error_rate)
    #     expected_stats = (
    #     self.sentences_solved, self.avg_speed, self.error_rate)
    #     self.assertEqual(self.db_handler.get_user_stats(), expected_stats)
    #
    # def test_update_user_stats_does_not_update_user_stats_when_user_is_not_authorised(
    #         self):
    #     self.db_handler.update_user_stats(self.sentences_solved,
    #                                       self.avg_speed, self.error_rate)
    #     self.assertEqual(self.db_handler.get_user_stats(), (0, 0, 0))
    #
    # def test_get_user_stats_returns_user_stats_when_user_is_authorised(self):
    #     self.db_handler.authorise(self.user_name)
    #     self.db_handler.update_user_stats(self.sentences_solved,
    #                                       self.avg_speed, self.error_rate)
    #     expected_stats = (
    #     self.sentences_solved, self.avg_speed, self.error_rate)
    #     self.assertEqual(self.db_handler.get_user_stats(), expected_stats)
    #
    # def test_get_user_stats_returns_zeros_when_user_is_not_authorised(self):
    #     self.assertEqual(self.db_handler.get_user_stats(), (0, 0, 0))


if __name__ == "__main__":
    unittest.main()
