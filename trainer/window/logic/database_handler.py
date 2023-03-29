import json


class DatabaseHandler:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = {}
        self._load_data()
        self.user_name = None

    def is_authorised(self) -> bool:
        return self.user_name

    def authorise(self, user_name: str):
        self.user_name = user_name
        self._add_user(user_name)

    def _load_data(self):
        with open(self.file_path, 'r') as f:
            self.data = json.load(f)

    def _save_data(self):
        with open(self.file_path, 'w') as f:
            json.dump(self.data, f)

    def _add_user(self, name: str):
        if name not in self.data:
            self.data[name] = {
                'sentences_solved': 0,
                'avg_speed': 0,
                'error_rate': 0
            }
            self._save_data()

    def update_user_stats(self, sentences_solved, avg_speed, error_rate):
        if self.is_authorised:
            self.data[self.user_name]['sentences_solved'] += sentences_solved
            self.data[self.user_name]['avg_speed'] = avg_speed
            self.data[self.user_name]['error_rate'] = error_rate
            self._save_data()

    def get_user_stats(self) -> tuple[int, int, int]:
        if self.is_authorised():
            return tuple(self.data[self.user_name].values())
