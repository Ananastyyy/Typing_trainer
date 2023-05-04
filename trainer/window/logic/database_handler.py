import json

from config.conf_parser import ConfParser


class DatabaseHandler:
    def __init__(self, file_path: str) -> None:
        self.file_path = file_path
        self.data = {}
        self._load_data()
        self._init_config_file()
        self.user_name = None

    def _init_config_file(self) -> None:
        config = ConfParser()
        constants = config.database_handler
        self.solved = constants["solved"]
        self.speed = constants["avg_speed"]
        self.error = constants["error_rate"]

    def is_authorised(self) -> bool:
        return self.user_name

    def authorise(self, user_name: str) -> None:
        self.user_name = user_name
        self._add_user(user_name)

    def _load_data(self) -> None:
        try:
            with open(self.file_path, "r") as f:
                self.data = json.load(f)
        except json.decoder.JSONDecodeError:
            self.data = {}

    def _save_data(self) -> None:
        with open(self.file_path, "w") as f:
            json.dump(self.data, f, indent=4)

    def _add_user(self, name: str) -> None:
        if name not in self.data:
            self.data[name] = {
                self.solved: 0,
                self.speed: 0,
                self.error: 0
            }
            self._save_data()

    def update_user_stats(self, sentences_solved: int, avg_speed: int,
                          error_rate: int) -> None:
        if self.is_authorised():
            self.data[self.user_name][self.solved] += \
                sentences_solved
            self.data[self.user_name][self.speed] = avg_speed
            self.data[self.user_name][self.error] += \
                error_rate
            self._save_data()

    def get_user_stats(self) -> tuple | None:
        if self.is_authorised():
            return tuple(self.data[self.user_name].values())
