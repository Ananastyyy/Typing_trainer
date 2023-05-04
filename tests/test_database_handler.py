import json

import pytest

from trainer.window.logic.database_handler import DatabaseHandler

database = DatabaseHandler("database/test.json")
is_authorised = [
    ("Max", True),
    (" ", False)
]
update_user_stats = [
    ("Dan", (3, 230, 0), (3, 230, 0)),
    (" ", (1, 1, 1), None)
]


@pytest.fixture
def setUp():
    _clear_file()


def _clear_file():
    with open("database/test.json", "w") as f:
        json.dump({}, f)


@pytest.mark.parametrize("name, expected", is_authorised)
def test_is_authorised(name, expected):
    database.authorise(name)
    assert (database.is_authorised(), expected)


@pytest.mark.parametrize("name, stats, expected", update_user_stats)
def test_update_user_stats(name, stats, expected):
    database.authorise(name)
    database.update_user_stats(stats[0], stats[1], stats[2])
    assert (database.get_user_stats(), expected,
            "Ошибка в обновлении статуса пользователя")
